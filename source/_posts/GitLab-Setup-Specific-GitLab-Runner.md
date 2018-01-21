---
title: GitLab - Setup Specific GitLab Runner
date: 2018-01-21 11:00:18
tags: [GitLab]
---

要設定 Specific GitLab Runner，需先至 GitLab 的 CI/CD 設定頁面。  

<!-- More -->

{% asset_img 1.png %}
 
<br/>


找到 Runner settings。  

{% asset_img 2.png %}
 
<br/>


這邊會顯示 GitLab Runner 註冊時需要的 URL 與 Token。  

{% asset_img 3.png %}
 
<br/>


接著回到命令列調用 GitLab Runner 的 register，設定剛剛拿到的 URL 位置、Token、Runner 描述...等資訊。  

{% asset_img 4.png %}
 
<br/>


Specific GitLab Runner 就設定完成了。  

{% asset_img 5.png %}
 
<br/>
