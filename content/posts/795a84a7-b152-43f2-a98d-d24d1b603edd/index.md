---
title: "[C#]DropBox開發系列 - 使用DropNet進行DropBox的OAuth認證"
slug: "[CSharp]DropBox開發系列 - 使用DropNet進行DropBox的OAuth認證"
date: "2013-11-06 12:00:00"
description: "[C#]DropBox開發系列 - 使用DropNet進行DropBox的OAuth認證"
tags: [CSharp]
---

筆者在DropBox開發系列 - App Key與App Secret的申請這篇介紹了DropBox開發前所要做的準備動作，這篇開始要進入實際撰寫程式的部分，介紹如何使用DropNet進行DropBox的OAuth認證。

要用DropNet進行DropBox程式的開發，首先我們必須要將DropNet必要的組件加入參考，這邊筆者是用NuGet直接將參考加入，不用NuGet的也可以直接去官網下載組件後加入參考。

![image_thumb.png](/images/posts/795a84a7-b152-43f2-a98d-d24d1b603edd/image_thumb.png)

DropNet組件加入後我們開始進行程式部份的撰寫，要用DropNet做DropBox的OAuth認證，大致來說可分為三個步驟：

1. Get Request Token
2. Authorize App with Dropbox
3. Get an Access Token from the Request Token

這三個步驟其實就是OAuth認證的步驟，有寫過OAuth認證的應該都不陌生，若是對OAuth不熟悉可參閱筆者[[C#]OAuth認證開發這篇。](http://www.dotblogs.com.tw/larrynung/archive/2011/04/28/23779.aspx)

第一步取得Request Token的部份，我們直接叫用DropNetClient.GetToken()就可以了。

```csharp
m_DropNetClient.GetToken();
```

第二步Authorize App with Dropbox則是先用DropNetClient.BuildAuthorizeUrl()取得使用者授權頁面的網址，然後開個瀏覽器把網頁導過去就可以了。

```csharp
using (var dialog = new Form())
{
	var browesr = new WebBrowser()
	{
		Dock = DockStyle.Fill
	};
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

	...
	dialog.Controls.Add(browesr);
	dialog.ShowDialog();
	...
}
```

授權頁面跑起來會像是下面這樣，需要使用者先行用DropBox帳號做登入。

![image_thumb_3.png](/images/posts/795a84a7-b152-43f2-a98d-d24d1b603edd/image_thumb_3.png)

登入後會詢問使用者是否同意授權給該應用程式。

![image_thumb_1.png](/images/posts/795a84a7-b152-43f2-a98d-d24d1b603edd/image_thumb_1.png)

這邊若是選取Deny，頁面會被導到https://www.dropbox.com/home。

![image_thumb_4.png](/images/posts/795a84a7-b152-43f2-a98d-d24d1b603edd/image_thumb_4.png)

若是選取Allow，頁面會被導到指定的返回位置，也就是在叫用m_DropNetClient.BuildAuthorizeUrl()時帶入的位置。若是未指定返回位置，則頁面預設會被帶到https://www.dropbox.com/1/oauth/authorize。

![image_thumb_2.png](/images/posts/795a84a7-b152-43f2-a98d-d24d1b603edd/image_thumb_2.png)

所以在撰寫這步必須特別注意到要處理瀏覽器的Navigated事件，依照不同狀況做不同的處理。

第三步Get an Access Token from the Request Token跟第一步一樣簡單，在認證成功時叫用DropNetClient.GetAccessToken()就可以了。

整個認證部分的程式撰寫起來會像下面這樣：

```csharp
...
var callbackUrl = "https://www.dropbox.com/1/oauth/authorize";
var cancelCallbackUrl = "https://www.dropbox.com/home";
var size = new Size(1024, 600);

if (DoOAuth(callbackUrl, cancelCallbackUrl, size) == DialogResult.OK)
{
	var accessToken = m_DropNetClient.GetAccessToken();
}
...

private DialogResult DoOAuth(string callbackUrl, string cancelCallbackUrl, System.Drawing.Size size)
{
	using (var dialog = new Form())
	{
		var browesr = new WebBrowser()
		{
			Dock = DockStyle.Fill
		};

		m_DropNetClient.GetToken();
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
```

最後一樣完整的附上筆者在學習時所撰寫的使用範例：

```csharp
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using DropNet;

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

		private void btnLogin_Click(object sender, EventArgs e)
		{
			var callbackUrl = "https://www.dropbox.com/1/oauth/authorize";
			var cancelCallbackUrl = "https://www.dropbox.com/home";
			var size = new Size(1024, 600);

			if (DoOAuth(callbackUrl, cancelCallbackUrl, size) == DialogResult.OK)
			{
				var accessToken = m_DropNetClient.GetAccessToken();
			}
		}

		private DialogResult DoOAuth(string callbackUrl, string cancelCallbackUrl, System.Drawing.Size size)
		{
			using (var dialog = new Form())
			{
				var browesr = new WebBrowser()
				{
					Dock = DockStyle.Fill
				};

				m_DropNetClient.GetToken();
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
	}
}
```
