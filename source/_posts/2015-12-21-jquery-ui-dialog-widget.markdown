---
layout: post
title: "JQuery UI - Dialog Widget"
date: 2015-12-21 23:22
comments: true
categories: 
keywords: 
description: "JQuery UI - Dialog Widget"
---

要使用 JQuery UI 的 Dialog Widget，首先必須引用 JQuery、JQueryUI。

<!-- More -->

{% codeblock lang:html %}
<link rel="stylesheet" href="http://apps.bdimg.com/libs/jqueryui/1.10.4/css/jquery-ui.min.css">
<script src="http://apps.bdimg.com/libs/jquery/1.10.2/jquery.min.js"></script>
<script src="http://apps.bdimg.com/libs/jqueryui/1.10.4/jquery-ui.min.js"></script>
<link rel="stylesheet" href="jqueryui/style.css">
{% endcodeblock %}


接著在畫面上放入一個 div element。

{% codeblock lang:html %}
<div id="dialog">
Hello World
</div>
{% endcodeblock %}


在 Javascript 中用 JQuery 找到該 div element，並叫用 dialog 方法即可將該 div element 設為 Dialog。  

{% codeblock lang:js %}
$(function() {
  $("#dialog").dialog();
});
{% endcodeblock %}

<br/>


{% img /images/posts/JQueryUIDialog/1.png %}

<br/>


若要做些細部設定，Dialog 有提供些 options 可供我們使用，像是 resizable 可以讓 dialog 進行手動縮放、buttons 可設定 dialog 的按鈕。  

{% codeblock lang:js %}
$(function() {
  $("#dialog").dialog(
  {
      resizable: true,
      buttons: {
      OK: function() {
        $( this ).dialog( "close" );
      },
      Cancel: function() {
        $( this ).dialog( "close" );       
      }
      }
  });
});
{% endcodeblock %}

<br/>


{% img /images/posts/JQueryUIDialog/2.png %}

<br/>


若要主動觸發 Dialog，也提供了些 methods 讓我們使用，像是 open。  

{% codeblock lang:js %}
$("#open").click(function()
{
    $("#dialog").dialog("open");
});
{% endcodeblock %}

<br/>


{% img /images/posts/JQueryUIDialog/3.png %}

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
  	$("#dialog").dialog(
    {
    	autoOpen: false,
        resizable: true,
        buttons: {
        OK: function() {
          $( this ).dialog( "close" );
        },
        Cancel: function() {
          $( this ).dialog( "close" );
        }
        }
    });
    
    $("#open").click(function()
    {
    	$("#dialog").dialog("open");
    });
  });
  </script>
</head>
<body>

<div id="dialog" title="Dialog demo">
Hello World
</div>

<button id="open">Open</button>

</body>
</html>      
{% endcodeblock %}

</br>


Link
----
*[Dialog Widget | jQuery UI API Documentation](http://api.jqueryui.com/dialog/#option-title)
