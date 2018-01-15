---
title: SonarQube - Downgrade database
date: 2018-01-16 00:14:33
tags: [SonarQube]
---

若 SonarQube DB 升級過後想要使用回舊版本的 SonarQube，會發現資料庫已經不相容於舊版本的 SonarQube DB。  

<!-- More -->

{% asset_img 1.png %}
 
<br/>


這時將 SonarQube DB 刪除後重建。  

```sql
DROP DATABASE sonar;
CREATE DATABASE sonar CHARACTER SET utf8 COLLATE utf8_general_ci;
```

{% asset_img 2.png %}
 
<br/>


{% asset_img 3.png %}
 
<br/>


舊版本的 SonarQube 服務就可以正常運作了。  

{% asset_img 4.png %}
 
<br/>


{% asset_img 5.png %}
 
<br/>
