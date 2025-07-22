---
title: "[C#][VB.NET]自定義.NET WindowForm表單介面(二)"
slug: "[CSharp][VB.NET]自定義.NET WindowForm表單介面(二)"
date: "2009-03-21 11:19:35"
description: "[C#][VB.NET]自定義.NET WindowForm表單介面(二)"
tags: [VB.NET,CSharp]
---

之前寫過一篇『自定義.NET WindowForm表單介面』，據網友反應才注意到其做出來的視窗無縮放的效果，因此這篇的重點將Focuse在自定義表單的縮放功能實作。
要實作具縮放功能的WindowForm表單目前得知的方法大概有三種，這邊就讓我們分別來探討。

### 方法一  用 FormBorderStyle = None 來做自定義表單並自行實作縮放
用 FormBorderStyle = None 來做自定義表單的方法請參考『自定義.NET WindowForm表單介面』這篇，實做完後加入如下縮放代碼即可。
VB.NET

C#

用這方法的缺點就是比較麻煩，有點土法鍊鋼的感覺。而且有個問題存在，就是當滑鼠移到工作列上(如下圖)按右鍵，右鍵選單不會出來。

### 方法二 用 ControlBox = False 來做自定義表單

用 ControlBox = False 來做自定義表單的方法很簡單，簡述如下：
Step1.Form.ControlBox設為False
 
Step2.清空Form.Text
如下圖所示，設完後會發現表單的標題列已經消失。

Step3.依照『自定義.NET WindowForm表單介面』這篇的要領完成自定義表單。

用這方法可以很簡單的做出自定義表單，且表單本來具有的縮放功能仍會存在，因此我們不需額外處理表單的縮放。但是這個方法仍有缺點存在，如下圖，使用該方法工作列上的標題會是空的，且按右鍵也是無選單彈出。

### 方法三 利用Form.Region來做自定義表單

利用Form.Region來做自定義表單的方法簡述如下：
Step1.加入程式碼用以去掉標題列
VB.NET

C#

Step2.依照『自定義.NET WindowForm表單介面』這篇的要領完成自定義表單。

Step3.依照方法一的方法補上表單上方的縮放功能

用這方法可以很簡單的做出自定義表單，基本上該有的功能也都有，只是需要額外補上表單上方的縮放功能而已。