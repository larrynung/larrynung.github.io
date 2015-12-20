---
layout: post
title: "JQuery UI - Datepicker Widget"
date: 2015-12-20 17:22
comments: true
categories: 
keywords: 
description: "JQuery UI - Datepicker Widget"
---

要使用 JQuery UI 的 Datepicker Widget，首先必須引用 JQuery、JQueryUI。  

<!-- More -->

{% codeblock lang:html %}
<link rel="stylesheet" href="http://apps.bdimg.com/libs/jqueryui/1.10.4/css/jquery-ui.min.css">
<script src="http://apps.bdimg.com/libs/jquery/1.10.2/jquery.min.js"></script>
<script src="http://apps.bdimg.com/libs/jqueryui/1.10.4/jquery-ui.min.js"></script>
<link rel="stylesheet" href="jqueryui/style.css">
{% endcodeblock %}

<br/>


接著在畫面上放入一個 input element。  

{% codeblock lang:html %}
<p>Date：<input type="text" id="datepicker"></p>
{% endcodeblock %}

<br/>


在 Javascript 中用 JQuery 找到該 input element，並叫用 datapicker 方法即可將該 input element 設為 Datepicker。  

{% codeblock lang:js %}
  $(function() {
    $("#datepicker").datepicker();
  });
{% endcodeblock %}

<br/>


{% img /images/posts/JQueryUIDatepicker/1.png %}

<br/>


若要做些細部設定，Datepicker 有提供些 options 可供我們使用，像是 minDate、maxDate 可以用來決定可供選取的時間範圍，onSelect 方法可以設定日期選取後的動作。  

{% codeblock lang:js %}
  $(function() {
    $("#datepicker").datepicker(
    {
    	minDate: -7,
    	maxDate: +7,
        onSelect:  function(date) {
            alert(date);
        }
    });
  });
{% endcodeblock %}

<br/>


{% img /images/posts/JQueryUIDatepicker/2.png %}

<br/>


若要主動觸發 Datepicker，也提供了些 methods 讓我們使用，像是 setDate、show。  

{% codeblock lang:js %}
  $(function() {
    $("#datepicker").datepicker();
    $("#datepicker").datepicker('setDate', new Date());
    $("#open").click(function(){
    	$("#datepicker").datepicker('show');
    });
  });
{% endcodeblock %}

<br/>

{% img /images/posts/JQueryUIDatepicker/3.png %}

<br/>


最後這邊附上測試用的範例：  

{% codeblock lang:html %}
<!doctype html>
<html lang="en">
<head>
  <link rel="stylesheet" href="http://apps.bdimg.com/libs/jqueryui/1.10.4/css/jquery-ui.min.css">
  <script src="http://apps.bdimg.com/libs/jquery/1.10.2/jquery.min.js"></script>
  <script src="http://apps.bdimg.com/libs/jqueryui/1.10.4/jquery-ui.min.js"></script>
  <link rel="stylesheet" href="jqueryui/style.css">
  <script>
  $(function() {
    $("#datepicker").datepicker(
    {
    	minDate: -7,
    	maxDate: +7,
        onSelect:  function(date) {
            alert(date);
        }
    });
    $("#datepicker").datepicker('setDate', new Date());
    
    $("#open").click(function(){
    	$("#datepicker").datepicker('show');
    });
  });
  </script>
</head>
<body>
 
<p>Date：<input type="text" id="datepicker"></p>

<button id="open">Open</button>
 
</body>
</html>			
{% endcodeblock %}

<br/>


Link
----
* [Datepicker Widget | jQuery UI API Documentation](http://api.jqueryui.com/datepicker/#method-show)
