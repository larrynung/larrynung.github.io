---
layout: post
title: "TypeScript - Class"
date: 2015-12-02 22:45:00
comments: true
tags: [TypeScript]
keywords: "TypeScript"
description: "TypeScript - Class"
---

TypeScript 的類別透過 class 關鍵字宣告，透過 new 關鍵字建立物件實體。  

<!-- More -->

{% codeblock lang:js %}
class MyClass { 
	...
} 

var obj = new MyClass();
...
{% endcodeblock %}
	
<br/>


建構子的透過 constructor 關鍵字宣告。  

{% codeblock lang:js %}
...
constructor(...) { 
	... 
} 
...
{% endcodeblock %}

<br/>


類別屬性的宣告，是透過 get/set 關鍵字定義 get/set 區塊。  

{% codeblock lang:js %}
...
private _name: string; 
...
get name():string{ return this._name; } 
set name(value:string){ this._name = value; } 
...
{% endcodeblock %}

<br/>


類別方法的宣告不需要加上 function 關鍵字，還可依需求套上不同的存取修飾符，不過目前支援 private/public，若不加上存取修飾服，預設宣告的是 public 的方法。  

{% codeblock lang:js %}
...
MyFunction():void { 
	...
}

private PrivateFunction():void { 
        ...
}

public PublicFunction():void { 
        ...
}
...
{% endcodeblock %}

<br/>


類別的繼承則是透過 extends 關鍵字。  

{% codeblock lang:js %}
class ChildClass extends MyClass { 
	...
} 
{% endcodeblock %}

<br/>


最後附上完整的使用範例：  

{% codeblock lang:js %}
class Person { 
	private _name: string; 
	private _age: number; 

	get name():string{ return this._name; } 
	set name(value:string){ this._name = value; } 
	get age():number{ return this._age; } 
	set age(value:number){ this._age = value; } 

	constructor(name: string, age:number) {
		this.name = name; 
		this.age = age; 
	} 
	SayHello():string { 
		return "Hello~I'm " + this.name; 
	} 
} 
class Larry extends Person { 
	constructor() { 
		super("Larry Nung", 35); 
	} 
} 
var p = new Larry(); 
alert(p.SayHello());
{% endcodeblock %}

<br/>


{% img /images/posts/TypeScriptClass/1.png %}
