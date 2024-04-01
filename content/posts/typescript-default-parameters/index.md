---
title: "TypeScript - Default Parameters"
date: "2015-11-22 23:47:00"
description: "TypeScript - Default Parameters"
tags: [TypeScript]
---


TypeScript 的 Function 支援 Default Parameters，使用上只要在參數名稱後面帶入預設的參數值，當呼叫方法時忽略該參數，該參數則會以預設的參數值下去運行。  

<!-- More -->

<br/>


像是下面這樣：  

```js
function sayHello(name: string = 'World') {
  var msg:string = 'Hello~';
  if (name)
      msg += name;
  console.log(msg);
}

sayHello();
sayHello('Larry Nung');
```
