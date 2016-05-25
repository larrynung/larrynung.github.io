---
layout: post
title: "TypeScript - Generics"
date: 2015-12-02 23:56:00
comments: true
categories: [TypeScript]
keywords: "TypeScript"
description: "TypeScript - Generics"
---

TypeScript 支援泛型語法，使用方式如下：  

<!-- More -->

{% codeblock lang:js %}
function GenericsFunction<T>(param:T) { 
	 ...
} 
...
class GenericsClass<T>
{
	GenericsField:T;
	GenericsMethod(param:T) { 
		...
	} 
}
{% endcodeblock %}

<br/>


最後附上個簡單的使用範例：  

{% codeblock lang:js %}
function ShowMessage<T>(message:T) { 
	alert(message); 
} 

ShowMessage<string>("test"); 
ShowMessage<number>(123);
{% endcodeblock %}

<br/>


{% img /images/posts/TypeScriptGenerics/1.png %}
