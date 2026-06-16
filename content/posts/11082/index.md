---
title: "[C#]Effective C# Item 8: Ensure That 0 Is a Valid State for Value Types"
slug: "csharp-effective-csharp-item-8-ensure-that-0-is-a-valid-state-for-value-types"
aliases: ["/posts/csharpeffective-c#-條款八-確保0為值類型的有效狀態/"]
date: "2009-10-16 09:04:21"
description: ".NET程式在物件初始時，變數初始器會將成員變數做初始化的動作。對於值類型的成員變數來說，會被初始為0值。因此我們應將0視為值類型的默認值。 以列舉型別來看，假設今天我有一個列舉型別： 其列舉值並未從0，而是從1開始。則初始值0對該列舉來說，是一個無效的狀態。程式也可能因此無法正常運作。"
tags: [CSharp]
---

.NET程式在物件初始時，變數初始器會將成員變數做初始化的動作。對於值類型的成員變數來說，會被初始為0值。因此我們應將0視為值類型的默認值。

以列舉型別來看，假設今天我有一個列舉型別：

```csharp
enum Sex
    {
        Boy=1,
        Girl=2
    }
```

其列舉值並未從0，而是從1開始。則初始值0對該列舉來說，是一個無效的狀態。程式也可能因此無法正常運作。像是：

```csharp
class Program
    {
        static void Main(string[] args)
        {
            Person p=new Person();
            //p.Sex = Sex.Boy;
            Console.WriteLine(p.Sex.ToString ());
        }
    }
    enum Sex
    {
        Boy = 1,
        Girl = 2
    }
    struct Person
    {
        public String Name;
        public Sex Sex ;
    }
```

運行結果如下：

![image_thumb.png](/images/posts/11082/image_thumb.png)

但在正常的情況下，列舉值應該要在列舉範圍內，運行結果應顯示如下這般：

![image4_thumb.png](/images/posts/11082/image4_thumb.png)

這樣的問題我們無法透過建構子給予初始值來解決，因為就算指定了具備參數的建構子。

```csharp
struct Person
    {
        public String Name;
        public Sex Sex ;
        public Person(String name,Sex sex)
        {
            this.Name = name;
            this.Sex = sex;
        }
    }
```

對於值類型來說仍有預設建構子可以使用。像是：

```csharp
class Program
    {
        static void Main(string[] args)
        {
            Person p=new Person();
            Console.WriteLine(p.Sex.ToString ());
        }
    }
    enum Sex
    {
        Boy = 1,
        Girl = 2
    }

    struct Person
    {
        public String Name;
        public Sex Sex;

        public Person(String name, Sex sex)
        {
            this.Name = name;
            this.Sex = sex;
        }
    }
```

且值類型的預設建構子無法自行撰寫，若嘗試撰寫編譯器會發出"Structs cannot contain explicit parameterless constructors"的錯誤。

![image_thumb_2.png](/images/posts/11082/image_thumb_2.png)

而若想透過變數初始器來做設定的動作，編譯器也會以"cannot have instance field initializers"錯誤告知。

![image_thumb_3.png](/images/posts/11082/image_thumb_3.png)

因此我們在使用值類型時特別留意其初始值，確保0為值類型的有效狀態，避免上述問題的發生。就像這樣：

```csharp
class Program
    {
        static void Main(string[] args)
        {
            Person p=new Person();
            Console.WriteLine(p.Sex.ToString ());
        }
    }
    enum Sex
    {
        NotSet = 0,
        Boy = 1,
        Girl = 2
    }

    struct Person
    {
        public String Name;
        public Sex Sex;

        public Person(String name, Sex sex)
        {
            this.Name = name;
            this.Sex = sex;
        }
    }
```

除此之外，當撰寫設有Flags屬性的列舉型別，我們也要特別留意。除必須確保初始值0為有效狀態外，還需讓其值為沒有設定任何標記的狀態。像是：

```csharp
[Flags]
public enum Styles
{
    None=0,
    Flat=1.
    Sunken=2,
    Raised=4
}
```

這是因為設有Flags屬性的列舉型態，我們可能會拿來做像下面這樣的運算：

```csharp
if((flag & Styles.Flat) != 0)
    DoFlatThings();
```

當Flat是0的話，判斷式依舊為false，達不到預期的效果。不過，這例子只是告知建議遵守該條款的原因。事實上，這樣的問題可以像下面這樣避開：

```csharp
if((flag & Styles.Flat) == Styles.Flat)
    DoFlatThings();
```
