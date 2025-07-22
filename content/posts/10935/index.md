---
title: "[C#]Effective C# 條款四： 使用ConditionalAttribute替代#if條件編譯"
slug: "[CSharp]Effective C# 條款四： 使用ConditionalAttribute替代#if條件編譯"
date: "2009-10-07 09:04:23"
description: "[C#]Effective C# 條款四： 使用ConditionalAttribute替代#if條件編譯"
tags: [CSharp]
---

## 
	Introduction

	相信大多數的C#使用者，尤其是碰過C語言的開發者，多多少少應該都有用過#if/#endif條件編譯。#if條件編譯通常是用來讓同一份代碼產生不同的程式，最常見的就是拿來設定Debug版與Release版的不同。

	由於#if條件編譯具有常被開發者濫用、使用不便、及代碼難以閱讀等問題。C#設計者開始針對這個問題下去思考設計，為此C#在System.Diagnostics命名空間中添加了一個ConditionalAttribute。使用上不僅方便，且具有較好的可讀性與效率。

## 
	使用限制

	ConditionalAttribute在使用上只能設定在屬性類別 

	[Conditional("DEBUG")]
public class Documentation : System.Attribute

	或是設定在副程式上。 

	[Conditional("TRACE_ON")]
    public static void Msg(string msg)

	若是在函式或是一般類別上設定ConditionalAttribute，編譯器會提示錯誤。  

## 
	ConditionalAttribute

	ConditionalAttribute在使用上就跟一般的Attribute一樣，只要在正確的地方宣告ConditionalAttribute並帶入參數就可以了。若要使用多個編譯條件，且彼此間是or的關係。可以這樣寫： 

	[Conditional("A"), Conditional("B")]
static void DoIfAorB()

	若為And關係  ，則我們可以像下面這樣使用：

	[Conditional("A")]
static void DoIfA()
{
    DoIfAandB();
}

[Conditional("B")]
static void DoIfAandB()
{
    // Code to execute when both A and B are defined...
}

	除此之外，也可以利用#if與#define來輔助。 

	#if (A && B)
#define BOTH
#endif
        [Conditional("BOTH")]
        static void DoIfAandB()
        {
        }

	接著，讓我們直接來看段程式： 

	static void Main(string[] args)
        {
            HelloWord();
            SayHello1();
            SayHello2();
        }

        static void HelloWord()
        {
            Console.WriteLine("Hello~");
        }

        static void SayHello1()
        {
#if DEBUG
            HelloWord();
#endif
        }

        [System.Diagnostics .Conditional ("DEBUG")]
        static void SayHello2()
        {
            HelloWord();
        }

	程式運行後可以看到會因編譯條件不同而有不同的結果：

	Denug  

	Release  

	相信看到這邊，大家還是覺得ConditionalAttribute與#if條件編譯兩者是差不多的。沒關係，讓我們反組譯一下上面的範例就會更清楚了。

	internal class Program
{
    private static void HelloWord()
    {
        Console.WriteLine("Hello~");
    }

    private static void Main(string[] args)
    {
        HelloWord();
        SayHello1();
        //SayHello2被編譯器拿掉
    }

    private static void SayHello1()
    {
        //內容被編譯器拿掉
    }

    [Conditional("DEBUG")]
    private static void SayHello2()
    {
        HelloWord();
    }
}

	有感覺了嗎？使用ConditionalAttribute不會影響副程式的編譯，只會影響該副程式的叫用。從上面反組譯的程式碼，我們可以看到加上ConditionalAttribute的副程式在編譯後，其內容仍然存在。叫用副程式的地方在編譯後卻消失不見了。至於使用#if條件編譯的副程式，其內容在編譯後已被編譯器拿掉。而叫用副程式的地方卻仍然保留。也因如此，使用ConditionalAttribute來做條件編譯會較#if條件編譯來得有效率，因其少了叫用的地方，自然也就少了呼叫副程式所需的Push參數、區域變數、與返回位置等額外負擔。