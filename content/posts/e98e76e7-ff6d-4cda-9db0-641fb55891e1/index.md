---
title: "[C#]DropBox開發系列 - 使用DropNet進行DropBox的二次登入"
slug: "[CSharp]DropBox開發系列 - 使用DropNet進行DropBox的二次登入"
date: "2013-11-06 12:00:00"
description: "[C#]DropBox開發系列 - 使用DropNet進行DropBox的二次登入"
tags: [CSharp]
---

筆者在[C#]DropBox開發系列 - 使用DropNet進行DropBox的OAuth認證這篇稍稍介紹了一下怎樣用DropNet去登入DropBox帳號，並授權給應用程式存取DropBox。這樣的登入與授權的動作在應用程式中不會每次都做，通常是第一次做了取得Token後，再次登入時就改成用帶入Token的方式去做認證，只要Token尚未過期基本上都不會再次要求授權。

使用DropNet進行這樣的處理很簡單，DropNetClient類別有兩個建構子，有個建構子允許我們帶入userToken與userSecret。
  		public DropNetClient(string apiKey, string appSecret);
		public DropNetClient(string apiKey, string appSecret, string userToken, string userSecret);

而我們再做完OAuth認證後取得的AccessToken就內含userToken與userSecret這兩個值，我們只需要在第一次做完認證時將這兩個值儲存起來，在下次認證時一併帶入建構子中建立DropNetClient就可以了。或是後續再透過DropNetClient.UserLogin來設定也可以。

像是下面這樣：

			...
			if (!String.IsNullOrEmpty(Properties.Settings.Default.SECRET) && !String.IsNullOrEmpty(Properties.Settings.Default.TOKEN))
			{
				m_DropNetClient.UserLogin = new UserLogin() 
				{
					Secret = Properties.Settings.Default.SECRET,
					Token = Properties.Settings.Default.TOKEN
				};

				return;
			}
			
			...
			if (DoOAuth(callbackUrl, cancelCallbackUrl, size) == DialogResult.OK)
			{
				var accessToken = m_DropNetClient.GetAccessToken();
				Properties.Settings.Default.SECRET = accessToken.Secret;
				Properties.Settings.Default.TOKEN = accessToken.Token;
				Properties.Settings.Default.Save();
			}

這邊的程式筆者是在取得AccessToken後將Secret與Token存入設定檔中，下次認證時若是設定檔中有就直接取用。

最後一樣附上完整的範例程式：

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
			if (!String.IsNullOrEmpty(Properties.Settings.Default.SECRET) && !String.IsNullOrEmpty(Properties.Settings.Default.TOKEN))
			{
				m_DropNetClient.UserLogin = new UserLogin() 
				{
					Secret = Properties.Settings.Default.SECRET,
					Token = Properties.Settings.Default.TOKEN
				};
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
	}
}