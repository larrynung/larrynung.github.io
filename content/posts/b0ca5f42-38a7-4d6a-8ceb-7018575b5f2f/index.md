---
title: "停用Debug.Assert警示對話框與啟用訊息記錄"
date: "2013-11-06 12:00:00"
description: "據Disable System.Diagnostics.Debug.Assert dialogs這篇文章所提，有時我們會有需要將System.Diagnostics.Debug.Assert產生的對話框給停止使用，像是讓電腦自動運行整合測試時，"
---

據Disable System.Diagnostics.Debug.Assert dialogs這篇文章所提，有時我們會有需要將System.Diagnostics.Debug.Assert產生的對話框給停止使用，像是讓電腦自動運行整合測試時，若因為程式中有加入System.Diagnostics.Debug.Assert的判斷，像是：

```vb
System.Diagnostics.Debug.Assert(False)
```

在自動運行整合測試時就會因為跳出System.Diagnostics.Debug.Assert對話框而讓整個流程給卡住，待使用者按下對話框的按鈕才可繼續往下測試。

![image_thumb_3.png](/images/posts/b0ca5f42-38a7-4d6a-8ceb-7018575b5f2f/image_thumb_3.png)

要將System.Diagnostics.Debug.Assert對話框給停止動作，我們可以為程式專案或是測試專案加上應用程式組態檔。

![image_thumb_1.png](/images/posts/b0ca5f42-38a7-4d6a-8ceb-7018575b5f2f/image_thumb_1.png)

![image_thumb_2.png](/images/posts/b0ca5f42-38a7-4d6a-8ceb-7018575b5f2f/image_thumb_2.png)

加入應用程式組態檔後，開啟加入的應用程式組態檔，為其添加assert Xml元素標籤，並設定assertuienabled屬性值為false即可。

```xml
<assert assertuienabled="false" />
```

像是：

![image_thumb.png](/images/posts/b0ca5f42-38a7-4d6a-8ceb-7018575b5f2f/image_thumb.png)

加完後再次運行就會發現System.Diagnostics.Debug.Assert對話框不會再跳出了。

除了關閉System.Diagnostics.Debug.Assert對話框的警示外，您也可以為其添加訊息記錄，透過assert Xml元素的logfilename屬性，為其指定訊息記錄存放位置即可。

```xml
<assert assertuienabled="false" logfilename="c:\log.txt" />
```

像是：

![image_thumb_4.png](/images/posts/b0ca5f42-38a7-4d6a-8ceb-7018575b5f2f/image_thumb_4.png)

設完運行，即可在指定的位置找到訊息記錄檔，其格式如下：

![image_thumb_5.png](/images/posts/b0ca5f42-38a7-4d6a-8ceb-7018575b5f2f/image_thumb_5.png)

## Link

* #### [Disable System.Diagnostics.Debug.Assert dialogs](http://blog.benhall.me.uk/2008/05/disable-systemdiagnosticsdebugassert.html)
* #### [Debug.Assert 方法](http://msdn.microsoft.com/zh-tw/library/system.diagnostics.debug.assert(VS.80).aspx)
* #### [<assert> Element](http://msdn.microsoft.com/en-us/library/ty5e4c4h.aspx)
