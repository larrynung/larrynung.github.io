---
title: "[C#]Effective C# 條款三： 運算子is或as優於強制轉型"
slug: "[CSharp]Effective C# 條款三： 運算子is或as優於強制轉型"
date: "2009-09-30 08:17:52"
description: "[C#]Effective C# 條款三： 運算子is或as優於強制轉型"
tags: [CSharp]
---

對C#而言，在做型別轉換時，撇開一些型別有提供Parse可供轉型外，通常我們有兩種選擇：一種是利用as運算子、一種則是強制轉型。作型別轉換時，應盡量採用as運算子來做轉型的動作，因為它比強制轉型安全，也具有較好的效能。

這邊讓我們直接來看個例子。假設今天我們寫一段程式，需將Object轉型為MyType。我們可以使用as運算子處理：

```csharp
object o = Factory.GetObject();
            MyType t = o as MyType;
            if(t != null)
            {
                //轉型成功
            }else{
                //轉型失敗
            }
```

也可以使用強制轉型來做：

```csharp
try
            {
                object o = Factory.GetObject();
                MyType t = (MyType)o;
                if (t != null)
                {
                    //轉型成功
                }
                else
                {
                    //Null
                }
            }
            catch
            {
                //轉型失敗
            }
```

很明顯的，使用as運算子來做轉型，程式會較為簡單易讀，不需添加例外處理，在效能上自然也不會有額外的負擔。強制轉型在使用上除了需作例外處理，也需外加null的判斷(主要是因為null可轉為任意型態)。而as運算子轉型就只需要檢查轉型後是否為null即可。

as運算子只能用於參考類型，不能應用於值類型(除非是Nullable的值類型)。像下面的程式就無法通過編譯器的編譯：

```csharp
object o = Factory.GetObject();
            int i = o as int;
```

這是因為值類型不可為null導致(因若o無法轉型為整數，值類型也不可為null，其值無從填入i)。像這樣的值類型轉換，我們就可以使用強制轉型來處理：

```csharp
object o = Factory.GetObject();
            int i = 0;
            try
            {
                i = (int)o;
            }catch {
                //轉型失敗
            }
```

好一點的寫法，可以搭配is運算子來避免異常的發生

```csharp
object o = Factory.GetObject();
            int i = 0;
            if (o is int)
                i = (int)o;
```

一般來說只有當不能使用as運算子作轉型動作時，才會考慮使用is運算子，不然多半會產生冗餘的程式碼。像是：

```csharp
object o = Factory.GetObject();
            MyType t = null;
            if (o is MyType)
                t = o as MyType;
```

由上述，我們可以得知，在型別轉換的抉擇上，最好遵循著一個順序：

![image_thumb_1.png](/images/posts/10834/image_thumb_1.png)

值得一提的是，我們常用的foreach語法，由於要同時支援值類型與參考類型，內部的轉型是採用強制轉型，若轉型失敗會產生InvalidCastException例外。
