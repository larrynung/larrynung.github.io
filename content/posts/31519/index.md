---
title: "[C#]Stream.Write Extension Method"
slug: "[CSharp]Stream.Write Extension Method"
date: "2011-07-12 10:53:13"
description: "[C#]Stream.Write Extension Method"
tags: [CSharp]
---

在處理Stream型態時常會使用到Stream.Write這個方法，每次都會有種疑問就是，大多數的處理都是要將Buffer整個寫入，為何偏偏每次都要將索引帶0，長度帶為Buffer的大小呢?另外在處理Stream時，若要顯示其處理進度，是否能有更為簡單的方法?這邊將我為了解決這些問題所寫的擴充方法整裡如下：
```
using System;
using System.Reflection;
using System.ComponentModel;
using System.Linq;
using System.IO;

public static class StreamExtension
{
public static void Write(this Stream targetStream, byte[] buffer)
{
if (!targetStream.CanWrite)
throw new ArgumentException("targetStream", "Unwritable stream");

targetStream.Write(buffer, 0, buffer.Length);
}

public static void Write(this Stream targetStream, Stream sourceStream)
{
if (!targetStream.CanWrite)
throw new ArgumentException("targetStream", "Unwritable stream");

if (sourceStream == null)
throw new ArgumentNullException("sourceStream");

if (!sourceStream.CanRead)
throw new ArgumentException("sourceStream", "Unreadable stream");

targetStream.Write(sourceStream, 1024, null);
}

public static void Write(this Stream targetStream, Stream sourceStream, int bufferSize, Action progressChangedCallBack)
{
if (sourceStream == null)
throw new ArgumentNullException("sourceStream");

if (!sourceStream.CanRead)
throw new ArgumentException("sourceStream", "Unreadable stream");

if (!targetStream.CanWrite)
throw new ArgumentException("targetStream", "Unwritable stream");

if (bufferSize 0)
{
targetStream.Write(buffer, 0, readByteCount);

if (progressChangedCallBack != null)
{
offset += readByteCount;

var currentPercent = (int)(((double)offset) / sourceStream.Length * 100);
if (currentPercent == percent)
continue;

percent = currentPercent;
progressChangedCallBack(targetStream, new System.ComponentModel.ProgressChangedEventArgs(percent, null));
}
}
}
}
```
使用上Write方法會多三個多載版本，一個是將buffer整個寫入、一個是將stream的內容整個讀出並寫入、一個則是用來寫入整個stream內容，並可帶入處理的Buffer大小，與處理進度回報的Callback，用以處理進度的顯示。
```
targetStream.Write(buffer);
targetStream.Write(sourceStream);
targetStream.Write(sourceStream, 1024, (sender, e) => { Console.WriteLine(e.ProgressPercentage.ToString ()); });
```
這邊針對進度處理的擴充方法示範個較為詳細的範例，這邊我會讀取C槽下的test.data檔案，檔案大小為5MB多，開啟後將其寫入c槽下的test_copy.data。處理的buffer大小為1024，每當在處理時偵測到進度改變時會顯示出當前處理的進度比例。
```
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;

namespace ConsoleApplication11
{
class Program
{
static void Main(string[] args)
{
using (FileStream targetStream = File .Create (@"c: est_copy.dat"))
{
using (FileStream sourceStream= File.Open (@"c: est.dat", FileMode.Open))
{
targetStream.Write(sourceStream, 1024, (sender, e) => { Console.WriteLine(e.ProgressPercentage.ToString()); });
}
}
}
}
}
```
運行結果如下：

![](/images/posts/31519/)