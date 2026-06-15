---
title: "[VB.NET]VB 10.0 Statement Lambdas"
date: "2009-08-11 09:00:16"
description: "[VB.NET]VB 10.0 Statement Lambdas"
tags: [VB.NET]
---

## Introduction

在.NET Framework 3.5(含)以前，VB.NET的Lambdas在使用上存在諸多限制。像是只支援Singleline Lambdas，或是必需要有函式回傳值等問題，讓整個Lambdas在使用上十分的不便。但在VB 10.0以後，這些問題都已獲得了改善。

> C# 在3.5(含)以前就已具備Multiline Lambdas的能力。

## Support

* VB 10.0 or latter

## Multiline Lambdas

Multiline Lambdas在使用上就跟寫一般函式類似，只要在Function…End Function區塊內加入每行的程式即可。

簡單的範例程式碼片段如下：

```vb
'宣告addLambdas
Dim addLambdas = Function(num1, num2)
                                   Dim total = num1 + num2
                                   Return total
                            End Function

'呼叫addLambdas
Console.WriteLine(addLambdas(123, 456))
```

同樣的程式我們也可以明確的定義回傳值型態

```vb
Dim addLambdas = Function(num1, num2) As Integer
```

也可以明確的指定帶入的參數型態

```vb
Dim addLambdas = Function(num1 As Integer, num2 As Integer) As Integer
```

若有要傳遞參考的需求，也可以在函式參數前加上ByRef

```vb
Dim addLambdas = Function(ByRef num1 As Integer, num2 As Integer) As Integer
```

## Sub Lambdas

Sub Lambdas使用上就跟一般的Lambdas運算式一樣，不同的是Sub Lambdas呼叫後不會有回傳值。就跟副程式一樣是沒有回傳值的，使用上只需把Lambdas運算式的Function關鍵字改為Sub即可。跟副程式的寫法類似。

Sub Lambdas跟一般的Lambdas一樣，除了有Multiline lambdas外

```vb
'宣告addLambdas
Dim addLambdas = Sub(num1, num2)
                     Console.WriteLine(num1 + num2)
                 End Sub

'呼叫addLambdas
addLambdas(123, 456)
```

也有Singleline lambdas

```vb
'宣告addLambdas
Dim addLambdas = Sub(num1, num2) Console.WriteLine(num1 + num2)
```

使用上都大同小異

## 注意事項

**1.要指定參數型別時，必需同時指定所有參數型別。**

若在使用上只指定部份參數型，而未指定所有參數的型別，此時編譯器會提示 "All parameters must be explicitly typed if any of them are explicitly typed" 的錯誤。

![image_thumb.png](/images/posts/9989/image_thumb.png)

**2.不支援Optional關鍵字**

若在參數前面加上Optional，則編譯器會提示的 "'Lambdas' params cannot be declared 'Optional'" 錯誤。

![image_thumb_1.png](/images/posts/9989/image_thumb_1.png)

**3.不支援ParamArray關鍵字**

若在參數前面加上ParamArray，則編譯器會提示的 "'Lambdas' params cannot be declared ParamArray" 錯誤。

![image_thumb_2.png](/images/posts/9989/image_thumb_2.png)
