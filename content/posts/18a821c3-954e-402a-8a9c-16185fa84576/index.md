---
title: "[C#]取用.picasa.ini內存的現有資訊來做臉部偵測"
slug: "[CSharp]取用.picasa.ini內存的現有資訊來做臉部偵測"
date: "2013-11-06 12:00:00"
description: "[C#]取用.picasa.ini內存的現有資訊來做臉部偵測"
tags: [CSharp]
---Picasa應該很多人都有聽過、用過Picasa這套看圖軟體，這套看圖軟體功能強大且快速。該軟體裡面有個功能滿好玩的就是它可以對照片做臉部偵測，使用者可以為識別出來的人臉加上標記，後續還會自動偵測可能有該人士存在的圖片，讓整理的動作變得很簡單。

有用過這樣功能的人可能都會注意到它在目錄下會存放個.picasa.ini的檔案，裡面存放了一些額外的設定資訊，像是有將照片Tag的話臉部的區域資訊就會存放在裡面，裡面存放的內容像是下面這樣很明確的指出什麼檔案以及內含的臉部區域。
```
...
[2012-08-07 10.55.18.jpg]
faces=rect64(935838f6a7865d3c),a0f74040cf5a5af0
backuphash=42094
[2012-08-07 10.55.16.jpg]
faces=rect64(878631419a6c532f),bfd272ce42839572;rect64(98a439f8acee5ebe),a0f74040cf5a5af0;rect64(adc440abc26565f2),84c440386cc98c13;rect64(27b13aa33f7f65b2),6e2f7ec9de361aab;rect64(c8a32962e54b5cfc),b6ca817b8552664d
backuphash=48903
...
```
因為要做臉部偵測，我們比較關注的是臉部區域的編碼。可以看到上面的例子，臉部的資料是以rect64(CROP_RECTANGLE*), contact_id這樣的方式呈現，CROP_RECTANGLE部份是我們要的臉部範圍資訊，contact_id是用來識別這張是誰的臉，若是有多個臉部資訊則會用分號隔開。以這邊來說我們只要抓出人臉範圍並不需要知道這張臉是誰，因此只需要擷取出CROP_RECTANGLE的部份就可以了。但是透過上例我們可以看到CROP_RECTANGLE是串我們看不懂的數值，它有經過編碼的動作，在使用前我們必須將之解碼才知道臉部的區域在哪。詳細的格式說明可參閱.picasa.ini decoded：
```
# Picasa uses a special string format to store crop boxes of
# detected faces and from an applied crop filters. The number encased
# in the rect64() statement is a 64 bit hexadecimal number:

# rect64(3f845bcb59418507)

# break this number into 4 16-bit numbers by using substrings:

# '3f845bcb59418507'.substring(0,4) //"3f84"
# '3f845bcb59418507'.substring(4,8) //"5bcb"
# '3f845bcb59418507'.substring(8,12) // "5941"
# '3f845bcb59418507'.substring(12,16) // "8507"

# convert each obtained substring to an integer and divide it
# by the highest 16-bit number (2^16 = 65536), which should give 0
/// Extracts a RectangleF object from a 64-bit hex hash string.
///
/// The 64-bit hex hash string.
/// A RectangleF with the equivalent rectangle coordinates from the hash string.
public static RectangleF GetRectangleFrom64Hash(string hash64)
{
UInt64 hash = UInt64.Parse(hash64, System.Globalization.NumberStyles.HexNumber);
byte[] bytes = BitConverter.GetBytes(hash);

UInt16 l16 = BitConverter.ToUInt16(bytes, 6);
UInt16 t16 = BitConverter.ToUInt16(bytes, 4);
UInt16 r16 = BitConverter.ToUInt16(bytes, 2);
UInt16 b16 = BitConverter.ToUInt16(bytes, 0);

float left = l16 / 65535.0F;
float top = t16 / 65535.0F;
float right = r16 / 65535.0F;
float bottom = b16 / 65535.0F;

return new RectangleF(left, top, right - left, bottom - top);
}
```
解碼的部份是主要程式的核心，核心準備好了我們剩下的就是從圖片檔案找出ini檔，並從ini檔中找尋看看是否有該圖片的臉部資訊。如果有該圖片的臉部資訊就將該部份擷取出來解碼，換算我們慣用的Rectangle就可以了。這邊筆者簡單的整理了一個輔助類別：
```
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Drawing;
using System.IO;
using System.Runtime.InteropServices;
using System.Text.RegularExpressions;

namespace WindowsFormsApplication27
{
public class PicasaMetaDataHelper
{
#region DllImport
[DllImport("kernel32")]
private static extern int GetPrivateProfileString(string section, string key, string def, StringBuilder retVal, int size, string filePath);
#endregion

#region Const
const string PICASA_INI_FILE;
const string FACE_HASH_CODE_PATTERN = @"\((\w+)\)";
#endregion

#region Private Static Method
///
/// Gets the rectangle from64 hash.
///
/// The hash64.
/// The size.
///
private static RectangleF GetRectangleFrom64Hash(string hash64, Size size)
{
return GetRectangleFrom64Hash(hash64, size.Width, size.Height);
}

///
/// Gets the rectangle from64 hash.
///
/// The hash64.
/// The width.
/// The height.
///
private static RectangleF GetRectangleFrom64Hash(string hash64, int width, int height)
{
UInt64 hash = UInt64.Parse(hash64, System.Globalization.NumberStyles.HexNumber);
byte[] bytes = BitConverter.GetBytes(hash);

UInt16 l16 = BitConverter.ToUInt16(bytes, 6);
UInt16 t16 = BitConverter.ToUInt16(bytes, 4);
UInt16 r16 = BitConverter.ToUInt16(bytes, 2);
UInt16 b16 = BitConverter.ToUInt16(bytes, 0);

float left = l16 / 65535.0F;
float top = t16 / 65535.0F;
float right = r16 / 65535.0F;
float bottom = b16 / 65535.0F;

return new RectangleF(left * width, top * height, (right - left) * width, (bottom - top) * height);
}
#endregion

#region Public Static Method
///
/// Gets the face areas.
///
/// The photo file.
///
public static IEnumerable GetFaceAreas(string photoFile)
{
var photo = Bitmap.FromFile(photoFile);
return GetFaceAreas(photoFile, photo);
}

///
/// Gets the face areas.
///
/// The photo file.
/// The photo.
///
public static IEnumerable GetFaceAreas(string photoFile, Image photo)
{
var folder = Path.GetDirectoryName(photoFile);
var iniFile = Path.Combine(folder, PICASA_INI_FILENAME);

if (!File.Exists(iniFile))
yield break;

var file
var faceDataBuffer = new StringBuilder(512);
GetPrivateProfileString(fileName, "faces", string.Empty, faceDataBuffer, 512, iniFile);

var faceData = faceDataBuffer.ToString();

if (faceData.Length == 0)
yield break;

var ms = Regex.Matches(faceData, FACE_HASH_CODE_PATTERN);

foreach (Match m in ms)
{
var faceHashCode = m.Groups[1].Value;
yield return GetRectangleFrom64Hash(faceHashCode, photo.Size);
}
}
#endregion
}
}
```
使用起來就像這樣，將圖片載入後透過輔助類別取得臉部資訊，並在圖片上畫出臉部區域後顯示：
```
...
if (openFileDialog1.ShowDialog() == DialogResult.OK)
{
var image = Bitmap.FromFile(openFileDialog1.FileName);
var faceAreas = PicasaMetaDataHelper.GetFaceAreas(openFileDialog1.FileName, image);

using (var g = Graphics.FromImage(image))
{
g.DrawRectangles(new Pen(Brushes.Red, 5), faceAreas.ToArray());
}
pbxPhoto.Image = image;
}
...
```
實際運行後可以看到我們正確的將臉部給標示出來，跟Picasa上看到的臉部範圍完全一樣。

![](\images\posts\18a821c3-954e-402a-8a9c-16185fa84576\image_thumb_2.png) 

![](\images\posts\18a821c3-954e-402a-8a9c-16185fa84576\image_thumb_3.png)

## Link

- Picasa.ini 檔案

- .picasa.ini decoded

- GetPicasaFaces