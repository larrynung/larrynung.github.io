---
title: "[C#]使用Reflection檢查指定類別是否含有預設建構子"
slug: "[CSharp]使用Reflection檢查指定類別是否含有預設建構子"
date: "2013-11-06 12:00:00"
description: "昨天在抽空調整一下專案程式碼，用Attribute與反射搭配的機制去做一些載入的動作，讓程式擴充時能專注在新加入的類別就好，程式啟動自行會用反射將該載入的載入。但由於目前尚未把現有的程式改的比較一致，每個類別的建構子不盡相同，因為我預期這些類別應該都要有預設的建構子，"
tags: [CSharp]
---

昨天在抽空調整一下專案程式碼，用Attribute與反射搭配的機制去做一些載入的動作，讓程式擴充時能專注在新加入的類別就好，程式啟動自行會用反射將該載入的載入。但由於目前尚未把現有的程式改的比較一致，每個類別的建構子不盡相同，因為我預期這些類別應該都要有預設的建構子，不夠的資料應該後續再透過別條路下去取得，所以這邊只先用反射載入含有預設建構子的類別，其它沒有預設建構子的類別就先照本來的路做些特殊處理，待後續再行重構。

要做偵測類別是否含有建構子，換句話說就是要想辦法取得該類別的預設ConstructorInfo。最簡單的作法就是用Type.GetConstructors取得所有的ConstructorInfo，然後找出不含參數的ConstructorInfo就可以了。

```csharp
private static Boolean HasDefaultConstructor1<T>()
{
	var type = typeof (T);
	foreach (var c in type.GetConstructors(BindingFlags.Instance | BindingFlags.Public))
	{
		if (c.GetParameters().Length ==0)
			return true;
	}
	return false;
}
```

但這方法有點笨矬，比較好一點的作法應該是透過Type.GetConstructor去取得，帶入空的Type[]當作參數取得ConstructorInfo，當回傳的ConstructorInfo不為空則代表該類別有預設建構子。

```csharp
private static Boolean HasDefaultConstructor2<T>()
{
	var type = typeof (T);
	return type.GetConstructor(new Type[0]) != null;
}
```

除了帶入空的Type[]外，我們也可以帶入Type.EmptyTypes，可以得到一樣的效果。

```csharp
private static Boolean HasDefaultConstructor2<T>()
{
	var type = typeof (T);
	return type.GetConstructor(Type.EmptyTypes) != null;
}
```

最後附上比較完整的測試範例：

```csharp
using System;
using System.Reflection;

namespace ConsoleApplication17
{
	class Program
	{
		static void Main(string[] args)
		{
			Console.WriteLine(HasDefaultConstructor1<TestClass1>());
			Console.WriteLine(HasDefaultConstructor2<TestClass1>());

			Console.WriteLine(HasDefaultConstructor1<TestClass2>());
			Console.WriteLine(HasDefaultConstructor2<TestClass2>());
		}

		private static Boolean HasDefaultConstructor1<T>()
		{
			var type = typeof (T);
			foreach (var c in type.GetConstructors(BindingFlags.Instance | BindingFlags.Public))
			{
				if (c.GetParameters().Length ==0)
					return true;
			}
			return false;
		}

		private static Boolean HasDefaultConstructor2<T>()
		{
			var type = typeof (T);
			return type.GetConstructor(Type.EmptyTypes) != null;
		}
	}

	internal class TestClass1
	{
		public TestClass1()
		{

		}

		public TestClass1(int arg1)
		{

		}
	}

	internal class TestClass2
	{
		public TestClass2(int arg1)
		{

		}
	}
}
```

運行結果如下：

![image_thumb.png](/images/posts/b8597596-7c07-4d7c-8880-a71a20dabf05/image_thumb.png)

## Link

* Type.EmptyTypes 欄位
* Most efficient way to get default constructor of a Type
