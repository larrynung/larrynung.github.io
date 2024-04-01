---
title: "[C#]DropBox開發系列 - 使用DropNet遍巡DropBox內存放的檔案"
date: "2013-11-06 12:00:00"
description: "[C#]DropBox開發系列 - 使用DropNet遍巡DropBox內存放的檔案"
tags: [CSharp]
---

<p>
	認證的開發介紹完了，這邊要介紹一下如何遍巡DropBox內存放的檔案，使用DropNet去實做這個功能也很簡單，只需要透過DropNetClient.GetMetaData這個函式帶入要查閱的路徑就可以了。若是要查閱的是根目錄，可帶入"/"去做查閱，但需注意申請App Key時必需要允許對整個DropBox做控制才可以，不然只能針對該App的目錄下去巡覽。</p>
<p>
	 </p>
<p>
	用DropNetClient.GetMetaData問回來的資料是MetaData型態。DropNet將DropBox內的檔案都視為是MetaData，MetaData內會有檔案名稱、大小、是否是目錄之類的相關資訊。</p>
<p>
	<img alt="image" border="0" height="273" src="\images\posts\71dddf38-a05e-42c0-b7b7-57ad6912da4a\image_thumb_1.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="644" /></p>
<p>
	 </p>
<p>
	若MetaData是目錄的話，目錄下的存放的檔案資料會在Contents屬性中，我們只要遞迴去遍巡處理就可以了。但這邊需要特別留意的是，為了速度考量DropNet預設只會抓指定那層的資料，超過指定那層Contents屬性會是Null，因此再往下層處理時記得要再次叫用DropNetClient.GetMetaData。</p>
<p>
	<img alt="image" border="0" height="330" src="\images\posts\71dddf38-a05e-42c0-b7b7-57ad6912da4a\image_thumb_2.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="644" /></p>
<p>
	 </p>
<p>
	處理起來會像下面這樣：</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:51b01b09-951e-4f3c-a37b-6b92010e12f7" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c#" name="code">
...
private void btnLogin_Click(object sender, EventArgs e)
{
	if (!String.IsNullOrEmpty(Properties.Settings.Default.SECRET) &amp;&amp; !String.IsNullOrEmpty(Properties.Settings.Default.TOKEN))
	{
		m_DropNetClient.UserLogin = new UserLogin()
		{
			Secret = Properties.Settings.Default.SECRET,
			Token = Properties.Settings.Default.TOKEN
		};

		FillTreeView();
		return;
	}

	var callbackUrl = "https://www.dropbox.com/1/oauth/authorize";
	var cancelCallbackUrl = "https://www.dropbox.com/home";
	var size = new Size(1024, 600);

	if (DoOAuth(callbackUrl, cancelCallbackUrl, size) == DialogResult.OK)
	{
		var accessToken = m_DropNetClient.GetAccessToken();
		Properties.Settings.Default.SECRET = accessToken.Secret;
		Properties.Settings.Default.TOKEN = accessToken.Token;
		Properties.Settings.Default.Save();

		FillTreeView();
	}
}

private void FillTreeView()
{
	treeView1.Nodes.Clear();
	var metaData = m_DropNetClient.GetMetaData("/");

	FillDirOrFileToTreeView(null, metaData);
}

private void FillDirOrFileToTreeView(TreeNode parentNode, MetaData metaData)
{
	if (metaData.Contents == null)
		return;

	var nodes = (parentNode == null) ? treeView1.Nodes : parentNode.Nodes;
	try
	{
		treeView1.BeginUpdate();
		foreach (var childMetaData in metaData.Contents)
		{
			if (childMetaData.Is_Dir)
			{
				var node = nodes.Add(childMetaData.Name);
				node.Tag = childMetaData;
				node.Nodes.Add(string.Empty);
			}
			else
			{
				nodes.Add(childMetaData.Name).Tag = childMetaData;
			}
		}
	}
	finally
	{
		treeView1.EndUpdate();
	}
}

private void treeView1_BeforeExpand(object sender, TreeViewCancelEventArgs e)
{
	var node = e.Node;

	if (!(node.Nodes.Count == 1 &amp;&amp; node.Nodes[0].Tag == null))
		return;

	node.Nodes.Clear();

	FillDirOrFileToTreeView(node, m_DropNetClient.GetMetaData("/" + node.FullPath));
}
...
</pre>
</div>
<p>
	 </p>
<p>
	運行後可以看到我們確實的將整個DropBox內的內容都抓出來了。</p>
<p>
	<img alt="image" border="0" height="472" src="\images\posts\71dddf38-a05e-42c0-b7b7-57ad6912da4a\image_thumb.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="644" /></p>
<p>
	 </p>
<p>
	筆者在撰寫時為了方便都是以同步的方式下去做說明，實際使用時若有需要可以考慮用非同步的方式叫用，將程式改呼叫<code>GetMetaDataAsync就可以了。</code></p>
<p>
	 </p>
<p>
	最後一樣附上完整的範例程式碼：</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:51b01b09-951e-4f3c-a37b-6b92010e12f7" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c#" name="code">
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using DropNet;
using DropNetDemo.Properties;
using DropNet.Models;

namespace DropNetDemo
{
	public partial class Form1 : Form
	{
		#region Var
		private DropNetClient _dropNetClient;
		#endregion

		#region Private Property
		private DropNetClient m_DropNetClient
		{
			get
			{
				return _dropNetClient ?? (_dropNetClient = new DropNetClient(tbxAppKey.Text, tbxAppSecret.Text));
			}
			set
			{
				_dropNetClient = value;
			}
		}
		#endregion

		public Form1()
		{
			InitializeComponent();
		}

		private void SetSecretAndToken(string secret, string token)
		{
			Settings.Default.SECRET = secret;
			Settings.Default.TOKEN = token;
		}

		private void btnLogin_Click(object sender, EventArgs e)
		{
			if (!String.IsNullOrEmpty(Properties.Settings.Default.SECRET) &amp;&amp; !String.IsNullOrEmpty(Properties.Settings.Default.TOKEN))
			{
				m_DropNetClient.UserLogin = new UserLogin()
				{
					Secret = Properties.Settings.Default.SECRET,
					Token = Properties.Settings.Default.TOKEN
				};

				FillTreeView();
				return;
			}

			var callbackUrl = "https://www.dropbox.com/1/oauth/authorize";
			var cancelCallbackUrl = "https://www.dropbox.com/home";
			var size = new Size(1024, 600);

			if (DoOAuth(callbackUrl, cancelCallbackUrl, size) == DialogResult.OK)
			{
				var accessToken = m_DropNetClient.GetAccessToken();
				Properties.Settings.Default.SECRET = accessToken.Secret;
				Properties.Settings.Default.TOKEN = accessToken.Token;
				Properties.Settings.Default.Save();

				FillTreeView();
			}
		}

		private void FillTreeView()
		{
			treeView1.Nodes.Clear();
			var metaData = m_DropNetClient.GetMetaData("/");

			FillDirOrFileToTreeView(null, metaData);
		}

		private void FillDirOrFileToTreeView(TreeNode parentNode, MetaData metaData)
		{
			if (metaData.Contents == null)
				return;

			var nodes = (parentNode == null) ? treeView1.Nodes : parentNode.Nodes;
			try
			{
				treeView1.BeginUpdate();
				foreach (var childMetaData in metaData.Contents)
				{
					if (childMetaData.Is_Dir)
					{
						var node = nodes.Add(childMetaData.Name);
						node.Tag = childMetaData;
						node.Nodes.Add(string.Empty);
					}
					else
					{
						nodes.Add(childMetaData.Name).Tag = childMetaData;
					}
				}
			}
			finally
			{
				treeView1.EndUpdate();
			}
		}

		private void treeView1_BeforeExpand(object sender, TreeViewCancelEventArgs e)
		{
			var node = e.Node;

			if (!(node.Nodes.Count == 1 &amp;&amp; node.Nodes[0].Tag == null))
				return;

			node.Nodes.Clear();

			FillDirOrFileToTreeView(node, m_DropNetClient.GetMetaData("/" + node.FullPath));
		}

		private DialogResult DoOAuth(string callbackUrl, string cancelCallbackUrl, System.Drawing.Size size)
		{
			using (var dialog = new Form())
			{
				var browesr = new WebBrowser()
				{
					Dock = DockStyle.Fill
				};

				var token = m_DropNetClient.GetToken();
				var authUrl = m_DropNetClient.BuildAuthorizeUrl();
				browesr.Navigated += (s, ex) =&gt;
				{
					var url = ex.Url.ToString();
					if (url.Equals(callbackUrl))
					{
						dialog.DialogResult = DialogResult.OK;
					}
					else if (url.Equals(cancelCallbackUrl))
					{
						dialog.DialogResult = DialogResult.Cancel;
					}
				};
				browesr.Navigate(authUrl);

				dialog.Size = size;
				dialog.Controls.Add(browesr);

				return dialog.ShowDialog();
			}
		}

		private void tbxAppKey_TextChanged(object sender, EventArgs e)
		{
			m_DropNetClient = null;
		}

		private void tbxAppSecret_TextChanged(object sender, EventArgs e)
		{
			m_DropNetClient = null;
		}
	}
}</pre>
</div>
<p>
	 </p>
