---
title: 'C# 8.0 - Target-typed new-expressions'
date: 2019-03-25 07:32:56
tags: [CSharp, CSharp 8.0]
---

C# 8.0 的 Target-typed new-expressions 能讓開發人員在使用 new 關鍵字建立物件實體時省略帶入型別，編譯器編譯時會依照 Context 幫我們帶入。  

<!-- More -->

<br/>


以簡單的例子來說，假設已經宣告了變數 p 型別為 Point，那在用 new 關鍵字建立實體時就可以省略帶入 Point。  

'''c#
...
Point p = new (1, 2);
'''

{% asset_img 1.jpg %}

<br/>


反組譯看可以看到編譯器會幫我們在 new 關鍵字後面帶入正確的型別。  

{% asset_img 2.jpg %}

<br/>


複雜一點的情境像是陣列元素的宣告也是支援。  

'''c#
...
Point[] ps = { new (1, 2), new (2, 2) };
'''

{% asset_img 3.jpg %}

<br/>
