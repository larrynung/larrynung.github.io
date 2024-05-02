---
title: "Double.Parse、Double.TryParse、IsNumeric 使用注意事項"
date: "2013-11-06 12:00:00"
description: "Double.Parse、Double.TryParse、IsNumeric 使用注意事項"
---

<p>筆者今天根據[VB.NET]IsNumeric()'s bug?!這篇網友的回應嘗試使用IsNumeric("不是一個數字")下去測試，回傳的值會是True，執行結果不怎麼如我所預期，且將字串改成"不是兩個數字"、"是一個數字"...卻還都是False。研究後才發現到Double.Parse、Double.TryParse、IsNumeric這三個用爛了的方法，使用上還是有些小細節需要特別注意。</p>  <p> </p>  <p>這邊筆者寫了一個簡單的範例來示範一下：</p>  <div id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:40a7b103-b776-473c-96cd-8a3030896500" class="wlWriterSmartContent" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px"><pre name="code" class="c#">Imports System.Linq.Expressions

Module Module1

    Sub Main()
        Dim values = New String() {"不是一個數字", "正無窮大", "負無窮大"}
        For Each value In values
            Dim convertedValue = 0.0

            Dim result = Double.TryParse(value, convertedValue)

            Console.WriteLine("value: {0}", value)
            Console.WriteLine("Double.TryParse(value, convertedValue): {0} ({1})", result, convertedValue)
            Console.WriteLine("Double.Parse(value): {0}", Double.Parse(value))
            Console.WriteLine("IsNumeric(value): {0}", IsNumeric(value))

            Console.WriteLine(New String("=", 78))
        Next
    End Sub

End Module</pre></div>

<p> </p>

<p>運行結果會像下面這樣，可以看到"不是一個數字"、"正無窮大"、"負無窮大"...這些跟系統訊息比較相關的字串會被成功地轉換。</p>

<p><img style="border-left-width: 0px; border-right-width: 0px; border-bottom-width: 0px; border-top-width: 0px" border="0" alt="image" src="\images\posts\9aabfe74-18c5-4351-af67-cf16a75bd76a\image_thumb.png" width="681" height="367" /></p>

<p> </p>

<p>用監看式去看會更為清楚，分別會被替換為-1.#IND、1.#INF、-1.#INF。</p>

<p><img style="border-left-width: 0px; border-right-width: 0px; border-bottom-width: 0px; border-top-width: 0px" border="0" alt="image" src="\images\posts\9aabfe74-18c5-4351-af67-cf16a75bd76a\image_thumb_1.png" width="644" height="224" /></p>

<p> </p>

<p>若有興趣研究為甚麼會有這樣的現象，可進一步去查看.NET底層Number.ParseDouble的實作。</p>

<p><img style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" border="0" alt="image" src="\images\posts\9aabfe74-18c5-4351-af67-cf16a75bd76a\image_thumb_2.png" width="644" height="473" /></p>
