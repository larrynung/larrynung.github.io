---
title: "[Performance][C#]ToString V.S Enum.GetName"
date: "2013-11-06 12:00:00"
description: "[Performance][C#]ToString V.S Enum.GetName"
tags: [CSharp]
---

<p>
	這幾天筆者抽空看了一下程式中有Boxing與UnBoxing的地方，因為想要解決程式中列舉部分處理會有Boxing的問題，而注意到了將列舉值直接ToString與Enum.GetName的不同。兩種寫法有著效能上的差異，因此筆者用下面這樣的範例程式測試了一下兩者所需耗費的時間：</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:4bc57f67-66b9-4127-bbbc-c396e73635fb" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="c#" name="code">
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
			Console.WriteLine("ToString: {0} ms", DoTest(count, () =&gt;
			{
				var temp = MyEnum.EnumItem1.ToString();
			}).ToString());

			Console.WriteLine("Enum.GetName: {0} ms", DoTest(count, () =&gt;
			{ 
				var temp = Enum.GetName(typeof(MyEnum), MyEnum.EnumItem1);
			}).ToString());
		}

		static long DoTest(int count, Action action)
		{
			var sw = Stopwatch.StartNew();
			for(int i = 0;i&lt;count;++i)
			{
				action();
			}
			return sw.ElapsedMilliseconds;
		}
	}
}
</pre>
</div>
<p>
	 </p>
<p>
	可以看到如下的運行結果。跑1000000次運算，ToString會需耗時1239ms，而Enum.GetName只需耗時465ms。</p>
<p>
	<img alt="image" border="0" height="224" src="\images\posts\4f206954-76cd-41f9-95d2-3bc4f0ae2f86\image_thumb.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="433" /></p>
<p>
	 </p>
<p>
	這邊筆者也有將兩者的耗時做了一張長條圖，可以很清楚的看到Enum.GetName確實運行起來有著較佳的效能。</p>
<p>
	<img alt="image" border="0" height="237" src="\images\posts\4f206954-76cd-41f9-95d2-3bc4f0ae2f86\image_thumb_2.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="408" /></p>
<p>
	 </p>
<p>
	那這樣的效能差距是怎樣出來的呢？看一下BCL在列舉值ToString時所做的處理動作就可以知道了，它會額外的判斷列舉是否有標記FlagAttribute，若有的話將導到Enum.InternalFlagsFormat去處理，若無的話則用Enum.GetName。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:50da2a23-b76b-448a-b4b9-d87ee34993b2" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="c" name="code">
/// &lt;summary&gt;Converts the value of this instance to its equivalent string representation.&lt;/summary&gt;
/// &lt;returns&gt;The string representation of the value of this instance.&lt;/returns&gt;
/// &lt;filterpriority&gt;2&lt;/filterpriority&gt;
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
}</pre>
</div>
<p>
	 </p>
<p>
	所以若是列舉沒有附加FlagAttribute，其實它內部還是叫用Enum.GetName去做。那麼兩種寫法到底有什麼樣的差異呢？又為何ToString要特別去看FlagAttribute呢？這邊我們直接來看個簡易的範例就可以理解了。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:e7d78e1d-8e0c-42db-86dc-015ff9c2146f" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="c#" name="code">
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
}</pre>
</div>
<p>
	 </p>
<p>
	上面的程式運行後可得到像下面這樣的運行結果：</p>
<p>
	<img alt="image" border="0" height="256" src="\images\posts\4f206954-76cd-41f9-95d2-3bc4f0ae2f86\image_thumb_1.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="529" /></p>
<p>
	 </p>
<p>
	很明顯的在列舉沒有附加上FlagAttribute，且沒有做過or運算時，兩者運行起來的效果是一樣的。對應到相同數值的列舉值不論用ToString還是Enum.GetName都會錯亂，像是範例中的EnumItem1與EnumItem3其值都是1，用ToString或是Enum.GetName帶入EnumItem3都會得到EnumItem1。但是若是列舉有附加FlagAttribute且做了or運算，那就只有ToString可以正常運作，這也就是BCL內特別做處理的部分。</p>
<p>
	 </p>
<p>
	這篇稍稍紀錄一下兩者處理方式的差異，知道兩者的差異後，我們可以依照不同的狀況給予最適合的處理方式。</p>
