---
title: Database versioning
date: 2019-08-06 07:17:10
tags:
---

資料庫在做版本控制可被分為 State-driven 與 Migration-driven 兩種方式。  

<!-- More -->

</br>


State-driven
=============

State-driven 的做法是在開發時持續的去維護資料庫的快照，資料庫的快照主要用 Create database/table/procedure 這些語法撰寫，描述該版本資料庫的樣子。

</br>


部署時會去針對目的資料庫或其對應的快照進行比對，產生部署腳本，最後在目的資料庫運行部署腳本即可。要重現某一版本的資料庫的話，只要將對應版本的資料庫快照從版本控制系統中取出，將之做為目的資料庫快照就可以了。  

{% asset_img 1.png %}

</br>


使用 State-driven 的好處有:
- 維護資料庫快照易於了解該版資料庫的內容
- 現成的 Data modeling 工具可輔助，便於設計溝通
- 因為主要都是修改相同檔案的 Create database/table/procedure 語法，衝突發生易於排除

</br>

缺點有:  
- 比較受限於工具支援程度
- 彈性受限，如考慮資料部份，在某些情境可能還是會搭配 Migration 腳本

</br>


Migration-driven
================

Migration-driven 方法則是在維護變更，主要用 Create/Alter 語法撰寫，用來描述這次修改所需要對資料庫的變更。  

</br>


部署上只要直接對資料庫運行 Migration 腳本即可。若是要重現某版資料庫，只要將 Migration 從版本控制系統中取出，然後逐一從第一個 Migration 運行到指定版本的 Migration 就可以了。

{% asset_img 2.png %}

</br>


使用 Migration-driven 的好處有:  
- 彈性較大，資料的部份也可以處理
- 文字編輯工具即可撰寫，不受限於工具

</br>


缺點有:  
- 因為是維護變更，開發上都是撰寫用來疊加的 Migration，從 Migration 不易了解該版資料庫的樣子
- 在多人維護下 Migration 易互相衝突

</br>


Link
====
* [State vs migration-driven database delivery](https://enterprisecraftsmanship.com/2015/08/18/state-vs-migration-driven-database-delivery/)
* [Critiquing two different approaches to delivering databases: Migrations vs state](http://workingwithdevs.com/delivering-databases-migrations-vs-state/)
