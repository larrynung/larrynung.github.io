---
title: LogDevice - Show log tree using ldshell
date: 2018-10-10 00:11:29
tags: [LogDevice]
---

要查看 LogDevice 的 Log tree，可以調用 ldshell 命令使用 -c 參數指定使用 Interactive Mode，帶入 LogDevice 的設定檔，帶入 logs show 指定要查閱 Log tree 即可。  

<!-- More -->

    ldshell -c <Config> logs show

<br/>


一開始的 log tree 應該是空的，只有根目錄。  

{% asset_img 1.png %}
 
<br/>


log 增刪後可以用這方法在 log tree 中查閱對應的變化，  

{% asset_img 2.png %}
 
<br/>


Link
----
* [Log configuration · LogDevice](https://logdevice.io/docs/Logs.html)
