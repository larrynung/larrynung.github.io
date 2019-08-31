---
title: MethodBoundaryAspect.Fody - Altering method behavior
date: 2019-08-31 23:01:50
tags: [Fody]
---

MethodBoundaryAspect.Fody 要修改方法的回傳值，可在 OnExit 方法實作時透過 MethodExecutionArgs.ReturnValue 屬性填入新的方法值。  

<!-- More -->

</br>


像是如果要撰寫一個可將方法回傳值變大寫的 Attribute 的話，可像下面這樣撰寫。  

```c#
using MethodBoundaryAspect.Fody.Attributes;


namespace MethodBoundaryAspect.Fody.Demo
{
    public sealed class UpperAttribute : OnMethodBoundaryAspect
    {
        public override void OnExit(MethodExecutionArgs args)
        {
            args.ReturnValue = (args.ReturnValue as string).ToUpper();
        }
    }
}
```

{% asset_img 1.png %}

</br>


在要做大寫轉換的方法上加掛 Attribute。  

```c#
using System;


namespace MethodBoundaryAspect.Fody.Demo
{
    class Program
    {
        [Log]
        static void Main(string[] args)
        {
            Console.WriteLine(GetData());
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
