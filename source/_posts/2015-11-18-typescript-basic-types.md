---
layout: post
title: "TypeScript - Basic Types"
date: 2015-11-18 21:32:00
comments: true
categories: [TypeScript]
keywords: "TypeScript"
description: "TypeScript - Basic Types"
---

TypeScript 內可用的型態有 Boolean、Number、String、Array、Any、Void、Enum 這幾種。  

<!-- More -->

<br/>


{% img /images/posts/TypeScriptBasicTypes/1.png %}

<br/>

其中 Boolean、Number、String、Array、Any、Enum 的宣告方式如下：  

    var variableName: Type;

<br/>


所以宣告起來會像下面這樣：   

{% codeblock lang:js %}
var booleanVariable: boolean;
var numberVariable: number;
var stringVariable: string;
var arrayVariable1: number[];
var arrayVariable2: Array<number>;
var anyVariable: any;
var enumVariable: enumName; 
{% endcodeblock %}

<br/>


宣告指定的型態後，該變數就只能賦予相同型態的值，像是 Boolean 型態就只能賦予 true/false、Number 型態只能賦予數值、String 型態只能賦予字串值。若真的有需要讓變數支援賦予多種不同型態的值，只要將變數宣告成 Any 型態即可。  

<br/>


陣列的宣告比較特殊，支援兩種宣告方式。可以直接用型態後面接中括弧表示，也可以用 Array 的泛型的寫法。  

<br/>


列舉型態的宣告跟 C# 類似：  

    enum enumName{element1 = 1, element2, element3, ...};

<br/>


列舉參數的宣告與列舉的操作如下：  

    var enumValue: enumName = enumName. element1;
    var enumName: enumName = enumName[2];

<br/>


Void 型態則是用以指定方法無回傳值時使用：  

    function functionName(): void {…}

<br/>


最後附上完整的測試範例：  

{% codeblock lang:js %}
enum Color {Red, Green, Blue};

var booleanVariable: boolean = true;
var numberVariable: number = 1;
var stringVariable: string = "test";
var arrayVariable1: number[] = [123];
var arrayVariable2: Array<number> = arrayVariable1;
var anyVariable: any = 1;
var enumVariable: Color; 

var colorName:string = Color[2]; 
var colorValue:number = Color.Green;

function log(msg:any): void 
{
	console.log(msg);
}

log(colorName);
log(colorValue);
{% endcodeblock %}

<br/>

Link
----
* [Handbook - Welcome to TypeScript](http://www.typescriptlang.org/Handbook)
