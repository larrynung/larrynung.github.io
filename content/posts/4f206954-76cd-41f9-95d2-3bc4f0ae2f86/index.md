---
title: "[Performance][C#]ToString V.S Enum.GetName"
date: "2013-11-06 12:00:00"
description: "這幾天筆者抽空看了一下程式中有Boxing與UnBoxing的地方，因為想要解決程式中列舉部分處理會有Boxing的問題，而注意到了將列舉值直接ToString與Enum.GetName的不同。"
tags: [CSharp]
---

這幾天筆者抽空看了一下程式中有Boxing與UnBoxing的地方，因為想要解決程式中列舉部分處理會有Boxing的問題，而注意到了將列舉值直接ToString與Enum.GetName的不同。兩種寫法有著效能上的差異，因此筆者用下面這樣的範例程式測試了一下兩者所需耗費的時間：

```csharp
using System;
using System.Diagnostics;
using System.Linq;
namespace ConsoleApplication24
{
	enum MyEnum
	{
		EnumItem1
	}

	class Program
	{
		static void Main(string[] args)
		{
			var count = 1000000;
			Console.WriteLine("ToString: {0} ms", DoTest(count, () =>
			{
				var temp = MyEnum.EnumItem1.ToString();
			}).ToString());

			Console.WriteLine("Enum.GetName: {0} ms", DoTest(count, () =>
			{
				var temp = Enum.GetName(typeof(MyEnum), MyEnum.EnumItem1);
			}).ToString());
		}

		static long DoTest(int count, Action action)
		{
			var sw = Stopwatch.StartNew();
			for(int i = 0;i<count;++i)
			{
				action();
			}
			return sw.ElapsedMilliseconds;
		}
	}
}
```

可以看到如下的運行結果。跑1000000次運算，ToString會需耗時1239ms，而Enum.GetName只需耗時465ms。

![image_thumb.png](/images/posts/4f206954-76cd-41f9-95d2-3bc4f0ae2f86/image_thumb.png)

這邊筆者也有將兩者的耗時做了一張長條圖，可以很清楚的看到Enum.GetName確實運行起來有著較佳的效能。

![image_thumb_2.png](/images/posts/4f206954-76cd-41f9-95d2-3bc4f0ae2f86/image_thumb_2.png)

那這樣的效能差距是怎樣出來的呢？看一下BCL在列舉值ToString時所做的處理動作就可以知道了，它會額外的判斷列舉是否有標記FlagAttribute，若有的話將導到Enum.InternalFlagsFormat去處理，若無的話則用Enum.GetName。

```c
/// <summary>Converts the value of this instance to its equivalent string representation.</summary>
/// <returns>The string representation of the value of this instance.</returns>
/// <filterpriority>2</filterpriority>
[__DynamicallyInvokable]
public override string ToString()
{
	return Enum.InternalFormat((RuntimeType)base.GetType(), this.GetValue());
}

private static string InternalFormat(RuntimeType eT, object value)
{
	if (eT.IsDefined(typeof(FlagsAttribute), false))
	{
		return Enum.InternalFlagsFormat(eT, value);
	}
	string name = Enum.GetName(eT, value);
	if (name == null)
	{
		return value.ToString();
	}
	return name;
}
```

所以若是列舉沒有附加FlagAttribute，其實它內部還是叫用Enum.GetName去做。那麼兩種寫法到底有什麼樣的差異呢？又為何ToString要特別去看FlagAttribute呢？這邊我們直接來看個簡易的範例就可以理解了。

```csharp
using System;
using System.Diagnostics;
using System.Linq;
namespace ConsoleApplication24
{
	[Flags]
	enum MyEnum
	{
		EnumItem1 = 1,
		EnumItem2 = 2,
		EnumItem3 = 1
	}

	class Program
	{
		static void Main(string[] args)
		{
			Console.WriteLine(MyEnum.EnumItem1.ToString());
			Console.WriteLine(MyEnum.EnumItem2.ToString());
			Console.WriteLine(MyEnum.EnumItem3.ToString());
			Console.WriteLine((MyEnum.EnumItem1 | MyEnum.EnumItem2).ToString());

			Console.WriteLine();
			Console.WriteLine(Enum.GetName(typeof(MyEnum), MyEnum.EnumItem1));
			Console.WriteLine(Enum.GetName(typeof(MyEnum), MyEnum.EnumItem2));
			Console.WriteLine(Enum.GetName(typeof(MyEnum), MyEnum.EnumItem3));
			Console.WriteLine(Enum.GetName(typeof(MyEnum), MyEnum.EnumItem1 | MyEnum.EnumItem2));
		}
	}
}
```

上面的程式運行後可得到像下面這樣的運行結果：

![image_thumb_1.png](/images/posts/4f206954-76cd-41f9-95d2-3bc4f0ae2f86/image_thumb_1.png)

很明顯的在列舉沒有附加上FlagAttribute，且沒有做過or運算時，兩者運行起來的效果是一樣的。對應到相同數值的列舉值不論用ToString還是Enum.GetName都會錯亂，像是範例中的EnumItem1與EnumItem3其值都是1，用ToString或是Enum.GetName帶入EnumItem3都會得到EnumItem1。但是若是列舉有附加FlagAttribute且做了or運算，那就只有ToString可以正常運作，這也就是BCL內特別做處理的部分。

這篇稍稍紀錄一下兩者處理方式的差異，知道兩者的差異後，我們可以依照不同的狀況給予最適合的處理方式。
