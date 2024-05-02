---
title: "[C++][Visual Studio]Natived C++使用Visual Studio做單元測試"
date: "2011-08-18 01:19:50"
description: "[C++][Visual Studio]Natived C++使用Visual Studio做單元測試"
tags: [Visual Studio,C++]
---

<p>
	筆者在前面[C++]使用靜態函式庫(Static Library)開出類別給其他組件使用這篇帶出了如何將C++的類別開出給其他組件使用，這篇將延伸該篇概念，示範如何針對Natived C++去做Visual Studio的單元測試。</p>
<p>
	 </p>
<p>
	為了方便測試，這邊將[C++]使用靜態函式庫(Static Library)開出類別給其他組件使用這篇的範例程式改了一下，將本來的Test方法改為Add方法，其功能為將兩個數值相加後回傳。</p>
<p>
	<img alt="image" border="0" height="249" src="\images\posts\33415\image_thumb.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="243" /></p>
<p>
	 </p>
<p>
	接著為方案加入Test Project。</p>
<p>
	<img alt="image" border="0" height="446" src="\images\posts\33415\image_thumb_1.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="644" /></p>
<p>
	 </p>
<p>
	再來可參閱[C++]使用靜態函式庫(Static Library)開出類別給其他組件使用這篇，設定測試專案的屬性，讓測試專案得以引用要測試的組件。</p>
<p>
	<img alt="image" border="0" height="436" src="\images\posts\33415\image_thumb_2.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="644" /></p>
<p>
	<img alt="image" border="0" height="436" src="\images\posts\33415\image_thumb_3.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="644" /></p>
<p>
	 </p>
<p>
	都設定完後就可以在測試專案中撰寫測試程式了 ，測試程式的撰寫方式跟一般的.NET程式無太大的差異，惟需注意的是撰寫測試程式所用到的Assert</a>主要是Managed的類別，整個測試專案也是C++/CLI類型的專案，因此若想要判別的結果其型態非Managed與Natived共用的話，我們必須將Natived的型態的資料轉為Managed型態的資料，再將其帶入<a href="http://msdn.microsoft.com/zh-tw/library/microsoft.visualstudio.testtools.unittesting.assert(VS.80).aspx" target="_blank">Assert去比對。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:8e9985d8-eadf-4f9f-a98f-d134cd27dc88" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c" name="code">
#include "stdafx.h"
#include "MyClass.h"
...
namespace MyDllTest
{
	[TestClass]
	public ref class UnitTest1
	{
	...
		[TestMethod]
		void Add_AddTwoValue_ReturnAddedValue()
		{			
			//Arrange		
			int x = 1;
			int y = 2;
			int actual;
			int expected = x + y;
			MyClass myObj;
			
			//Act
			actual = myObj.Add(x, y);	

			//Assert
			Assert::AreEqual(actual, expected);		
		};
	};
}
</pre>
</div>
<p>
	 </p>
<p>
	因為這邊示範的是int型態，int型態為Natived與Managed共用的型態，因此這邊可以直接帶入使用，若型態是用std::string的話，就必須要像下面這樣轉換。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:4068c118-b9ac-4101-a4ee-3ded94b3e791" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c" name="code">
...
System::String^ GetManagedString(string nativedString)
{
	return %System::String(nativedString.c_str());
}
...
Assert::AreEqual(GetManagedString(actual),GetManagedString(expected));</pre>
</div>
<p>
	 </p>
<p>
	除了在比對上要特別留意外，其他的部分像是如何進行測試與單元測試的管理都跟Managed的單元測試大同小異，這邊不對此多做說明。</p>
<p>
	<img alt="image" border="0" height="503" src="\images\posts\33415\image_thumb_6.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="580" /></p>
<p>
	<img alt="image" border="0" height="130" src="\images\posts\33415\image_thumb_7.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="494" /></p>
<p>
	 </p>
<h2>
	Link</h2>
<ul>
	<li>
		Assert 類別</li>
</ul>
