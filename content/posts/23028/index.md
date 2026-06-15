---
title: "[C#]Windows RSS Platform"
slug: "[CSharp]Windows RSS Platform"
date: "2011-04-18 10:17:46"
description: "[C#]Windows RSS Platform"
tags: [CSharp]
---

Windows RSS Platform提供RSS訂閱清單、訂閱增減等功能，其RSS的訂閱資訊會整合在7.0以上的IE版本內。

![image_thumb_1.png](/images/posts/23028/image_thumb_1.png)

開發時需將Microsoft Feeds 2.0 Object Library這個COM物件加入參考。

![image_thumb.png](/images/posts/23028/image_thumb.png)

加入參考後需將Microsoft.Feeds.Interop命名空間加入，命名空間內含有開發所需要的類別，主要的類別有FeedManager、FeedFolder、Feed、與FeedItem等。FeedManager為主要的管理類別，具備有RootFolder屬性，指向RSS清單的根目錄。FeedFolder為訂閱節點目錄，可透過SubFolders瀏覽內含有子目錄，或是透過Feeds瀏覽所訂閱節點。Feed為訂閱的網站資訊，內含訂閱網站所提供的訂閱內容。FeedItem為訂閱內容，可取得其Title、發佈時間、RSS描述等資訊、與取得設定是否內容是否已讀取。

看到這裡可稍微參閱一下MSDN上的圖片，釐清其彼此間的關聯性並加深印象。

![image_thumb_2.png](/images/posts/23028/image_thumb_2.png)

這邊以Windows RSS Platform實做一個簡單的RSS訂閱程式，完整程式範例如下：

```
using System;
using System.Drawing;
using System.Windows.Forms;
using Microsoft.Feeds.Interop;
```

```
namespace WindowsFormsApplication2
{
    public partial class MainForm : Form
    {
        #region Var
        private IFeedsManager _feedsManager;
        private IFeedFolder _rootFolder;
        #endregion
```

```
        #region Property
        public IFeedsManager m_FeedsManager
        {
            get
            {
                if (_feedsManager == null)
                    _feedsManager = new FeedsManagerClass();
                return _feedsManager;
            }
        }
```

```
        public IFeedFolder m_RootFolder
        {
            get
            {
                if (_rootFolder == null)
                    _rootFolder = (IFeedFolder)m_FeedsManager.RootFolder;
                return _rootFolder;
            }
        }
        #endregion
```

```
        #region Constructor
        public MainForm()
        {
            InitializeComponent();
        }
        #endregion
```

```
        #region Private Method
        private void SetFeedNodes()
        {
            treeView1.Nodes.Clear();
            SetFeedNodes(treeView1.Nodes.Add("Feeds"), m_RootFolder);
        }
```

```
        private void SetFeedNodes(TreeNode parentnode, IFeedFolder folder)
        {
            if (folder.Subfolders != null)
            {
                foreach (IFeedFolder subfolder in (IFeedsEnum)folder.Subfolders)
                {
                    SetFeedNodes(parentnode.Nodes.Add(subfolder.Name), subfolder);
                }
            }
```

```
            if (folder.Feeds != null)
            {
                foreach (IFeed feed in (IFeedsEnum)folder.Feeds)
                {
                    parentnode.Nodes.Add(feed.Name).Tag = feed;
                }
            }
        }
        #endregion
```

```
        #region Event Process
        private void Form1_Load(object sender, EventArgs e)
        {
            SetFeedNodes();
            treeView1.ExpandAll();
        }
```

```
        private void treeView1_AfterSelect(object sender, TreeViewEventArgs e)
        {
            IFeed feed = e.Node.Tag as IFeed;
            if (feed == null)
                return;
```

```
            listView1.Items.Clear();
            webBrowser1.DocumentText = string.Empty;
```

```
            var unreadFont = new Font(listView1.Font, FontStyle.Bold);
```

```
            foreach (IFeedItem item in (IFeedsEnum)feed.Items)
            {
                listView1.Items.Add(new ListViewItem(new string[] { item.Title, item.PubDate.ToShortDateString() })
                {
                    Font = (item.IsRead) ? listView1.Font : unreadFont,
                    Tag = item
                });
            }
        }
```

```
        private void listView1_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (listView1.SelectedItems.Count == 0 || listView1.SelectedItems[0].Tag == null)
                return;
```

```
            ListViewItem li = listView1.SelectedItems[0];
            IFeedItem item = li.Tag as IFeedItem;
```

```
            if (item == null)
                return;
```

```
            item.IsRead = true;
            li.Font = listView1.Font;
```

```
            webBrowser1.DocumentText = item.Description;
            if (webBrowser1.DocumentText.Length == 0)
                webBrowser1.Navigate(item.Link);
        }
```

```
        private void toolStripLabel1_Click(object sender, EventArgs e)
        {
            FeedAddDialog dlg = new FeedAddDialog();
            if (dlg.ShowDialog() == DialogResult.OK)
            {
                ((IFeed)m_RootFolder.CreateFeed(dlg.FeedName, dlg.FeedURL)).AsyncDownload();
                SetFeedNodes();
                treeView1.ExpandAll();
            }
        }
```

```
        private void toolStripLabel2_Click(object sender, EventArgs e)
        {
            SetFeedNodes();
            treeView1.ExpandAll();
        }
        #endregion
    }
}
```

運行結果如下：

![image_thumb_3.png](/images/posts/23028/image_thumb_3.png)

## Download

WindowsFormsApplication2.zip

## Link

* Accessing the Windows RSS Platform with C#
* Working with the Windows RSS Platform (C#)
* Windows RSS Platform
* Windows RSS Platform Reference
* FeedsManager Object
* Introducing the Windows RSS Platform
