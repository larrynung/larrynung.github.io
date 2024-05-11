---
title: "[C#]RSS 資料讀取"
slug: "[CSharp]RSS 資料讀取"
date: "2011-04-04 09:50:45"
description: "[C#]RSS 資料讀取"
tags: [CSharp]
---

<p>
	RSS訂閱資訊是透過XML技術實現的，其XML格式欄位對應可參閱RSS 2.0 at Harvard Law這網站。</p>
<p>
	 </p>
<p>
	這邊以點部落-最新文章 的資訊提供來做練習，檢視一下該RSS的XML，發現RSS XML的架構大概就是RSS Channel下面會含許多的RSS Channel Item，RSS Channel用來描述該RSS的識別資訊，RSS Channel Item用來描述RSS所要提供給訂閱者的資訊。</p>
<p>
	<img alt="image" border="0" height="679" src="\images\posts\22274\image_thumb.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="605" /></p>
<p>
	 </p>
<p>
	有了以上的了解後，要讀取RSS資訊就很簡單了，簡單的說就是透過RSS訂閱位置取得RSS XML，接著進一步對其解析，從RSS XML中取得我們想要的資訊。像是若要取得RSS Channel Item就可以像下面這樣撰寫：</p>
<p>
	...</p>
<p>
	var xmlDom=new XmlDocument();</p>
<p>
	xmlDom.Load(tbxRSSURL.Text);</p>
<p>
	var rssItems = xmlDom.SelectNodes("/rss/channel/item");</p>
<p>
	...</p>
<p>
	 </p>
<p>
	這邊附上個完整的範例程式：</p>
<p>
	using System;</p>
<p>
	using System.Text;</p>
<p>
	using System.Windows.Forms;</p>
<p>
	using System.Xml;</p>
<p>
	using LevelUpLazy = LevelUp.Lazy;</p>
<p>
	using System.Diagnostics;</p>
<p>
	namespace WindowsFormsApplication2</p>
<p>
	{</p>
<p>
	    public partial class Form1 : Form</p>
<p>
	    {</p>
<p>
	        public Form1()</p>
<p>
	        {</p>
<p>
	            InitializeComponent();</p>
<p>
	        }</p>
<p>
	        private void btnSubmit_Click(object sender, EventArgs e)</p>
<p>
	        {          </p>
<p>
	            Stopwatch sw=Stopwatch.StartNew ();</p>
<p>
	            var xmlDom=new XmlDocument();</p>
<p>
	            xmlDom.Load(tbxRSSURL.Text);</p>
<p>
	            var rssItems = xmlDom.SelectNodes("/rss/channel/item");</p>
<p>
	            trvRSSItem.Nodes.Clear();</p>
<p>
	            wbRSSContent.DocumentText = string.Empty;</p>
<p>
	            trvRSSItem.BeginUpdate();</p>
<p>
	            for (var idx = 0; idx &lt; rssItems.Count; ++idx)</p>
<p>
	            {</p>
<p>
	                var xmlNode = rssItems[idx];</p>
<p>
	                trvRSSItem.Nodes.Add(xmlNode.ChildNodes[0].InnerText).Tag = new LevelUpLazy.Lazy&lt;string&gt;(() =&gt;</p>
<p>
	                {</p>
<p>
	                    StringBuilder ret = new StringBuilder();</p>
<p>
	                    ret.AppendLine(xmlNode.SelectSingleNode("title").InnerText);</p>
<p>
	                    ret.AppendLine("&lt;br/&gt;");</p>
<p>
	                    ret.AppendLine(xmlNode.SelectSingleNode("description").InnerText);</p>
<p>
	                    return ret.ToString();</p>
<p>
	                });</p>
<p>
	            }</p>
<p>
	            trvRSSItem.EndUpdate();</p>
<p>
	            this.toolStripStatusLabel1.Text = string.Format("Elapsed: {0} ms", sw.ElapsedMilliseconds.ToString());</p>
<p>
	            LevelUpLazy.Lazy&lt;string&gt;.EnableBackgroundInit = true;</p>
<p>
	        }</p>
<p>
	        private void trvRSSItem_AfterSelect(object sender, TreeViewEventArgs e)</p>
<p>
	        {</p>
<p>
	            if (trvRSSItem.SelectedNode == null)</p>
<p>
	                return;</p>
<p>
	            var lazy=trvRSSItem.SelectedNode.Tag as LevelUpLazy .Lazy &lt;string&gt;;</p>
<p>
	            wbRSSContent.DocumentText = lazy.Value;</p>
<p>
	        }</p>
<p>
	    }</p>
<p>
	}</p>
<p>
	 </p>
<p>
	運行效果：</p>
<p>
	<img alt="image" border="0" height="475" src="\images\posts\22274\image_thumb_2.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="520" /></p>
<p>
	<img alt="image" border="0" height="658" src="\images\posts\22274\image_thumb_1.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="559" /></p>
<p>
	 </p>
<h2>
	Download</h2>
<p>
	SimpleRSSReader.zip</p>
<p>
	 </p>
<h2>
	Link</h2>
<ul>
	<li>
		RSS 2.0 at Harvard Law</li>
	<li>
		點部落-最新文章 的資訊提供</li>
</ul>
