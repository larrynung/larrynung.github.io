---
title: "[C#]使用BitmapDecoder快速讀取圖檔的大小"
slug: "[CSharp]使用BitmapDecoder快速讀取圖檔的大小"
date: "2013-11-06 12:00:00"
description: "[C#]使用BitmapDecoder快速讀取圖檔的大小"
tags: [CSharp]
---

一般我們想要讀取圖檔的大小，通常在Windows Form中都是直接載入成Bitmap，再去讀取Bitmap物件的長、寬、或是大小屬性，像是像下面這樣撰寫：
```
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

<img  border="0" alt="image" src="\images\posts