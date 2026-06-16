---
title: "[C#]如何解決在Vista以後開啟檔案FileSystemWatcher無法觸發LastAccess的問題"
slug: "csharp-如何解決在vista以後開啟檔案filesystemwatcher無法觸發lastaccess的問題"
aliases: ["/posts/csharp如何解決在vista以後開啟檔案filesystemwatcher無法觸發lastaccess的問題/"]
date: "2013-11-06 12:00:00"
description: "筆者在論壇中看到FileSystemWatcher在不同系統上的事件觸發問題這篇發問，覺得十分有趣，同樣的程式在不同的OS有不同的結果。為了確定這個問題，筆者實際撰寫了像下面這樣的測試程式做了點測試。 發現開啟檔案時在筆者的Win8是不會觸發事件的。"
tags: [CSharp]
---

筆者在論壇中看到FileSystemWatcher在不同系統上的事件觸發問題這篇發問，覺得十分有趣，同樣的程式在不同的OS有不同的結果。為了確定這個問題，筆者實際撰寫了像下面這樣的測試程式做了點測試。

```csharp
static FileSystemWatcher fw = new FileSystemWatcher();
static void Main(string[] args)
{
	fw.NotifyFilter = NotifyFilters.LastAccess;
	fw.Path = @"c:\";
	fw.Changed += fw_Changed;
	fw.EnableRaisingEvents = true;
	Console.ReadKey();
}

static void fw_Changed(object sender, FileSystemEventArgs e)
{
}
```

發現開啟檔案時在筆者的Win8是不會觸發事件的。

因此上網看了一下是不是有些系統的設定造成的，找到FileSystemWatcher.Changed Event - does it fire when a file is accessed?這篇，發現在Vista後的電腦預設是關閉更新LastAccess的，所以我們在怎麼開啟檔案，在檔案的屬性頁中他的存取日期都不會變動。像筆者在1:30幾分開啟了2.txt檔，它的存取日期也不會變動。

![image_thumb_1.png](/images/posts/754d52d6-f1e1-43b6-b711-6593cbd7d6c4/image_thumb_1.png)

要讓系統更新這個日期的話，我們必須將HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem下的NtfsDisableLastAccessUpdate給關閉，像是下面這樣設成0關閉。

![image_thumb.png](/images/posts/754d52d6-f1e1-43b6-b711-6593cbd7d6c4/image_thumb.png)

或是直接到How to Enabled or Disable Last Access Updating in Vista這網站下載它包好的登錄檔，點選兩下執行登錄檔的修改也可以。

修改後系統就會開始更新LastAccessTime了，我們一樣可以開啟檔案，然後用檔案的屬性頁來確定，這時應該存取日期會開始正常的更新。

![image_thumb_2.png](/images/posts/754d52d6-f1e1-43b6-b711-6593cbd7d6c4/image_thumb_2.png)

透過FileSystemWatcher來偵測也會正常了。

![image_thumb_3.png](/images/posts/754d52d6-f1e1-43b6-b711-6593cbd7d6c4/image_thumb_3.png)

## Link

* FileSystemWatcher在不同系統上的事件觸發問題
* FileSystemWatcher.Changed Event - does it fire when a file is accessed?
* How to Enabled or Disable Last Access Updating in Vista
