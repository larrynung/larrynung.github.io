---
title: "Visual Studio 2013 Preview New Feature - XAML Editor's Code Snippets"
date: "2013-11-06 12:00:00"
description: "Visual Studio 2013 Preview New Feature - XAML Editor's Code Snippets"
---

Visual Studio 2013 Preview在XAML編輯區開始支援Code Snippets功能，在XAML編輯區中按下滑鼠右鍵，就可以在滑鼠右鍵快顯選單中看到[Insert Snippet...]，以及[Surround With...]這兩個選單選項。 

不過雖然支援了Code Snippets功能，但在Visual Studio 2013 Preview中仍未放入任何可用的Code Snippets。

我們必須要自行撰寫並存放在特定位置，這邊筆者暫用Snippet Designer來示範如何加入自己的Code Snippets進Visual Studio 2013 Preview。首先開啟程式編輯畫面，在程式編輯區中按下滑鼠右鍵，在彈出的滑鼠右鍵快顯選單中，選取[Export as Snippet]選單選項，將Snippet Designer的Code Snippets編輯畫面帶出。

Snippet Designer的Code Snippets編輯畫面出來後，這邊的動作就跟一般用Snippet Designer做Code Snippets一樣，放入我們想要Visual Studio幫我們帶出的XAML Code，設定Snippet名稱、Short Cut、與Replacement...等，Language這邊為了方便，可選取XML。

設定好後存檔…

存完檔後將檔案開啟，將Code Language這邊由xml改為xaml。

完成後回到Visual Studio 2013 Preview再試一次Code Snippets功能

可以發現我們剛剛所編輯的Code Snippets已經可以使用了。