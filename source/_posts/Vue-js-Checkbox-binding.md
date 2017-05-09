---
title: Vue.js - Checkbox binding
date: 2017-05-09 23:24:53
tags: [Vue.js]
---

Checkbox 的繫結一樣是在 Vue 建立時連帶設定要用來繫結的屬性，然後在 Checkbox 元素這邊透過 v-model 指定所要繫結的屬性，設定完後資料屬性與控制項之間即會連動。

<!-- More -->

<br/>


如果有多個 Checkbox 要做繫結，只要將繫結的屬性宣告成陣列，Checkbox 這邊使用 v-model 指定繫結至相同的屬性，並在 Checkbox 指定選取時的 value 即可。    

<br/>


最後附上一個完整的測試範例：  

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
    <input type="checkbox" v-model="checked">
    {{ checked }}
    <br/><br/>

    <input type="checkbox" value="option1" v-model="options">option1<br/>
    <input type="checkbox" value="option2" v-model="options">option2<br/>
    <input type="checkbox" value="option3" v-model="options">option3<br/>
    <br/>
    {{ options }}
  </div>

  <script>
    new Vue({
      el: '#app',
      data:{
        checked: false,
        options: ["option2"]
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


{% asset_img 2.png %}

<br/>

