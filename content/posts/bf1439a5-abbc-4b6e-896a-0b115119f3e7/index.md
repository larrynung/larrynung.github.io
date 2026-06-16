---
title: "[C#]Emulating Chrome's Multi-Process Architecture"
slug: "csharp-emulating-chrome-s-multi-process-architecture"
aliases: ["/posts/csharp仿照chrome的multi-process-architecture/"]
date: "2013-11-06 12:00:00"
description: "筆者在上一篇[C#]如何在程式中內嵌其它應用程式稍稍整理了一下怎樣嵌入外部程式到UI上，這邊要接著嘗試仿照Chrome的Multi-process Architecture做一個簡易的瀏覽器。"
tags: [CSharp]
---

筆者在上一篇[C#]如何在程式中內嵌其它應用程式稍稍整理了一下怎樣嵌入外部程式到UI上，這邊要接著嘗試仿照Chrome的Multi-process Architecture做一個簡易的瀏覽器。若有需要範例程式，可至[larrynung / MultiProcessArchitectureDemo這邊下載。](https://github.com/larrynung/MultiProcessArchitectureDemo)

首先準備個很簡易的Browser主UI，上方放一個內建的TabControl，而下方則是放置個按鈕，期望使用時按下下面的按鈕上方就可以加入一頁瀏覽器分頁。

![image_thumb_4.png](/images/posts/bf1439a5-abbc-4b6e-896a-0b115119f3e7/image_thumb_4.png)

另外還要準備一個瀏覽器頁面用來讓我們內嵌到瀏覽器分頁中。

![image_thumb_3.png](/images/posts/bf1439a5-abbc-4b6e-896a-0b115119f3e7/image_thumb_3.png)

接著進入程式的撰寫，這邊筆者透過Command Line Parser去做命令列參數處理。當程式透過滑鼠點擊開啟，預設是沒有帶任何的命令列參數，這時叫出主要的表單。若是有帶特定的參數，則改叫出瀏覽器頁面讓已開啟的程式嵌進瀏覽器分頁。

```csharp
[STAThread]
static void Main(string[] args)
{
	Application.EnableVisualStyles();
	Application.SetCompatibleTextRenderingDefault(false);

	var options = new Options();
	ICommandLineParser parser = new CommandLineParser();
	if (parser.ParseArguments(args, options))
	{
		m_ReceiverHandel = (IntPtr)options.Handle;
		if (options.IsBrowser)
		{
			var browserTab = new WebBrowserPage()
			{
				StartPosition = FormStartPosition.Manual,
				Top = -3200,
				Left = -3200,
				Width = 0,
				Height = 0
			};

			browserTab.TextChanged += browserTab_TextChanged;

			Application.Run(browserTab);
			return;
		}
	}

	Application.Run(new MainForm());
}
```

而主頁面下方加入瀏覽器分頁的按鈕這邊，我們需要建立一個TabPage，並將[C#]如何在程式中內嵌其它應用程式整理好的ApplicationHost元件放置於其中，帶入當前的執行擋位置以及特定的參數，讓ApplicationHost幫我們帶出瀏覽器分頁並嵌進元件內。(這邊因為瀏覽器分頁的Process若發生異常時我們需要關閉對應的分頁，所以必須要在ApplicationHost.ProcessUnLoaded事件觸發時做關閉分頁的動作。)

```csharp
private void btnAddTab_Click(object sender, EventArgs e)
{
	var tabpage = new TabPage();
	tabControl1.TabPages.Add(tabpage);

	var host = new ApplicationHost()
	{
		File = Application.ExecutablePath,
		Arguments = string.Format("-b -h {0}", this.Handle),
		HideApplicationTitleBar = true,
		Dock = DockStyle.Fill
	};

	host.ProcessLoaded += host_ProcessLoaded;
	host.ProcessUnLoaded += host_ProcessUnLoaded;

	tabpage.Controls.Add(host);
}
```

到這邊為止，這個簡易的瀏覽器已經具備了類似的效果了，但仍美中不足，因為瀏覽器分頁與瀏覽器主視窗之間並無法溝通，所以運行起來還是怪怪的，離Chrome的架構也還有一點距離。因此我們必須將IPC給加上去，這邊可以用很多方法來達成，像是Memory-mapped file、Named pipe...，這邊筆者為了方便選用了比較一般的SendMessage方式來做。

因為這邊只是個嘗試，並沒有想做到多強大、多複雜，這邊筆者只將顯示瀏覽的網頁Title給稍稍補上，在瀏覽器頁面那邊Title變動時主動發送訊息給瀏覽器主視窗。

```csharp
static void browserTab_TextChanged(object sender, EventArgs e)
{
	var browserTab = sender as WebBrowserPage;
	var buffer = Encoding.Default.GetBytes(browserTab.Text);

	var cds = new CopyDataStruct();
	cds.cbData = buffer.Length;
	cds.dwData = browserTab.Handle;
	cds.lpData = Marshal.AllocHGlobal(buffer.Length);

	Marshal.Copy(buffer, 0, cds.lpData, buffer.Length);

	SendMessage(m_ReceiverHandel, WM_COPYDATA, 0x401, ref cds);
}
```

當瀏覽器主視窗收到瀏覽器頁面送過來的訊息，會將收到的Title替換到對應的分頁上。

```csharp
protected override void WndProc(ref Message m)
{
	if (m.Msg == WM_COPYDATA && m.WParam == (IntPtr)0x401)
	{
		var cds = (CopyDataStruct)Marshal.PtrToStructure(m.LParam, typeof(CopyDataStruct));

		m_HostPool[cds.dwData].Parent.Text = Marshal.PtrToStringAnsi(cds.lpData, cds.cbData);
	}
	base.WndProc(ref m);
}
```

整個簡易的瀏覽器做到這邊就已經完成了，程式運行起來會像下面這樣，每一個分頁都會是一個Process，各分頁都會有當前瀏覽的網站名稱。

![image_thumb.png](/images/posts/bf1439a5-abbc-4b6e-896a-0b115119f3e7/image_thumb.png)

若某頁面的Process不慎毀壞。

![image_thumb_1.png](/images/posts/bf1439a5-abbc-4b6e-896a-0b115119f3e7/image_thumb_1.png)

該分頁會自動關閉，且不會影響到整個程式的運作。

![image_thumb_2.png](/images/posts/bf1439a5-abbc-4b6e-896a-0b115119f3e7/image_thumb_2.png)
