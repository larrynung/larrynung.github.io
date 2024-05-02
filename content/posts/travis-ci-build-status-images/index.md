---
title: "Travis CI - Build Status images"
date: "2014-01-15 23:57:00"
description: "Travis CI - Build Status images"
tags: [Travis, CI]
---


Travis CI 支援 Build status image，能讓我們將 Repository 建置的狀態嵌至網站上。  

<!-- More -->

使用時只要開啟 Travis CI，將左側這邊切換至 My Repositories。  

{% img /images/posts/TravisCIBuildStatusImages/1.png %}

<br/>


切換至欲使用的 Repository ，在右側的建置資訊這邊，可以看到右上方有個圖片表示著這個 Repository 的建置狀態，這就是我們要拿來內嵌的圖片。

{% img /images/posts/TravisCIBuildStatusImages/2.png %}

<br/>


滑鼠點擊後會出現像下面這樣的對話框。  

{% img /images/posts/TravisCIBuildStatusImages/3.png %}

<br/>


對話框裡面有提供嵌入用的語法，將之複製並貼入欲嵌入的位置就可以了。  

多半我們會將它嵌在 GitHub 的 README.md 內。  

{% img /images/posts/TravisCIBuildStatusImages/4.png %}

<br/>


瀏覽 Repository 時就能一眼看出是否能成功的建置。  

{% img /images/posts/TravisCIBuildStatusImages/5.png %}


Link
----
* [Travis CI: Status Images] (http://about.travis-ci.org/docs/user/status-images/)
