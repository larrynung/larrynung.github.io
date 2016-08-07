---
title: >-
  The Diagnostic Tools window does not support the current debugging
  configuration
date: 2016-08-07 22:40:03
tags:
---

Diagnostic Tools 視窗若出現 `The Diagnostic Tools window does not support the current debugging configuration` 這樣的訊息。  

<!-- More -->

{% asset_img 1.png %}

<br/>


可開啟 Options 視窗，切到 [Debugging | General]，取消勾選 `Use Managed Compatiability Mode` 選項。  

{% asset_img 2.png %}

<br/>


Diagnostic Tools 就可正常運作了。  

{% asset_img 3.png %}

<br/>


Link
----
* [c# - Visual Studio 2015 diagnostics tool does not support current debugging configuration - Stack Overflow](http://stackoverflow.com/questions/32167640/visual-studio-2015-diagnostics-tool-does-not-support-current-debugging-configura)
