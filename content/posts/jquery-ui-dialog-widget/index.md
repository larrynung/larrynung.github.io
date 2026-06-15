---
title: "JQuery UI - Dialog Widget"
date: "2015-12-21 23:22:00"
description: "JQuery UI - Dialog Widget"
---

要使用 JQuery UI 的 Dialog Widget，首先必須引用 JQuery、JQueryUI。

```html

```

接著在畫面上放入一個 div element。

```html

Hello World

```

在 Javascript 中用 JQuery 找到該 div element，並叫用 dialog 方法即可將該 div element 設為 Dialog。  

```js
$(function() {
  $("#dialog").dialog();
});
```

![1.png](/images/posts/JQueryUIDialog/1.png)

若要做些細部設定，Dialog 有提供些 options 可供我們使用，像是 resizable 可以讓 dialog 進行手動縮放、buttons 可設定 dialog 的按鈕。  

```js
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
```

![2.png](/images/posts/JQueryUIDialog/2.png)

若要主動觸發 Dialog，也提供了些 methods 讓我們使用，像是 open。  

```js
$("#open").click(function()
{
    $("#dialog").dialog("open");
});
```

![3.png](/images/posts/JQueryUIDialog/3.png)

最後這邊附上測試用的範例：

```html

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

Hello World

Open

```

Link
----
*[Dialog Widget | jQuery UI API Documentation](http://api.jqueryui.com/dialog/#option-title)