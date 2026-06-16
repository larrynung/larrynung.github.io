---
title: "[C#]使用NetSparkle為應用程式加入自動更新機制"
date: "2013-11-06 12:00:00"
description: "NetSparkle是從Mac的Sparkle移值而來的，一個號稱易於使用的自動更新開源框架。雖然號稱易於使用，但相關的文件真是少的可憐，實際使用上也令我卡關滿久的一個框架(它的類別成員與類別我真的無法一眼看懂它想要幹嘛...orz)。Anyway~這邊隨手做個簡單的整理與記錄。"
tags: [CSharp]
---

NetSparkle是從Mac的Sparkle移值而來的，一個號稱易於使用的自動更新開源框架。雖然號稱易於使用，但相關的文件真是少的可憐，實際使用上也令我卡關滿久的一個框架(它的類別成員與類別我真的無法一眼看懂它想要幹嘛...orz)。Anyway~這邊隨手做個簡單的整理與記錄。

使用前我們必須先將NetSparkle的組件加入參考，可以從官網NetSparkle - AutoUpdate for .NET Developer取得NetSparkle的組件後將之加入參考，或是直接透過NuGet加入參考也可以。

![image_thumb_6.png](/images/posts/c769a641-8d0b-4b7e-8d81-fe57d9daf989/image_thumb_6.png)

將組件加入參考後，必須加入AppLimit.NetSparkle命名空間，接著宣告並建立Sparkle的物件實體。在建立Sparkle物件實體時，我們需將用來檢查應用程式是否有更新的RSS網址一併帶入。

```csharp
using AppLimit.NetSparkle;
...
private Sparkle m_Sparkle { get; set; }
...
m_Sparkle =  new Sparkle("https://yourspace/YourUpdateFeed.xml");
```

這邊的RSS網址我們需要自行準備好，RSS網址的XML文件格式會像下面這樣，Follow格式去調整就可以了，基本上要注意的就是應用程式的Release Note的網頁位置、應用程式的版號、以及應用程式的下載位置這些要記得設定。

```xml
<?xml version="1.0" encoding="utf-8"?>

<rss version="2.0" xmlns:sparkle="http://www.andymatuschak.org/xml-namespaces/sparkle"  xmlns:dc="http://purl.org/dc/elements/1.1/">
  <channel>
    <title>Sparkle Update</title>
    <link>https://yourspace/YourUpdateFeed.xml</link>
    <description></description>
    <language>en</language>
    <item>
      <title>Version 1.0.1</title>
      <sparkle:releaseNotesLink>http://YourReleaseNote</sparkle:releaseNotesLink>
      <pubDate>Sun, 31 Oct 2010 10:21:11 +0000</pubDate>
      <enclosure
          url="http://YourAppFile.exe
          length="5120"
          type="application/octet-stream"
          sparkle:version="1.0.1"
            />
    </item>
  </channel>
</rss>
```

接著我們可以呼叫Sparkle.StartLoop讓NetSparkle自動檢查更新(這邊筆者一開始很混淆StartLoop是什麼?是要Loop什麼?!)，它具有以下幾個多載版本。簡單的來說doInitialCheck是表示啟動自動更新檢查的同時是否要開始檢查是否有更新，若是true則是啟動的同時就會開始檢查更新，false則會等設定的檢查週期到了才檢查；forceInitialCheck是表示是否要強制檢查，若是true則是不管有沒有關掉或是延遲通知更新對話框，只要開啟時有檢查到更新就會要求使用者更新，若是false則是關掉或是延遲通知更新對話框，下次開啟時設定的檢查週期還沒到就不會要求使用者更新；checkFrequency是給使用者設定檢查週期的，若沒特別指定預設是24小時檢查一次。

```csharp
public void StartLoop(bool doInitialCheck);
public void StartLoop(bool doInitialCheck, bool forceInitialCheck);
public void StartLoop(bool doInitialCheck, TimeSpan checkFrequency);
public void StartLoop(bool doInitialCheck, bool forceInitialCheck, TimeSpan checkFrequency);
```

一般來說這邊我們通常最簡單的用法就是將doInitialCheck直接帶true。

```csharp
m_Sparkle.StartLoop(true);
```

或是除了doInitialCheck帶true外，還特別指定checkFrequency去設定要多久檢查一次更新。

```csharp
var timeSpan = TimeSpan.FromHours(5);
m_Sparkle.StartLoop(true, timeSpan);
```

除了指定週期性的檢查更新外，NetSparkle也可以手動Trigger更新，Sparkle.IsUpdateRequired可讓我們掌握目前是否有新的版本可供更新，也可以知道目前的最新版本為何，將可供更新的版本帶給Sparkle.ShowUpdateNeededUI，我們就可以秀出更新畫面要求使用者做更新的動作(這邊筆者還是不能理解Sparkle.GetApplicationConfig為何要開出，而Sparkle.IsUpdateRequired又是為何要帶入)。

```csharp
private Boolean IsUpdateRequired(out NetSparkleAppCastItem latestVersion)
{
	return m_Sparkle.IsUpdateRequired(m_Spakle.GetApplicationConfig(),
		out latestVersion);
}

...

public bool HasUpdate()
{
	var versionInfo = new NetSparkleAppCastItem();
	return IsUpdateRequired(out versionInfo);
}

...

public void CheckUpdate()
{
	var versionInfo = new NetSparkleAppCastItem();
	IsUpdateRequired(out versionInfo);
	m_Sparkle.ShowUpdateNeededUI(versionInfo);
}
```

到這邊我們的應用程式已經成功的加入自動更新的機制了，當偵測到有新的應用程式時，我們可以看到類似下面的更新視窗。

![image_thumb_3.png](/images/posts/c769a641-8d0b-4b7e-8d81-fe57d9daf989/image_thumb_3.png)

更新視窗的Icon若有需要可以透過m_Sparkle.ApplicationIcon與m_Sparkle.ApplicationWindowIcon來設定。其中的m_Sparkle.ApplicationWindowIcon是用來設定視窗標題列的圖示，而m_Sparkle.ApplicationIcon是設定內容區塊左上方那塊圖示(NetSparkle對於更新對話框與更新的流程不能做些客制，不動到原始碼的話，能改的只有Icon)。

```csharp
Icon icon = null;
...
m_Sparkle.ApplicationIcon = icon;
m_Sparkle.ApplicationWindowIcon = icon;
```

若在使用NetSparkle位應用程式加入自動更新機制的同時碰到了些不如預期的問題，NetSparkle也提供了一些除錯的資訊可幫助開發人員排除，透過m_Sparkle.ShowDiagnosticWindow屬性我們可以將NetSparkle的除錯視窗給開出來輔助除錯。

```xml
m_Sparkle.ShowDiagnosticWindow = true;
```

![image_thumb_4.png](/images/posts/c769a641-8d0b-4b7e-8d81-fe57d9daf989/image_thumb_4.png)

若是需要查驗一些檢查時間、忽略的版號之類的，NetSparkle都將這些資訊寫在HKCU\Software\Vendor\Application登錄位置裡面，像是這邊我的範例用的公司名稱是LevelUp，而產品名稱是WindowsFormsApplication4，那我就可以到HKCU\Software\LevelUp\WindowsFormsApplication4這邊去看。

![image_thumb_5.png](/images/posts/c769a641-8d0b-4b7e-8d81-fe57d9daf989/image_thumb_5.png)

介紹到這邊若有耐著性子看完相信大家都能完全的掌握NetSparkle的用法了。接著我必須要提醒一下使用NetSparkle所要注意的一些事項，首先在使用NetSparkle必須要注意應用程式的產品名稱與公司的資訊必須要妥善的填好。

![image_thumb_2.png](/images/posts/c769a641-8d0b-4b7e-8d81-fe57d9daf989/image_thumb_2.png)

不然在使用NetSparkle時會發生"STOP:Sparkle is missing the company or productname tag in"的錯誤。

![image_thumb.png](/images/posts/c769a641-8d0b-4b7e-8d81-fe57d9daf989/image_thumb.png)

這是因為它的一些資訊會記錄在登錄檔中，而登錄檔的位置就如前面所提的必須有產品名稱與公司名稱。

![image_thumb_1.png](/images/posts/c769a641-8d0b-4b7e-8d81-fe57d9daf989/image_thumb_1.png)

另外就是在多個產品使用NetSparkle時我們必須要修改程式碼(多個產品可能是都自己的，或是自己的跟別人的)，這是因為NetSparkle在記錄log時它是寫在AppData下的NetSparkle.log，多個產品用NetSparkle所寫的log並不會分開，只要一個獨佔住另一個想要寫就掛了。

```csharp
public NetSparkleMainWindows()
{
    // init ui
    InitializeComponent();

    // init logfile
    sw = File.CreateText(Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData), "NetSparkle.log"));
}
```

所以這邊我們必須修改程式碼，可以不寫log，或是將不同產品的log分開，抑或是像筆者一樣偷懶改用File.Open搭配FileShare讓它能Work。

```csharp
public NetSparkleMainWindows()
{
...
var fs = File.Open(Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData), "NetSparkle.log"), FileMode.OpenOrCreate, FileAccess.Write, FileShare.Write);
sw = new StreamWriter(fs);
...
}
```

## Link

* I get an STOP: Sparkle is missing the company or productname tag error when trying to run my app.
* NetSparkle - AutoUpdate for .NET Developer
* Automatische Updates
