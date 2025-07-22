---
title: "ProGet - Push npm package via npm command line"
date: "2017-08-21 13:27:51"
tags: [ProGet]
---

要透過 npm 命令上傳 npm 套件到 ProGet 的 npm feed，可在 ProGet 的 npm feed 頁面按下 Add Package 按鈕。

![1.png](1.png)

點選 Push via npm (Command line)。

![2.png](2.png)

這邊會告知怎樣使用 npm publish 命令上傳 npm 套件，使用前需點選 configured npm，參閱該連結做些設定。

![3.png](3.png)

![4.png](4.png)

像是設定 npm 的 registry 位置。

npm set registry

設定 npm registry 使用者帳號，這邊直接使用 ProGet 帳號轉小寫後輸入、輸入密碼。

npm adduser

![5.png](5.png)

再使用 npm publish 將指定的 npm 套件發佈上 Registry。

npm publish

![6.png](6.png)

選取的套件即會上傳到 ProGet 的 npm feed。

![7.png](7.png)

![8.png](8.png)