---
title: "[C#]快速將字串轉換為結構"
date: "2011-03-19 09:20:12"
description: "[C#]快速將字串轉換為結構"
tags: [CSharp]
---

<p>看到MSDN上請問將一個字串copy到一個結構中最快的方式為何?這篇的發問，做些紀錄：</p>  <p> </p>  <p>要將字串快速轉換為結構，首先我們必須要在結構上加些Attribute，像是設定每個欄位所佔用的型態、大小...等：</p>  <pre>[StructLayout(LayoutKind.Sequential, CharSet = CharSet.Unicode)]<br />public struct MyStruct<br />{<br />    [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 4)]<br />    public string fname;<br />    [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 4)]<br />    public string lname;<br />    [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 7)]<br />    public string phone;<br />}</pre>

<p> </p>

<p>在轉換時先透過Marshal.StringToBSTR將字串轉為指標，再透過Marshal.PtrToStructure將指標轉換為指定的結構型態，最後再用Marshal.FreeBSTR把剛剛的指標位置給釋放掉就可以了：</p>

<pre>private static T ConvertToStruct&lt;T&gt;(string val)<br />{<br />    IntPtr valPoint = Marshal.StringToBSTR(val);<br />    T ret = (T)Marshal.PtrToStructure(valPoint, typeof(T));<br />    Marshal.FreeBSTR(valPoint);<br />    return ret;<br />}</pre>

<p> </p>

<p>完整範例如下：</p>

<pre>using System;<br />using System.Collections.Generic;<br />using System.Linq;<br />using System.Text;<br />using System.IO;<br />using System.Runtime.InteropServices;<br /> <br />namespace ConsoleApplication20<br />{<br />    class Program<br />    {<br />        [StructLayout(LayoutKind.Sequential, CharSet = CharSet.Unicode)]<br />        public struct MyStruct<br />        {<br />            [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 4)]<br />            public string fname;<br />            [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 4)]<br />            public string lname;<br />            [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 7)]<br />            public string phone;<br />        }<br /> <br />        private static T ConvertToStruct&lt;T&gt;(string val)<br />        {<br />            IntPtr valPoint = Marshal.StringToBSTR(val);<br />            T ret = (T)Marshal.PtrToStructure(valPoint, typeof(T));<br />            Marshal.FreeBSTR(valPoint);<br />            return ret;<br />        }<br /> <br />        public static void Main()<br />        {<br />            MyStruct ms = ConvertToStruct&lt;MyStruct&gt;("abcdefgh2223333");<br />            Console.WriteLine("fname is: {0}", ms.fname);<br />            Console.WriteLine("lname is: {0}", ms.lname);<br />            Console.WriteLine("phone is: {0}", ms.phone);          <br />        }<br />    }<br />}<br /></pre>

<p> </p>

<p>運行後可以發現abcdefgh2223333字串會依照我們在結構欄位所設定的長度自動填入：</p>

<p><img style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" border="0" alt="image" src="\images\posts\21957\image_thumb.png" width="417" height="159" /> </p>

<p> </p>

<h2>Link</h2>

<ul>
  <li>How to copy a String into a struct using C#</li>

  <li>請問將一個字串copy到一個結構中最快的方式為何?</li>
</ul>
