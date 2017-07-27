---
title: >-
  PL/SQL & SQL CODING GUIDELINE 65 - Try to keep your packages small. Include
  only few procedures and functions that are used in the same context
date: 2017-07-27 13:40:15
tags: [PL/SQL and SQL Coding Guidelines]
---

條款六十五，試著讓 package 只有少量的內容，只在裡面保存少量的 procedure 與 function。  

<!-- More -->

<br/>


因為 package 會在第一次叫用時被載入進記憶體中，所以為了最佳化記憶體的耗費，與載入的時間，我們需要盡可能的將 package 切割乾淨，職責劃分乾淨，確保 package 內只有適當且少量的內容。