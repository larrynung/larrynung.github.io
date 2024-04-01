---
title: "[C++][Visual Studio]Visual studio 2010 C++0x new feature: nullptr"
date: "2011-08-24 01:01:59"
description: "[C++][Visual Studio]Visual studio 2010 C++0x new feature: nullptr"
tags: [Visual Studio,C++]
---

<p>
	Visual studio 2010為C++的開發人員新增了nullptr這個C++0x的功能，用以表示空的指標位置，取代原先我們所使用的NULL，將空指標和整數0 的概念拆開，會有這樣的功能提出是因為以前用NULL來做空指標的處理時，由於NULL的定義為整數0，並非是真的空指標型態，所以在某些特定的狀況下使用會錯亂。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:f4650509-722b-4006-9676-bd7d8f15c18d" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c" name="code">
/* Define NULL pointer value */
#ifndef NULL
#ifdef __cplusplus
#define NULL    0
#else
#define NULL    ((void *)0)
#endif
#endif</pre>
</div>
<p>
	 </p>
<p>
	像是下面這個範例帶入NULL，我們預期運行到參數為int*型態的多載方法。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:4d4a3343-ffe7-48c6-8172-3ca130c2eedd" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c" name="code">
...
void Test(int* value)
{
	cout &lt;&lt; "void Test(int* value)";
}

void Test(int value)
{
	cout &lt;&lt; "void Test(int value)";
}

int _tmain(int argc, _TCHAR* argv[])
{	
	Test(NULL);
	return 0;
}</pre>
</div>
<p>
	 </p>
<p>
	但在運行後卻發現他進入的是參數型態為int的多載方法，整個運行不如我們所預期。</p>
<p>
	<img alt="image" border="0" height="175" src="\images\posts\34077\image_thumb.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="441" /></p>
<p>
	 </p>
<p>
	要將運行導回正確的多載方法，我們必須自行做些額外的轉換動作，將NULL轉型為預期的型態再帶入方法叫用。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:fed67ec7-1c87-4a59-80d7-3dc05a374a4b" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c" name="code">
Test((int*)NULL);</pre>
</div>
<p>
	<img alt="image" border="0" height="143" src="\images\posts\34077\image_thumb_1.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="425" /></p>
<p>
	 </p>
<p>
	在VS2010由於支援了C++0x的nullptr，可以直接用nullptr來取代NULL。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:5bb05626-7396-4a22-b08d-0aa44599d59f" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c" name="code">
Test(nullptr);</pre>
</div>
<p>
	 </p>
<p>
	完整的範例如下：</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:fbebf8b6-6dc2-412c-a654-2208cedd95cb" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c" name="code">
// test auto.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include &lt;iostream&gt;

using namespace std;

void Test(int* value)
{
	cout &lt;&lt; "void Test(int* value)
";
}

void Test(int value)
{
	cout &lt;&lt; "void Test(int value)
";
}

int _tmain(int argc, _TCHAR* argv[])
{	
	Test(NULL);
	Test((int*)NULL);
	Test(nullptr);
	return 0;
}</pre>
</div>
<p>
	 </p>
<p>
	運行結果如下：</p>
<p>
	<img alt="image" border="0" height="191" src="\images\posts\34077\image_thumb_2.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="369" /></p>
<p>
	 </p>
<h2>
	Link</h2>
<ul>
	<li>
		C++0x：static_assert 和 nullptr</li>
	<li>
		C++0x features in VC2010 - nullptr</li>
	<li>
		C++0x: nullptr</li>
	<li>
		C++0x：static_assert 和 nullptr</li>
	<li>
		C++0x - nullptr</li>
</ul>
