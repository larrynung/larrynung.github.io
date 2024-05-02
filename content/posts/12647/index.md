---
title: "[VB.NET]IsNumeric()'s bug?!"
date: "2009-12-24 09:03:21"
description: "[VB.NET]IsNumeric()'s bug?!"
tags: [VB.NET]
---

<p>前陣子因為需要用同事的Code，發現同事在判斷是否是數值的部份自己寫了一道函式。詢問了一下為何不用內建的IsNumeric?她回答道：「微軟內建的有Bug」，傳入字串都會判斷錯誤。</p>  <p> </p>  <p>但…真的有Bug嗎?好奇之下稍稍看了一下。發現那並不是Bug，原來只是內建的IsNumeric比我們想的還聰明而已。</p>  <p> </p>  <p>看看MSDN就可以發現一點端倪。</p>  <p><img style="border-bottom: 0px; border-left: 0px; display: inline; border-top: 0px; border-right: 0px" title="image" border="0" alt="image" src="\images\posts\12647\image_thumb.png" width="310" height="66" /> </p>  <p> </p>  <p>函式的說明寫的是"是否可做為數字來評估"。因此看起來，我們一般常見能經過處理變為數值的字串，呼叫IsNumeric函式，都會回傳True。</p>  <p> </p>  <p>.NET內建的IsNumeric會接受","當作千位分隔符號、接受"+"與"-"當作正負號、接受字串中含有一個逗點當作小數點、接受"e"當作科學符號、接受括弧、與八進制和十六進制的數值字串。</p>  <p> </p>  <p>測試Code如下：    <br /></p>  <div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:6cbdf2d3-e1ee-43f9-866b-83fb7cd7f7e9" class="wlWriterEditableSmartContent"><pre name="code" class="c#:nocontrols">    Sub Main()
        Dim testStrings() As String = {"123,，", "1,，23", "123,", "123，", "123,000", "1.23", "+123", "-123", "12e3", "2d3", "&amp;H0A", "&amp;6", "(123)", "￥12.3"}
        Dim value As Decimal
        For Each testString As String In testStrings
            Console.Write(testString &amp; " : ")
            Console.Write(IsNumeric(testString).ToString() &amp; vbTab)
            Console.WriteLine("value : " &amp; If(Decimal.TryParse(testString, value), value.ToString, String.Empty))
        Next
    End Sub</pre></div>

<p />

<p />

<p />

<p> </p>

<p>運行結果如下： 
  <br /><img style="border-right-width: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" title="image" border="0" alt="image" src="\images\posts\12647\image_thumb_1.png" width="513" height="351" />   </p>

<p> </p>

<h2>Link</h2>

<ul>
  <li>IsNumeric 函式 (Visual Basic) </li>

  <li>我认为isnumeric()函数有bug,不知大家以为如何,有例子 </li>

  <li>让我意外的IsNumeric()函数 </li>
</ul>
