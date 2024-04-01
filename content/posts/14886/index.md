---
title: "[VB.NET]Keys lt;=gt; Char"
date: "2010-04-27 11:46:52"
description: "[VB.NET]Keys &lt;=&gt; Char"
tags: [VB.NET]
---

<p>今天在撰寫控制項的KeyPress事件，由於事件的參數無法點出Keys直接比對，做了一些轉換動作，這邊紀錄一下：</p>  <p> </p>  <p>要把Keys轉換成Char，可以使用Convert.ToChar</p>  <div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:afe9f100-272f-4ef9-946e-6f5623ed8e4c" class="wlWriterEditableSmartContent"><pre name="code" class="vb">Dim keyChar As Char = Convert.ToChar(key)</pre></div>

<p> </p>

<p>或是ChrW函式</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:9e125732-db7c-44c0-b678-2c898793fdeb" class="wlWriterEditableSmartContent"><pre name="code" class="vb">Dim keyChar As Char = Microsoft.VisualBasic.ChrW(key)</pre></div>

<p> </p>

<p>而要把Char轉成Keys則可以使用Asc函式</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:a4ddefc5-9a03-476e-b1be-8733a2dbd61a" class="wlWriterEditableSmartContent"><pre name="code" class="vb">Dim key As Keys = Asc(keyChar)</pre></div>

<p> </p>

<p />

<p />

<p>簡易範例如下</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:cf604067-7349-45c7-b8f9-f13794b7939a" class="wlWriterEditableSmartContent"><pre name="code" class="vb">Imports System.Windows.Forms

Module Module1

    Sub Main()
        Dim key As Keys = Keys.A
        Dim keyChar As Char = Convert.ToChar(key)

        Console.WriteLine(Convert.ToChar(key))
        Console.WriteLine(Asc(keyChar))
        Console.WriteLine(Microsoft.VisualBasic.ChrW(key))
    End Sub

End Module</pre></div>
