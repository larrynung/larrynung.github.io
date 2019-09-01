---
title: "MethodBoundaryAspect.Fody - Altering asynchronous method behavior"
date: 2019-09-01 23:52:57
tags: [Fody]
---

MethodBoundaryAspect.Fody 要修改非同步方法的回傳值，可在 OnExit 方法實作時將 MethodExecutionArgs.ReturnValue 屬性值轉回 Task<T>，用 ContinueWith 串接處理，並將之塞回 MethodExecutionArgs.ReturnValue。  

<!-- More -->

```c#
if (args.ReturnValue is Task<...> t)
{
    args.ReturnValue = t.ContinueWith(...);
}
```

</br>


像是如果要撰寫一個可將方法回傳值變大寫的 Attribute 的話，可像下面這樣撰寫。  

```c#
using System.Threading.Tasks;
using MethodBoundaryAspect.Fody.Attributes;


namespace MethodBoundaryAspect.Fody.Demo
{
    public sealed class UpperAttribute : OnMethodBoundaryAspect
    {
        public override void OnExit(MethodExecutionArgs args)
        {
            if (args.ReturnValue is Task<string> t)
            {
                args.ReturnValue = t.ContinueWith(task => t.Result.ToUpper());
            }
            else
            {
                args.ReturnValue = (args.ReturnValue as string).ToUpper();
            }
        }
    }
}
```

{% asset_img 1.png %}

</br>


在要做大寫轉換的方法上加掛 Attribute。  

```c#
using System;
using System.Threading.Tasks;


namespace MethodBoundaryAspect.Fody.Demo
{
    class Program
    {
        [Log]
        static void Main(string[] args)
        {
            Console.WriteLine(GetDataAsync().Result);
        }


        [Upper]
        static Task<string> GetDataAsync()
        {
            return Task.FromResult("hello world!");
        }

        [Upper]
        static string GetData()
        {
            return "hello world!";
        }
    }
}
```

{% asset_img 2.png %}

</br>


程式在編譯時即會加掛對應的處理，方法運行後可看到回傳值會被轉為大寫。  

{% asset_img 3.png %}
