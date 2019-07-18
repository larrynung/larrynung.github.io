---
title: MariaDB - Enable performance schema
date: 2019-07-18 22:03:47
tags: [MariaDB]
---

透過 MySQL CLI 查閱 Performance schema 的啟用狀態。  

<!-- More -->

    show variables like 'performance_schema';

{% asset_img 1.png %}

</br>


如果 Performance schema 未啟用，可開啟 MariaDB 的設定檔，加入 performance_schema=on 設定後存檔，然後將 MariaDB 服務重啟。  

```ini
[mysqld]
performance_schema=on
```

{% asset_img 2.png %}

</br>


Performance schema 就會被啟用。這邊可再次查詢 Performance schema 的啟用狀態做個確認。  

{% asset_img 3.png %}
