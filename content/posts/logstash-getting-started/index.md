---
title: "Logstash - Getting started"
date: "2017-06-03 00:05:46"
tags: [Logstash]
---


Logstash 安裝好後，可以用 Logstash 的 -e 參數帶入 Logstash 設定快速的體驗一下。  

<!-- More -->

    logstash -e <Setting>

<br/>


像是下面這樣帶入簡單的設定，將標準輸入串流輸入的資料導到標準輸出串流。  

    logstash -e 'input { stdin{} } output { stdout{} }'

![1.png](1.png)

<br/>


將資料輸入。  

![2.png](2.png)

<br/>


資料就會被輸出到標準輸出串流。  

![3.png](3.png)

<br/>


不再使用時按下熱鍵 Ctrl + D 即可退出。  

![4.png](4.png)

<br/>


除了 Input & Output 外，也可以試著設定 Filter，像是要用 Filter 去將訊息內的 IP 切成 client field，可以像下面這樣調用。  

    logstash -e 'input { stdin{} } filter { grok { match => { "message" => "%{IP:client}" } } } output { stdout { codec => rubydebug } }'
 
![5.png](5.png)

<br/>
