---
title: Vue.js - .lazy modifier
date: 2017-05-10 23:27:19
tags: [Vue.js]
---

Vue.js 的 .lazy modifier 可以讓繫結的資料在資料改變後才進行同步，而非在輸入的同時就進行同步。  

<!-- More -->

<br/>


像是下面這樣的程式：  

```html
<!DOCTYPE html>
<html>
<head>
  <title>Vue - Hello World</title>
  <script src="https://unpkg.com/vue/dist/vue.js"></script>
</head>
<body>
  <div id="app">
    <input v-model.lazy="message">
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
```

<br/>


運行起來會像下面這樣，資料在輸入時並不會被同步。    

{% asset_img 1.png %}

<br/>


當輸入完畢焦點移開或是按下 Enter 按鈕，資料被視為變更，才會進行資料的同步。  

{% asset_img 2.png %}

<br/>
