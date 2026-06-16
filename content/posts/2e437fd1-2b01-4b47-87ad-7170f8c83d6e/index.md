---
title: "使用滑鼠右鍵快速產生XML序列化組件"
date: "2013-11-06 12:00:00"
description: "之前記錄過一篇使用XML序列化程式產生器工具加速XML序列化，裡面有提到使用建置事件來產生XML序列化組件的方法。但若只想更新XML序列化組件，不想要開啟專案重新建置時，這樣的方法就顯得有點麻煩。此時我們可以透過本篇紀錄的方法用滑鼠右建快速產生XML序列化組件。"
---

之前記錄過一篇使用XML序列化程式產生器工具加速XML序列化，裡面有提到使用建置事件來產生XML序列化組件的方法。但若只想更新XML序列化組件，不想要開啟專案重新建置時，這樣的方法就顯得有點麻煩。此時我們可以透過本篇紀錄的方法用滑鼠右建快速產生XML序列化組件。

只要把下面的內容修改一下放至文字檔中，儲存成附檔名為reg的檔案，用滑鼠點選兩下登陸至註冊檔，滑鼠右鍵中即會出現產生序列化組件的選單。

```xml
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Classes\exefile\shell\Sgen]
@="產生序列化組件"

[HKEY_LOCAL_MACHINE\SOFTWARE\Classes\exefile\shell\Sgen\command]
@="cmd /c  Title 產生%1的序列化組件&& @echo 產生序列化組件... && @echo 來源檔案: %1 && \"C:\\Program Files\\Microsoft SDKs\\Windows\\v7.0A\\bin\\sgen.exe\" /a:\"%1\" /force /n && pause"

[HKEY_LOCAL_MACHINE\SOFTWARE\Classes\dllfile\shell\Sgen]
@="產生序列化組件"

[HKEY_LOCAL_MACHINE\SOFTWARE\Classes\dllfile\shell\Sgen\command]
@="cmd /c  Title 產生%1的序列化組件&& @echo 產生序列化組件... && @echo 來源檔案: %1 && \"C:\\Program Files\\Microsoft SDKs\\Windows\\v7.0A\\bin\\sgen.exe\" /a:\"%1\" /force /n && pause"
```

使用時可在組件檔上按下滑鼠右鍵

![image_thumb_4.png](/images/posts/2e437fd1-2b01-4b47-87ad-7170f8c83d6e/image_thumb_4.png)

點選產生序列化組件

![image_thumb_3.png](/images/posts/2e437fd1-2b01-4b47-87ad-7170f8c83d6e/image_thumb_3.png)

點選後會開始產生XML序列化組件

![image_thumb_1.png](/images/posts/2e437fd1-2b01-4b47-87ad-7170f8c83d6e/image_thumb_1.png)

產生完後附檔名為XmlSerializers.dll的XML序列化組件就會出現在目前所在的檔案系統中

![image_thumb_2.png](/images/posts/2e437fd1-2b01-4b47-87ad-7170f8c83d6e/image_thumb_2.png)
