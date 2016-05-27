---
layout: post
title: "JQuery UI - Spinner Widget"
date: 2015-12-24 05:44:00
comments: true
categories: 
keywords: 
description: "JQuery UI - Spinner Widget"
---

要使用 JQuery UI 的 Spinner Widget，首先必須引用 JQuery、JQueryUI。  

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
<input id="spinner">
{% endcodeblock %}

<br/>


在 Javascript 中用 JQuery 找到該 input element，並叫用 spinner 方法即可將該 input element 設為 spinner。  

{% codeblock lang:js %}
$(function() {
  $("#spinner").spinner();
});
{% endcodeblock %}

<br/>


{% img /images/posts/JQueryUISpinner/1.png %}

<br/>


若要做些細部設定，spinner 有提供些 options 可供我們使用，像是 min 可以設定  spinner 的最小值，max 可以設定 spinner 的最大值，step 可以設定 spinner 按一次要增加多少值。  

{% codeblock lang:js %}
$(function() {
  $("#spinner").spinner(
  {
      min:0,
      max:100,
      step:10
  });
});
{% endcodeblock %}

<br/>


若要主動觸發 spinner，也提供了些 methods 讓我們使用，像是 value。  

{% codeblock lang:js %}
$(function() {
  $("#spinner").spinner();
  $("#spinner").spinner("value", 0);
});
{% endcodeblock %}

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
    $("#spinner").spinner(
    {
    	min:0,
        max:100,
        step:10
    });
    $("#spinner").spinner("value", 0);
  });
  </script>
</head>
<body>

<input id="spinner">

</body>
</html>     
{% endcodeblock %}


Link
----
* [Spinner Widget | jQuery UI API Documentation](http://api.jqueryui.com/spinner/#event-change)
