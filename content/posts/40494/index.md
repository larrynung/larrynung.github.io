---
title: "[WinRT][C#]Windows.Storage.Pickers.FileOpenPicker"
date: "2011-10-10 11:01:49"
description: "[WinRT][C#]Windows.Storage.Pickers.FileOpenPicker"
tags: [CSharp]
---

WinRT中的FileOpenPicker相當於以往WindowForm所用的OpenFileDialog，是可用來選取檔案的界面。該類別存放在Windows.Storage.Pickers命名空間內，使用上需先將Windows.Storage.Pickers命名空間加入，接著建立出FileOpenPicker物件實體，設定必要的屬性後，透過PickSingleFileAsync或是PickMultipleFileAsync方法啟動。

簡單的範例程式如下。

裡面帶出了FileOpenPicker比較重要的幾個成員。像是FileTypeFilter屬性可用來設定界面所要顯示的檔案類型、CommitButtonText屬性可用來設定確定按鈕上顯示的字串。

SettingsIdentifer可設定識別用的字串、ViewMode設定是要用清單還是縮圖方式呈現。

SuggestedStartLocation則是設定選取檔案時的起始位置。

實際運行此範例程式，點選Select File驅動檔案選取界面。

WinRT中的檔案選取界面會像下面這樣，左上方Files字樣提示這是檔案選取界面，Files右邊的字樣則是當前所在的目錄。Files字樣下方是工具條，能做向上巡覽、排序、選取全部。中間區塊是主要的檔案瀏覽區。下方是選取的檔案呈現區。

點選左上方的Files，可快速切換幾個常用的系統路徑。

檔案目錄與檔案會以不同的方式呈現，檔案目錄會在左半邊，以方塊呈現。檔案則會在右半邊。 

 滑鼠移到目錄或是檔案上，會顯示詳細的資訊。

若需要切換排序，可點選Go up後面的Sort by XXXX，有兩種排序方式可供選擇，一種是按名稱排序的Sort by name，一種是按時間排序的Sort by date。

選取檔案後可在下方的選取檔案呈現區看到選取的檔案，當確定選取無誤後可按下[Open]按鈕確定選取。

以這範例來說選取的檔案會顯示在ListBox中。

## Link
     FileOpenPicker class