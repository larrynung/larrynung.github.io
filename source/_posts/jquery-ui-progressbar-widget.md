---
layout: post
title: "JQuery UI - Progressbar Widget"
date: 2015-12-23 00:30:00
comments: true
tags: 
keywords: 
description: "JQuery UI - Progressbar Widget"
---

要使用 JQuery UI 的 Progressbar Widget，首先必須引用 JQuery、JQueryUI。  

<!-- More -->

```html
<link rel="stylesheet" href="http://apps.bdimg.com/libs/jqueryui/1.10.4/css/jquery-ui.min.css">
<script src="http://apps.bdimg.com/libs/jquery/1.10.2/jquery.min.js"></script>
<script src="http://apps.bdimg.com/libs/jqueryui/1.10.4/jquery-ui.min.js"></script>
<link rel="stylesheet" href="jqueryui/style.css">
```

<br/>


接著在畫面上放入一個 div element。   

```html
<div id="pb">
</div>
```

<br/>


在 Javascript 中用 JQuery 找到該 div element，並叫用 progressbar 方法即可將該 div element 設為 progressbar。  

{% codeblock lang:js %}
  $(function() {
    $("#pb").progressbar();
  });
```

<br/>


{% img /images/posts/JQueryUIProgressbar/1.png %}

<br/>


若要做些細部設定，progressbar 有提供些 options 可供我們使用，像是 max 可以設定 progressbar 的最大值、value 可設定 progressbar 的當前值。  

{% codeblock lang:js %}
  $(function() {
    $("#pb").progressbar(
    {
    	max:100,
        value:50
    });
  });
```

<br/>


{% img /images/posts/JQueryUIProgressbar/2.png %}

<br/>


若要主動觸發 progressbar，也提供了些 methods 讓我們使用，像是 value。 

{% codeblock lang:js %}
  $(function() {
    $("#pb").progressbar();
    $("#increase").click(function()
    {
    	var value = $("#pb").progressbar("value");
        value += 10;
        value %= 100;
        $("#pb").progressbar("value", value);
    });
  });
```

<br/>


{% img /images/posts/JQueryUIProgressbar/3.png %}

<br/>


此外，也有提供些事件讓我們監聽，像是 change。  

{% codeblock lang:js %}
  $(function() {
    $("#pb").progressbar(
    {
        change:function()
        {
            var value = $("#pb").progressbar("value");
        	$("#percentage").text(value + "%");
        }
    });
    $("#increase").click(function()
    {
    	var value = $("#pb").progressbar("value");
        value += 10;
        value %= 100;
        $("#pb").progressbar("value", value);
    });
  });
```

<br/>


{% img /images/posts/JQueryUIProgressbar/4.png %}

<br/>


最後這邊附上測試用的範例： 

```html
<!doctype html>
<html lang="en">
<head>
  <link rel="stylesheet" href="http://apps.bdimg.com/libs/jqueryui/1.10.4/css/jquery-ui.min.css">
  <script src="http://apps.bdimg.com/libs/jquery/1.10.2/jquery.min.js"></script>
  <script src="http://apps.bdimg.com/libs/jqueryui/1.10.4/jquery-ui.min.js"></script>
  <link rel="stylesheet" href="jqueryui/style.css">
  <script>
  $(function() {
    $("#pb").progressbar(
    {
    	max:100,
        value:0,
        change:function()
        {
            var value = $("#pb").progressbar("value");
        	$("#percentage").text(value + "%");
        }
    });
    $("#increase").click(function()
    {
    	var value = $("#pb").progressbar("value");
        value += 10;
        value %= 100;
        $("#pb").progressbar("value", value);
    });
  });
  </script>
</head>
<body>
 
<div id="percentage">0%</div>
<div id="pb">
</div>

<button id="increase">Increase</button>
 
</body>
</html>		
```

<br/>


Link
----
* [Progressbar Widget | jQuery UI API Documentation](http://api.jqueryui.com/progressbar/#method-value)
