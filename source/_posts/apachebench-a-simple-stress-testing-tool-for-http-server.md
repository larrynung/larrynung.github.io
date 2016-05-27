---
layout: post
title: "ApacheBench - A simple stress testing tool for http server"
date: 2015-03-02 08:36:00
comments: true
categories: 
keywords: [ApacheBench]
description: "ApacheBench - A simple stress testing tool for http server"
---

ApacheBench 簡稱 ab，是 Apache 自帶的 HTTP 負載測試命令列工具，程式主檔在 Apache 安裝目錄下的 bin 目錄內，可安裝 Apache 後取出使用，或是下載 [Standalone 版本](https://code.google.com/p/apachebench-standalone/) 使用也可。  

<!-- More -->

{% img /images/posts/ApacheBench/1.png %}

<br/>


使用方式及參數如下：  

    Usage: /usr/sbin/ab [options] [http[s]://]hostname[:port]/path
    Options are:
        -n requests     Number of requests to perform
        -c concurrency  Number of multiple requests to make
        -t timelimit    Seconds to max. wait for responses
        -p postfile     File containg data to POST
        -T content-type Content-type header for POSTing
        -v verbosity    How much troubleshooting info to print
        -w              Print out results in HTML tables
        -i              Use HEAD instead of GET
        -x attributes 
      String to insert as table attributes
        -y attributes   String to insert as tr attributes
        -z attributes   String to insert as td or th attributes
        -C attribute    Add cookie, eg. 'Apache=1234' (repeatable)
        -H attribute    Add Arbitrary header line, eg. 'Accept-Encoding: zop'
                        Inserted after all normal header lines. (repeatable)
        -A attribute    Add Basic WWW Authentication, the attributes
                        are a colon separated username and password.
        -P attribute    Add Basic Proxy Authentication, the attributes
                        are a colon separated username and password.
        -X proxy:port   Proxyserver and port number to use
        -V              Print version number and exit
        -k              Use HTTP KeepAlive feature
        -d              Do not show percentiles served table.
        -S              Do not show confidence estimators and warnings.
        -g filename     Output collected data to gnuplot format file.
        -e filename     Output CSV file with percentages served
        -s              Use httpS instead of HTTP (SSL)
        -h              Display usage information (this message)


有需要隨時可在命令列叫用下列命令查閱：   

    ab
    ab -h
    

{% img /images/posts/ApacheBench/2.png %}

<br/>


比較常用的參數有 -n、-c、-k，-n 用來指定所要發送的 Request 數、-c 用來指定同時發送的 Request 數、-k 用來指定是否 Keep-Alive。  

<br/>


如果要簡單的發送一定數量的 Request 給網站，我們只要帶入 -n 參數並指定 Request 的數量，並帶上要發送的網站即可。  

    ab -n 10 http://www.google.com


發送完 ApacheBench 會有詳細的報告。  

{% img /images/posts/ApacheBench/3.png %}

<br/>


若要輸出報告留底，可用參數 -e 並帶上輸出的檔案位置，ApacheBench 會將之輸出成 CSV 檔。  

<br/>


如果除了發送一定數量的 Request 外還要設定 Concurrent 的量，可加帶 -c 參數與 Concurrent 的數量。  

    ab -n 10 -c 5 http://www.google.com

<Br/>


Link
----
* [The Will Will Web | 使用ApacheBench 進行網站的壓力測試]( http://blog.miniasp.com/post/2008/06/Using-ApacheBench-ab-to-to-Web-stress-test.aspx )
* [apachebench-standalone - Apachebench from httpd-2.2.11, modified to be more indepentive - Google Project Hosting](https://code.google.com/p/apachebench-standalone/)
