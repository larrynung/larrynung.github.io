---
title: "Yarn - Yarn add"
date: "2017-06-27 23:40:27"
tags: [Yarn]
---

yarn add 命令可以用來載入要使用的套件。

調用 yarn add，帶入套件名稱，即可將指定的套件載入。

yarn add

![1.png](1.png)

若要指定版本，可在套件名稱後面加上套件的版本號。

yarn add @

![2.png](2.png)

套件載入的同時會寫入 package.json 的 dependencies。

![3.png](3.png)

如果要將套件載入的同時寫入 package.json 的 devDependencies，可帶入參數 --dev 或是 -D。

yarn add  --dev
yarn add  -D

![4.png](4.png)

![5.png](5.png)

要在套件載入的同時寫入 package.json 的 peerDependencies，可帶入參數 --peer 或 -P。

yarn add  --peer
yarn add  -P

![6.png](6.png)

![7.png](7.png)

要在套件載入的同時寫入 package.json 的 optionalDependencies，可帶入參數 --optional 或 -O。

yarn add  --optional
yarn add  -O

![8.png](8.png)

![9.png](9.png)

Link
----
* [yarn add | Yarn](https://yarnpkg.com/en/docs/cli/add)