---
title: "[C#]Reset an Object Using Reflection and an Extension Method"
slug: "csharp-reset-an-object-using-reflection-and-an-extension-method"
aliases: ["/posts/csharp使用反射搭配extension-method來reset物件/"]
date: "2011-04-18 09:52:22"
description: "看到網友在論壇發問的問題，想起之前在開發時有用過反射與擴充方法去將物件初始，擴充方法如下，可將物件的屬性值初始： 簡易的使用範例： 運行結果如下："
tags: [CSharp]
---

看到網友在論壇發問的問題，想起之前在開發時有用過反射與擴充方法去將物件初始，擴充方法如下，可將物件的屬性值初始：

```
public static class ObjectExtension
{
    public static void Reset(this object obj)
    {
        foreach (var p in obj.GetType().GetProperties(BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic))
        {
            if (!p.CanWrite)
                continue;
            var defaultValue = (p.GetCustomAttributes(typeof(DefaultValueAttribute), false) as DefaultValueAttribute[]).FirstOrDefault();
            p.SetValue(obj, (defaultValue == null) ? (p.PropertyType.IsValueType ? Activator.CreateInstance(p.PropertyType) : null) : defaultValue.Value, null);
        }
    }
}
```

簡易的使用範例：

```
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.ComponentModel;
```

```
namespace ConsoleApplication13
{
    class Program
    {
        static void Main(string[] args)
        {
            var people = new Person()
            {
                Name ="Larry",
                Sex= Person.SexType.Boy,
                Age=32
            };
```

```
            ShowPeople(people);
```

```
            people.Reset();
```

```
            Console.WriteLine(new string('=', 50));
            ShowPeople(people);
        }
```

```
        static void ShowPeople(Person people)
        {
            Console.WriteLine(String.Format ("Name: {0}",people.Name));
            Console.WriteLine(String.Format("Sex: {0}", people.Sex));
            Console.WriteLine(String.Format("Age: {0}", people.Age));
        }
    }
```

```
    public class Person
    {
        public enum SexType
        {
            Boy,
            Girl
        }
```

```
        public string Name { get; set; }
        public SexType Sex { get; set; }
```

```
        [DefaultValue(18)]
        public int Age { get; set; }
    }
}
```

運行結果如下：

![image_thumb.png](/images/posts/23027/image_thumb.png)
