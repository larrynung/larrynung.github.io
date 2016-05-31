---
layout: post
title: "RazorCandle - Render a razor template and save it to a file from command line"
date: 2015-11-17 05:45:00
comments: true
tags: 
keywords: "RazorCandle"
description: "RazorCandle - Render a razor template and save it to a file from command line"
---

RazorCandle 是一命令列程式，能讓我們透過命令列進行 Razor 的轉換。  

<!-- More -->

<br/>


該程式未有 Release 的版本，所以需要自己下載原始碼下來編譯。  

<br/>


命令列使用的方式如下：  

    RazorCandle.exe source  [destination] [/M]  [/V]
    
    source         Specifies the source razor file.
    [destination]  Specify the output file. By default is the same name as the
                   source with the html extension.
    [/?]           Show Help
    [/M]           Json model as string to the model.
    [/V]           Verbose mode. Show result in the output.


簡單說就只要在命令列後面帶入來源檔案、輸出的檔案 (若不帶則預設為同名的 html 檔)，如果轉換需要參數可以使用 /M 後面接 Json 帶入。

<br/>


舉個例子來說，假設今天我們有個 cshtml，裡面的 Model 有 FirstName 與 LastName。  

{% img /images/posts/RazorCandle/1.png %}

<br/>


我們可以像下面這樣進行轉換。 

    RazorCandle hello.cshtml /M="{FirstName: 'Larry', LastName: 'Nung'}"

{% img /images/posts/RazorCandle/2.png %}

<br/>


轉換出來的檔案會像下面這樣，可以正確的取得 Model 值並轉換。  

{% img /images/posts/RazorCandle/3.png %}

<br/>


它也支援 Partial view 的 Support，像是上面這個例子，使用 Partial View 來做。  

{% img /images/posts/RazorCandle/4.png %}

<br/>


{% img /images/posts/RazorCandle/5.png %}

<br/>


一樣運行良好。  

{% img /images/posts/RazorCandle/6.png %}

<br/>

Link
----
* [jfromaniello/RazorCandle](https://github.com/jfromaniello/RazorCandle)
