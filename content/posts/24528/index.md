---
title: "[C#][Visual Studio]使用DebuggerTypeProxyAttribute客製除錯資訊"
slug: "[CSharp][Visual Studio]使用DebuggerTypeProxyAttribute客製除錯資訊"
date: "2011-05-08 07:33:11"
description: "[C#][Visual Studio]使用DebuggerTypeProxyAttribute客製除錯資訊"
tags: [Visual Studio,CSharp]
---

有時候我們在撰寫類別時，因為功能上的需求有時會將類別加入許多的額外資訊，有些資訊可能在某些情況下我們必須要能夠取得並查看，但有些資訊則是在大多數的情況下不是我們所關注的焦點，尤其是在除錯時更是如此的話，會在無形之中增加除錯人員除錯上的困難，此時我們可以透過DebuggerTypeProxyAttribute為該類別客製我們所需要的除錯資訊。

	透過DebuggerTypeProxyAttribute我們可以將類別的除錯資訊精簡化，也可以為類別增添一些方便用以查閱的資訊。這樣的做法其實在BCL中也用了很多。以Hashtable類別為例，在我們監看Hashtable物件時，會看到下面的畫面。上方顯示我們使用Hashtable時所會關心的Key/Value的集合，最下面會有一個Raw View用以隱藏物件本來的除錯資訊。

	在實作上需為要客製化的類別準備一個用於顯示除錯資訊的輔助類別，該輔助類別的建購子會傳入所要客製化除錯資訊的類別物件，並用公開屬性開出所想要顯示在監看視窗中的資訊，就像下面這樣：

	    public class MyHashTableDebuggerProxy  

	    {  

	        #region Property  

	        public int Count { get; set; }  

	        #endregion

	        #region Constructor  

	        public MyHashTableDebuggerProxy(MyHashTable value)  

	        {  

	            this.Count = value.Count;  

	        }  

	        #endregion  

	    }

	最後為要客製化的類別加上DebuggerTypeProxy屬性，指定客製化資訊要由哪個輔助類別取得，整個除錯資訊的客製化就完成了。

	      [DebuggerTypeProxy(typeof(ConsoleApplication4.MyHashTableDebuggerProxy))]  

	    public class MyHashTable : Hashtable  

	    { }

	完整範例如下：

	using System;  

	using System.Diagnostics;  

	using System.Runtime.InteropServices;  

	using System.Security;  

	using System.Text;  

	using System.Collections;

	namespace ConsoleApplication4  

	{  

	    class Program  

	    {  

	        static void Main(string[] args)  

	        {  

	            MyHashTable table = new MyHashTable();  

	            table.Add("Blog", "Level Up");  

	            table.Add("Url", "http://www.dotblogs.com.tw/larrynung");  

	            Console.Read();  

	        }  

	    }

	    [DebuggerTypeProxy(typeof(ConsoleApplication4.MyHashTableDebuggerProxy))]  

	    public class MyHashTable : Hashtable  

	    { }

	    public class MyHashTableDebuggerProxy  

	    {  

	        #region Property  

	        public int Count { get; set; }  

	        #endregion

	        #region Constructor  

	        public MyHashTableDebuggerProxy(MyHashTable value)  

	        {  

	            this.Count = value.Count;  

	        }  

	        #endregion  

	    }  

	}

	運行結果如下：

## 
	Link

		DebuggerTypeProxyAttribute 類別
	
		使用 DebuggerTypeProxy 屬性