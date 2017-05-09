---
title: Vue.js - Input text binding
date: 2017-05-09 23:09:06
tags: [Vue.js]
---

要用 Vue.js 將資料與輸入框做繫結，我們可在 vue 建立的同時設定用來繫結的屬性，然後在 HTML 的輸入框元素中使用 v-model 設定所要繫結的屬性，這樣設定後輸入框的資料就會被寫入指定的屬性中，而指定屬性其值的變化也會呈現在輸入框中。  

<!-- More -->

<br/>


像是下面這樣的程式：  

{% codeblock lang:html %}
{% raw %}
<!DOCTYPE html>
<html>
<head>
  <title>Vue - Hello World</title>
  <script src="https://unpkg.com/vue/dist/vue.js"></script>
</head>
<body>
  <div id="app">
    <input v-model="message">
    <p>{{message}}</p>
  </div>

  <script>
    new Vue({
      el: '#app',
      data:{
        message: "Hello World"
      }      
    })
  </script>
</body>
</html>
{% endraw %}
{% endcodeblock %}

<br/>


其運行結果如下：  

{% asset_img 1.png %}

<br/>
