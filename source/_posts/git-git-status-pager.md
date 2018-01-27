---
title: "Git - Git status pager"
date: 2018-01-28 00:03:51
tags: [Git]
---

使用 Git 做版控的程式如果一次變動過多，使用 Git Status 查閱變動時，我們會看到所有變動會一次全部都顯示出來，無法有效的查閱程式的變動。  

<!-- More -->

{% asset_img 1.png %}
 
<br/>


這時我們可以調用 Git Config 命令將 Git Status 的分頁功能開啟。  

    git config --global pager.status true

{% asset_img 2.png %}
 
<br/>


或是手動修改設定檔開啟也可以。  

{% asset_img 3.png %}
 
<br/>


這樣 Git Status 就會一頁一頁的顯示。  

{% asset_img 4.png %}
 
<br/>
