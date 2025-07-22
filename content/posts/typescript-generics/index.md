---
title: "TypeScript - Generics"
date: "2015-12-02 23:56:00"
description: "TypeScript - Generics"
tags: [TypeScript]
---

TypeScript 支援泛型語法，使用方式如下：

```js
function GenericsFunction(param:T) {
...
}
...
class GenericsClass
{
GenericsField:T;
GenericsMethod(param:T) {
...
}
}
```

最後附上個簡單的使用範例：

```js
function ShowMessage(message:T) {
alert(message);
}

ShowMessage("test");
ShowMessage(123);
```

{% img /images/posts/TypeScriptGenerics/1.png %}