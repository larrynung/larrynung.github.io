---
title: ".NET 4.0 New Feature - 程式碼合約(Code Contracts) (五) 介面合約與抽象方法合約"
date: "2013-11-06 12:00:00"
description: "介面合約主要功用為為實作介面的類別提供統一的驗證合約，當我們為介面定義好了介面合約以後，所有實作該介面的類別都會享有到合約驗證的好處，不需每個類別各自撰寫，可減少撰寫重覆的驗證合約程式、增加程式中合約驗證覆蓋完整度、與加快實現合約式編程。"
tags: [CSharp]
---

介面合約主要功用為為實作介面的類別提供統一的驗證合約，當我們為介面定義好了介面合約以後，所有實作該介面的類別都會享有到合約驗證的好處，不需每個類別各自撰寫，可減少撰寫重覆的驗證合約程式、增加程式中合約驗證覆蓋完整度、與加快實現合約式編程。

要使用介面契約，我們必須要加入對應該介面的驗證合約抽象類別，為介面提供對應的合約。透過使用成對的屬性ContractClass與ContractClassFor修飾驗證合約抽象類別與介面，其中ContractClass屬性表示所修飾的類別為介面，並指定介面對應的驗證合約抽象類別，而ContractClassFor屬性則表示所修飾的類別為驗證合約抽象類別，並指出該驗證合約抽象類別所對應的介面。

![clip_image002_thumb.jpg](/images/posts/d3796a9f-821d-4f0e-a111-6d456bfdf166/clip_image002_thumb.jpg)

值得注意的是，在撰寫驗證合約抽象類別時，若要驗證的方法為函式，方法回傳值須用default(T)替代回傳。

這邊來看一段UserManual中的範例程式加深印象：

```csharp
[ContractClass(typeof(IFooContract))]
interface IFoo
{
    int Count { get; }
    void Put(int value);
}

[ContractClassFor(typeof(IFoo))]
abstract class IFooContract : IFoo
{
    int IFoo.Count
    {
        get
        {
            Contract.Ensures(0 <= Contract.Result<int>());
            return default(int); // dummy return
        }
    }

    void IFoo.Put(int value)
    {
        Contract.Requires(0 <= value);
    }
}
```

至於抽象方法合約(Abstract Method Contracts)，跟介面合約用法一樣，透過加入繼承抽象方法持有類別的驗證合約抽象類別，為抽象方法提供對應的合約，覆寫該抽象方法的方法皆具有合約驗證的效果。

這邊來看一段UserManual中的範例程式，來釐清兩者之間的差異：

```csharp
[ContractClass(typeof(FooContract))]
abstract class Foo
{
    public abstract int Count { get; }
    public abstract void Put(int value);
}

[ContractClassFor(typeof(Foo))]
abstract class FooContract : Foo
{
    public override int Count
    {
        get
        {
            Contract.Ensures(0 <= Contract.Result<int>());
            return default(int); // dummy return
        }
    }

    public override void Put(int value)
    {
        Contract.Requires(0 <= value);
    }
}
```

很明顯的，兩者的差異只在於一個是介面，而一個是抽象方法
