---
title: Vue.js - Watch
date: 2017-05-12 13:52:05
tags: [Vue.js]
---

Vue.js 的 watch 可以設定監控特定的屬性，當屬性值變動時做對應的處理。  

<!-- More -->

<br/>


使用上只要在建構 Vue 建立時設定 watch 物件，裡面放置屬性值變化時要做的處理即可。   

{% codeblock lang:html %}
{% raw %}
  <div  id = "app">
    ...
    <input  v-model = "<PropertyName>">
	...
  </div>
  <script>
    new Vue({
      el : '#app' ,
      data :{
        ...
      },
      watch: {
        <PropertyName>: function (val) {
          ...
        }
      }      
    })
  </script>
{% endraw %}
{% endcodeblock %}

<br/>


像是下面這樣的程式，設定了 message 變動時將訊息寫入 console 內。  

{% codeblock lang:html %}
{% raw %}
<!DOCTYPE html>
<html>
<head>
  <title> Vue - Hello World </title>
  <script  src = "https://unpkg.com/vue/dist/vue.js"></script>
</head>
<body>
  <div  id = "app">
    <input  v-model = "message">
    <p> {{message}} </p>
  </div>
  <script>
    new Vue({
      el : '#app' ,
      data :{
        message : ""
      },
      watch: {
        message: function (val) {
          console.log(val)
        }
      }      
    })
  </script>
</body>
</html>
{% endraw %}
{% endcodeblock %}

<br/>


運行起來當輸入框的輸入值變動，會連帶變動輸入框繫結的 message 屬性，然後因為監控到了 message 屬性值的變動，所以會將屬性值輸出到 console。  

{% asset_img 1.png %}

<br/>
