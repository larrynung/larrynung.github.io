---
title: "[C#]如何做出類似Facebook的web preview"
date: "2013-11-06 12:00:00"
description: "因為不是走Web開發的，這塊對於筆者滿陌生的，一直滿好奇Facebook打入網址後會顯示的預覽畫面是怎樣做的。抽空參閱Creating a Facebook Like Website Previewer這篇並試玩了一下，發現沒有想像中的困難，只是很單純的從網頁內容中擷取資訊而已，"
tags: [CSharp]
---

因為不是走Web開發的，這塊對於筆者滿陌生的，一直滿好奇Facebook打入網址後會顯示的預覽畫面是怎樣做的。抽空參閱Creating a Facebook Like Website Previewer這篇並試玩了一下，發現沒有想像中的困難，只是很單純的從網頁內容中擷取資訊而已，這邊稍稍對此做個整理。

![image_thumb.png](/images/posts/ca63594b-5f89-4ee2-a87c-a7c50712dc45/image_thumb.png)

這邊我們可以先來檢視一下奇摩的原始碼，對照上圖在FB所擷取到的資訊，我們不難看出資訊都是從網頁原始碼中擷取出來的。

![image_thumb_1.png](/images/posts/ca63594b-5f89-4ee2-a87c-a7c50712dc45/image_thumb_1.png)

其中網頁預覽中的標題部份對應到的是<Title>這個HTML標籤所包的值，可以用下面的正規表示式將之擷取出來：

```csharp
<title>\s*(?<Title>[^<>]+)\s*</title>
```

而網頁預覽中的網頁描述部份則是對應到name值為description的meta標籤，可以用下面的正規表示式將之擷取出來：

```xml
<meta\s+name="description"\s+content\s*=\s*"(?<Description>[^<>"]*)"
```

至於網頁預覽中的縮圖部份，可能是來自rel值為image_src的link標籤或是來自img標籤，圖片的網址部份要盡可能完整才收進來，可以用下面的正規表示式將之擷取出來：

```xml
<(?:img\s+src\s*=|link\s+rel\s*=\s*"image_src"\s+ href\s*=)"(?<Thumbnail>http://[\w/.]+(?:jpg|bmp|gif))"
```

實際在做擷取時，就會像下面這樣：

```csharp
...
#region Const
private const string TITLE_MATCH_PATTERN = @"<title>\s*(?<Title>[^<>]+)\s*</title>";
private const string DESCRIPTION_MATCH_PATTERN = @"<meta\s+name=""description""\s+content\s*=\s*""(?<Description>[^<>""]*)""";
private const string THUMBNAIL_MATCH_PATTERN = @"<(?:img\s+src\s*=|link\s+rel\s*=\s*""image_src""\s+ href\s*=)""(?<Thumbnail>http://[\w/.]+(?:jpg|bmp|gif))""";
#endregion
...
string htmlSourceCode;
...
var title = Regex.Match(htmlSourceCode, TITLE_MATCH_PATTERN).Groups["Title"].Value;
var description = Regex.Match(htmlSourceCode,DESCRIPTION_MATCH_PATTERN).Groups["Description"].Value;
var thumbnailURLs = Regex.Matches(htmlSourceCode, THUMBNAIL_MATCH_PATTERN, RegexOptions.IgnorePatternWhitespace).Cast<Match>().Select(m => m.Groups["Thumbnail"].Value);
```

這邊筆者在測試時隨手將這功能簡單的包了一下。

```csharp
	public class WebPreview
	{
		#region Const
		private const string TITLE_MATCH_PATTERN = @"<title>\s?(?<Title>[^<>]+)\s?</title>";
		private const string DESCRIPTION_MATCH_PATTERN = @"<meta\s+name=""description""\s+content\s?=""(?<Description>[^<>""]*)"">";
		private const string THUMBNAIL_MATCH_PATTERN = @"<(?:img\s+src\s*=|link\s+rel\s*=\s*""image_src""\s+ href\s*=)""(?<Thumbnail>http://[\w/.]+(?:jpg|bmp|gif))""";
		#endregion

		#region Var
		private string _sourceCode;
		private string _title;
		private string _description;
		private IEnumerable<String> _thumbnailURLs;
		#endregion

		#region Private Property
		public string m_SourceCode
		{
			get
			{
				return _sourceCode ?? (_sourceCode = GetHTMLSourceCode(URL));
			}
		}
		#endregion

		#region Public Property
		/// <summary>
		/// Gets or sets the URL.
		/// </summary>
		/// <value>The URL.</value>
		public string URL { get; private set; }

		/// <summary>
		/// Gets the title.
		/// </summary>
		/// <value>The title.</value>
		public string Title
		{
			get
			{
				return _title ?? (_title = Regex.Match(m_SourceCode, TITLE_MATCH_PATTERN).Groups["Title"].Value);
			}
		}

		/// <summary>
		/// Gets the description.
		/// </summary>
		/// <value>The description.</value>
		public string Description
		{
			get
			{
				return _description ?? (_description = Regex.Match(m_SourceCode,DESCRIPTION_MATCH_PATTERN).Groups["Description"].Value);
			}
		}

		public IEnumerable<String> ThumbnailURLs
		{
			get
			{
				return _thumbnailURLs ?? (_thumbnailURLs = Regex.Matches(m_SourceCode, THUMBNAIL_MATCH_PATTERN, RegexOptions.IgnorePatternWhitespace).Cast<Match>().Select(m => m.Groups["Thumbnail"].Value));
			}
		}
		#endregion

		#region Constructor
		public WebPreview (string url)
		{
			this.URL = url;
		}
		#endregion

		#region Private Method
        private string GetHTMLSourceCode(string url)
        {
            HttpWebRequest request = (WebRequest.Create (url)) as HttpWebRequest;
            HttpWebResponse response = request.GetResponse() as HttpWebResponse;
            using (StreamReader sr = new StreamReader(response.GetResponseStream()))
            {
                return sr.ReadToEnd();
            }
        }
		#endregion
	}
```

使用起來就只要在建立物件時帶入網址就可以了。

```csharp
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication36
{
	public partial class Form1 : Form
	{
		private int m_Index { get; set; }
		private string[] m_ThumbnailURLs { get; set; }

		public Form1()
		{
			InitializeComponent();
		}

		private void UpdateThumbnailIndexStatus()
		{
			lblIndexStatus.Text = string.Format("{0}/{1}", m_Index + 1, m_ThumbnailURLs.Length);
		}

		private void btnGO_Click(object sender, EventArgs e)
		{
			var preview = new WebPreview(tbxUrl.Text);
			lblTitle.Text = preview.Title;
			lblUrl.Text = preview.URL;
			lblDescription.Text = preview.Description;

			m_Index = 0;
			m_ThumbnailURLs = preview.ThumbnailURLs.ToArray();
			UpdateThumbnailIndexStatus();

			if (m_ThumbnailURLs.Length == 0)
				return;

			pbxThumbnail.ImageLocation = m_ThumbnailURLs[m_Index];
		}

		private void btnNext_Click(object sender, EventArgs e)
		{
			if (m_Index == m_ThumbnailURLs.Length - 1)
				return;
			m_Index += 1;
			pbxThumbnail.ImageLocation = m_ThumbnailURLs[m_Index];
			UpdateThumbnailIndexStatus();
		}

		private void btnPrevious_Click(object sender, EventArgs e)
		{
			if (m_Index == 0)
				return;
			m_Index -= 1;
			pbxThumbnail.ImageLocation = m_ThumbnailURLs[m_Index];
			UpdateThumbnailIndexStatus();
		}
	}
}
```

運行的結果如下：

![image_thumb_2.png](/images/posts/ca63594b-5f89-4ee2-a87c-a7c50712dc45/image_thumb_2.png)

![image_thumb_3.png](/images/posts/ca63594b-5f89-4ee2-a87c-a7c50712dc45/image_thumb_3.png)

## Link

* Creating a Facebook Like Website Previewer
