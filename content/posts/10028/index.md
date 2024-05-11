---
title: "[C#][VB.NET]使用Nothing或Null作數值運算"
slug: "[CSharp][VB.NET]使用Nothing或Null作數值運算"
date: "2009-08-13 09:02:18"
description: "[C#][VB.NET]使用Nothing或Null作數值運算"
tags: [VB.NET, CSharp]
---

<p>今天突然發現VB.NET的Nothing可以拿來作運算，因此作了一點小實驗。意外發現VB.NET與C#在相同的程式邏輯下會跑出不一樣的結果。</p>  <p> </p>  <p>以VB.NET來說，假設我們拿Nothing來跟數值作運算</p>  <div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:cd7fc944-e1bc-426e-a534-ca50f7a1e39a" class="wlWriterSmartContent">   <pre class="vb:nocontrols" name="code">        Console.WriteLine(0 + Nothing)
        Console.WriteLine(0 - Nothing)
        Console.WriteLine(1 * Nothing)
        Console.WriteLine(1 / Nothing)
        Console.WriteLine(2 ^ Nothing)</pre>
</div>

<p> </p>

<p>則我們會得到像下面的執行結果
  <br /><img style="border-bottom: 0px; border-left: 0px; display: inline; border-top: 0px; border-right: 0px" title="image" border="0" alt="image" src="\images\posts\10028\image_thumb.png" width="409" height="207" /> </p>

<p> </p>

<p>可以發現Nothing在VB.NET中作數值運算時會先被轉換成0後再來處理。讓我們來確認一下</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:798ea6f8-72cb-43de-854d-371600ec53aa" class="wlWriterSmartContent">
  <pre class="vb:nocontrols" name="code">        Console.WriteLine(0 = Nothing)
        Console.WriteLine(1 = Nothing)</pre>
</div>

<p> </p>

<p>結果發現Nothing真的被當作0來處理</p>

<p><img style="border-right-width: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" title="image" border="0" alt="image" src="\images\posts\10028\image1_thumb.png" width="504" height="193" /></p>

<p> </p>

<p>再來看一下C#程式</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:8f35270b-735b-4593-a561-531fe32c4c61" class="wlWriterSmartContent">
  <pre class="c#:nocontrols" name="code">            Console.WriteLine(0 + null);
            Console.WriteLine(0 - null);
            Console.WriteLine(1 * null);
            Console.WriteLine(1 / null);
            Console.WriteLine(2 ^ null);</pre>
</div>

<p> </p>

<p>執行後會得到像下面這樣</p>

<p><img style="border-right-width: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" title="image" border="0" alt="image" src="\images\posts\10028\image_thumb.png" width="504" height="206" /></p>

<p> </p>

<p>完全看不到任何東西，猜測應該是運算後被變成null了。做個簡單的實驗看看就知道了</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:0313ffb6-170f-40d6-9d9b-e2b67167510c" class="wlWriterSmartContent">
  <pre class="c#:nocontrols" name="code">Console.WriteLine((0 + null) == null);</pre>
</div>

<p> </p>

<p>運行後可以證明真的被轉為null了</p>

<p><img style="border-right-width: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" title="image" border="0" alt="image" src="\images\posts\10028\image15_thumb.png" width="504" height="188" /></p>
