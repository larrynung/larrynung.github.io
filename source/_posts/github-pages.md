---
layout: post
title: "GitHub Pages"
date: 2013-11-10 13:13:00
comments: true
tags: 
---

GitHub Pages服務可讓使用者免費Hosting網頁在GitHub上，享用GitHub不受限的儲存空間與網路流量。依用途不同可分為User/Organization Pages與Project Pages兩種。

<!--more-->

User & Organization Pages
----------------------------
User & Organization Pages，顧名思義是用於部署個人或是組織的網頁。 

它對應到Github上特殊的Repository。使用上只要建立一個遵循下面命名規則的Repository。

    username/username.github.io


像是以筆者來說，Repository就是larrynung/larrynung.github.io。 


該特定的Repository建立完後，網頁的部署就只要將網頁Commit至master分支就可以了。 


網頁部署完成後，可以輸入網址username.github.io下去查看。


這邊要提一下，上面提到的Repository是新的格式，之前舊有的格式為

    username/username.github.com


這邊仍舊是支援的。 


瀏覽網頁時，GitHub也會自動在username.github.com與username.github.io之間做轉換。 


不過若兩個Repository同時存在，仍舊是以username.github.io為主。
   

Project Pages
--------------
Project Pages則是跟程式專案相關網頁。   


因為跟專案相關，所以每個程式專案都可以建立。 


只要將網頁Commit至gh-pages分支就可以了。 


Automatic Page Generator
------------------------
除了手動建置與部屬網頁外，這邊也可以透過GitHub內建的Automatic Page Generator功能幫我們快速的產生對應的網頁。  

只要開啟專案的Settings

{% img /images/posts/GitHubPages/1.png %}


點選Automatic Page Generator按鈕

{% img /images/posts/GitHubPages/2.png %}


編輯頁面想要呈現的內容

{% img /images/posts/GitHubPages/3.png %}


按下Continue to Layouts按鈕繼續

{% img /images/posts/GitHubPages/4.png %}


這邊GitHub Pages會提供一些預設的樣板供套用，上方可供樣版的選取與切換，下方則是將選取的樣板作即時的御覽

{% img /images/posts/GitHubPages/5.png %}


選取好樣板後按下PUBLISH按鈕確定

{% img /images/posts/GitHubPages/6.png %}


網頁會被帶回到對應的GitHub Repository，上方會提示頁面的建置動作已經完成，以及提示對應的網址，不過網址要生效大概要10分鐘的處理時間

{% img /images/posts/GitHubPages/7.png %}


網址生效後就可以看到我們剛剛透過Automatic Page Generator所產生的頁面

{% img /images/posts/GitHubPages/8.png %}
