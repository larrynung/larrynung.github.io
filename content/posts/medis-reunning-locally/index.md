---
title: "Medis - Reunning locally"
date: "2019-12-02 07:44:24"
description: "要在本地運行 Medis，先要將 Medis 下載下來。 git clone https://github.com/luin/medis 進入 Media 目錄。 cd medis 安裝需要的 npm 套件。 npm install 建置。"
tags: [Medis]
---

要在本地運行 Medis，先要將 Medis 下載下來。

git clone https://github.com/luin/medis

![1.png](1.png)

進入 Media 目錄。

cd medis

![2.png](2.png)

安裝需要的 npm 套件。

npm install

![3.png](3.png)

建置。

npm run build

![4.png](4.png)

因為運行需依賴 electron，若未安裝，這邊可進行全域安裝。

npm install -g electron

![5.png](5.png)

最後使用 npm 的 start 命令啟用程式即可。

npm start

![6.png](6.png)

![7.png](7.png)