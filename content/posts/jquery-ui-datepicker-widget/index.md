---
title: "JQuery UI - Datepicker Widget"
date: "2015-12-20 17:22:00"
description: "JQuery UI - Datepicker Widget"
---

要使用 JQuery UI 的 Datepicker Widget，首先必須引用 JQuery、JQueryUI。  

```html

```

接著在畫面上放入一個 input element。  

```html
Date：
```

在 Javascript 中用 JQuery 找到該 input element，並叫用 datapicker 方法即可將該 input element 設為 Datepicker。  

```js
  $(function() {
    $("#datepicker").datepicker();
  });
```

{% img /images/posts/JQueryUIDatepicker/1.png %}

若要做些細部設定，Datepicker 有提供些 options 可供我們使用，像是 minDate、maxDate 可以用來決定可供選取的時間範圍，onSelect 方法可以設定日期選取後的動作。  

```js
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
```

{% img /images/posts/JQueryUIDatepicker/2.png %}

若要主動觸發 Datepicker，也提供了些 methods 讓我們使用，像是 setDate、show。  

```js
  $(function() {
    $("#datepicker").datepicker();
    $("#datepicker").datepicker('setDate', new Date());
    $("#open").click(function(){
    	$("#datepicker").datepicker('show');
    });
  });
```

{% img /images/posts/JQueryUIDatepicker/3.png %}

最後這邊附上測試用的範例：  

```html

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

Date：

Open

```

Link
----
* [Datepicker Widget | jQuery UI API Documentation](http://api.jqueryui.com/datepicker/#method-show)