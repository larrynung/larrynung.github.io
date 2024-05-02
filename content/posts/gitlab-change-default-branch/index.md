---
title: "GitLab - Change default branch"
date: "2018-02-27 00:02:29"
tags: [GitLab]
---


GitLab 在建立 Merge Request 時，Target branch 會幫我們自動帶入預設的 branch，也就是 master branch。  

<!-- More -->

![1.png](1.png)
 
<br/>



![2.png](2.png)
 
<br/>


在某些情境這樣的設定並不恰當，也可能會增加操作錯誤的風險。  

<br/>


這時我們可以開啟專案的 General project settings。  

![3.png](3.png)
 
<br/>


將 Default Branch 從預設的 master。  

![4.png](4.png)
 
<br/>


切換至其它更為適當的 Branch。  

![5.png](5.png)
 
<br/>


這樣設定完後新開的 Merge Request 所帶出的 Target branch 就會是我們指定的 Branch。  

![6.png](6.png)
 
<br/>
