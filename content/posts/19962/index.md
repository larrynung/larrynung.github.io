---
title: "[C#][VB.NET]最大公因數 amp; 最小公倍數"
slug: "[CSharp][VB.NET]最大公因數 amp; 最小公倍數"
date: "2010-12-07 12:49:24"
description: "[C#][VB.NET]最大公因數 & 最小公倍數"
tags: [CSharp,VB.NET]
---
翻閱程式發現以前在處理合併儲存格時，為該功能撰寫了最大公因數與最小公倍數的處理，這邊稍微整理記錄一下。

最大公因數的取法為使用遞迴去實作輾轉相除法，最小公倍數則是利用最大公因數與下面公式來計算：

## 程式碼

C#
private int GCD(int num1, int num2)
{
int min = 0;
int max = 0;
int maxModMin = 0;
min = Math.Min(num1, num2);
max = Math.Max(num1, num2);
maxModMin = max % min;
return maxModMin > 0 ? GCD(min, maxModMin) : min;
}

private int LCM(int num1, int num2)
{
return num1 * num2 / GCD(num1, num2);
}

VB.NET

Private Function GCD(ByVal num1 As Integer, ByVal num2 As Integer) As Integer
Dim min, max, maxModMin As Integer
min = Math.Min(num1, num2)
max = Math.Max(num1, num2)
maxModMin = max Mod min
Return If(maxModMin > 0, gcd(min, maxModMin), min)
End Function

Private Function LCM(ByVal num1 As Integer, ByVal num2 As Integer) As Integer
Return num1 * num2 / GCD(num1, num2)
End Function

## 完整範例

C#

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ConsoleApplication1
{
class Program
{
private static int GCD(int num1, int num2)
{
int min = 0;
int max = 0;
int maxModMin = 0;
min = Math.Min(num1, num2);
max = Math.Max(num1, num2);
maxModMin = max % min;
return maxModMin > 0 ? GCD(min, maxModMin) : min;
}

private static int LCM(int num1, int num2)
{
return num1 * num2 / GCD(num1, num2);
}

static void Main(string[] args)
{
const int EXAMPLE_COUNT = 5;
const int MIN_RANDOM_VALUE = 2;
const int MAX_RANDOM_VALUE = 50;

int num1, num2;
Random ran = new Random();

Console.WriteLine("GCD...");
for (int i = 0; i 0, gcd(min, maxModMin), min)
End Function

Private Function LCM(ByVal num1 As Integer, ByVal num2 As Integer) As Integer
Return num1 * num2 / GCD(num1, num2)
End Function

Sub Main()
Const EXAMPLE_COUNT As Integer = 5
Const MIN_RANDOM_VALUE As Integer = 2
Const MAX_RANDOM_VALUE As Integer = 50

Dim num1 As Integer, num2 As Integer
Dim ran As New Random()

Console.WriteLine("GCD...")
For i As Integer = 0 To EXAMPLE_COUNT - 1
num1 = ran.Next(MIN_RANDOM_VALUE, MAX_RANDOM_VALUE)
num2 = ran.Next(MIN_RANDOM_VALUE, MAX_RANDOM_VALUE)
Console.WriteLine("GCD({0},{1}) = {2}", num1, num2, GCD(num1, num2).ToString())
Next

Console.WriteLine()
Console.WriteLine("LCM...")
For i As Integer = 0 To EXAMPLE_COUNT - 1
num1 = ran.Next(MIN_RANDOM_VALUE, MAX_RANDOM_VALUE)
num2 = ran.Next(MIN_RANDOM_VALUE, MAX_RANDOM_VALUE)
Console.WriteLine("LCM({0},{1}) = {2}", num1, num2, LCM(num1, num2).ToString())
Next
End Sub

End Module

運行結果如下：