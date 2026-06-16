---
title: "conventional-changelog-cli - Generate a changelog from git metadata"
date: "2020-06-16 23:27:00"
description: "conventional-changelog-cli 是一命令列工具，能解析 Git 符合 Angular style 的 Commit log，產生對應的 Change log。 使用前先透過 Npm 安裝套件至全域。"
tags: [git]
---

conventional-changelog-cli 是一命令列工具，能解析 Git 符合 Angular style 的 Commit log，產生對應的 Change log。

使用前先透過 Npm 安裝套件至全域。  

    npm install -g conventional-changelog-cli

![1.png](1.png)

即可開始使用。  

像是顯示 Change log 會產出的內容可帶參數 -w。

    conventional-changelog -p angular -i CHANGELOG.md -w -r 0

要產生 Change log 可帶參數 -s。

    conventional-changelog -p angular -i CHANGELOG.md -s

這邊筆者用簡單的例子稍微示範一下。  

首先先初始 Npm 專案設定檔，因為後面產生的 Change log 版號會要看這設定檔。  

    npm init

![2.png](2.png)

接著初始專案的 Git 版控。  

    git init

![3.png](3.png)

將第一版檔案加入版控。

    git add .

![4.png](4.png)

    git commit

![5.png](5.png)

![6.png](6.png)

![7.png](7.png)

確認上版。  

    git log

![8.png](8.png)

![9.png](9.png)

嘗試切換專案版本至 1.0.0。  

    npm version 1.0.0 --allow-same-version

![10.png](10.png)

透過 conventional-changelog 命令列工具帶入參數 -w 查閱產出的 Change log 會是怎樣。  

    conventional-changelog -p angular -i CHANGELOG.md -w -r 0

![11.png](11.png)

預期產出的 Change log 應該會含有 feat 與 fix 類型的修改紀錄。  

如果確認無誤，改用參數 -s 實際寫入 Change log 檔案。  

    conventional-changelog -p angular -i CHANGELOG.md -s -r 0

![12.png](12.png)

    ls

![13.png](13.png)

    code CHANGELOG.md

![14.png](14.png)

![15.png](15.png)

把 Change log 加入 Git 版控。

    git add .

![16.png](16.png)

    git commit

![17.png](17.png)

![18.png](18.png)

![19.png](19.png)

    git log

![20.png](20.png)

![21.png](21.png)

加入專案程式。  

    dotnet new console -o helloworld

![22.png](22.png)

把專案程式加入版控。  

    git add .

![23.png](23.png)

    git commit

![24.png](24.png)

![25.png](25.png)

![26.png](26.png)

專案版本切至 1.0.1。  

    npm version 1.0.1

![27.png](27.png)

透過 conventional-changelog 命令列工具產生 Change log。  

    conventional-changelog -p angular -i CHANGELOG.md -s -r 0

![28.png](28.png)

查驗產出的 Change log。

    code CHANGELOG.md

![29.png](29.png)

可看到 Change log 會含有新的修改紀錄。  

![30.png](30.png)