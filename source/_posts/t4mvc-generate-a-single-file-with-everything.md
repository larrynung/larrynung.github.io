---
layout: post
title: "T4MVC - Generate a single file with everything"
date: 2014-07-24 22:25:00
comments: true
tags: [T4MVC, T4]
keywords: "T4MVC, T4"
description: "T4MVC - Generate a single file with everything"
---

T4MVC 預設在產生程式碼時會依 Controller 產生不同的檔案，這樣會在專案目錄下產生很多的檔案，然而以自動產出的檔案來說，只要產生無誤，功能都正常，那麼產生的程式是不是照 Controller 分開，說實話一點都不重要。  

<!-- More -->

<br/>

且以現階段來說，T4MVC 無法脫離 Visual Studio 運行，因此 CI Server 無法運行 T4MVC 去產生檔案，這樣的設定使得每新增一個檔案就必需記得 Commit 對應的產出檔到版控上，反而造成不便。

<br/>

好在 T4MVC 有留這部份的設定彈性，我們只要在 T4MVC.tt.settings.xml 設定檔中將 SplitIntoMultipleFiles 設為 False 即可。  

{% codeblock lang:xml %}
...
<!-- If true,the template output will be split into multiple files. -->
<SplitIntoMultipleFiles>false</SplitIntoMultipleFiles>
...
```
