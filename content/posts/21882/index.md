---
title: "[C#]絕對路徑轉相對路徑"
date: "2011-03-17 01:05:51"
description: "[C#]絕對路徑轉相對路徑"
tags: [CSharp]
---

<p>之前在做壓縮的函式庫時，有碰到一個需求是壓縮整個目錄的資料，目錄裡面可能又含有許多子目錄，要壓縮時會需要指派其在壓縮檔內的存放位置，故會需要將要壓縮的檔案位置轉換為相對路徑，壓縮檔內依其相對位置做存放。當初在做這個功能時，找了一下網路上的資料，多半找到的都是用遞迴下去自行處理，雖然運作良好，但程式在理解上會變得稍微困難一點。</p>  <p> </p>  <p>最近再回過頭來稍微看了一下，發現.NET內建的Uri類別中就可以達到我們的需求，像是下面這樣透過MakeRelativeUri去取得兩個絕對路徑運算後的相對路徑：</p>  <p> </p>  <pre>static String GetRelativePath(String basePath, String targetPath)
{
	Uri baseUri = new Uri(basePath);
	Uri targetUri = new Uri(targetPath);
	return baseUri.MakeRelativeUri(targetUri).ToString().Replace(@"/", @"\");
}</pre>

<p> </p>

<p> </p>

<p>完整範例如下：</p>

<p> </p>

<pre>static void Main(string[] args)
{
	String basePath = @"c:	est\123\456\789\";	// @"c:	est\123";
	String targetPath = @"c:	est\123\";			// @"c:	est\123\456\789";
	String relativePath = GetRelativePath(basePath, targetPath);
 
	Console.WriteLine("Base Path: " + basePath);
	Console.WriteLine("Target Path: " + targetPath);
	Console.WriteLine("Relative Path: " + relativePath);
}
 
static String GetRelativePath(String basePath, String targetPath)
{
	Uri baseUri = new Uri(basePath);
	Uri targetUri = new Uri(targetPath);
	return baseUri.MakeRelativeUri(targetUri).ToString().Replace(@"/", @"\");
}</pre>

<p> </p>

<p>運行結果如下：</p>

<p><img style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" border="0" alt="image" src="\images\posts\21882\image_thumb.png" width="417" height="191" /></p>
