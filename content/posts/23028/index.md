---
title: "[C#]Windows RSS Platform"
slug: "[CSharp]Windows RSS Platform"
date: "2011-04-18 10:17:46"
description: "[C#]Windows RSS Platform"
tags: [CSharp]
---

<p>
	Windows RSS Platform提供RSS訂閱清單、訂閱增減等功能，其RSS的訂閱資訊會整合在7.0以上的IE版本內。</p>
<p>
	<img alt="image" border="0" height="419" src="\images\posts\23028\image_thumb_1.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="549" /></p>
<p>
	 </p>
<p>
	開發時需將Microsoft Feeds 2.0 Object Library這個COM物件加入參考。</p>
<p>
	<img alt="image" border="0" height="372" src="\images\posts\23028\image_thumb.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="644" /></p>
<p>
	 </p>
<p>
	加入參考後需將Microsoft.Feeds.Interop命名空間加入，命名空間內含有開發所需要的類別，主要的類別有FeedManager、FeedFolder、Feed、與FeedItem等。FeedManager為主要的管理類別，具備有RootFolder屬性，指向RSS清單的根目錄。FeedFolder為訂閱節點目錄，可透過SubFolders瀏覽內含有子目錄，或是透過Feeds瀏覽所訂閱節點。Feed為訂閱的網站資訊，內含訂閱網站所提供的訂閱內容。FeedItem為訂閱內容，可取得其Title、發佈時間、RSS描述等資訊、與取得設定是否內容是否已讀取。</p>
<p>
	 </p>
<p>
	看到這裡可稍微參閱一下MSDN上的圖片，釐清其彼此間的關聯性並加深印象。</p>
<p>
	<img alt="image" border="0" height="347" src="\images\posts\23028\image_thumb_2.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="457" /></p>
<p>
	 </p>
<p>
	這邊以Windows RSS Platform實做一個簡單的RSS訂閱程式，完整程式範例如下：</p>
<p>
	using System;<br />
	using System.Drawing;<br />
	using System.Windows.Forms;<br />
	using Microsoft.Feeds.Interop;</p>
<p>
	namespace WindowsFormsApplication2<br />
	{<br />
	    public partial class MainForm : Form<br />
	    {<br />
	        #region Var<br />
	        private IFeedsManager _feedsManager;<br />
	        private IFeedFolder _rootFolder;<br />
	        #endregion</p>
<p>
	        #region Property<br />
	        public IFeedsManager m_FeedsManager<br />
	        {<br />
	            get<br />
	            {<br />
	                if (_feedsManager == null)<br />
	                    _feedsManager = new FeedsManagerClass();<br />
	                return _feedsManager;<br />
	            }<br />
	        }</p>
<p>
	        public IFeedFolder m_RootFolder<br />
	        {<br />
	            get<br />
	            {<br />
	                if (_rootFolder == null)<br />
	                    _rootFolder = (IFeedFolder)m_FeedsManager.RootFolder;<br />
	                return _rootFolder;<br />
	            }<br />
	        }<br />
	        #endregion</p>
<p>
	        #region Constructor<br />
	        public MainForm()<br />
	        {<br />
	            InitializeComponent();<br />
	        }<br />
	        #endregion</p>
<p>
	        #region Private Method<br />
	        private void SetFeedNodes()<br />
	        {<br />
	            treeView1.Nodes.Clear();<br />
	            SetFeedNodes(treeView1.Nodes.Add("Feeds"), m_RootFolder);<br />
	        }</p>
<p>
	        private void SetFeedNodes(TreeNode parentnode, IFeedFolder folder)<br />
	        {<br />
	            if (folder.Subfolders != null)<br />
	            {<br />
	                foreach (IFeedFolder subfolder in (IFeedsEnum)folder.Subfolders)<br />
	                {<br />
	                    SetFeedNodes(parentnode.Nodes.Add(subfolder.Name), subfolder);<br />
	                }<br />
	            }</p>
<p>
	            if (folder.Feeds != null)<br />
	            {<br />
	                foreach (IFeed feed in (IFeedsEnum)folder.Feeds)<br />
	                {<br />
	                    parentnode.Nodes.Add(feed.Name).Tag = feed;<br />
	                }<br />
	            }<br />
	        }<br />
	        #endregion</p>
<p>
	        #region Event Process<br />
	        private void Form1_Load(object sender, EventArgs e)<br />
	        {<br />
	            SetFeedNodes();<br />
	            treeView1.ExpandAll();<br />
	        }</p>
<p>
	        private void treeView1_AfterSelect(object sender, TreeViewEventArgs e)<br />
	        {<br />
	            IFeed feed = e.Node.Tag as IFeed;<br />
	            if (feed == null)<br />
	                return;</p>
<p>
	            listView1.Items.Clear();<br />
	            webBrowser1.DocumentText = string.Empty;</p>
<p>
	            var unreadFont = new Font(listView1.Font, FontStyle.Bold);</p>
<p>
	            foreach (IFeedItem item in (IFeedsEnum)feed.Items)<br />
	            {<br />
	                listView1.Items.Add(new ListViewItem(new string[] { item.Title, item.PubDate.ToShortDateString() })<br />
	                {<br />
	                    Font = (item.IsRead) ? listView1.Font : unreadFont,<br />
	                    Tag = item<br />
	                });<br />
	            }<br />
	        }</p>
<p>
	        private void listView1_SelectedIndexChanged(object sender, EventArgs e)<br />
	        {<br />
	            if (listView1.SelectedItems.Count == 0 || listView1.SelectedItems[0].Tag == null)<br />
	                return;</p>
<p>
	            ListViewItem li = listView1.SelectedItems[0];<br />
	            IFeedItem item = li.Tag as IFeedItem;</p>
<p>
	            if (item == null)<br />
	                return;</p>
<p>
	            item.IsRead = true;<br />
	            li.Font = listView1.Font;</p>
<p>
	            webBrowser1.DocumentText = item.Description;<br />
	            if (webBrowser1.DocumentText.Length == 0)<br />
	                webBrowser1.Navigate(item.Link);<br />
	        }</p>
<p>
	        private void toolStripLabel1_Click(object sender, EventArgs e)<br />
	        {<br />
	            FeedAddDialog dlg = new FeedAddDialog();<br />
	            if (dlg.ShowDialog() == DialogResult.OK)<br />
	            {<br />
	                ((IFeed)m_RootFolder.CreateFeed(dlg.FeedName, dlg.FeedURL)).AsyncDownload();<br />
	                SetFeedNodes();<br />
	                treeView1.ExpandAll();<br />
	            }<br />
	        }</p>
<p>
	        private void toolStripLabel2_Click(object sender, EventArgs e)<br />
	        {<br />
	            SetFeedNodes();<br />
	            treeView1.ExpandAll();<br />
	        }<br />
	        #endregion<br />
	    }<br />
	}</p>
<p>
	 </p>
<p>
	運行結果如下：</p>
<p>
	 <img alt="image" border="0" height="486" src="\images\posts\23028\image_thumb_3.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="632" /></p>
<p>
	 </p>
<h2>
	Download</h2>
<p>
	WindowsFormsApplication2.zip</p>
<p>
	 </p>
<h2>
	Link</h2>
<ul>
	<li>
		Accessing the Windows RSS Platform with C#</li>
	<li>
		Working with the Windows RSS Platform (C#)</li>
	<li>
		Windows RSS Platform</li>
	<li>
		Windows RSS Platform Reference</li>
	<li>
		FeedsManager Object</li>
	<li>
		Introducing the Windows RSS Platform</li>
</ul>
