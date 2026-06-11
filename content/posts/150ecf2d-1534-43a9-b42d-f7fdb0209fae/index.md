---
title: "[C#]DropBox開發系列 - 使用DropNet下載DropBox內存放的檔案"
slug: "[CSharp]DropBox開發系列 - 使用DropNet下載DropBox內存放的檔案"
date: "2013-11-06 12:00:00"
description: "[C#]DropBox開發系列 - 使用DropNet下載DropBox內存放的檔案"
tags: [CSharp]
---

要使用DropNet下載DropBox內存放的檔案，我們可以透過DropNetClient.GetFile來做，將我們想要下載的檔案位置帶入該函式，會將指定檔案的內容回傳，因此成式撰寫起來會像下面這樣：
  			...
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
...

實際運作起來會像下面這樣，假設我嚐試要抓取的是Batch目錄下的Close.bat檔。

下載時會先詢問要存放的檔案位置，這邊為了方便就先將檔案放在桌面上。 

按下儲存後桌面上會有我們剛剛所選取的檔案，將檔案開起來查驗，可以看到檔案確確實實的下載下來了。 

筆者在撰寫時為了方便都是以同步的方式下去做說明，實際使用時若有需要可以考慮用非同步的方式叫用，將程式改呼叫GetFileAsync就可以了。

最後一樣附上完整的使用範例：

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
if (!String.IsNullOrEmpty(Properties.Settings.Default.SECRET) && !String.IsNullOrEmpty(Properties.Settings.Default.TOKEN))
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

if (!(node.Nodes.Count == 1 && node.Nodes[0].Tag == null))
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
browesr.Navigated += (s, ex) =>
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
}
}