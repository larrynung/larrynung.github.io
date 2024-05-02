---
title: "[VC.NET] 如何修復 quot;C2039: lsquo;GetCurrentDirectoryA()rsquo; : is Not a Member of lsquo;System::IO::Directoryrsquo;quot;問題"
date: "2009-10-03 12:57:56"
description: "[VC.NET] 如何修復 &quot;C2039: &lsquo;GetCurrentDirectoryA()&rsquo; : is Not a Member of &lsquo;System::IO::Directory&rsquo;&quot;問題"
tags: [C++]
---

<p>
	看到論壇上有人問到如何處理這樣的問題。看了一下前輩的回應後才發現，原來這樣的問題是由於Windows.h檔案內，已定義了GetCurrentDirectory這個巨集所導致。該巨集會在編譯時把GetCurrentDirectory給改為GetCurrentDirectoryA或是GetCurrentDirectoryW。</p>
<div class="wlWriterEditableSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:482f9f73-a119-4c5e-9651-92461be6e310" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c:nocontrols" name="code">
#if UNICODE
#define GetCurrentDirectory GetCurrentDirectorryW
#else
#define GetCurrentDirectory GetCurrentDirectorryA
#endif</pre>
</div>
<p>
	 </p>
<p>
	因此使用類似下面的程式，在編譯時就會發生錯誤。</p>
<div class="wlWriterEditableSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:785720bb-6f35-4ee2-9df4-78bcc8fb6d62" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c:nocontrols" name="code">
#include "stdafx.h"
#include &lt;windows.h&gt;
using namespace System;
using namespace System::IO;

int main(array&lt;System::String ^&gt; ^args)
{
	Console::WriteLine(L"Dir: "+System::IO::Directory::GetCurrentDirectory()); // Error!
    return 0;
}
</pre>
</div>
<p>
	 </p>
<p>
	 </p>
<p>
	 </p>
<p>
	錯誤訊息<br />
	<img alt="image" border="0" height="73" src="\images\posts\10899\image_thumb.png" style="border-right-width: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" title="image" width="465" /></p>
<p>
	 </p>
<p>
	解決辦法可利用#undef去把該巨集給取消。</p>
<div class="wlWriterEditableSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:8740e6a8-2db0-48a1-b159-30c057f259dd" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c:nocontrols" name="code">
#undef GetCurrentDirectory</pre>
</div>
<p>
	 </p>
<p>
	 </p>
<p>
	像是</p>
<div class="wlWriterEditableSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:36509590-ef4e-49d3-a66f-00b040d98366" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c:nocontrols" name="code">
#include "stdafx.h"
#include &lt;windows.h&gt;
using namespace System;
using namespace System::IO;

#undef GetCurrentDirectory

int main(array&lt;System::String ^&gt; ^args)
{
	Console::WriteLine(L"Dir: "+System::IO::Directory::GetCurrentDirectory());
    return 0;
}
</pre>
</div>
<p>
	 </p>
<p>
	 </p>
<h2>
	Link</h2>
<ul>
	<li>
		How to Fix – "C2039: ‘GetCurrentDirectoryA()’ : is Not a Member of ‘System::IO::Directory’"</li>
</ul>
