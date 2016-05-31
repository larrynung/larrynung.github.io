---
layout: post
title: "Octopress - Add About Me section in sidebar"
date: 2014-06-14 18:21:00
comments: true
tags: [Octopress]
keywords: "Octopress"
description: "Octopress - Add About Me section in sidebar"
---

新增 About Me 檔，檔案位置存放在 `source/_includes/custom/asides` 下。  

<!-- More -->

{% img /images/posts/OctopressAboutMe/1.png %}

<br/>

編輯後存檔退出。  

{% img /images/posts/OctopressAboutMe/2.png %}

<br/>

接著開啟 `_config.yml` 設定檔找到 `blog_index_asides` 設定，將剛編輯好的 About Me 檔設上。  

{% img /images/posts/OctopressAboutMe/3.png %}

<br/>

存檔退出，編譯網頁後啟用預覽功能，即會看到側欄這邊多出剛我們設在 About Me 檔的內容。  

{% img /images/posts/OctopressAboutMe/4.png %}

<br/>

Link
----
* [Theming & Customization - Octopress](http://octopress.org/docs/theme/template/)
