---
layout: post
title: "Octopress - Add categories page"
date: 2014-06-09 23:22:00
comments: true
tags: [Octopress]
keywords: "Octopress, Categories"
description: "Octopress - Add categories page"
---

要為 Octopress 新增 Categories 頁面，首先需先叫用下列命令產生新的頁面：

<!-- More -->

    rake new_page[page]


像是下面這樣：

{% img /images/posts/OctopressCategories/1.png %}

<br/>

然後開啟剛所建立的頁面，加入用來產生 Categories 頁面的程式。

{% img /images/posts/OctopressCategories/2.png %}

<br/>

這邊頁面的 Sharing ，Comments 與 Footer 都可以順帶修改將之關閉，一般來說 Categories 頁面是不需要這些的，修改完後存檔離開。  

接著開啟 `/source/_includes/custom/navigation.html` 設定檔設定上方的選單，把我們剛建的 Categories 頁面設定上去。  

{% img /images/posts/OctopressCategories/3.png %}

<br/>

存檔離開，建置後啟用預覽功能，即會看到上方選單多出 Categories 這個選單選項，點擊切換可看的到 Categories 頁面正常的運作。 

{% img /images/posts/OctopressCategories/4.png %}

Link
----
* [Theming & Customization - Octopress](http://octopress.org/docs/theme/template/)
