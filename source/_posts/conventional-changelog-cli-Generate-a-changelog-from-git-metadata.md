---
title: conventional-changelog-cli - Generate a changelog from git metadata
date: 2020-06-16 23:27:00
tags: [git]
---

conventional-changelog-cli 是一命令列工具，能解析 Git 符合 Angular style 的 Commit log，產生對應的 Change log。

<!-- More -->

<br>


使用前先透過 Npm 安裝套件至全域。  

    npm install -g conventional-changelog-cli

{% asset_img 1.png %}

</br>


即可開始使用。  

</br>


像是顯示 Change log 會產出的內容可帶參數 -w。

    conventional-changelog -p angular -i CHANGELOG.md -w -r 0


要產生 Change log 可帶參數 -s。

    conventional-changelog -p angular -i CHANGELOG.md -s

</br>


這邊筆者用簡單的例子稍微示範一下。  

</br>


首先先初始 Npm 專案設定檔，因為後面產生的 Change log 版號會要看這設定檔。  

    npm init

{% asset_img 2.png %}

</br>


接著初始專案的 Git 版控。  

    git init

{% asset_img 3.png %}

</br>


將第一版檔案加入版控。

    git add .

{% asset_img 4.png %}

</br>


    git commit

{% asset_img 5.png %}

</br>


{% asset_img 6.png %}

</br>


{% asset_img 7.png %}

</br>


確認上版。  

    git log

{% asset_img 8.png %}

</br>


{% asset_img 9.png %}

</br>


嘗試切換專案版本至 1.0.0。  

    npm version 1.0.0 --allow-same-version

{% asset_img 10.png %}

</br>


透過 conventional-changelog 命令列工具帶入參數 -w 查閱產出的 Change log 會是怎樣。  

    conventional-changelog -p angular -i CHANGELOG.md -w -r 0

{% asset_img 11.png %}

</br>


預期產出的 Change log 應該會含有 feat 與 fix 類型的修改紀錄。  

</br>


如果確認無誤，改用參數 -s 實際寫入 Change log 檔案。  

    conventional-changelog -p angular -i CHANGELOG.md -s -r 0

{% asset_img 12.png %}

</br>


    ls

{% asset_img 13.png %}

</br>


    code CHANGELOG.md

{% asset_img 14.png %}

</br>


{% asset_img 15.png %}

</br>


把 Change log 加入 Git 版控。

    git add .

{% asset_img 16.png %}

</br>


    git commit

{% asset_img 17.png %}

</br>


{% asset_img 18.png %}

</br>


{% asset_img 19.png %}

</br>


    git log

{% asset_img 20.png %}

</br>


{% asset_img 21.png %}

</br>


加入專案程式。  

    dotnet new console -o helloworld

{% asset_img 22.png %}

</br>


把專案程式加入版控。  

    git add .

{% asset_img 23.png %}

</br>


    git commit

{% asset_img 24.png %}

</br>


{% asset_img 25.png %}

</br>


{% asset_img 26.png %}

</br>


專案版本切至 1.0.1。  

    npm version 1.0.1

{% asset_img 27.png %}

</br>


透過 conventional-changelog 命令列工具產生 Change log。  

    conventional-changelog -p angular -i CHANGELOG.md -s -r 0

{% asset_img 28.png %}

</br>


查驗產出的 Change log。

    code CHANGELOG.md

{% asset_img 29.png %}

</br>


可看到 Change log 會含有新的修改紀錄。  

{% asset_img 30.png %}
