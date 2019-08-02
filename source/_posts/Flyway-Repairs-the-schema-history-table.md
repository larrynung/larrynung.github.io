---
title: Flyway - Repairs the schema history table
date: 2019-08-01 21:31:10
tags: [Flyway]
---

Flyway 的 Repair 功能可用來修復 Flyway 存放在資料庫內的資料。  

<!-- More -->

{% asset_img 1.png %}

</br>

像是 Migrate 發生錯誤，可用來清楚錯誤狀態。或是重新套用 Migration，去修復 Migration type/description/checkchecksum。  

</br>


像是這邊筆者的資料庫狀態如下...

{% asset_img 2.png %}

</br>


因為沒有造資料表所以塞資料的 Migration migrate 時會出錯。  

{% asset_img 3.png %}

</br>


這時資料庫內的 Migration 的狀態會是 Failed。  

{% asset_img 4.png %}

</br>


這時使用 Repair 功能...

    flyway repair

{% asset_img 5.png %}

</br>


資料庫內的 Migration 會回到 Pending 狀態。

{% asset_img 6.png %}
