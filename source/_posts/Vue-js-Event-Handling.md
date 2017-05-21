---
title: Vue.js - Event Handling
date: 2017-05-21 23:04:27
tags: [Vue.js]
---

Vue.js 在事件處理上，主要是透過 v-on 去監聽事件，事件觸發後可以指定對應的動作。  

<!-- More -->

<br/>


像是點擊後用運算式處理對應的動作。  

```html
<!DOCTYPE html>
<html>
<head>
  <title>Vue - Hello World</title>
  <script src="https://unpkg.com/vue/dist/vue.js"></script>
</head>
<body>
  <div id="app">
    <button v-on:click="click += 1">Click</button>
    <p>{{click}}</p>
  </div>
  <script>
    new Vue({
      el: '#app',
      data:{
        click: 0
      }
    })
  </script>
</body>
</html>
```

<br/>


{% asset_img 1.png %}

<br/>


或是調用對應的方法處理。  

```html
<!DOCTYPE html>
<html>
<head>
  <title>Vue - Hello World</title>
  <script src="https://unpkg.com/vue/dist/vue.js"></script>
</head>
<body>
  <div id="app">
    <button v-on:click="onClick">Click</button>
    <p>{{click}}</p>
  </div>
  <script>
    new Vue({
      el: '#app',
      data:{
        click: 0
      },
      methods: {
        onClick: function(event){
          this.click += 1
        }
      }
    })
  </script>
</body>
</html>
```

<br/>


若有需要，在方法調用時也可以附帶參數進去調用。  

```html
<!DOCTYPE html>
<html>
<head>
  <title>Vue - Hello World</title>
  <script src="https://unpkg.com/vue/dist/vue.js"></script>
</head>
<body>
  <div id="app">
    <button v-on:click="onClick(2)">Click</button>
    <p>{{click}}</p>
  </div>
  <script>
    new Vue({
      el: '#app',
      data:{
        click: 0
      },
      methods: {
        onClick: function(value){
          this.click += value
        }
      }
    })
  </script>
</body>
</html>
```

<br/>


{% asset_img 2.png %}

<br/>


需要 DOM event 做些處理的話，也可以透過 $event 將 DOM event 傳入對應的方法內使用。  

```html
<!DOCTYPE html>
<html>
<head>
  <title>Vue - Hello World</title>
  <script src="https://unpkg.com/vue/dist/vue.js"></script>
</head>
<body>
  <div id="app">
    <button v-on:click="onClick(2, $event)">Click</button>
    <p>{{click}}</p>
  </div>
  <script>
    new Vue({
      el: '#app',
      data:{
        click: 0
      },
      methods: {
        onClick: function(value, event){
          if (event) event.preventDefault()
          this.click += value
        }
      }
    })
  </script>
</body>
</html>
```
