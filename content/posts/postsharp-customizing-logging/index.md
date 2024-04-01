---
title: "PostSharp - Customizing Logging"
date: "2015-02-03 08:36:00"
description: "PostSharp - Customizing Logging"
tags: [PostSharp]
---


如果預設的 Log 設定不敷使用，像是 Log 的層級應該是 Error 而不是 Warning，或是 Log 應該含更多的資訊，這邊PostSharp 也支援我們有限幅度的客製。我們可以在類別上直接按下右鍵，在彈出的滑鼠右鍵快顯選單中，選取 Add logging... 選單選項。  

<!-- More -->

{% img /images/posts/PostSharpCustomLogging/1.png %}

<br/>


在 Log 設定這邊注意到下方有個 `New logging profile...` 連結按鈕，按下該連結按鈕即可建立一個新的設定。  

{% img /images/posts/PostSharpCustomLogging/2.png %}

<br/>


按下後會彈出 Log 設定的設定對話框，依需求決定這個設定的名稱、何時進行 Log 的紀錄、Log 紀錄時所要包含的資訊、以及 Log 的層級。  

{% img /images/posts/PostSharpCustomLogging/3.png %}

<br/>


選取剛所建立的設定，按下 Next 按鈕繼續。  

{% img /images/posts/PostSharpCustomLogging/4.png %}

<br/>


再來是要決定 Log 機制背後要用哪種服務，有 Trace、Console、Log4Net、NLog、Enterprise Library，一樣選取完後按下 Next 按鈕繼續。  

{% img /images/posts/PostSharpCustomLogging/5.png %}

<br/>


Summary 頁面這邊只是告訴我們繼續下去會做什麼事，不外乎就是加入套件引用、加上 Attribute、 設定 Config，一樣按下 Next 繼續。  

{% img /images/posts/PostSharpCustomLogging/6.png %}

<br/>


如 Summary 頁面所提，要處理的東西有點多，進度要稍微跑一下。  

{% img /images/posts/PostSharpCustomLogging/7.png %}

<br/>


跑完後按下 Finish 按鈕結束精靈頁面。  

{% img /images/posts/PostSharpCustomLogging/8.png %}

<br/>


可以看到專案已套上對應的修改，已引用該引用的套件、產生副檔名為 psproj 與 pssln 的設定檔、Attribute 也正確的加上 (這邊的 Attribute 會明確的指定要使用的 Profile)。  

{% img /images/posts/PostSharpCustomLogging/9.png %}

<br/>


開啟副檔名為 pssln 的設定檔，可看到剛所設定的 Profile 資訊會放置在裡面。  

```xml 
<? xml version="1.0 " encoding=" utf-8"?>
< Project xmlns="http://schemas.postsharp.org/1.0/configuration " xmlns:d="clr-namespace:PostSharp.Patterns.Diagnostics;assembly:PostSharp.Patterns.Diagnostics " xmlns:p=" http://schemas.postsharp.org/1.0/configuration ">
  < Property Name="LoggingEnabled " Value="{has-plugin('PostSharp.Patterns.Diagnostics')} " Deferred=" true" />
  < d:LoggingProfiles p:Condition="{$LoggingEnabled} ">
    < d:LoggingProfile Name="New profile " OnEntryOptions=" IncludeParameterType | IncludeParameterName | IncludeParameterValue | IncludeThisArgument" OnSuccessOptions="IncludeParameterType | IncludeParameterName | IncludeParameterValue | IncludeReturnValue | IncludeThisArgument" OnExceptionOptions="IncludeParameterType | IncludeParameterName | IncludeParameterValue | IncludeThisArgument" />
  </ d:LoggingProfiles>
</ Project>
```

<br/>


運行後 Log 會送入對應的服務。  

{% img /images/posts/PostSharpCustomLogging/10.png %}

<br/>


Link
-----
* [Walkthrough: Customizing Logging](http://doc.postsharp.net/logging-profiles)
