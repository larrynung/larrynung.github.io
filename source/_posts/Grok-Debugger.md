---
title: Grok Debugger
date: 2017-06-21 13:17:08
tags: [Grok]
---

要測試 Grok pattern，可以借助一些線上工具，像是 [Grok Debugger](http://grokdebug.herokuapp.com/)。  

<!-- More -->

<br/>


使用上只要在 Input 部份帶入要被 Grok 處理的資料，Pattern 部份帶入要用來處理資料的 Grok pattern 即可。 

{% asset_img 1.png %}

<br/>


像是要處理 IP 資料，就可以在 Input 部份帶入要處理的 IP，在 Pattern 部份帶入 %{IP:<SEMANTIC>} 這樣的 Grok pattern，下方即會顯現經由 Grok pattern 處理完的結果。  

{% asset_img 2.png %}

<br/>


處理完的結果如果資訊太多不易閱讀，可勾選 Named Captures Only 選項。  

{% asset_img 3.png %}

<br/>


若要增加自定義的 Grok pattern，這邊也可勾選 Add custom patterns 選項進行設定。  

{% asset_img 4.png %}

<br/>


除了 Grok pattern 的測試外，Grok Debugger 也提供一些定義好的 Grok pattern 可供參考，點選上方的連接切換至 Patterns 頁面即可。  

{% asset_img 5.png %}

<br/>


{% asset_img 6.png %}

<br/>


Link
----
* [Grok Debugger](http://grokdebug.herokuapp.com/)