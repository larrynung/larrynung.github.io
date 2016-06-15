---
title: Hexo - Add category page
date: 2016-06-15 21:13:22
tags: Hexo
---

要為 Hexo 部落格建立分類頁面，首先要建立 categories 的頁面。  

<!-- More -->

    hexo n page categories

{% asset_img 1.png %}

<br/>


開啟剛產生的分類頁面，設定 type 為 categories。如果不希望能在分類頁面上留言的話，這邊也可以順便將 comments 為 false。  

{% asset_img 2.png %}

<br/>


再來開啟 Hexo 的設定檔，確定 default_category/category_map 設定是否需要更動。  

{% asset_img 3.png %}

<br/>


並在文章上方設定 categories，指定文章的分類。  

{% asset_img 4.png %}

<br/>


將服務運行起來就可以在 `/categories` 看到分類頁面了。  

{% asset_img 5.png %}

<br/>


Link
---
* [Hexo使用攻略：（四）Hexo的分类和标签设置 | { GoonX }](http://ijiaober.github.io/2014/08/05/hexo/hexo-04/)
* [創建分類頁面· iissnan/hexo-theme-next Wiki](https://github.com/iissnan/hexo-theme-next/wiki/%E5%88%9B%E5%BB%BA%E5%88%86%E7%B1%BB%E9%A1%B5%E9%9D%A2)
