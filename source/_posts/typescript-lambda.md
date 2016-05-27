---
layout: post
title: "TypeScript - Lambda"
date: 2015-11-30 23:57:00
comments: true
categories: [TypeScript]
keywords: "TypeScript, Lambda"
description: "TypeScript - Lambda"
---

TypeScript 支援 Lambda 語法，語法如下：  

<!-- More -->

    (input parameters) => expression
    (input parameters) => {statement;}

<br/>


寫起來就像下面這樣：  

{% codeblock lang:js %}
var Execute = (cmd: string, ...params: string[]): void =>
        alert(cmd + "(" + params.join(", ") + ")");

Execute("Test", "Param1", "Param2");
{% endcodeblock %}

<br/>


{% img /images/posts/TypeScriptLambda/1.png %}
