---
title: "[.Net Resource]Mono Migration Analyzer (MoMA)"
date: "2010-08-03 11:44:53"
description: "[.Net Resource]Mono Migration Analyzer (MoMA)"
tags: [.NET Resource]
---

<p>Mono Migration Analyzer (MoMA)工具主要功能為偵測.NET應用程式是否可以被移轉到Mono上面，可幫助我們找到應用程式中有用到的平台叫用或是Mono尚未支援的部分。</p>  <p> </p>  <h2>如何使用</h2>  <h3>Step1.歡迎畫面，按下[Next]繼續。</h3>  <p><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" src="\images\posts\16997\image_thumb.png" width="644" height="444" /></p>  <p> </p>  <h3>Step2.加入要偵測的組件，選取要測試的Mono版本，按下[Next]繼續。</h3>  <p><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" src="\images\posts\16997\image3_thumb.png" width="644" height="444" /></a></p>  <p> </p>  <h3>Step3.該頁面會顯示分析完的結果，若有錯誤可按下下方的<em>View Detail Report</em>超連結觀看錯誤報表，或按下[Next]繼續。</h3>  <p><a href="http://files.dotblogs.com.tw/larrynung/1008/bfb9b85eb192_14EDC/image6.png"><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" src="\images\posts\16997\image6_thumb.png" width="644" height="444" /></a> </p>  <p><a href="http://files.dotblogs.com.tw/larrynung/1008/bfb9b85eb192_14EDC/image9.png"><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" src="\images\posts\16997\image9_thumb.png" width="626" height="484" /></a></p>  <p> </p>  <h3>Step4.該頁面能將看不懂的錯誤訊息反饋，可向Mono團隊尋求幫助，或按下[Next]繼續。</h3>  <p><a href="http://files.dotblogs.com.tw/larrynung/1008/bfb9b85eb192_14EDC/image12.png"><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" src="\images\posts\16997\image12_thumb.png" width="644" height="444" /></a></p>  <p> </p>  <h3>Step5.按下[Close]關閉。</h3>  <p><a href="http://files.dotblogs.com.tw/larrynung/1008/bfb9b85eb192_14EDC/image15.png"><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" src="\images\posts\16997\image15_thumb.png" width="644" height="444" /></a></p>  <p> </p>  <h2>影響移轉的四大問題</h2>  <p>MoMA會偵測到的主要有下列四種問題 :</p>  <ol>   <li>Missing Methods </li>    <li>MonoTodo </li>    <li>NotImplementedException </li>    <li>P/Invokes </li> </ol>  <p> </p>  <h3>Missing Methods</h3>  <p>該問題是因為使用的方法在Mono中尚未實作。依照編譯器的不同可能會看到不同的錯誤訊息，像是用Mono編譯的話，在編譯時就會報錯，可看到下列的訊息：</p>  <p>myfile.cs(22,16): error CS0117: 'xxxxxxxxxxxxxxxxx' does not contain a definition for 'xxxxxxxxxxxxxxx'</p>  <p> </p>  <p>而如果用微軟編譯器編輯的話，則必須執行到該方法處才會跳出MissingMethodException的例外：</p>  <p>System.MissingMethodException: Method not found: xxxxxxxxxxxxxxxxxxx</p>  <p> </p>  <p><a name="MonoTodo"></a></p>  <h3>MonoTodo</h3>  <p>該問題是因為應用程式中存在標記有MonoTodo的方法。這標記是用來提醒開發人員尚須處理的地方，通常這代表著方法尚未實做完全，或是實做完後開發者忘了將該標記移除。</p>  <p><a name="NotImplementedException"></a></p>  <p> </p>  <h3>NotImplementedException</h3>  <p>該問題是因為應用程式中存在會丟出NotImplementedException的方法。</p>  <p><a name="P.2FInvokes"></p>  <p> </p>  <h3>P/Invokes</h3>  <p>該問題是因為應用程式中存在著平台叫用。平台叫用通常是用來呼叫非託管的方法，尤其是平台本身提供的方法。</p>  <p> </p>  <h2>命令列執行</h2>  <p>MoMa從1.9版開始就已支援命令列執行的功能。</p>  <p>若要用命令列設定要偵測的組件並開啟MoMa，可以像下面這樣：</p>  <div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:f7c8f370-857d-46f0-b594-35b600c03c6b" class="wlWriterSmartContent"><pre name="code" class="xml">MoMA C:pp\myapp.exe</pre></div>

<p> </p>

<p>若要用設定加入多個要偵測的組件並開啟MoMa，可以像下面這樣：</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:71dfc44b-6e97-4a60-b5f0-3ed5755bb0d1" class="wlWriterSmartContent"><pre name="code" class="xml">MoMA C:pp\myapp.exe C:pp\myapp.dll C:pp\myapp2.dll</pre></div>

<p> </p>

<p>若不想帶出MoMa介面，可透過--nogui設定並指派組件的位置，像是：</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:8f6f012c-f032-4f66-a118-b19ca9bf480d" class="wlWriterSmartContent"><pre name="code" class="xml">MoMA --nogui C:pp\myapp.exe</pre></div>

<p> </p>

<p>執行完後，在命令提示字元看不到任何訊息，須自行開啟報表查看，其報表會存放在MoMa目錄下的Reports目錄內。若要自行指定報表位置，可透過--out來設定，並指派輸出的報表檔位置，像是：</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:d08597fd-8253-40d6-857e-105a48dbc573" class="wlWriterSmartContent"><pre name="code" class="xml">MoMA --nogui --out C:pp\momareporteport.html C:pp\myapp.exe</pre></div>

<pre> </pre>

<h2>Link</h2>

<ul>
  <li>MoMA </li>

  <li>Guide: Using MoMA </li>

  <li>Guide: Fixing issues MoMA finds </li>

  <li>Guide: Run MoMA from command line (automated builds, etc.) </li>

  <li>介紹好用工具：Mono Migration Analyzer (MoMA) </li>
</ul>
