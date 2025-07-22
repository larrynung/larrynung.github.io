---
title: "gauth - Host Google authenticator server"
date: "2021-03-08 07:56:59"
tags: [gauth]
---

要起 gauth 服務供二階段認證使用，可將 gauth 程式碼下載下來。

git clone https://github.com/gbraadnl/gauth.git

![1.png](1.png)

切換到 gauth 程式碼目錄。

cd gauth

![2.png](2.png)

安裝 gauth 所需的 npm 套件。

npm install

![3.png](3.png)

然後透過 node 將 gauth 服務起起來。

node server

![4.png](4.png)

服務起來後用瀏覽器連至 8080 port，即可開始使用 gauth 來做二階段認證。

http://localhost:8080/

![5.png](5.png)

Link
====
* [GitHub - gbraad/gauth](https://github.com/gbraad/gauth/)