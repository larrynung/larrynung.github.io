---
layout: post
title: "Octopress - Remove reduant blog folder"
date: 2013-11-25 21:52
comments: true
categories: [Octopress]
keywords: "Octopress"
description: "Octopress - Remove reduant blog folder"
---

Octopress blog架設好後，預設的部落格網址格式為/blog/:year/:month/:day/:title/，會在網址那邊多一層不必要的blog目錄，要將這層不必要的目錄拿掉，我們可以開啟_config.yaml進行些修改，將permalink、 category_dir、與 pagination_dir的/bloh前綴給拿掉 ([Demo](/images/posts/OctopressRemoveReduantBlogFolder/1.png))。

<!--More-->

    #permalink: /blog/:year/:month/:day/:title/
    permalink: /:year/:month/:day/:title/

    #category_dir: blog/categories
    category_dir: categories

    #pagination_dir: blog  # Directory base for pagination URLs eg. /blog/page/2/
    pagination_dir:       # Directory base for pagination URLs eg. /page/2/


接著將source/_includes/custom/navigation.html檔案開啟，針對上方巡覽列這邊的連結部分作些修改，一樣將/blog前綴給移掉 ([Demo](/images/posts/OctopressRemoveReduantBlogFolder/2.png))。

    <li><a href="/">Home</a></li>
    <li><a href="/archives">Archives</a></li>


同樣的動作也要對source/index.html做一次。

    <a href="/archives">Archives</a>


網址跟連結都做完，記得要將本來放在source/blog下的資料移到source ([Demo](/images/posts/OctopressRemoveReduantBlogFolder/3.png))。

    mv -v source/blog/archives source/


最後老樣子建置網頁並預覽
    
    rake generate
    rake preview


預覽沒什麼問題的話將之佈署上去

    rake deploy


一樣要記得將 Source Commit 回 Github

    git add .
    git commit -a -m "..."
    git push


Link
----
* [Remove Octopress' Default Blog/ Directory](http://blog.floriancargoet.com/2012/03/remove-octopress-default-blog-slash-directory/)
* [Octopress Customizations](http://www.ewal.net/2012/09/08/octopress-customizations/)
* [When Octopress lives in /blog, the extra blog subdirectory attached to categories and archives results in a redundant “/blog/blog/resource” path. Here’s how to fix that.](http://hackingoff.com/blog/jekyll-octopress-in-a-subdirectory-removing-redundant-slash-blog-path-to-archives-and-categories/)
* [Remove Redundant /blog Prefix From Octopress Website](http://xit0.org/2013/04/remove-redundant-slash-blog-prefix-from-octopress-website/)
