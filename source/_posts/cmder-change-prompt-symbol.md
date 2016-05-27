---
layout: post
title: "Cmder - Change Prompt symbol"
date: 2015-10-17 00:56:00
comments: true
categories: [Cmder]
keywords: "Cmder"
description: "Cmder - Change Prompt symbol"
---

Cmder 裝完後啟動，預設是使用 `λ`，若要改成自己習慣的符號，我們可以修改 `config\cmder.lua` 檔。  

<!-- More -->

{% img /images/posts/ChangeCmderPrompt/1.png %}

<br/>


找到第二行的 `λ` 符號。  

{% img /images/posts/ChangeCmderPrompt/2.png %}

<br/>


將之改成我們習慣的符號存檔，這邊筆者還是看 `>` 比較順眼，所以將之改成了 `>`。  

{% img /images/posts/ChangeCmderPrompt/3.png %}

<br/>


啟動 Cmder 後會發現 Prompt 符號已經變成我所設定的 `>`。  

{% img /images/posts/ChangeCmderPrompt/4.png %}

<br/>


當然從 `vendor\init.bat` 這邊下手，將裡面的 `@prompt $E[1;32;40m$P$S{git}{hg}$S$_$E[1;30;40m{lamb}$S$E[0m` 中的 `{lamb}` 變數改成期望的符號，也可以達到類似的效果，但這樣等於捨棄本來就提供好的抽換機制，個人並不傾向這樣的修改方式。  
