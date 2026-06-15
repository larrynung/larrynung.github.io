---
title: "[WinRT][C#]Windows.Storage.Pickers.FolderPicker"
date: "2011-10-10 09:15:15"
description: "[WinRT][C#]Windows.Storage.Pickers.FolderPicker"
tags: [CSharp]
---

WinRT中的FolderPicker類似於WindowForm中的FolderBrowserDialog，可用來做選取目錄之用。使用上跟FileOpenPicker非常類似，一樣是建立實體後，設定一些屬性像是瀏覽的起始位置、或是用縮圖模式還是清單模式顯示之類的，然後叫用PickSingleFolderAsync方法即可，程式撰寫起來像下面這般。

![image_thumb_2.png](/images/posts/40780/image_thumb_2.png)

選取完的目錄資訊可由PickSingleFolderAsync方法的回傳值取得，也可再進一步取得裡面的檔案、目錄、或是縮圖等等資訊。

當我們透過PickSingleFolderAsync方法叫起FolderPicker時，我們可以看到像下面的畫面，跟OpenFilePicker也十分類似，不同的是透過FolderPicker我們只能針對目錄去選取，無法選取檔案，且選取方式變得要先[Choose this folder]，才能[Ok]確定。

![image_thumb.png](/images/posts/40780/image_thumb.png)

![image_thumb_1.png](/images/posts/40780/image_thumb_1.png)

## Link

* [Exploring WinRT: File and Folder Pickers](http://lunarfrog.com/blog/2011/10/07/winrt-file-and-folder-pickers/)
* [FolderPicker class](http://msdn.microsoft.com/en-us/library/windows/apps/br207881(v=VS.85).aspx)
