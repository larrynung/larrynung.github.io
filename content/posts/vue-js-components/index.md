---
title: "Vue.js - Components"
date: "2017-05-05 00:18:38"
tags: [Vue.js]
---


Vue.js Component 可讓我們將畫面與程式封裝程可重用的元件。

<!-- More -->

<br/>


可在建立 Vue 時透過 components 宣告，進行局部註冊。  

```html
<!DOCTYPE html>
<html>
<head>
  <title>Vue - Hello World</title>
  <script src="https://unpkg.com/vue/dist/vue.js"></script>
</head>
<body>
  <div id="app">
    <Hello></Hello>
  </div>

  <script>
    new Vue({
      el: '#app',
      components: {
        'Hello' : {
          template : '<h1>Hello World</h1>'
        }
      }     
    })
  </script>
</body>
</html>
```

<br/>


也可以使用 Vue.component 宣告，進行全域註冊。  

```html
<!DOCTYPE html>
<html>
<head>
  <title>Vue - Hello World</title>
  <script src="https://unpkg.com/vue/dist/vue.js"></script>
</head>
<body>
  <div id="app">
    <Hello></Hello>
  </div>

  <script>
    Vue.component( 'Hello' , {
      template : '<h1>Hello World</h1>'
    })
    new Vue({
      el: '#app'  
    })
  </script>
</body>
</html>
```

<br/>


像是這邊筆者就註冊了名為 Hello 的 Component，該 Component 會顯示出 Hello World 的字樣，Component 註冊完後可以在 HTML 中使用 Hello 這個 Component 的 Element。  

![1.png](1.png)

<br/>


Component 也支援設定 data，可存放ㄧ些 Component 會使用到的資料，但 data 必須是用 function 的方式宣告。  

```html
<!DOCTYPE html>
<html>
<head>
  <title>Vue - Hello World</title>
  <script src="https://unpkg.com/vue/dist/vue.js"></script>
</head>
<body>
  <div id="app">
    <Hello></Hello>
  </div>

  <script>
    Vue.component( 'Hello' , {
      template : '<h1>{{message}}</h1>',
      data: function (){
        return {
          message: 'Hello World',
        }
      }
    })
    new Vue({
      el: '#app'      
    })
  </script>
</body>
</html>
```

<br/>


如果 Component 需要由外面傳遞資訊進去，可以在註冊 Component 的同時用 props 設定接受的參數名稱，然後在 HTML 中使用 Component element 時，就可以使用設定的參數將資訊傳入。  

```html
<!DOCTYPE html>
<html>
<head>
  <title>Vue - Hello World</title>
  <script src="https://unpkg.com/vue/dist/vue.js"></script>
</head>
<body>
  <div id="app">
    <Hello name='Larry'></Hello>
  </div>

  <script>
    Vue.component( 'Hello' , {
      props: ['name'],
      template : '<h1>Hello {{name}}</h1>'
    })
    new Vue({
      el: '#app'  
    })
  </script>
</body>
</html>
```

<br/>


![2.png](2.png)

<br/>


Link
----
* [Components — Vue.js](https://vuejs.org/v2/guide/components.html)
