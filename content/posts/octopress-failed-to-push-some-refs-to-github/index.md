---
title: "Octopress - Failed to push some refs to GitHub"
date: "2016-05-11 22:05:00"
description: "Octopress - Failed to push some refs to GitHub"
tags: [Octopress]
---


今天在使用 rake deploy 試圖發佈文章時，在發佈到 Github 這步驟時發生了錯誤，發佈的動作被 rejected 了。  

<!-- More -->

{% img /images/posts/OctopressDeployFail/1.png %}

<br/>


要解決這樣的問題我們可以依下面步驟操作。  

```bash
cd _deploy
git reset --hard origin/master
cd ..
```

<br/>


就像下面這樣：  

{% img /images/posts/OctopressDeployFail/2.png %}

<br/>


操作完就重新建立靜態檔案並 Deploy。   
 
```bash
rake generate
rake deploy
```

<br/>


沒意外的話就能正確的發佈。  

{% img /images/posts/OctopressDeployFail/3.png %}

<br/>

Link
----
* [ruby - Octopress pushing error to GitHub - Stack Overflow](http://stackoverflow.com/questions/19619280/octopress-pushing-error-to-github)
