---
title: "[C#]Export PowerPoint file to photos"
slug: "[CSharp]Export PowerPoint file to photos"
date: "2013-11-06 12:00:00"
description: "[C#]Export PowerPoint file to photos"
tags: [CSharp]
---

要將PowerPoint檔案中的每張投影片匯出成圖檔，我們可以將PowerPoint的Com元件加入參考。

![image_thumb.png](/images/posts/28b5cc09-7376-43e5-aeec-0aaee81d3419/image_thumb.png)

撰寫如下的程式：

```csharp
void ConvertPptToJpg(string file, string outputPath)
{
	var application = new Microsoft.Office.Interop.PowerPoint.Application();

	var ppt = application.Presentations.Open(file, MsoTriState.msoFalse, MsoTriState.msoFalse, MsoTriState.msoFalse);

	var index = 0;
	var fileName = Path.GetFileNameWithoutExtension(file);
	foreach (Slide slid in ppt.Slides)
	{
		++index;
		slid.Export(Path.Combine(outputPath, string.Format("{0}{1}.jpg", fileName, index)), "jpg", Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height);
	}

	ppt.Close();
	application.Quit();
	GC.Collect();
}
```

程式碼很簡單，就是建立出PowerPoint應用程式後，讓PowerPoint應用程式將投影片檔案開啟，開啟時設定不顯示視窗，然後遍巡所有的投影片匯出，匯出時帶入匯出的檔案位置以及想要的解析度大小，做完後再將PowerPoint檔及應用程式關閉。

實際將投影片位置以及匯出檔案存放的位置帶入

```csharp
...
ConvertPptToJpg(@"C:\Users\larry\Desktop\Win8 Screen Capture.pptx", @"c:\");
...
```

可以看到投影片如我們預期的轉成一張張的圖檔。

![image_thumb_1.png](/images/posts/28b5cc09-7376-43e5-aeec-0aaee81d3419/image_thumb_1.png)

這邊也可以進一步用Late-Binding的方式處理，效果一樣。

```csharp
private void NAR(object o)
{
	try
	{
		while ((Marshal.ReleaseComObject(o) > 0) || (Marshal.FinalReleaseComObject(o) > 0))
		{
		}
	}
	catch
	{
	}
	finally
	{
		o = null;
	}
}

void ConvertPptToJpg(string file, string outputPath)
{
	Type t = Type.GetTypeFromProgID("PowerPoint.Application");
	object o = Activator.CreateInstance(t);

	object p = t.InvokeMember(
		"Presentations",
		BindingFlags.Public | BindingFlags.GetProperty,
		null, o, null, null);

	Type t2 = p.GetType();
	object ppt = t2.InvokeMember("Open",
		BindingFlags.Public | BindingFlags.InvokeMethod,
		null, p, new object[] { file, 0, 0, 0 }, null);

	object slides = t2.InvokeMember(
	"Slides",
	BindingFlags.Public | BindingFlags.GetProperty,
	null, ppt, null, null);

	var index = 0;
	var fileName = Path.GetFileNameWithoutExtension(file);
	foreach (object slid in (slides as IEnumerable))
	{
		++index;
		var slidType = slid.GetType();
		slidType.InvokeMember("Export",
		BindingFlags.Public | BindingFlags.InvokeMethod,
		null, slid, new object[] { Path.Combine(outputPath, string.Format("{0}{1}.jpg", fileName, index)), "jpg", Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height }, null);
		NAR(slid);
	}

	NAR(p);
	p = null;

	NAR(slides);
	slides = null;

	t2.InvokeMember("Close",
		BindingFlags.Public | BindingFlags.InvokeMethod,
		null, ppt, null, null);

	NAR(ppt);
	ppt = null;

	t.InvokeMember(
		"Quit",
		BindingFlags.Public | BindingFlags.InvokeMethod,
		null, o, null, null);

	NAR(o);
	o = null;

	GC.Collect();
}
```

## Link

* How to convert PowerPoint (.ppt, .pptx) to several images of each slide?
