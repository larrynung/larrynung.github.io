---
layout: post
title: "C# 6.0 - Await in catch/finally"
date: 2015-03-13 07:59
comments: true
categories: [C#]
keywords: "C#"
description: "C# 6.0 - Await in catch/finally"
---

C# 6.0 以前 await 無法用在 catch/finally 區塊，C# 6.0 後開始支援。  

<!-- More -->

{% codeblock lang:c# %}
using System;
using System.Threading.Tasks;

namespace ConsoleApplication10
{
    class Program
    {
        static void Main(string[] args)
        {
            Test();
            System.Threading.Thread.Sleep(10000);
        }

        private static async void Test()
        {
            try
            {
                throw new Exception();
            }
            catch
            {
                Console.WriteLine("Catch...");
                await Task.Delay(500);                
            }
            finally
            {
                Console.WriteLine("Finally...");
                await Task.Delay(500);
            }
        }
    }
}
{% endcodeblock %}
