---
title: "C++_CLI Managed 與 Nativated 型態互轉"
date: "2013-11-06 12:00:00"
description: "C++_CLI Managed 與 Nativated 型態互轉"
---

<ol>
	<li>
		<p>
			CString -&gt; System::String^    </p>
		<p>
			 </p>
		<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:c6375931-9644-48df-b804-fa09a60b1d34" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
			<pre class="c" name="code">
CString strNativedMsg = _T("Test");
System::String^ strManagedMsg = %System::String(strNativedMsg);
</pre>
		</div>
		<p>
			 </p>
		<p>
			 </p>
		<p>
			 </p>
	</li>
	<li>
		System::String^ -&gt; CString
		<p>
			 </p>
		<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:ad2f36d1-9efc-420d-a956-7bc0612ae4dc" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
			<pre class="c" name="code">
System::String^ strManagedMsg = "Test";
CString strNativedMsg = (CString) strManagedMsg ;
</pre>
		</div>
		<p>
			 </p>
		<p>
			 </p>
	</li>
	<li>
		System::String^ -&gt; int
		<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:44baca9c-0fb5-4b33-b394-03fb287de55a" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
			<pre class="c" name="code">
System::String^ strManagedNumber = "123";
int nNativatedNumber = System::Convert::ToInt32(strManagedNumber );
</pre>
		</div>
	</li>
</ol>
