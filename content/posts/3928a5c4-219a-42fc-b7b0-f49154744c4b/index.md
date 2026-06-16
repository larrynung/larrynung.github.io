---
title: "[C#]使用ExifLibrary簡易快速的擷取圖片的Exif資訊"
slug: "[CSharp]使用ExifLibrary簡易快速的擷取圖片的Exif資訊"
date: "2013-11-06 12:00:00"
description: "最近在玩讀取圖片的Exif資訊，試了一下.NET內建的方法與別人包好的類別，但都不怎麼好用，最後找到CodeProject的ExifLibrary for .NET這篇，試起來功能算是滿齊全的，用起來也很容易，這邊稍稍記錄一下。"
tags: [CSharp]
---

最近在玩讀取圖片的Exif資訊，試了一下.NET內建的方法與別人包好的類別，但都不怎麼好用，最後找到CodeProject的ExifLibrary for .NET這篇，試起來功能算是滿齊全的，用起來也很容易，這邊稍稍記錄一下。

要使用ExifLibrary for .NET來做擷取圖片Exif的動作，首先我們必須下載組件並將之加入參考。

![image_thumb.png](/images/posts/3928a5c4-219a-42fc-b7b0-f49154744c4b/image_thumb.png)

接著再將ExifLibrary命名空間加入，就可以開始進行程式部分的撰寫了。

```csharp
using ExifLibrary;
```

程式撰寫時我們必須先取得ExifFile的物件實體，只要用ExifFile.Read將圖檔的位置帶入就可以了。

```csharp
...
ExifFile exifFile = ExifFile.Read(photoFile);
...
```

有了ExifFile物件實體後，後續的動作就簡單多了，因為都是針對這個物件下去操作，像是要取得藏在圖檔Exif內的縮圖就可以透過ExifFile.Thumbnail.ToBitmap()。

```csharp
...
var thumbnail = exifFile.Thumbnail.ToBitmap();
...
```

而要取得圖檔的Exif資訊的話，可以直接透過ExifFile.Properties，並用ExifTag指定要取得的Exif資訊。

```csharp
...
var xResolution = exifFile.Properties[ExifTag.XResolution].Value;
var yResolution = exifFile.Properties[ExifTag.YResolution].Value;
...
```

也可以透過ExifFile.Properties.Values將圖檔所有的Exif資訊都逐一掃出。

```csharp
...
foreach (ExifProperty item in exifFile.Properties.Values)
{
	tbxMessage.Text += string.Format("{0}:{1}\r\n", item.Name, item.Value);
}
...
```

基本上ExifLibrary的大致操作就是那麼簡單，但是有一些要注意的事，就是ExifLibrary之所以好用在於它的架構切的還不錯，雖然我們透過ExifFile.Properties看到的都是ExifProperty型態(像是ExifURational就是繼承ExifProperty的類別)，但不轉成本來的型態我們能取用的資訊就會有限。

![image_thumb_1.png](/images/posts/3928a5c4-219a-42fc-b7b0-f49154744c4b/image_thumb_1.png)

因此在撰寫時若需要更詳細、更細部的資料的話，我們必須注意他本來的型態為何。

![image_thumb_2.png](/images/posts/3928a5c4-219a-42fc-b7b0-f49154744c4b/image_thumb_2.png)

然後像下面這樣轉型後取用就可以了：

```csharp
...
var xResolution = (ExifURational)exifFile.Properties[ExifTag.XResolution];
var xResolutionNumerator = (int)xResolution.Value.Numerator;
var xResolutionDenominator = (int)xResolution.Value.Denominator;
...
```

最後附上筆者用來測試的完整程式碼片段：

```csharp
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using ExifLibrary;

namespace WindowsFormsApplication34
{
	public partial class Form1 : Form
	{
		public Form1()
		{
			InitializeComponent();
		}

		private void btnLoad_Click(object sender, EventArgs e)
		{
			if (openFileDialog1.ShowDialog() == DialogResult.OK)
			{
				var photoFile = openFileDialog1.FileName;

				ExifFile exifFile = ExifFile.Read(photoFile);

				pbxThumbnail.Image = exifFile.Thumbnail.ToBitmap();

				tbxMessage.Clear();
				foreach (ExifProperty item in exifFile.Properties.Values)
				{
					tbxMessage.Text += string.Format("{0}:{1}\r\n", item.Name, item.Value);
				}
			}
		}
	}
}
```

運行後可看到圖片內含的所有Exif資訊。

![image_thumb_4.png](/images/posts/3928a5c4-219a-42fc-b7b0-f49154744c4b/image_thumb_4.png)

## Link

* ExifLibrary for .NET
