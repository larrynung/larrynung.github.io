---
layout: post
title: "JQuery DataTables - Table plug-in for jQuery"
date: 2014-04-27 13:20
comments: true
categories: [JQuery]
keywords: "DataTables"
description: "JQuery DataTables - Table plug-in for jQuery"
published: false
---

jQuery 1.7 or newer 

建立 Table，設定 Header 與 Footer，如果是要用 Client side 處理的話，這邊可連帶設定欲呈現的資料。

{% codeblock lang:html %} 
<table id="table_id" class="display">
    <thead>
        <tr>
            <th>Column 1</th>
            <th>Column 2</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Row 1 Data 1</td>
            <td>Row 1 Data 2</td>
        </tr>
        <tr>
            <td>Row 2 Data 1</td>
            <td>Row 2 Data 2</td>
        </tr>
    </tbody>
</table>
{% endcodeblock %}


Table 建好後， 引用對應的 JavaScript 檔，

{% codeblock lang:html %} 
<!-- DataTables CSS -->
<link rel="stylesheet" type="text/css" href="/DataTables-1.10.0/css/jquery.dataTables.css">
  
<!-- jQuery -->
<script type="text/javascript" charset="utf8" src="/DataTables-1.10.0/js/jquery.js"></script>
  
<!-- DataTables -->
<script type="text/javascript" charset="utf8" src="/DataTables-1.10.0/js/jquery.dataTables.js"></script>
{% endcodeblock %}

加入 JavaScript 去啟用 JQuery Table

{% codeblock lang:html %} 
$(document).ready( function () {
    $('#table_id').DataTable();
} );
{% endcodeblock %}

啟用的同時可視需求下去設定對應的參數

像是欄位的設定、分頁與排序的設定，或是設定是要做 Client side 的處理還是 Server side 的處理。

Link
----
* [DataTables | Table plug-in for jQuery](https://datatables.net/)
