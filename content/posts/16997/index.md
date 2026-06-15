---
title: "[.Net Resource]Mono Migration Analyzer (MoMA)"
date: "2010-08-03 11:44:53"
description: "[.Net Resource]Mono Migration Analyzer (MoMA)"
tags: [.NET Resource]
---

Mono Migration Analyzer (MoMA)工具主要功能為偵測.NET應用程式是否可以被移轉到Mono上面，可幫助我們找到應用程式中有用到的平台叫用或是Mono尚未支援的部分。

## 如何使用

### Step1.歡迎畫面，按下[Next]繼續。

![image_thumb.png](/images/posts/16997/image_thumb.png)

### Step2.加入要偵測的組件，選取要測試的Mono版本，按下[Next]繼續。

![image3_thumb.png](/images/posts/16997/image3_thumb.png)

### Step3.該頁面會顯示分析完的結果，若有錯誤可按下下方的*View Detail Report*超連結觀看錯誤報表，或按下[Next]繼續。

![image6_thumb.png](/images/posts/16997/image6_thumb.png)

![image9_thumb.png](/images/posts/16997/image9_thumb.png)

### Step4.該頁面能將看不懂的錯誤訊息反饋，可向Mono團隊尋求幫助，或按下[Next]繼續。

![image12_thumb.png](/images/posts/16997/image12_thumb.png)

### Step5.按下[Close]關閉。

![image15_thumb.png](/images/posts/16997/image15_thumb.png)

## 影響移轉的四大問題

MoMA會偵測到的主要有下列四種問題 :

1. Missing Methods
2. MonoTodo
3. NotImplementedException
4. P/Invokes

### Missing Methods

該問題是因為使用的方法在Mono中尚未實作。依照編譯器的不同可能會看到不同的錯誤訊息，像是用Mono編譯的話，在編譯時就會報錯，可看到下列的訊息：

myfile.cs(22,16): error CS0117: 'xxxxxxxxxxxxxxxxx' does not contain a definition for 'xxxxxxxxxxxxxxx'

而如果用微軟編譯器編輯的話，則必須執行到該方法處才會跳出MissingMethodException的例外：

System.MissingMethodException: Method not found: xxxxxxxxxxxxxxxxxxx

### MonoTodo

該問題是因為應用程式中存在標記有MonoTodo的方法。這標記是用來提醒開發人員尚須處理的地方，通常這代表著方法尚未實做完全，或是實做完後開發者忘了將該標記移除。

### NotImplementedException

該問題是因為應用程式中存在會丟出NotImplementedException的方法。

### P/Invokes

該問題是因為應用程式中存在著平台叫用。平台叫用通常是用來呼叫非託管的方法，尤其是平台本身提供的方法。

## 命令列執行

MoMa從1.9版開始就已支援命令列執行的功能。

若要用命令列設定要偵測的組件並開啟MoMa，可以像下面這樣：

```xml
MoMA C:\app\myapp.exe
```

若要用設定加入多個要偵測的組件並開啟MoMa，可以像下面這樣：

```xml
MoMA C:\app\myapp.exe C:\app\myapp.dll C:\app\myapp2.dll
```

若不想帶出MoMa介面，可透過--nogui設定並指派組件的位置，像是：

```xml
MoMA --nogui C:\app\myapp.exe
```

執行完後，在命令提示字元看不到任何訊息，須自行開啟報表查看，其報表會存放在MoMa目錄下的Reports目錄內。若要自行指定報表位置，可透過--out來設定，並指派輸出的報表檔位置，像是：

```xml
MoMA --nogui --out C:\app\momareport\report.html C:\app\myapp.exe
```

```

```

## Link

* MoMA
* Guide: Using MoMA
* Guide: Fixing issues MoMA finds
* Guide: Run MoMA from command line (automated builds, etc.)
* 介紹好用工具：Mono Migration Analyzer (MoMA)
