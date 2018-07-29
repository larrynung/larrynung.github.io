---
title: Mochawesome - A Gorgeous HTML/CSS Reporter for Mocha.js
date: 2018-07-29 22:59:47
tags: [Node.js]
---

Mochawesome 能讓 Mocha 支援產出 HTML 的測試報告。  

<!-- More -->

<br/>


使用前需安裝 Mochawesome 套件。  

    npm install --save-dev mochawesome

<br/>


調用 Mocha 並使用 -reporter 參數指定使用 Mochawesome 產出測試報告。  

    mocha --reporter mochawesome

{% asset_img 1.png %}
 
<br/>


產出的測試報告會存放在 mochawesome-report 下的 mochawesome.html。  

{% asset_img 2.png %}
 
<br/>


Link
----
* [Mochawesome](http://adamgruber.github.io/mochawesome/)
