---
title: "[C#]如何為程式加上Windows的SendTo功能支援"
slug: "[CSharp]如何為程式加上Windows的SendTo功能支援"
date: "2013-11-06 12:00:00"
description: "相信大家都有看過，當我們在檔案總管上的任一檔案或是目錄上點選滑鼠右鍵，彈出的滑鼠右鍵選單中有個叫做SendTo的功能，可以將檔案送至對應的應用程式處理。要在應用程式中加上SendTo功能的支援，"
---

相信大家都有看過，當我們在檔案總管上的任一檔案或是目錄上點選滑鼠右鍵，彈出的滑鼠右鍵選單中有個叫做SendTo的功能，可以將檔案送至對應的應用程式處理。要在應用程式中加上SendTo功能的支援，我們必須要先知道其實SendTo功能跟前面筆者所介紹的[C#]如何取出最近在Windows上所使用的文件檔案這篇Recent Items是類似的處理方式。它也是以在特定目錄中放入檔案捷徑來達成這樣的效果，只是SendTo功能它對應的檔案目錄是在%APPDATA%\Microsoft\Windows\SendTo這個位置。

除了鍵入%APPDATA%\Microsoft\Windows\SendTo這個目錄位置外，我們也可以透過在執行對話框中鍵入shell:sendto跳至對應的目錄。

![image_thumb.png](/images/posts/d5a7723a-f9b5-4ed7-aea8-97793afadccb/image_thumb.png)

不論用哪種方式我們都可以找到其對應的目錄。開啟對應的目錄後，我們可以發現如上面所介紹的，裡面存放的幾乎都是捷徑檔案，而且這些捷徑都是在SendTo選單可以看到的選單選項。

![image_thumb_1.png](/images/posts/d5a7723a-f9b5-4ed7-aea8-97793afadccb/image_thumb_1.png)

因此我們要讓程式加上SendTo功能的支援，我們只要在對應的目錄中產生捷徑，像是下面這樣：

```csharp
...
CreateSendToShortCut("test.lnk", @"C:\Users\larry\Dropbox\Software\FSCapture v5.3.exe");
...

private static void CreateShortCut(string shortCutFile, string targetPath, string description = "")
{
    var type = Type.GetTypeFromProgID("WScript.Shell");
    object instance = Activator.CreateInstance(type);
    var result = type.InvokeMember("CreateShortCut", BindingFlags.InvokeMethod, null, instance, new object[] { shortCutFile });

    type = result.GetType();
    type.InvokeMember("TargetPath", BindingFlags.SetProperty, null, result, new object[] { targetPath });
    type.InvokeMember("Description", BindingFlags.SetProperty, null, result, new object[] { description });
    type.InvokeMember("Save", BindingFlags.InvokeMethod, null, result, null);
}

private static void CreateSendToShortCut(string shortCutFileName, string targetPath, string description = "")
{
    var sendToFolderPath = Environment.GetFolderPath(Environment.SpecialFolder.SendTo);
    var shortCutFile = Path.Combine(sendToFolderPath, shortCutFileName);
    CreateShortCut(shortCutFile, targetPath, description);
}
```

運行後若程式沒甚麼錯誤，我們應該在對應的目錄中會看到剛剛所建立的捷徑檔。

![image_thumb_2.png](/images/posts/d5a7723a-f9b5-4ed7-aea8-97793afadccb/image_thumb_2.png)

SendTo選單中也會多出我們所加進去的項目。

![image_thumb_3.png](/images/posts/d5a7723a-f9b5-4ed7-aea8-97793afadccb/image_thumb_3.png)

接著我們只要在我們的程式啟動時，依啟動的參數做些處理，像是把參數帶給已經開啟的程式處理緒，或是依照所帶入的檔案與目錄位置做些處理，這邊大家應該都很了解，筆者就不對此多做說明。

若是程式是透過Wix部屬，我們也可以改利用內建的功能來建立捷徑，像是下面這樣指定在SendToFolder中加入一個捷徑：

```xml
...
<Directory Id="TARGETDIR" Name="SourceDir" DiskId="1">
  ...
  <Directory Id="SendToFolder" Name="SendTo">
    <Component Id="SendToShortcut" Guid="{EFA4DF70-B9D3-417D-BAE6-FA3445A6E5E2}">
      <RegistryValue Root="HKCU" Key="SOFTWARE\$(var.AppCode)\SendToShortcut" Type="string" Value="SendToShortcut" KeyPath="yes"/>
      <Shortcut Id="SendToShortCut" Name="!(loc.APPNAME)" WorkingDirectory="INSTALLDIR" Target="[INSTALLLOCATION]WindowsClient.exe"></Shortcut>
    </Component>
  </Directory>
  ...
</Directory>
...
```

## Link

* Making a Send To Shortcut
* Customize the Windows 7 or Vista Send To Menu
