---
title: "[C#]IEnumerable型態回傳注意事項"
slug: "[CSharp]IEnumerable型態回傳注意事項"
date: "2011-03-19 08:44:03"
description: "[C#]IEnumerable型態回傳注意事項"
tags: [CSharp]
---

<p>自Linq出來以後，個人的程式撰寫習慣又因此有了些許的改變，變得習慣會盡量用IEnumerable型態去傳遞集合的資料，因為透過這樣的型態可以將集合真正的型態隱含在背後，若某天有需求要替換集合類型，動到的部份會比較少，也可以實現像Linq一樣具延遲載入的效果。</p>  <p>   <br />在前陣子開發時才發現，這樣的做法會隱藏著一些必需注意到的細節。像是使用Linq查詢：</p>  <pre>using System;<br />using System.Collections.Generic;<br />using System.Linq;<br />using System.Text;<br />using System.IO;<br /> <br />namespace ConsoleApplication20<br />{<br />    class Program<br />    {<br />        static void Main(string[] args)<br />        {<br />            IEnumerable&lt;FileInfo&gt; allDatas = GetDatas(@"c:\");<br /> <br />            foreach (FileInfo item in allDatas)<br />            {<br />                item.Name = "New FileName";<br />            }<br /> <br />            foreach (FileInfo item in allDatas)<br />            {<br />                Console.WriteLine(item.Name);<br />            }<br />        }<br />        public static IEnumerable&lt;FileInfo&gt; GetDatas(String path)<br />        {<br />            var linq = from file in Directory.GetFiles(path)<br />                       select new FileInfo() { Name = Path.GetFileName(file) };<br />            return linq;<br />        }<br /> <br />    }<br /> <br />    class FileInfo<br />    {<br />        private string _name;<br />        public string Name<br />        {<br />            get { return _name; }<br />            set<br />            {<br />                if (_name != value)<br />                {<br />                    _name = value;<br />                }<br />            }<br />        }<br />    }<br />}<br /></pre>

<p> </p>

<p>或是透過yield實現IEnumerable型態的回傳時</p>

<pre>...</pre>

<pre>public static IEnumerable&lt;FileInfo&gt; GetDatas(String path)<br />{<br />    foreach (var file in Directory.GetFiles(path))<br />    {<br />        yield return new FileInfo() { Name = Path.GetFileName(file) };<br />    }<br />}<br />...</pre>

<p> </p>

<p>我們都可以注意到ㄧ開始從GetDatas取得的物件實體跟後續透過臨時變數取得的都不同...</p>

<p><img style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" border="0" alt="image" src="\images\posts\21956\image_thumb_1.png" width="425" height="207" /></p>

<p> </p>

<p>必須要在取得IEnumerable型態的資料時透過ToArray、或是ToList之類的方法先行處理過，或是盡量避免使用Linq與yield去獲取IEnumerable型態的資料後直接回傳：</p>

<pre>...</pre>

<pre>IEnumerable&lt;FileInfo&gt; allDatas = GetDatas(@"c:\").ToArray();</pre>

<pre>...<br /></pre>

<p><img style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" border="0" alt="image" src="\images\posts\21956\image_thumb_2.png" width="361" height="191" /> </p>

<p> </p>

<p>目前這問題尚無確切的定論，個人暫時姑且推測應該是因為yield的特性所導致的效果。</p>
