---
layout: post
title: "[C#]如何為程式加上Windows的SendTo功能支援"
date: 2013-11-06 12:00:00
comments: true
categories: 
description: "[C#]如何為程式加上Windows的SendTo功能支援"
---
<p>相信大家都有看過，當我們在檔案總管上的任一檔案或是目錄上點選滑鼠右鍵，彈出的滑鼠右鍵選單中有個叫做SendTo的功能，可以將檔案送至對應的應用程式處理。要在應用程式中加上SendTo功能的支援，我們必須要先知道其實SendTo功能跟前面筆者所介紹的[C#]如何取出最近在Windows上所使用的文件檔案</a>這篇Recent Items是類似的處理方式。它也是以在特定目錄中放入檔案捷徑來達成這樣的效果，只是SendTo功能它對應的檔案目錄是在%APPDATA%\Microsoft\Windows\SendTo這個位置。</p>  <p> </p>  <p>除了鍵入%APPDATA%\Microsoft\Windows\SendTo這個目錄位置外，我們也可以透過在執行對話框中鍵入shell:sendto跳至對應的目錄。</p>  <p><a href="http://files.dotblogs.com.tw/larrynung/1301/46e43cb2128a_12DAB/image_2.png"><img style="border-left-width: 0px; border-right-width: 0px; border-bottom-width: 0px; border-top-width: 0px" border="0" alt="image" src="\images\posts\d5a7723a-f9b5-4ed7-aea8-97793afadccb\image_thumb.png" width="417" height="217" /></a> </p>  <p> </p>  <p>不論用哪種方式我們都可以找到其對應的目錄。開啟對應的目錄後，我們可以發現如上面所介紹的，裡面存放的幾乎都是捷徑檔案，而且這些捷徑都是在SendTo選單可以看到的選單選項。</p>  <p><a href="http://files.dotblogs.com.tw/larrynung/1301/46e43cb2128a_12DAB/image_4.png"><img style="border-left-width: 0px; border-right-width: 0px; border-bottom-width: 0px; border-top-width: 0px" border="0" alt="image" src="\images\posts\d5a7723a-f9b5-4ed7-aea8-97793afadccb\image_thumb_1.png" width="644" height="378" /> </p>  <p> </p>  <p>因此我們要讓程式加上SendTo功能的支援，我們只要在對應的目錄中產生捷徑，像是下面這樣：</p>  <div id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:36360ea8-3d68-4ea7-ab07-c4b7a50c3e7d" class="wlWriterSmartContent" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px"><pre name="code" class="c#">        ...
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
        }</pre></div>

<p> </p>

<p>運行後若程式沒甚麼錯誤，我們應該在對應的目錄中會看到剛剛所建立的捷徑檔。</p>

<p><img style="border-left-width: 0px; border-right-width: 0px; border-bottom-width: 0px; border-top-width: 0px" border="0" alt="image" src="\images\posts\d5a7723a-f9b5-4ed7-aea8-97793afadccb\image_thumb_2.png" width="644" height="378" /> </p>

<p> </p>

<p>SendTo選單中也會多出我們所加進去的項目。</p>

<p><img style="border-left-width: 0px; border-right-width: 0px; border-bottom-width: 0px; border-top-width: 0px" border="0" alt="image" src="\images\posts\d5a7723a-f9b5-4ed7-aea8-97793afadccb\image_thumb_3.png" width="622" height="278" /> </p>

<p> </p>

<p>接著我們只要在我們的程式啟動時，依啟動的參數做些處理，像是把參數帶給已經開啟的程式處理緒，或是依照所帶入的檔案與目錄位置做些處理，這邊大家應該都很了解，筆者就不對此多做說明。</p>

<p> </p>

<p>若是程式是透過Wix部屬，我們也可以改利用內建的功能來建立捷徑，像是下面這樣指定在SendToFolder中加入一個捷徑：</p>

<div id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:82560e72-8a6c-4034-baae-465ac770b695" class="wlWriterSmartContent" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px"><pre name="code" class="xml">    ...
    &lt;Directory Id="TARGETDIR" Name="SourceDir" DiskId="1"&gt;
      ...
      &lt;Directory Id="SendToFolder" Name="SendTo"&gt;
        &lt;Component Id="SendToShortcut" Guid="{EFA4DF70-B9D3-417D-BAE6-FA3445A6E5E2}"&gt;
          &lt;RegistryValue Root="HKCU" Key="SOFTWARE\$(var.AppCode)\SendToShortcut" Type="string" Value="SendToShortcut" KeyPath="yes"/&gt;
          &lt;Shortcut Id="SendToShortCut" Name="!(loc.APPNAME)" WorkingDirectory="INSTALLDIR" Target="[INSTALLLOCATION]WindowsClient.exe"&gt;&lt;/Shortcut&gt;
        &lt;/Component&gt;
      &lt;/Directory&gt;
      ...
    &lt;/Directory&gt;
    ...</pre></div>

<p> </p>

<h2>Link</h2>

<ul>
  <li>Making a Send To Shortcut </li>

  <li>Customize the Windows 7 or Vista Send To Menu </li>
</ul>