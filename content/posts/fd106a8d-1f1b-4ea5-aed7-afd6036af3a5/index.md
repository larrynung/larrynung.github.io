---
title: "[C#]使用Windows API Code Pack存取媒體櫃內存放的資料"
date: "2013-11-06 12:00:00"
description: "[C#]使用Windows API Code Pack存取媒體櫃內存放的資料"
tags: [CSharp]
---

<p>要用程式存取媒體櫃內存放的資料，我們大概可以有兩種方法，一種是自行解析，一種則是使用包好的函式庫(像是Windows API Code Pack)去作控制。之所以能夠自行解析是因為媒體櫃的資訊是存放在附檔名為.library-ms的XML檔案中。</p>  <p><img style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" border="0" alt="image" src="\images\postsd106a8d-1f1b-4ea5-aed7-afd6036af3a5\image_thumb.png" width="642" height="304" /></a> </p>  <p> </p>  <p>可以看到裡面有很多資訊存放在裡面，而我們最關心的目錄位置也在其中。</p>  <p><a href="http://files.dotblogs.com.tw/larrynung/1208/347b5a527747_124A6/image_4.png"><img style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" border="0" alt="image" src="\images\postsd106a8d-1f1b-4ea5-aed7-afd6036af3a5\image_thumb_1.png" width="562" height="484" /></a> </p>  <p> </p>  <p>這邊不再對自行解析多作解釋，只要會了解格式與熟悉XML的操作應該都沒問題。而若是使用Windows API Code Pack來做，我們需要將Microsoft.WindowsAPICodePack.dll以及Microsoft.WindowsAPICodePack.Shell.dll這兩個組件加入參考。</p>  <p><a href="http://files.dotblogs.com.tw/larrynung/1208/347b5a527747_124A6/image_6.png"><img style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" border="0" alt="image" src="\images\postsd106a8d-1f1b-4ea5-aed7-afd6036af3a5\image_thumb_2.png" width="284" height="110" /> </p>  <p> </p>  <p>加入參考後加入命名空間Microsoft.WindowsAPICodePack.Shell，就可以開始程式的撰寫。</p>  <div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:6bfb0439-5677-4771-a1ad-05d9d2962cef" class="wlWriterSmartContent"><pre name="code" class="c#">using Microsoft.WindowsAPICodePack.Shell;</pre></div>

<p> </p>

<p>使用Windows API Code Pack來操作媒體櫃主要要用到ShellLibrary這個類別，若要建立一個新的媒體櫃，很簡單的建立一個ShellLibrary物件就可以了，建立時要帶入新媒體櫃的名稱。</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:405e4f35-f11f-4c0e-8ebc-6883899790e2" class="wlWriterSmartContent"><pre name="code" class="c#">			using (ShellLibrary library = new ShellLibrary(libraryName, true))
			{
			...
			}</pre></div>

<p> </p>

<p>而若是要載入現有的媒體櫃，則可以呼叫ShellLibrary.Load，帶入要載入的媒體櫃名稱。</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:5a88be69-1b46-49e8-a780-2a4f8941f7fe" class="wlWriterSmartContent"><pre name="code" class="c#">using (ShellLibrary shellLibrary =
    ShellLibrary.Load(libraryName, folderPath, isReadOnly))
{
...
}</pre></div>

<p> </p>

<p>不論是建立還是載入媒體櫃，我們都可以拿到ShellLibrary的物件實體，透過這個物件實體我們可以針對媒體櫃做增刪目錄等進階的操作。</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:a433d9d9-53ad-47fa-8a7f-99e1cfd3cb73" class="wlWriterSmartContent"><pre name="code" class="c#">...
shellLibrary.Remove(folderToRemove);
shellLibrary.Add(folderToAdd);
...</pre></div>

<p> </p>

<p>若是要遍巡找出媒體櫃內有哪些目錄及檔案，可以直接對取得的ShellLibrary物件實體去遍巡，這邊要注意的是，遍巡的元素可能是ShellFolder，也有可能是ShellFile，若有需要ShellFolder還必須再另行處理。</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:eb234f2e-0691-4ec9-a0a5-966efe2689d1" class="wlWriterSmartContent"><pre name="code" class="c#">			...
			using (ShellLibrary library = ShellLibrary.Load("Pictures", false))
			{
				foreach (ShellFolder folder in library)
				{
					var folderPath = folder.ParsingName;
					Console.WriteLine(folderPath);
				}
			}
			...</pre></div>

<p> </p>

<p><img style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" border="0" alt="image" src="\images\postsd106a8d-1f1b-4ea5-aed7-afd6036af3a5\image_thumb_3.png" width="644" height="225" /> </p>

<p> </p>

<h2>Link</h2>

<ul>
  <li>Windows 7 Libraries C# Quick Reference</li>

  <li>如何以程式設計方式操作 Windows 7 殼層文件庫</li>
</ul>
