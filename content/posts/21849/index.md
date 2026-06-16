---
title: "相對路徑與絕對路徑做合併處理"
date: "2011-03-15 01:05:49"
description: "有時撰寫程式時我們會需要以當前路徑做為基底路徑，在其下面存放對應的資料，可能直接放在當前路徑下、或是放在當前路徑下面的目錄裡面，此時我們會需要以做相對路徑與絕對路徑的合併，換算所要存取的檔案的絕對路徑。"
tags: [CSharp,VB.NET]
---

有時撰寫程式時我們會需要以當前路徑做為基底路徑，在其下面存放對應的資料，可能直接放在當前路徑下、或是放在當前路徑下面的目錄裡面，此時我們會需要以做相對路徑與絕對路徑的合併，換算所要存取的檔案的絕對路徑。

要做相對路徑與絕對路徑做合併處理，多數人直覺想到的是System.IO.Path.Combine方法，但其實他對於此種處理並不能處理得很好，只能幫我們補個斜線並做字串的合併：

Const basePath As String = "c:\test\123\456\789"
Const relativePath As String = "..\888"

Console.WriteLine(System.IO.Path.Combine(basePath, relativePath))

![image_thumb_1.png](/images/posts/21849/image_thumb_1.png)

若使用的是VB.NET，我們還可以透過My.Computer.FileSystem.CombinePath去做合併的動作，我們可以看到的是，透過這個方法來處理的效果比System.IO.Path.Combine好得太多了：

Const basePath As String = "c:\test\123\456\789"
Const relativePath As String = "..\888"
Console.WriteLine(My.Computer.FileSystem.CombinePath(basePath, relativePath))

![image_thumb_2.png](/images/posts/21849/image_thumb_2.png)

但在C#中並沒有My這樣的東西可以使用，除非將VB.NET的函示庫加入使用，不然我們就只可以透過一些小技巧來處理這樣的問題，當然這樣的技巧也能套用在VB.NET上面。像是使用System.IO.Path.Combine合併後，再透過System.IO.Path.GetFullPath去幫我們處理，或是建立Uri物件實體，並透過LocalPath屬性取得合併處理後的路徑：

Const basePath As String = "c:\test\123\456\789"
Const relativePath As String = "..\888"
Console.WriteLine(System.IO.Path.GetFullPath(System.IO.Path.Combine(basePath, relativePath)))
Console.WriteLine(New Uri(System.IO.Path.Combine(basePath, relativePath)).LocalPath)

![image_thumb_3.png](/images/posts/21849/image_thumb_3.png)
