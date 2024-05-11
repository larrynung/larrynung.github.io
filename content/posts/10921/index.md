---
title: "[C#]使用DebuggerDisplayAttribute自訂除錯監看訊息"
slug: "[CSharp]使用DebuggerDisplayAttribute自訂除錯監看訊息"
date: "2009-10-06 09:01:20"
description: "[C#]使用DebuggerDisplayAttribute自訂除錯監看訊息"
tags: [CSharp]
---

<h2>Introduction</h2>  <p>DebuggerDisplayAttribute可為自己開發的類別，及其所包含的欄位與屬性，加上自訂的除錯監看訊息。</p>  <p> </p>  <h2>NameSpace</h2>  <p>System.Diagnostics</p>  <p> </p>  <h2>Assembly</h2>  <p>mscorlib (in mscorlib.dll)</p>  <p> </p>  <h2>DebuggerDisplayAttribute</h2>  <p>一般我們在除錯的時候，都會使用Visual Studio IDE所內建的監看視窗來查看變數。但一個類別內含多個成員，往往我們要查看的、常用的就是那幾個。卻要展開才能查看，十分不便。</p>  <p> </p>  <p>未展開時    <br /><img style="border-right-width: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" title="image" border="0" alt="image" src="\images\posts\10921\image_thumb.png" width="571" height="62" /></a> </p>  <p> </p>  <p>展開時    <br /><a href="http://files.dotblogs.com.tw/larrynung/0910/DebuggerDisplayAttribute_12A2D/image_4.png" rel="lightbox"><img style="border-right-width: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" title="image" border="0" alt="image" src="\images\posts\10921\image_thumb_1.png" width="568" height="93" /> </p>  <p> </p>  <p>而透過DebuggerDisplayAttribute，我們可以自訂除錯監看訊息，可把自己常看的變數資訊直接顯示。使用上很簡單，只要在類別上方或是屬性、類別的上方設定DebuggerDisplay即可。像是：    <br /></p>  <div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:3b44822d-dd0f-4f05-9808-c766a1549dd1" class="wlWriterEditableSmartContent"><pre name="code" class="c#:nocontrols">    [System.Diagnostics.DebuggerDisplay("Name = {Name}, Year = {Year}")]
    class Person</pre></div>

<p />

<p>其監看結果如下： 
  <br /><img style="border-right-width: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" title="image" border="0" alt="image" src="\images\posts\10921\image_thumb_2.png" width="572" height="59" /></p>

<p>需特別注意，DebuggerDisplayAttribute參數在設定上，要帶入成員數值的地方需用"{}"包住。 </p>

<p> </p>

<h2>Example</h2>

<p>
  <br /></p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:3451cc80-1921-4a34-903e-1ab8c2170710" class="wlWriterEditableSmartContent"><pre name="code" class="c#:nocontrols">    class Program
    {
        static void Main(string[] args)
        {
            Person larry = new Person("Larry",28);
        }
    }

    [System.Diagnostics.DebuggerDisplay("Name = {Name}, Year = {Year}")]
    class Person
    {
        [System.Diagnostics.DebuggerDisplay("Name = {Name}")]
        string Name { get; set; }
        int Year { get; set; }

        public Person(string name, int year)
        {
            this.Name = name;
            this.Year = year;
        }
    }</pre></div>

<p />

<p> </p>

<p>監看結果</p>

<p><img style="border-right-width: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" title="image" border="0" alt="image" src="\images\posts\10921\image_thumb_3.png" width="568" height="93" /></p>
