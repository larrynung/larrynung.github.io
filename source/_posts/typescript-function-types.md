---
layout: post
title: "TypeScript - Function Types"
date: 2015-11-18 22:57:00
comments: true
categories: [TypeScript]
keywords: "TypeScript"
description: "TypeScript - Function Types"
---

用 JavaScript 撰寫 Function，要馬是使用 Named function，要馬就是使用 Anonymous function。  

<!-- More -->

{% codeblock lang:js %}
//Named function
function add(x, y) {
    return x+y;
}

//Anonymous function
var myAdd = function(x, y) { return x+y; };
{% endcodeblock %}

<br/>


因為 JavaScript 不具型態的關係，Function 有時候會被傳入不如預期的資料，回傳不預期的結果。像是上述的例子可能預期是用做數值的加總，但因為不具型態的關係就有可能被傳入字串，做為字串的串接使用。  

<br/> 


TypeScript 可以在定義方法時設定參數與回傳值的型態，像是下面這樣：  

    function functionName(param1: Type1, [param2: Type2, ...]): Type {...}

<br/>


所以上述的程式透過 TypeScript 改寫成像下面這樣，就不會碰到本來面臨的問題了。

{% codeblock lang:js %}
function add(x: number, y: number): number {
    return x+y;
}

var myAdd = function(x: number, y: number): number { return x+y; };
{% endcodeblock %}

<br/>


Link
----
* [Handbook - Welcome to TypeScript](http://www.typescriptlang.org/Handbook#functions-function-types)
