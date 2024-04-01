---
title: "[Visual Studio][C#].NET 4.5 New Feature - Caller Information"
date: "2013-11-06 12:00:00"
description: "[Visual Studio][C#].NET 4.5 New Feature - Caller Information"
tags: [CSharp]
---

<p>
	Caller Information是.NET 4.5的新功能，它能在編譯時為我們提供些額外的資訊給副程式，像是被哪個方法叫用、叫用的方法所在的檔案位置、以及程式碼行數，我們可以用這些額外的資訊提供Log更為詳細的資訊，再也不需要用StackTrace來提供這些資訊了，不僅簡單，在效能上也會因此提升，此外也可以避免實作INotifyPropertyChanged時用字串處理把程式寫的太死，造成後續重構時重新命名有所遺漏，導致整個程式運作不如預期。</p>
<p>
	 </p>
<p>
	Caller Information在使用上很簡單，我們只要為方法中加入對應的選擇性參數，並在選擇性參數前加入對應的Attribute就可以了，像是CallerMemberNameAttribute可以提供呼叫的方法，CallerFileNameAttribute可以提供呼叫的方法所在的檔案位置，CallerLineNumberAttribute則是提供呼叫的方法所在的行數。我們可以看下下面的簡易範例：</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:0e7f327f-f46a-42ec-9394-cd6bc5cd6cd3" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c#" name="code">
        private void TraceMessage(string message,
            [CallerMemberName] string memberName = "",
            [CallerFilePath] string sourceFilePath = "",
            [CallerLineNumber] int sourceLineNumber = 0)
        {
            Console.WriteLine("message: " + message);
            Console.WriteLine("member name: " + memberName);
            Console.WriteLine("source file path: " + sourceFilePath);
            Console.WriteLine("source line number: " + sourceLineNumber);
        }</pre>
</div>
<p>
	 </p>
<p>
	使用上我們可以撰寫像下面這樣的程式呼叫上面的提到的方法，這邊只填入必要參數：</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:ce056ef8-0615-435c-afde-4a07e0dbb300" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c#" name="code">
        public CallerTestClass()
        {
            TraceMessage("Constructor");
        }</pre>
</div>
<p>
	 </p>
<p>
	運行起來會像下面這樣子，可以看到呼叫的方法名稱、檔案位置、行數都正確的顯示了。</p>
<p>
	<img alt="image" border="0" height="84" src="\images\posts