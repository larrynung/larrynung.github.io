---
title: "[C#][VB.NET]GC.Collect()造成的怪現象"
slug: "[CSharp][VB.NET]GC.Collect()造成的怪現象"
date: "2009-01-30 10:48:06"
description: "[C#][VB.NET]GC.Collect()造成的怪現象"
tags: [CSharp,VB.NET]
---

## Abstract
IntroductionExampleConclusionDownload

## Introduction

前一陣子在用同事程式時，總覺得速度有點慢，但卻不知道問題出在哪個同事的Code，因此針對底層同事的程式做了效率上面的測試。測試的結果是，當拿同事的類別來用時，若只建立並使用一次，則其效能不差。但若用迴圈去建立並使用多次時，其效能就變的十分的低落。

當我把我測出的情況告知同事後，同事也用相同的方法測了一遍，但是在他的電腦上卻看不到效能變差的跡象。相同的程式，不同的電腦，跑出不同的結果，然而其中的差異又不像是電腦速度差異所造成的。研究了老半天，才發現此差異是出在我拿正在開發的產品專案來測試，介面較為複雜，控制項使用的較多。而同事則是開他的測試用專案，沒有啥麼介面。

雖然發現了造成差異的點，但是若自己寫的類別會因介面上控制項的多寡而造成效能上的影響亦是一件怪事，最後才發現原來一切都是因為GC.Collect()造成的，同事的程式寫了很多GC.Collect()想要回收記憶體。卻意外的造成此怪現象的產生。

此現象應是由於GC回收資源時會針對目前使用到的物件下去回收，所以記憶體中使用的物件越多執行速度就越慢。而由於程式內部有許多地方有呼叫到GC.Collect()，因此程式的執行速度連帶也會受到GC回收速度影響。

## Example

舉個例子來說，假設今天有個Data的類別寫法如下：

VB.NET

C#
class Data
{
...
public void SetValue(Object val)
{
    _val = val;
    GC.Collect();
}
...
}

則下列這段Code的執行結果，將會依據介面上控制項的多寡而定。

VB.NET

C#
private void Button1_Click(object sender, EventArgs e)
{
    this.Button1.Enabled = false;
    Stopwatch  sw = Stopwatch.StartNew();
    for (int i = 1; i <= 1000; i++)
    {
        Data d = new Data();
        d.SetValue("test");
    }
    this.TextBox1.Text = String.Format("花費時間: {0} ms", sw.ElapsedMilliseconds.ToString());
    this.Button1.Enabled = true;
}

執行結果如下:

## Conclusion

一般說來，若非必要普遍都不建議程式設計師下GC.Collect，但畢竟是開出來的函式，仍是不能避免有人會使用GC.Collect，因此我們必須要了解使用GC.Collect可能會產生的現象與濫用的徵兆(執行效能會因控制項或是記憶體中的物件量而變化)，碰到這類問題時才能發現問題的所在。

## Download
TestGC.zip