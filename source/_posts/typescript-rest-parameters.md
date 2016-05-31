---
layout: post
title: "TypeScript - Rest Parameters"
date: 2015-11-28 16:06:00
comments: true
tags: [TypeScript]
keywords: "TypeScript"
description: "TypeScript - Rest Parameters"
---

TypeScript 的方法支援不定數量的參數，使用上只要在最後一個方法的陣列參數前面加上 `...` 即可。  

<!-- More -->

<br/>


像是下面這個例子，定義了一個接口，可傳入要執行的命令名稱與命令要帶入的參數，因為命令的參數的個數可能不定，所以這邊就可以用 Rest Parameters 去做。  

{% codeblock lang:js %}
function Execute(cmd: string, ...params: string[]): void { 
	alert(cmd + "(" + params.join(", ") + ")"); 
} 

Execute("Test", "Param1", "Param2");
{% endcodeblock %}

<br/>


{% img /images/posts/TypeScriptRestParameters/1.png %}
