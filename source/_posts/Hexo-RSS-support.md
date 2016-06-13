---
title: Hexo - RSS support
date: 2016-06-13 23:14:07
tags: Hexo
---

要為部落格加入 RSS，我們需先安裝 [hexo-generator-feed](https://github.com/hexojs/hexo-generator-feed)。  

<!-- More -->

    npm install hexo-generator-feed --save

{% asset_img 1.png %}

<br/>


然後開啟 Hexo 的設定檔做些設定，像是 RSS feed 的數量等。  

    feed:
      type: atom
      path: atom.xml
      limit: 20
      hub:

{% asset_img 2.png %}

<br/>


這樣在產生靜態檔案時就會一併產生出 RSS 的 xml 檔。  

{% asset_img 3.png %}

<br/>


部落格發佈上去 RSS 就可以使用了。  

{% asset_img 4.png %}

<br/>


這邊要注意的是，有的主題也支援 RSS 的整合，像是筆者用的 Next 主題就有支援，設定方式要參閱主題的使用文件，像是 Next 這邊的設定方式就是將主題設定黨內的 rss 設定留空。  

{% asset_img 5.png %}

<br/>


主題就會在預期的地方顯示 RSS 訂閱的連結。  

{% asset_img 6.png %}

<br/>


Link
---
* [hexojs/hexo-generator-feed: Feed generator for Hexo.](https://github.com/hexojs/hexo-generator-feed)
