---
title: "[C#]C# 4.0 選擇性參數 (Optional Parameters)"
date: "2009-07-29 09:04:42"
description: "[C#]C# 4.0 選擇性參數 (Optional Parameters)"
tags: [CSharp]
---

<h2><img style="border-right-width: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" title="image" border="0" alt="image" src="\images\posts\9720\image_thumb_12.png" width="534" height="125" /></a></h2>  <h2>Introduction</h2>  <p>選擇性參數是C# 4.0的特色之一，可減少多載函式的建立，卻可達到相同的效果，加快使用者開發。</p>  <p> </p>  <h2>Support</h2>  <ul>   <li>C# 4.0 or latter</li> </ul>  <p> </p>  <h2>使用方式</h2>  <p>選擇性參數在使用上就跟C++一樣，只需用等號為函數的參數加上預設值即可。</p>  <p>範例程式碼片段如下：</p>  <p><a href="http://files.dotblogs.com.tw/larrynung/0908/C4.0Optionalparameters_147CF/image_14.png" rel="lightbox"><img style="border-right-width: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" title="image" border="0" alt="image" src="\images\posts\9720\image_thumb_6.png" width="275" height="20" /></a></p>  <p>在使用具有選擇性參數的函式時，IDE所彈出的提示視窗在顯示上會用中括弧包住選擇性參數，用以告知該參數為選擇性參數，且會用等號指出當未明確帶入參數時其自動帶入的參數預設值為何。</p>  <p><a href="http://files.dotblogs.com.tw/larrynung/0908/C4.0Optionalparameters_147CF/image_10.png" rel="lightbox"><img style="border-right-width: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" title="image" border="0" alt="image" src="\images\posts\9720\image_thumb_3.png" width="243" height="37" /></p>  <blockquote>   <p>在VB.NET 8.0中其實也有提供對應的用法，使用上也大同小異，只要在參數後面帶入預設值，並在參數前面加入Optional關鍵字即可。</p> </blockquote>  <p> </p>  <h2>注意事項</h2>  <p><strong>1.選擇性參數後不得存在必要性參數</strong></p>  <p>C# 4.0的選擇性參數在使用上跟其它語言一樣，除了給予預設值之外，還需注意選擇性參數要放在必要性參數的後面，也就是說選擇性參數後面不得有必要性參數的存在。</p>  <p>若是在選擇性參數後存在必要性參數的話</p>  <div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:99068e86-eb71-4a45-8135-c61819517908" class="wlWriterSmartContent">   <pre class="c#:nocontrols" name="code">public void SayHello(string name="無名氏",string msg)</pre>
</div>

<p>在編譯時就會顯示 "Optional parameters must appear after all required parameters”錯誤。</p>

<p><img style="border-right-width: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" title="image" border="0" alt="image" src="\images\posts\9720\image_thumb_2.png" width="335" height="21" /></p>

<p> </p>

<p><strong>2.了解多載函式的取用依據</strong></p>

<p>C# 4.0中的選擇性參數在使用上跟VB.NET有些不同。以VB.NET來說，當有選擇性參數的多載函式能涵蓋處理其它多載函式，或是說兩個多載函式的差異只在於選擇性參數時，Compile會提出警示，且不允許程式進行編譯。</p>

<p>簡單的範例程式碼片段如下：</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:d6afb8b2-f31b-412c-9444-1422db99a447" class="wlWriterSmartContent">
  <pre class="vb:nocontrols" name="code">    Sub SayHello()
        Console.WriteLine("Hi~")
    End Sub

    Sub SayHello(Optional ByVal name As String = "無名氏")
        Console.WriteLine("Hello~My name is " &amp; name)
    End Sub</pre>
</div>

<p> </p>

<p>警示訊息如下：</p>

<p><img style="border-right-width: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" title="image" border="0" alt="image" src="\images\posts\9720\image_thumb.png" width="378" height="47" /> </p>

<p> </p>

<p>但同樣的程式在C# 4.0中卻是可以運行的。像是下面這段程式碼片段：</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:fb3806e9-b0e1-41d4-a3f0-b1f237044d4c" class="wlWriterSmartContent">
  <pre class="c#:nocontrols" name="code">        static void Main(string[] args)
        {
            SayHello();
            SayHello("Larry");
        }
        static void SayHello()
        {
            Console.WriteLine("Hi~");
        }
        static void SayHello(String name = "無名氏")
        {
            Console.WriteLine("Hello~My name is " + name);
        }</pre>
</div>

<p> </p>

<p>不僅可以編譯成功，也可以執行。</p>

<p><img style="border-right-width: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" title="image" border="0" alt="image" src="\images\posts\9720\image_thumb_1.png" width="369" height="187" /></p>

<p> </p>

<p>以這個例子來看，其實兩個多載函式都可以處理指定的函式呼叫。雖哪個函式被呼叫都不奇怪，但若不了解其規則仍會讓人造成混亂，因此我們必需要了解其多載函式的取用依據。</p>

<p>在多載函式的取用上，C#編譯器會自動幫我們判斷最適用的多載函式。其取用順序如下：</p>

<p><img style="border-right-width: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" title="image" border="0" alt="image" src="\images\posts\9720\image_thumb_8.png" width="640" height="96" /> </p>

<p>不用轉型的函式優先取用</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:b5c04e14-0b5f-4dcc-a014-1a4a6f1eb873" class="wlWriterSmartContent">
  <pre class="c#:nocontrols" name="code">        static void Main(string[] args)
        {
            SayHello("Larry");
        }
        static void SayHello(object name)
        {
            Console.WriteLine("Hi~My name is" + name.ToString());
        }

        static void SayHello(String name = "無名氏")
        {
            Console.WriteLine("Hello~My name is " + name);
        }</pre>
</div>

<p><img style="border-right-width: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" title="image" border="0" alt="image" src="\images\posts\9720\image_thumb_4.png" width="425" height="203" /></p>

<p> </p>

<p>不用省略選擇性參數的函式優先取用</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:c4e2fa7d-89f8-47ba-9fbb-eb8ba5d0b2e5" class="wlWriterSmartContent">
  <pre class="c#:nocontrols" name="code">        static void Main(string[] args)
        {
            SayHello();
        }
        static void SayHello()
        {
            Console.WriteLine("Hi~");
        }
        static void SayHello(String name = "無名氏")
        {
            Console.WriteLine("Hello~My name is " + name);
        }</pre>
</div>

<p><img style="border-right-width: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" title="image" border="0" alt="image" src="\images\posts\9720\image_thumb_7.png" width="425" height="203" /> </p>

<p> </p>

<h2>範例程式 </h2>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:2243d885-b115-46dd-b129-4fdd5c135d4b" class="wlWriterSmartContent">
  <pre class="c#:nocontrols" name="code">using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace SayHello
{
    class Program
    {
        static void Main(string[] args)
        {
            SayHello();
            SayHello(name:"Larry");
            SayHello("Larry");
        }
        static void SayHello()
        {
            Console.WriteLine("Hi~");
        }
        static void SayHello(object name)
        {
            Console.WriteLine("Hi~My name is" + name.ToString());
        }
        static void SayHello(String name = "無名氏")
        {
            Console.WriteLine("Hello~My name is " + name);
        }
    }
}</pre>
</div>

<p>  </p>

<p>執行結果</p>

<p><img style="border-right-width: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" title="image" border="0" alt="image" src="\images\posts\9720\image_thumb_10.png" width="433" height="203" /> </p>

<p> </p>

<h2>Video</h2>

<p>下面列出一些網路上的示範影片，有興趣的可以順便看一下。</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:5737277B-5D6D-4f48-ABFC-DD9C333F4C5D:24d1a0f6-eac2-4214-b798-f150df2d05ce" class="wlWriterEditableSmartContent"><div id="5916b5d1-31b6-4eab-9f16-c8e4c371358c" style="margin: 0px; padding: 0px; display: inline;"><div><img src="\images\posts\9720ideo8a1f6f262cc1.jpg" style="border-style: none" galleryimg="no" onload="var downlevelDiv = document.getElementById('5916b5d1-31b6-4eab-9f16-c8e4c371358c'); downlevelDiv.innerHTML = &quot;&lt;div&gt;&lt;object width=\&quot;425\&quot; height=\&quot;355\&quot;&gt;&lt;param name=\&quot;movie\&quot; value=\&quot;http://www.youtube.com/v/Fas0KUzMWes&amp;hl=en\&quot;&gt;&lt;\/param&gt;&lt;embed src=\&quot;http://www.youtube.com/v/Fas0KUzMWes&amp;hl=en\&quot; type=\&quot;application/x-shockwave-flash\&quot; width=\&quot;425\&quot; height=\&quot;355\&quot;&gt;&lt;\/embed&gt;&lt;\/object&gt;&lt;\/div&gt;&quot;;" alt="" /></div></div></div>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:5737277B-5D6D-4f48-ABFC-DD9C333F4C5D:f2019be5-b1f5-4525-935d-bd96a6f24a55" class="wlWriterEditableSmartContent"><div id="222b1efa-7190-44c7-8a56-4205bfe47361" style="margin: 0px; padding: 0px; display: inline;"><div><img src="\images\posts\9720ideoab99331e5866.jpg" style="border-style: none" galleryimg="no" onload="var downlevelDiv = document.getElementById('222b1efa-7190-44c7-8a56-4205bfe47361'); downlevelDiv.innerHTML = &quot;&lt;div&gt;&lt;object width=\&quot;425\&quot; height=\&quot;355\&quot;&gt;&lt;param name=\&quot;movie\&quot; value=\&quot;http://www.youtube.com/v/vDHIPeLaREQ&amp;hl=en\&quot;&gt;&lt;\/param&gt;&lt;embed src=\&quot;http://www.youtube.com/v/vDHIPeLaREQ&amp;hl=en\&quot; type=\&quot;application/x-shockwave-flash\&quot; width=\&quot;425\&quot; height=\&quot;355\&quot;&gt;&lt;\/embed&gt;&lt;\/object&gt;&lt;\/div&gt;&quot;;" alt="" /></div></div></div>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:5737277B-5D6D-4f48-ABFC-DD9C333F4C5D:8b04ace5-1bed-4e87-93f8-3efd4ee9435c" class="wlWriterEditableSmartContent"><div id="479d17b6-f337-4de0-b8a8-406eca1631d7" style="margin: 0px; padding: 0px; display: inline;"><div><img src="\images\posts\9720ideo161ce344d569.jpg" style="border-style: none" galleryimg="no" onload="var downlevelDiv = document.getElementById('479d17b6-f337-4de0-b8a8-406eca1631d7'); downlevelDiv.innerHTML = &quot;&lt;div&gt;&lt;object width=\&quot;425\&quot; height=\&quot;355\&quot;&gt;&lt;param name=\&quot;movie\&quot; value=\&quot;http://www.youtube.com/v/8RN14Rgrw5w&amp;hl=en\&quot;&gt;&lt;\/param&gt;&lt;embed src=\&quot;http://www.youtube.com/v/8RN14Rgrw5w&amp;hl=en\&quot; type=\&quot;application/x-shockwave-flash\&quot; width=\&quot;425\&quot; height=\&quot;355\&quot;&gt;&lt;\/embed&gt;&lt;\/object&gt;&lt;\/div&gt;&quot;;" alt="" /></div></div></div>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:5737277B-5D6D-4f48-ABFC-DD9C333F4C5D:0bbb60b0-6408-46d0-9309-7d8a7dcc7905" class="wlWriterEditableSmartContent"><div id="da688b15-5d32-4d65-bba9-38af759ef6f7" style="margin: 0px; padding: 0px; display: inline;"><div><img src="\images\posts\9720ideo0725efbcc95e.jpg" style="border-style: none" galleryimg="no" onload="var downlevelDiv = document.getElementById('da688b15-5d32-4d65-bba9-38af759ef6f7'); downlevelDiv.innerHTML = &quot;&lt;div&gt;&lt;object width=\&quot;425\&quot; height=\&quot;355\&quot;&gt;&lt;param name=\&quot;movie\&quot; value=\&quot;http://www.youtube.com/v/rSekCQIDDbE&amp;hl=en\&quot;&gt;&lt;\/param&gt;&lt;embed src=\&quot;http://www.youtube.com/v/rSekCQIDDbE&amp;hl=en\&quot; type=\&quot;application/x-shockwave-flash\&quot; width=\&quot;425\&quot; height=\&quot;355\&quot;&gt;&lt;\/embed&gt;&lt;\/object&gt;&lt;\/div&gt;&quot;;" alt="" /></div></div></div>

<p> </p>

<h2>Conclusion</h2>

<p><font size="2">選擇性參數雖然不是新的概念，但對於缺少該功能的C#而言，習慣VB.NET甚至是C++的程式員來說，寫起來總是會覺得不順，在多載函式的建立上也麻煩了許多。好在這個問題在C# 4.0中已獲得改善。</font></p>

<p> </p>

<h2>Link</h2>

<ul>
  <li>C# 4.0 新特性：動態型別、選用參數、具名參數</li>

  <li>Inside C# 4.0: dynamic typing, optional parameters, covariance and contravariance</li>

  <li>C# 4.0 Optional Parameters</li>

  <li>C# 4.0 Named Parameters for better code quality</li>

  <li>New Features in C# 4.0</li>

  <li>C# 4.0's New Features Explained</li>
</ul>

<p> </p>

<p><img style="border-right-width: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" title="image" border="0" alt="image" src="\images\posts\9720\image_thumb_11.png" width="469" height="290" /></p>
