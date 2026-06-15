---
title: "[C#]擷取Picasa資料庫(_.PMP)內現有的資料"
slug: "[CSharp]擷取Picasa資料庫(_.PMP)內現有的資料"
date: "2013-11-06 12:00:00"
description: "[C#]擷取Picasa資料庫(_.PMP)內現有的資料"
tags: [CSharp]
---

筆者在[C#]取用.picasa.ini內存的現有資訊來做臉部偵測這篇透過了Picasa的ini檔擷取出了臉部的資訊，但是該ini檔如果不經過Picasa去整理相片就不會產生。因此這邊筆者想要直接去擷取Picasa的資料庫，因為用Picasa瀏覽時多半相片都會顯示臉部的範圍，儘管使用者沒有做過Tag的動作，代表Picasa其實不論是否有做過Tag都會有臉部識別的資訊，只是可能存放在自己的資料庫中。

Picasa的資料庫檔存放在%localappdata%\Google\Picasa2\db3下，以.pmp為附檔名。

![image_thumb_1.png](/images/posts/45365d47-127e-4354-8d69-6d5aa9eb9b6d/image_thumb_1.png)

.pmp是Picasa自己的檔案格式，格式的說明可參閱[The Picasa .pmp format，簡單的來說該檔案的Header長得像下面這樣：](http://sbktech.blogspot.tw/2011/12/picasa-pmp-format.html)

4bytes: magic: 0x3fcccccd
2bytes: field-type: unsigned short.
2bytes: 0x1332 -- constant.
4bytes: 0x00000002 -- constant.
2bytes: field-type: unsigned short -- identical with field-type above.
2bytes: 0x1332 -- constant.
4bytes: number-of-entries: unsigned int.

1~4 Byte是用來識別的，固定是0x3fcccccd。

5~6 Byte是後面存放的資料型態，這主要是告訴我們後面要怎樣將存放的資料讀取出來，它的值介於0x00 - 0x07：

0x0: null-terminated strings.
0x1: unsigned integers, 4 bytes.
0x2: dates, 8 bytes as a double.
0x3: byte field, 1 unsigned byte.
0x4: unsigned long, 8bytes.
0x5: unsigned short, 2bytes.
0x6: null-terminated string.
0x7: unsigned int, 4 bytes.

7~8 Byte是個常數值，固定是0x1332。

9~12 Byte也是個常數，固定是0x00000002。

13~14 Byte一樣是檔案的型態，取出的值必須要跟5~6 Byte取出的值是一樣的。

15~16 Byte是個常數值，固定是0x1332。

17~20 Byte是表示後面有多少的資料量。

第21個Byte後面就是實際的資料，資料的讀取方式依照前面取出的資料型態不同，解析的方式就有所不同。

規則知道後我們可以很輕鬆的分析檔案是否是.pmp的格式，也可以擷取出裡面的資料。像是下面這樣：

```csharp
			...
			using (var fs = File.OpenRead(file))
			{
				using (var br = new BinaryReader(fs))
				{
					var magic = br.ReadBytes(4);
					if(magic[0] != 0xcd ||
						magic[1] != 0xcc ||
						magic[2] != 0xcc ||
						magic[3] != 0x3f)
					{
						throw new Exception("Incorrect format");
					}

					var type = br.ReadInt16();

					if (0x1332 != br.ReadInt16())
					{
						throw new Exception("Incorrect format");
					}

					if (0x00000002 != br.ReadInt32())
					{
						throw new Exception("Incorrect format");
					}

					if (type != br.ReadInt16())
					{
						throw new Exception("Incorrect format");
					}

					if (0x1332 != br.ReadInt16())
					{
						throw new Exception("Incorrect format");
					}

					var number = br.ReadInt32();

					switch (type)
					{
 						case 0x00:
							DumpStringField(br, number);
							break;
						case 0x01:
							Dump4ByteField(br, number);
							break;
						case 0x02:
							DumpDateField(br, number);
							break;
						case 0x03:
							DumpByteField(br, number);
							break;
						case 0x04:
							Dump8ByteField(br, number);
							break;
						case 0x05:
							Dump2ByteField(br, number);
							break;
						case 0x06:
							DumpStringField(br, number);
							break;
						case 0x07:
							Dump4ByteField(br, number);
							break;
						default:
							throw new Exception("Incorrect format");
					}
				}
			}
			...
```

比較完整的程式碼範例如下(Date那邊的處理程式是壞的，以筆者的需求來說也暫時用不到，故目前請忽略該段處理)：

```csharp
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO;

namespace WindowsFormsApplication28
{
	public partial class Form1 : Form
	{
		public Form1()
		{
			InitializeComponent();
		}

		private void btnLoad_Click(object sender, EventArgs e)
		{
			if (openFileDialog1.ShowDialog() != DialogResult.OK)
				return;

			textBox1.Text = string.Empty;

			var file = openFileDialog1.FileName;

			using (var fs = File.OpenRead(file))
			{
				using (var br = new BinaryReader(fs))
				{
					var magic = br.ReadBytes(4);
					if(magic[0] != 0xcd ||
						magic[1] != 0xcc ||
						magic[2] != 0xcc ||
						magic[3] != 0x3f)
					{
						throw new Exception("Incorrect format");
					}

					var type = br.ReadInt16();

					if (0x1332 != br.ReadInt16())
					{
						throw new Exception("Incorrect format");
					}

					if (0x00000002 != br.ReadInt32())
					{
						throw new Exception("Incorrect format");
					}

					if (type != br.ReadInt16())
					{
						throw new Exception("Incorrect format");
					}

					if (0x1332 != br.ReadInt16())
					{
						throw new Exception("Incorrect format");
					}

					var number = br.ReadInt32();

					switch (type)
					{
 						case 0x00:
							DumpStringField(br, number);
							break;
						case 0x01:
							Dump4ByteField(br, number);
							break;
						case 0x02:
							DumpDateField(br, number);
							break;
						case 0x03:
							DumpByteField(br, number);
							break;
						case 0x04:
							Dump8ByteField(br, number);
							break;
						case 0x05:
							Dump2ByteField(br, number);
							break;
						case 0x06:
							DumpStringField(br, number);
							break;
						case 0x07:
							Dump4ByteField(br, number);
							break;
						default:
							throw new Exception("Incorrect format");
					}
				}
			}
		}

		private void DumpStringField(BinaryReader br, int number)
		{
			var sb = new StringBuilder(1024);
			for (long i = 0; i < number; i++)
			{
				var value = getString(br);//br.ReadString();
				sb.AppendFormat("[{0}] {1}", i, value);
				sb.Append(Environment.NewLine);
			}
			textBox1.Text = sb.ToString();
		}

		private String getString(BinaryReader br)
		{
			var sb = new StringBuilder();
			int c;
			while((c = br.Read()) != 0) {
				sb.Append((char)c);
			}
			return sb.ToString();
		}

		private void DumpDateField(BinaryReader br, int number)
		{
			var sb = new StringBuilder();
			int[] bytes = new int[8];
			for (long idx = 0; idx < number; idx++)
			{
				long ld = 0;
				for (int i = 0; i < 8; i++)
				{
					bytes[i] = br.ReadByte();
					var temp = bytes[i];
					temp <<= (8 * i);
					ld += temp;
				}

				sb.Append("[" + idx + "] ");

				double d = BitConverter.Int64BitsToDouble(ld);

				d -= 25569;
				long ut = (long)Math.Round(d * 864001 * 10001);

				sb.Append(DateTime.FromFileTime(ut));
			}
			textBox1.Text = sb.ToString();
		}

		private void DumpByteField(BinaryReader br, int number)
		{
			var sb = new StringBuilder(1024);
			for (long i = 0; i < number; i++)
			{
				var value = br.ReadByte();
				sb.AppendFormat("[{0}] {1}", i, value);
				sb.Append(Environment.NewLine);
			}
			textBox1.Text = sb.ToString();
		}

		private void Dump2ByteField(BinaryReader br, int number)
		{
			var sb = new StringBuilder(1024);
			for (long i = 0; i < number; i++)
			{
				var value = br.ReadInt16();
				sb.AppendFormat("[{0}] {1}", i, value);
				sb.Append(Environment.NewLine);
			}
			textBox1.Text = sb.ToString();
		}

		private void Dump4ByteField(BinaryReader br, int number)
		{
			var sb = new StringBuilder(1024);
			for (long i = 0; i < number; i++)
			{
				var value = br.ReadInt32();
				sb.AppendFormat("[{0}] {1}", i, value);
				sb.Append(Environment.NewLine);
			}
			textBox1.Text = sb.ToString();
		}

		private void Dump8ByteField(BinaryReader br, int number)
		{
			var sb = new StringBuilder();
			int[] bytes = new int[8];
			for (long idx = 0; idx < number; idx++)
			{
				for (int i = 0; i < 8; i++)
				{
					bytes[i] = br.ReadByte();
				}

				sb.Append("[" + idx + "] ");

				for (int i = 7; i >= 0; i--)
				{
					String x = Convert.ToString(bytes[i], 16);

					if (x.Length == 1)
					{
						sb.Append("0");
					}
					sb.Append(x);
				}
				sb.AppendLine();
			}
			textBox1.Text = sb.ToString();
		}
	}
}
```

運行後我們就可以查驗.pmp的檔案，像是下圖筆者就成功的將Picasa內的目錄資訊給正確的擷取出來了。

![image_thumb.png](/images/posts/45365d47-127e-4354-8d69-6d5aa9eb9b6d/image_thumb.png)

## Link

* The Picasa .pmp format
