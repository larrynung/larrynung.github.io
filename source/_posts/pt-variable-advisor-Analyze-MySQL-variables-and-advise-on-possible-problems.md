---
title: pt-variable-advisor - Analyze MySQL variables and advise on possible problems
date: 2020-03-11 08:21:10
tags: [Percona Toolkit, MySQL, MariaDB]
---

pt-variable-advisor 是 Percona Toolkit 內的工具之一，能調用 MySQL/MariaDB 的 SHOW VARIABLES 命令偵測參數值，並根據 Rule 分析給予修正的建議。  

<!-- More -->

<br>


使用方式如下:  

    pt-variable-advisor [OPTIONS] [DSN]

<br>


像是:  

    pt-variable-advisor h=$host,P=$port,u=$user,p=$password

{% asset_img 1.png %}

<br>


Link
====
* [pt-variable-advisor](https://www.percona.com/doc/percona-toolkit/3.0/pt-variable-advisor.html)
