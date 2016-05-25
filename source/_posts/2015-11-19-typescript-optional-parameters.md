---
layout: post
title: "TypeScript - Optional Parameters"
date: 2015-11-19 23:49:00
comments: true
categories: [TypeScript]
keywords: "TypeScript"
description: "TypeScript - Optional Parameters"
---

TypeScript 的 Function 支援 Optional Parameters，使用上只要在參數名稱後面加上 `?` 即可，但需注意 Optional Parameters 必須放在 Required Parameters 的後面。  

<!-- More -->

<br/>


使用起來會像下面這樣：  

{% codeblock lang:js %}
function sayHello(name?: string) { 
	var msg:string = 'Hello~';
	if (name) 
		msg += name;
	console.log(msg);
} 

sayHello();
sayHello('Larry Nung');
{% endcodeblock %}
