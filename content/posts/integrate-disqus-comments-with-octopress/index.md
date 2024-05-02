---
title: "Integrate disqus comments with Octopress"
date: "2013-11-08 23:15:00"
tags: [Octopress ]
---


Disqus是ㄧ提供留言功能的服務，整合了多種社群服務，能用社群帳號直接登入留言，除此之外也支援匿名留言、分享、以及完整的過濾與管理功能。

透過Disqus與Octopress的整合，使用Octopress架設的部落格也能提供留言的功能。 

<!--more-->
  
Sign up Disqus
----------------
進行整合前需先取至Disqus網站上註冊，以取得Disqus的帳戶。 

{% img /images/posts/Disqus/1.png %}

{% img /images/posts/Disqus/2.png %}

Config Octopress
------------------
將Disqus帳號設定至_config.yaml中，並將Disqus comment功能開啟。 

{% img /images/posts/Disqus/3.png %}

Generate and deploy
---------------------
進行建置與部署。  
 
    rake generate
    rake deploy

透過Octopress架設的部落格就可以支援留言功能了。 

{% img /images/posts/Disqus/4.png %}
