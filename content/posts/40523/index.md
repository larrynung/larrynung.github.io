---
title: "[WinRT][C#]Windows.Storage.Pickers.FileSavePicker"
date: "2011-10-10 12:04:21"
description: "WinRT中的FileSavePicker相當於以往WindowForm所用的SaveFileDialog，是可用來選取檔案儲存位置的界面。該類別存放在Windows.Storage.Pickers命名空間內，使用上需先將Windows.Storage.Pickers命名空間加入，"
tags: [CSharp]
---

WinRT中的FileSavePicker相當於以往WindowForm所用的SaveFileDialog，是可用來選取檔案儲存位置的界面。該類別存放在Windows.Storage.Pickers命名空間內，使用上需先將Windows.Storage.Pickers命名空間加入，接著建立出FileSavePicker物件實體，設定必要的屬性後，透過PickSaveFileAsync方法啟動。

簡單的範例程式如下：

![image_thumb_2.png](/images/posts/40523/image_thumb_2.png)

裡面帶出了FileSavePicker比較重要的幾個成員。像是DefaultFileExtension屬性是設定預設的副檔名、SuggestedFileName屬性是設定預設的儲存檔名、SuggestedStartLocation屬性是設定預設的儲存位置、FileTypeChoices是設定有哪些類型的檔案可以儲存。

運行後出現的FileSavePicker會像下面這樣，跟FileOpenPicker十分類似，但下方允許輸入儲存的檔名與檔案類型。

![image_thumb.png](/images/posts/40523/image_thumb.png)

當檔案存在時，FileSavePicker也會幫我們做些確定處理。

![image_thumb_1.png](/images/posts/40523/image_thumb_1.png)

## Link

* [Quickstart: Transcoding](http://msdn.microsoft.com/en-us/library/windows/apps/hh452795(v=vs.85).aspx)
* [Exploring WinRT: File and Folder Pickers](http://lunarfrog.com/blog/2011/10/07/winrt-file-and-folder-pickers/)
