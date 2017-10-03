---
title: >-
  Fix Mac Remote Desktop Connection Client “The certificate or associated chain
  is not valid.”
date: 2017-10-03 23:46:03
tags:
---

MAC 電腦升級到 MacOS Sierra 後，使用 Remote Desktop Connection 進行遠端連線時，會出現 The certificate or associated chain is not valid. 這個視窗，怎麼按 Connect 按鈕都會一直出現。  

<!-- More -->

{% asset_img 1.png %}

<br/>


這時可以點選 [RDC | Perferences...] 主選單選項，或是按下熱鍵 Command + ,，開啟 Perferences 對話框。  

{% asset_img 2.png %}

<br/>


切至 Security 頁面。  

{% asset_img 3.png %}

<br/>


將設定調成 Always connect, even if authentication fails 即可。  

{% asset_img 4.png %}

<br/>


Link
----
* [Fix Mac Remote Desktop Connection Client "The certificate or associated chain is not valid." | Next of Windows](https://www.nextofwindows.com/fix-mac-remote-desktop-the-certificate-or-associated-chain-is-not-valid)
