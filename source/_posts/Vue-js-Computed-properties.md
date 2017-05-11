---
title: Vue.js - Computed properties
date: 2017-05-11 23:49:09
tags: [Vue.js]
---

Vue.js 的 Computed properties 可以設定經過運算而來的屬性。  

<!-- More -->

<br/>


只要在建構 Vue 建立實設定 computed 物件，裡面放置 Computed property 的方法，這樣在使用 Computed property 時就會去調用 Computed property 定義的方法去運算。   

{% codeblock lang:html %}
{% raw %}
  <div id="app">
    ...
    {{<PropertyName>}}
    ...
  </div>
  ...
  <script>
    new Vue({
      el: '#app',
      data:{
        ...
      },
      computed: {
        <PropertyName>: function () {
          ...
        }
      }     
    })
  </script>
{% endraw %}
{% endcodeblock %}

<br/>


像是下面這樣的程式，設定了 firstName 與 lastName 兩個屬性，並設定了名為 fullName 的 Computed property，其值為 firstName 與 lastName 用空格串接。  

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
    <input v-model="firstName">
    <input v-model="lastName">
    <p>{{fullName}}</p>
  </div>
  <script>
    new Vue({
      el: '#app',
      data:{
        firstName: "Larry",
        lastName:"Nung"
      },
      computed: {
        fullName: function () {
          return this.firstName + " " + this.lastName;
        }
      }     
    })
  </script>
</body>
</html>
{% endraw %}
{% endcodeblock %}

<br/>


運行起來不論 firstName 與 lastName 怎樣變動，都可以正確的顯示出 fullName。  

{% asset_img 1.png %}

<br/>


如果需要將設定的值經過運算處理存回一般的屬性，可以設定 Computed property 的 setter，只要在建構 Vue 建立實設定 computed 物件，裡面放置 Computed property 的物件，Computed property 物件內放置 get 與 set 的方法，定義讀取與寫入資料要做的運算。  

{% codeblock lang:html %}
{% raw %}
  <div id="app">
    ...
    <input v-model="<PropertyName>">
    ...
  </div>
  ...
  <script>
    new Vue({
      el: '#app',
      data:{
        ...
      },
      computed: {
        <PropertyName>: {
          get: function () {
            ...
          },
          set: function (value) {
            ...
          }
        }
      }     
    })
  </script>
{% endraw %}
{% endcodeblock %}

<br/>


像是下面這樣的程式，設定了 fullName 這個 Computed property，當該值被設定時會將資料切分到 firstName 與 lastName 這兩個屬性。   

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
    <input v-model="firstName">
    <input v-model="lastName">
    <p><input v-model="fullName"></p>
  </div>
  <script>
    new Vue({
      el: '#app',
      data:{
        firstName: "",
        lastName:""
      },
      computed: {
        fullName: {
          get: function () {
            return this.firstName + " " + this.lastName;
          },
          set: function (value) {
            var names = value.split(' ')
            this.firstName = names[0]
            this.lastName = names[names.length - 1]
          }
        }
      }     
    })
  </script>
</body>
</html>
{% endraw %}
{% endcodeblock %}

<br/>


運行起來會像下面這樣：  

{% asset_img 2.png %}

<br/>

