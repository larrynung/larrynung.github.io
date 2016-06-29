---
title: Hexo - Post asset folder
date: 2016-06-29 23:00:02
tags: Hexo
---

要使用 Asset folder，我們可以開啟 Hexo 的設定檔，將 post_asset_folder 設定設為 true。  

<!-- More -->

{% asset_img 1.png %}

<br/>


當使用 Hexo 建立一篇文章時。  

{% asset_img 2.png %}

<br/>


就會連帶幫我們建一個與文章同名的 Asset folder。  

{% asset_img 3.png %}

<br/>


我們可以將文章以外所有的檔案放置在這目錄下，然後使用下列語法將之引用。  

    {% asset_path slug %}
    {% asset_img slug [title] %}
    {% asset_link slug [title] %}

<br/>


像是這邊筆者將圖片放置在 Asset folder 內。  

{% asset_img 4.png %}

<br/>


在文章中使用就會像下面這樣：  

{% asset_img 5.png %}

<br/>


Link
----
* [資產資料夾 | Hexo](https://hexo.io/zh-tw/docs/asset-folders.html)
