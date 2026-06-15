---
title: "[.NET Resource]將Visual Studio編寫的.NET程式移轉至Mono平台上運行"
date: "2010-08-09 11:23:44"
description: "[.NET Resource]將Visual Studio編寫的.NET程式移轉至Mono平台上運行"
tags: [.NET Resource]
---

要將Visual Studio編寫的.NET程式移轉至Mono平台上運行，我們可先用Moma判斷程式是否可以移轉至Mono，這部分可參閱[.Net Resource]Mono Migration Analyzer (MoMA)。

確定可移轉後，可以直接在Mono Command Prompt下執行：

```xml
Mono [FileName].exe
```

這樣.NET程式就會以Mono運行，運行後程式Style會跟一般Windows程式有所不同。

而若是要以Mono將.NET程式做成免安裝的綠色軟體，只要把執行所需要的組件都複製一份到程式目錄中，並透過Mono啟動就可以了。

必要的組件主要有bin目錄下的mono.exe 、mono.dll 、libglib-2.0-0.dll 、與libgthread-2.0-0.dll 。lib\mono\x.xx目錄下的mscorlib.dll，與lib\mono\gac\Accessibility\xxxx\Accessibility.dll、\lib\mono\gac\Mono.Posix\xxxx\Mono.Posix.dll、還有\lib\mono\gac目錄下程式所參考到的組件。

當檔案放置完畢，我們可撰寫如下批次檔來方便使用Mono運行。

```xml
bin\mono.exe [FileName].exe
```

或是自行撰寫程式來使用Mono運行。

若在運行時發生問題，可帶入--Debug參數運行，運行時就會告知錯誤發生的原因，方便來排除錯誤。

```xml
bin\mono.exe --Debug [FileName].exe
```

這邊我寫了一隻小程式，能自動偵測程式中所使用到的組件，放置必要的檔案至程式目錄。只要指定Mono的程式路徑與程式執行檔完整路徑，按下Convert按鈕就可以了。由於是隨便寫寫的小程式，使用上會有可能少複製一些必要的檔案，若發現使用完後不能以Mono運行，自行把缺少的必要檔案補齊就可以了。

![image_thumb.png](/images/posts/17101/image_thumb.png)

## Download

[ConvertMonoPortableSW.zip](http://Files.Dotblogs.com.tw/larrynung/1008/20108923254865.zip)

## Link

* *[Main Page - Mono](http://www.mono-project.com/)*
* [透過Mono讓.Net Framework開發的軟體，搖身一變成為綠色軟體](http://blog.colorbase.tw/programming/525)
