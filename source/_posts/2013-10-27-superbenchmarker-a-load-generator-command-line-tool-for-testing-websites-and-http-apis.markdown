---
layout: post
title: "SuperBenchmarker - A load generator command-line tool for testing websites and HTTP APIs"
date: 2013-10-27 20:25
comments: true
categories: 
---

SuperBenchmarker 是ㄧ開放源碼的壓力測試命令列工具。用.NET Framework 4.5開發而成。

<!--more-->

可支援Get、Post、Put、Delete這些呼叫方式，叫用時能設定Concurrent user、Request數、Header template...等。


程式主檔可由Github、Nuget以及Chocolatey這三種方式取得。

Nuget使用者可在Visual Studio的Package Manager Console視窗中輸入下列命令進行下載
    Install-Package SuperBenchmarker

{% img /images/posts/SuperBenchmarker/1.jpeg %}

Github使用者可在download目錄內取得編譯好的程式主檔  
{% img /images/posts/SuperBenchmarker/2.jpeg %}  
{% img /images/posts/SuperBenchmarker/3.jpeg %}  

Chocolatey使用者可輸入下列命令進行下載
    cinst SuperBenchmarker

不過該程式作者在開發時有用一些第三方的套件，而Nuget上所放置的版本並沒有把那些參考到的組件連帶釋出，所以要手動將參考到的組件ㄧㄧ補齊，不然無法正常運行。 
{% img /images/posts/SuperBenchmarker/4.jpg %}

而且該程式其實是一個獨立的主控台程式，跟專案與方案應該無任何關聯，為此要開個方案進行下載是有點弔詭。且依筆者的觀察，Nuget上的更新也比較緩慢。

程式的作者是建議用Chocolatey去取得程式主檔，因為放置的程式主檔已經被作者用ILMerge將參考到的組件合併，故取得後既可直接使用。 

至於Github上放置的版本本來也跟Nuget取得的版本一樣需要自行下載相依的組件，但後來的版本看起來跟Chocolatey一樣也做了合併處理，所以要由此取得應該也是可以的。

程式的使用方式可直接在命令列下輸入sb查看，裡面會有程式的使用方式、參數、及簡易的使用範例   
{% img /images/posts/SuperBenchmarker/5.jpeg %}

其中比較重要的參數大概有下列幾個   
    -u 可用來指定要打的網站或是API位置   
    -n 可用來指定要打的Request數量   
    -c 可用來指定Concurrent Request數量   
    -m 可用來指定要使用的HTTP Method    
    -h 可用來指定要顯示HTTP Header    
    -q 可用來指定要顯示Cookie    

所以我們要發送1000個Request去測試google的話 可以輸入命令
    sb -u http://google.com -n 1000

要發送1000個Request, 且同時間可能有10個Concurrent Request去測試google的話 可以輸入命令
    sb -u http://google.com -n 1000 -c 10

要在發送命令後顯示Header的話, 可帶入參數-h    
    sb -u http://google.com -n 1000 -c 10 -h

要在發送命令後顯示Cookie, 可帶入參數-q    
    sb -u http://google.com -n 1000 -c 10 -h -q

要在發送命令的同時指定Http Header與Payload的話, 可以先將Http Header與Payload設定在文字檔中    

{% img /images/posts/SuperBenchmarker/6.png %}

<br/>

然後帶入參數-t與檔名去發送Request  

{% img /images/posts/SuperBenchmarker/7.png %}

<br/>

命令運行的最後我們都會看到類似下面這樣的畫面:   

{% img /images/posts/SuperBenchmarker/8.jpg %}

<br/>

這邊有簡易的測試統計，可以看出每秒可處理多少的Request、最大的處理時間、最小的處理時間、平均的處理時間、以及打了這麼多次的API，依比例分大概在哪個Range。


這些數值有助我們評估網站或是API的效能與負載量。

除了看這些數值外，這邊建議也可以在打的時候看一下Server上的CPU Loading，磁碟IO，以及記憶體的使用狀況，甚至可以用效能監視器拉些數值來看。

 
Link
----
- [免費網站與REST服務壓力測試工具]( http://blog.kkbruce.net/2013/09/free-website-rest-service-stress-test-tool.html?m=1 ) 
- [aliostad/SuperBenchmarker · GitHub]( https://github.com/aliostad/SuperBenchmarker )
