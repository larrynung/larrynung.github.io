---
title: Flyway - Disable Clean command
date: 2019-08-03 08:44:59
tags: [Flyway]
---

Flyway 的 Clean 命令是比較危險的命令，因此在上正式環境時會透過設訂將之關閉。  

<!-- More -->

</br>


開啟設定檔將 flyway.cleanDisable 設定值設定為 true 後存檔離開。

    flyway.cleanDisable=true

{% asset_img 1.png %}

</br>


Clean 命令就會被禁止使用了。  

{% asset_img 2.png %}
