---
title: Vue.js - Components
date: 2017-05-05 00:18:38
tags: [Vue.js]
---

Vue.js Component 可使用局部註冊。  

<!-- More -->

{% codeblock lang:html %}
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
{% endcodeblock %}

<br/>


也可以使用全域註冊。  

{% codeblock lang:html %}
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
{% endcodeblock %}

<br/>


像是這邊筆者就註冊了 Hello Component，該 Component 會顯示 Hello World 的字樣，註冊完我們就可以在 HTML 中使用 Hello 這個 Element。  

{% asset_img 1.png %}

<br/>


Component 也支援設定 data，但 data 必須是 function。  

{% codeblock lang:html %}
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
{% endcodeblock %}

<br/>


如果 Component 需要由外面傳遞資訊進去，可以在註冊 Component 的同時用 props 設定接受的參數名稱，然後在 HTML 中使用 Component element 時，就可以使用設定的參數將資訊傳入。  

{% codeblock lang:html %}
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
{% endcodeblock %}

<br/>


{% asset_img 2.png %}

<br/>


Link
----
* [Components — Vue.js](https://vuejs.org/v2/guide/components.html)
