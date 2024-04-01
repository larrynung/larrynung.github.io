---
title: "TypeScript - Lambda"
date: "2015-11-30 23:57:00"
description: "TypeScript - Lambda"
tags: [TypeScript]
---


TypeScript 支援 Lambda 語法，語法如下：  

<!-- More -->

    (input parameters) => expression
    (input parameters) => {statement;}

<br/>


寫起來就像下面這樣：  

```js
var Execute = (cmd: string, ...params: string[]): void =>
        alert(cmd + "(" + params.join(", ") + ")");

Execute("Test", "Param1", "Param2");
```

<br/>


{% img /images/posts/TypeScriptLambda/1.png %}
