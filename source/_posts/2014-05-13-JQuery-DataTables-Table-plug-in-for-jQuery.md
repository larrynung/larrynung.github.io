---
layout: post
title: "JQuery DataTables - Table plug-in for jQuery"
date: 2014-05-13 13:20:00
comments: true
categories: [JQuery]
keywords: "DataTables"
description: "JQuery DataTables - Table plug-in for jQuery"
---

JQuery DataTables 是 JQuery 的 DataTable 元件，需要使用 jQuery 1.7 以後的版本。  
<!-- More -->

使用時需再 HTML 檔建立 Table，設定 Header 與 Footer，如果是要用 Client side 處理的話，這邊可連帶設定欲呈現的資料：   

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


Table 建好後，加上對應的 JavaScript 檔引用：  

{% codeblock lang:html %} 
<!-- DataTables CSS -->
<link rel="stylesheet" type="text/css" href="/DataTables-1.10.0/css/jquery.dataTables.css">
  
<!-- jQuery -->
<script type="text/javascript" charset="utf8" src="/DataTables-1.10.0/js/jquery.js"></script>
  
<!-- DataTables -->
<script type="text/javascript" charset="utf8" src="/DataTables-1.10.0/js/jquery.dataTables.js"></script>
{% endcodeblock %}

加入 JavaScript，用 JQuery 找到剛在 HTML 中建立的 Table，接著叫用 DataTable() 方法去啟用 JQuery Table：  

{% codeblock lang:js %} 
$(document).ready( function () {
    $('#table_id').DataTable();
} );
{% endcodeblock %}


{% img /images/posts/JQueryDataTables/1.png %}


啟用的同時可視需求下去設定對應的參數：  

{% codeblock lang:js %} 
$(document).ready( 
    function () 
    {
        $('#table_id').DataTable(
        {
            "bProcessing": true,
            "sPaginationType": "full_numbers",
            "bFilter": true,
            "iDisplayLength": 1,
            "bJQueryUI": true,
            "sDom": '<"dt_top_toolbar"p>rt<"dt_bottom_toolbar"p><"clear-b">',
        });
    }
);
{% endcodeblock %}

像是欄位的設定、分頁與排序的設定，或是設定是要做 Client side 的處理還是 Server side 的處理。  

{% img /images/posts/JQueryDataTables/2.png %}

詳細的參數可參閱 [DataTables - Usage](http://legacy.datatables.net/usage/)。  

Link
----
* [DataTables | Table plug-in for jQuery](https://datatables.net/)
