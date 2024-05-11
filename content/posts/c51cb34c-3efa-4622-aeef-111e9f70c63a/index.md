---
title: "[C#]DropBox開發系列 - 使用DropNet上傳檔案至DropBox"
slug: "[CSharp]DropBox開發系列 - 使用DropNet上傳檔案至DropBox"
date: "2013-11-06 12:00:00"
description: "[C#]DropBox開發系列 - 使用DropNet上傳檔案至DropBox"
tags: [CSharp]
---

<p>要使用DropNet上傳檔案至DropBox，我們可以在做完DropBox認證後叫用DropNetClient.Upload函式，帶入檔案要存放的相對路徑、要儲存的檔名、以及要儲存的檔案內容，我們就可以將檔案上傳至DropBox指定的位置。程式撰寫起來會像下面這樣：</p>  <div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:6720442d-a65d-4bc4-9681-e64c5e6ae040" class="wlWriterSmartContent"><pre name="code" class="c#">			if (openFileDialog1.ShowDialog() == DialogResult.OK)
			{
				tbxFile.Text = openFileDialog1.FileName;
			}
	
			...
			var selectedNode = treeView1.SelectedNode;
			if (selectedNode == null)
				return;

			var metaData = selectedNode.Tag as MetaData;
			if (metaData == null)
				return;

			if (!metaData.Is_Dir)
			{
				MessageBox.Show("Please select a folder first.");
				return;
			}

			if (tbxFile.Text.Length == 0)
			{
				MessageBox.Show("Please select a file to upload first.");
				return;
			}

			if (!File.Exists(tbxFile.Text))
			{
				MessageBox.Show("File not found.");
				return;
			}

			m_DropNetClient.UploadFile(metaData.Path, Path.GetFileName(tbxFile.Text), File.ReadAllBytes(tbxFile.Text));
			...</pre></div>

<p> </p>

<p>這邊筆者在撰寫時為了方便都是以同步的方式下去做說明，實際使用時若有需要可以考慮用非同步的方式叫用，將程式改呼叫<code>UploadFileAsync就可以了。</code></p>

<p> </p>

<p>最後一樣附上比較完整的範例程式：</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:7ca07bd1-2ccb-4c85-89e7-6ad5ac9d2e29" class="wlWriterSmartContent"><pre name="code" class="c#">using System;
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
using System.IO;

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

		private void treeView1_MouseDoubleClick(object sender, MouseEventArgs e)
		{
			var selectedNode = treeView1.SelectedNode;
			if (selectedNode == null)
				return;

			var metaData = selectedNode.Tag as MetaData;
			if(metaData == null)
				return;

			using (var saveFileDialog = new SaveFileDialog())
			{
				saveFileDialog.FileName = metaData.Name;

				if(saveFileDialog.ShowDialog() == DialogResult.OK)
				{
					var fileData = m_DropNetClient.GetFile(metaData.Path);
					File.WriteAllBytes(saveFileDialog.FileName, fileData);
				}
			}
		}

		private void button2_Click(object sender, EventArgs e)
		{
			if (openFileDialog1.ShowDialog() == DialogResult.OK)
			{
				tbxFile.Text = openFileDialog1.FileName;
			}
		}

		private void button1_Click_1(object sender, EventArgs e)
		{
			var selectedNode = treeView1.SelectedNode;
			if (selectedNode == null)
				return;

			var metaData = selectedNode.Tag as MetaData;
			if (metaData == null)
				return;

			if (!metaData.Is_Dir)
			{
				MessageBox.Show("Please select a folder first.");
				return;
			}

			if (tbxFile.Text.Length == 0)
			{
				MessageBox.Show("Please select a file to upload first.");
				return;
			}

			if (!File.Exists(tbxFile.Text))
			{
				MessageBox.Show("File not found.");
				return;
			}

			m_DropNetClient.UploadFile(metaData.Path, Path.GetFileName(tbxFile.Text), File.ReadAllBytes(tbxFile.Text));
		}
	}
}</pre></div>
