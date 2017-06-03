---
title: Logstash - Getting started
date: 2017-06-03 00:05:46
tags: [Logstash]
---

Logstash 安裝好後，可以用 Logstash 的 -e 參數帶入 Logstash 設定快速的體驗一下。  

<!-- More -->

    logstash -e <Setting>

<br/>


像是下面這樣帶入簡單的設定，將標準輸入串流輸入的資料導到標準輸出串流。  

    logstash -e 'input { stdin{} } output { stdout{} }'

{% asset_img 1.png %}

<br/>


將資料輸入。  

{% asset_img 2.png %}

<br/>


資料就會被輸出到標準輸出串流。  

{% asset_img 3.png %}

<br/>


不再使用時按下熱鍵 Ctrl + D 即可退出。  

{% asset_img 4.png %}

<br/>
