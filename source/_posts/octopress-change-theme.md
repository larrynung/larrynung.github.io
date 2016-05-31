---
layout: post
title: "Octopress - Change theme"
date: 2013-12-14 22:27:00
comments: true
tags: [Octopress]
keywords: Octopress, Theme
description: Octopress - Change theme
---

要更換 Octopress 的 Theme，我們可先找到要替換的 Theme。  

這部份可參閱 [Opthemes · Octopress Themes](http://opthemes.com/) ，它有將 Octopress 可用的 Theme 做個整理，並以縮圖方式呈現， Theme 套用起來的樣子一目了然。

<!--More-->

找到喜歡的 Theme 後可以到範例網站做進一步的預覽。

若沒有什麼問題，也以確定就是要套用該 Theme 的話，可到 GitHub 查閱進一步的安裝與設定步驟。  

除了 [Opthemes · Octopress Themes](http://opthemes.com/) 外，也可以到 [3rd Party Octopress Themes · imathis/octopress Wiki · GitHub](https://github.com/imathis/octopress/wiki/3rd-Party-Octopress-Themes) 這邊看看有無喜歡的 Theme，它的 Theme 介紹的比較多，但沒提供縮圖預覽，使用上比較沒那麼直覺。  


找到 Theme 後，基本上安裝方式都一樣，就是將 Theme 用 Git Clone 下來，Clone 下來後呼叫 `rake install` 任務進行安裝，安裝完後叫用 `rake generate` 產生靜態網頁。

    git clone GIT_URL .themes/THEME_NAME
    rake install['THEME_NAME']
    rake generate


安裝完後，各套件可能會要做不同的設定動作，因此建議還是要到對應的 GitHub 網站，餅以上面的操作為主。

這邊筆者以 Octoflat 來做個示範。

首先將 Theme 用 Git Clone 下來，並進行安裝。

{% img /images/posts/OctopressChangeTheme/7.png %}


安裝完後預設是深色的 Theme，若需要淺色的 Theme 可開啟 `sass/custom/_colors.scss `，將前後的註解給拿掉就可以了。

{% img /images/posts/OctopressChangeTheme/8.png %}


此外我們還需要對 _config.yml 作些調整。該 Theme 上方的巡覽列設定方式跟預設的 Theme 不太一樣，它是要設定在 _config.yml 內，因此我們要在 _config.yml 中加入我們的巡覽列設定，設定巡覽列上的每個元素的名稱與連結位置。

{% img /images/posts/OctopressChangeTheme/9.png %}


最後呼叫 `rake generate` 建立靜態網頁，沒意外的話 Theme 就套用完成了。


Link
----
* [Opthemes · Octopress Themes](http://opthemes.com/)
* [3rd Party Octopress Themes · imathis/octopress Wiki · GitHub](https://github.com/imathis/octopress/wiki/3rd-Party-Octopress-Themes)
* [Top 10+ Octopress Themes](http://www.evolument.com/blog/2013/03/02/top-10-plus-octopress-themes/)
