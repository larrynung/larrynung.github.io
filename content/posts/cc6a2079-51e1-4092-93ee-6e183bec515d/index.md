---
title: "[C#]使用BitmapDecoder快速讀取圖檔的大小"
date: "2013-11-06 12:00:00"
description: "一般我們想要讀取圖檔的大小，通常在Windows Form中都是直接載入成Bitmap，再去讀取Bitmap物件的長、寬、或是大小屬性，像是像下面這樣撰寫： 但這樣做會有個問題就是效率會比較差，因為必須將整個圖檔先行載入，圖檔越大就越久，記憶體也吃的兇。"
tags: [CSharp]
---

一般我們想要讀取圖檔的大小，通常在Windows Form中都是直接載入成Bitmap，再去讀取Bitmap物件的長、寬、或是大小屬性，像是像下面這樣撰寫：

```csharp
...
using (var image = Bitmap.FromFile(file))
{
	var size = image.Size;
	...
}
...
```

但這樣做會有個問題就是效率會比較差，因為必須將整個圖檔先行載入，圖檔越大就越久，記憶體也吃的兇。

比較好的作法應該是直接讀取檔案的檔頭，圖檔的大小資訊再圖檔的檔頭就有了，所以不需要將整個圖檔載入就可以得知，效率也會因此有所增進。比較簡單的作法就是直接使用WPF的功能，若是Window Form程式的話我們可以額外將PresentationCore.dll、System.Xaml、與WindowsBase.dll加入參考。

![image_thumb_2.png](/images/posts/cc6a2079-51e1-4092-93ee-6e183bec515d/image_thumb_2.png)

並引用System.Windows.Media命名空間。

```csharp
using System.Windows.Media;
```

實際撰寫我們可以用BitmapDecoder.Create將要讀取的圖檔位置帶入，然後取得第一個Frame，裡面的PixelWidth與PixelHeight就是我們所要擷取的圖檔大小。

```csharp
...
var decoder = BitmapDecoder.Create(new Uri(file), BitmapCreateOptions.DelayCreation, BitmapCacheOption.None);
var frame = decoder.Frames.FirstOrDefault();

var size = new Size(frame.PixelWidth, frame.PixelHeight);
...
```

完整的測試範例如下：

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
using System.IO;
using System.Drawing.Imaging;
using System.Windows.Threading;
using System.Windows.Media;
using System.Diagnostics;

namespace WindowsFormsApplication32
{
	public partial class Form1 : Form
	{
		public Form1()
		{
			InitializeComponent();
		}

		private long StopwatchMethod(Action act, int testCount, Boolean returnAverageValue = false)
		{
			var sw = Stopwatch.StartNew();
			for (int i = 0; i < testCount;++i )
				act();

			sw.Stop();
			var elapsedMilliseconds = sw.ElapsedMilliseconds;
			return (returnAverageValue) ? elapsedMilliseconds / testCount : elapsedMilliseconds;
		}

		public Size GetImageSize1(string file)
		{
			var decoder = BitmapDecoder.Create(new Uri(file), BitmapCreateOptions.DelayCreation, BitmapCacheOption.None);
			var frame = decoder.Frames.FirstOrDefault();

			return new Size(frame.PixelWidth, frame.PixelHeight);
		}

		public Size GetImageSize2(string file)
		{
			using (var image = Bitmap.FromFile(file))
			{
				return image.Size;
			}
		}

		private void button1_Click(object sender, EventArgs e)
		{
			if (openFileDialog1.ShowDialog() == System.Windows.Forms.DialogResult.OK)
			{
				var file = openFileDialog1.FileName;

				GetImageSize1(file);
				GetImageSize2(file);

				textBox1.Clear();
				textBox1.Text += "BitmapDecoder" + Environment.NewLine;
				textBox1.Text += StopwatchMethod(() => GetImageSize1(file), 10).ToString() + Environment.NewLine;

				textBox1.Text += Environment.NewLine;
				textBox1.Text += "Bitmap" + Environment.NewLine;
				textBox1.Text += StopwatchMethod(() => GetImageSize2(file), 10).ToString() + Environment.NewLine;
			}
		}
	}
}
```

實際運行時筆者帶入大概4~5 MB的圖檔，可以看到光運行十次在效能上就有很大的差異。

![image_thumb.png](/images/posts/cc6a2079-51e1-4092-93ee-6e183bec515d/image_thumb.png)

## Link

* Determining height and width of an image without loading it into memory?
* Reading Image Headers to Get Width and Height
* Getting image dimensions without reading the entire file
