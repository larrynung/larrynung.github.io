---
title: "PostSharp - Contract Inheritance"
date: "2015-02-08 16:17:00"
description: "PostSharp - Contract Inheritance"
tags: [PostSharp]
---


PostSharp 的 Contract 跟 Conde Contract 一樣，具備可被繼承的特性。凡是套用在 abstract、virtual、或 interface 方法上的 Contract，其子類別都會繼承到，在開發上十分的好用。  

<!-- More -->

<br/>


這邊來看個例子，筆者撰寫了個 IWritable 的介面，在其 Write 方法上我們加上了 RequiredAttribute，再建立個 Blog 類別去實作該介面。    

```c# 
Using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using PostSharp.Patterns.Contracts;

namespace ConsoleApplication1
{
	class Program
	{
		static void Main(string[] args)
		{
			IWriteable blog = new Blog("LevelUp", "http://larrynung.github.io");
			blog.Write("PostSharp Contract Inheritance", "Hello~Contract");
			blog.Write("", "");
		}
	}

	public interface IWritable
	{
		void Write([Required]string title, string content);
	}

	public class Blog : IWritable
	{
		public string Name
		{
			get;
			set;
		}

		public string Url
		{
			get;
			set;
		}

		public Blog(string name, string url)
		{
			this.Name = name;
			this.Url = url;
		}

		public void Write(string title, string content)
		{
			Console.WriteLine(String.Format("== {0} =={1}{2}", title, Environment.NewLine, content));
		}
	}
}
```


<br/>


當我們呼叫 Blog.Write 時，因為 Blog 類別從 IWritable 介面繼承了 Write 方法及其 Contract，所以叫用時若帶的是空值就會丟出例外。  

{% img /images/posts/PostSharpContractInheritance/1.png %}

<br/>


Link
----
* [Contracts](http://doc.postsharp.net/contracts)
