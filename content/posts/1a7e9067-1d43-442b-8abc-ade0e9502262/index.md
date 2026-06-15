---
title: "[C#]使用BitmapDecoder快速取用圖檔內含的縮圖"
slug: "[CSharp]使用BitmapDecoder快速取用圖檔內含的縮圖"
date: "2013-11-06 12:00:00"
description: "[C#]使用BitmapDecoder快速取用圖檔內含的縮圖"
tags: [CSharp]
---

為了記憶體的佔用或是速度上面的考量，有的時候我們會有為圖檔產生縮圖的需求。產生縮圖的方法很多，多半都需要耗費一點時間，所以有時候我們可能會考慮直接取用圖檔本身就內含的縮圖。

這邊一樣是用WPF內的BitmapDecoder來取用圖檔內含的縮圖。若是Window Form程式的話我們必須額外將PresentationCore.dll、System.Xaml、與WindowsBase.dll加入參考。

![image_thumb_2.png](/images/posts/1a7e9067-1d43-442b-8abc-ade0e9502262/image_thumb_2.png)

實際的程式撰寫部份跟[[C#]使用BitmapDecoder快速讀取圖檔的大小這篇類似，用BitmapDecoder.Create將要讀取的圖檔位置帶入，然後取得第一個Frame，裡面的Thumbnail就是我們所需要的縮圖圖檔。這邊要注意到的是，Thumbnail屬性的型態是BitmapSource，若是在Window Form程式中使用必須將BitmapSource轉換成Bitmap才能使用。](http://www.dotblogs.com.tw/larrynung/archive/2012/09/05/74627.aspx)

```csharp
...
public static Bitmap GetBitmap(this BitmapSource bitmapsource)
{
	Bitmap bitmap;
	using (MemoryStream outStream = new MemoryStream())
	{
		BitmapEncoder enc = new BmpBitmapEncoder();
		enc.Frames.Add(BitmapFrame.Create(bitmapsource));
		enc.Save(outStream);
		bitmap = (new Bitmap(outStream)).Clone() as Bitmap;
	}
	return bitmap;
}
...

public Image GetThumbnail(string file)
{
	var decoder = BitmapDecoder.Create(new Uri(file), BitmapCreateOptions.DelayCreation, BitmapCacheOption.None);
	var frame = decoder.Frames.FirstOrDefault();

	return (frame.Thumbnail == null) ? null : frame.Thumbnail.GetBitmap();
}
...
```

完整的程式範例如下：

```csharp
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Windows.Media.Imaging;
using System.Diagnostics;

namespace WindowsFormsApplication33
{
	public partial class Form1 : Form
	{
		public Form1()
		{
			InitializeComponent();
		}

		public Image GetThumbnail(string file)
		{
			var decoder = BitmapDecoder.Create(new Uri(file), BitmapCreateOptions.DelayCreation, BitmapCacheOption.None);
			var frame = decoder.Frames.FirstOrDefault();

			return (frame.Thumbnail == null) ? null : frame.Thumbnail.GetBitmap();
		}

		private void button1_Click(object sender, EventArgs e)
		{
			if (openFileDialog1.ShowDialog() == System.Windows.Forms.DialogResult.OK)
			{
				var file = openFileDialog1.FileName;

				var sw = Stopwatch.StartNew();
				pictureBox1.Image = GetThumbnail(file);
				toolStripStatusLabel1.Text = String.Format("Elapsed {0} ms", sw.ElapsedMilliseconds.ToString());
			}
		}
	}
}
```

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows.Media.Imaging;
using System.Drawing;
using System.IO;

public static class BitmapSourceExtension
{
	public static Bitmap GetBitmap(this BitmapSource bitmapsource)
	{
		Bitmap bitmap;
		using (MemoryStream outStream = new MemoryStream())
		{
			BitmapEncoder enc = new BmpBitmapEncoder();
			enc.Frames.Add(BitmapFrame.Create(bitmapsource));
			enc.Save(outStream);
			bitmap = (new Bitmap(outStream)).Clone() as Bitmap;
		}
		return bitmap;
	}
}
```

程式運作起來會像下面這樣，可以看到抓取4-5 MB的圖檔只需花費43ms。

![image_thumb.png](/images/posts/1a7e9067-1d43-442b-8abc-ade0e9502262/image_thumb.png)

以這張圖片來說縮圖的大小也有160X120。

![image_thumb_1.png](/images/posts/1a7e9067-1d43-442b-8abc-ade0e9502262/image_thumb_1.png)
