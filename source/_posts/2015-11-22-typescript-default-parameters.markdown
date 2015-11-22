---
layout: post
title: "TypeScript - Default Parameters"
date: 2015-11-22 23:47
comments: true
categories: [TypeScript]
keywords: "TypeScript"
description: "TypeScript - Default Parameters"
---

TypeScript 的 Function 支援 Default Parameters，使用上只要在參數名稱後面帶入預設的參數即可：  

<!-- More -->

<br/>


像是下面這樣：  

{% codeblock lang:js %}
function sayHello(name: string = 'World') {
  var msg:string = 'Hello~';
  if (name)
      msg += name;
  console.log(msg);
}

sayHello();
sayHello('Larry Nung');
{% endcodeblock %}
