---
title: GitLab - Manage wiki with git repository
date: 2019-06-25 06:49:23
tags: [GitLab]
---

GitLab wiki 其實背後是放在一個 Git repository 內，所以除了支援線上編輯外，也支援離線編輯。  

<!-- More -->

</br>


要離線編輯我們先要找到 GitLab wiki repository 位置。  

{% asset_img 1.png %}

</br>


{% asset_img 2.png %}

</br>


用 Git 將 GitLab wiki repository clone 下來。  

{% asset_img 3.png %}

</br>


Clone 下來後離線編譯 Wiki，透過喜好的 Markdown 文件撰寫工具撰寫。這邊注意因為 Wiki 支援線上撰寫，所以建議 Follow 線上撰寫的文件配置方式，可實際線上撰寫後用 Git Pull 下來參考。  

</br>


這邊筆者簡單放置個 Markdown 文件與其用到的圖檔做個測試。  

{% asset_img 4.png %}

</br>


將檔案加入、Commit、推到遠端。  

{% asset_img 5.png %}

</br>


回到 GitLab wiki 就可以看到剛離線編輯的內容了。  

{% asset_img 6.png %}
