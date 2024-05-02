---
title: "CA1810_ Initialize reference type static fields inline"
date: "2013-11-06 12:00:00"
description: "CA1810_ Initialize reference type static fields inline"
---

<p>
	筆者常常會用些工具去輔助找出程式美中不足的地方，像是FxCop分析出來的結果，在效能方面的Rule就是筆者必看的項目。但是筆者一直以來都沒有深究某些規則，像是CA1810: Initialize reference type static fields inline這個效能規則為甚麼要這麼做？而它的重要程度又為什麼會可以佔到90%？</p>
<p>
	 <img alt="image" border="0" height="484" src="\images\posts\e9b4d162-717f-4fa6-9f6d-48bdcd8ae97e\image_thumb_2.png" style="border-left-width: 0px; border-right-width: 0px; border-bottom-width: 0px; border-top-width: 0px" width="622" /></p>
<p>
	 </p>
<p>
	這邊筆者實際撰寫了個簡單的程式下去測試：</p>
<p>
	 </p>
<script src="\images\posts\e9b4d162-717f-4fa6-9f6d-48bdcd8ae97e\5509011.js"></script>
<p>
	 </p>
<p>
	 </p>
<p>
	運行起來我們可以看到像是下面這樣的結果，注意到這邊有個有趣的現象，就是Class1.TimeStamp的初始會比顯示的時間來的早。</p>
<p>
	<img alt="image" border="0" height="208" src="\images\posts\e9b4d162-717f-4fa6-9f6d-48bdcd8ae97e\image_thumb.png" style="border-left-width: 0px; border-right-width: 0px; border-bottom-width: 0px; border-top-width: 0px" width="497" /></p>
<p>
	 </p>
<p>
	為了探討這樣的問題，我們將上面的程式反組譯成MSIL。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:bdd98c05-7d15-4dfc-8e79-a91bcc6359fe" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="xml" name="code">
.namespace ConsoleApplication43
{
	.class private auto ansi beforefieldinit ConsoleApplication43.Class1
		extends [mscorlib]System.Object
	{
		// Fields
		.field public static valuetype [mscorlib]System.DateTime TimeStamp

		// Methods
		.method public hidebysig specialname rtspecialname 
			instance void .ctor () cil managed 
		{
			// Method begins at RVA 0x20e6
			// Code size 7 (0x7)
			.maxstack 8

			IL_0000: ldarg.0
			IL_0001: call instance void [mscorlib]System.Object::.ctor()
			IL_0006: ret
		} // end of method Class1::.ctor

		.method private hidebysig specialname rtspecialname static 
			void .cctor () cil managed 
		{
			// Method begins at RVA 0x20da
			// Code size 11 (0xb)
			.maxstack 8

			IL_0000: call valuetype [mscorlib]System.DateTime [mscorlib]System.DateTime::get_Now()
			IL_0005: stsfld valuetype [mscorlib]System.DateTime ConsoleApplication43.Class1::TimeStamp
			IL_000a: ret
		} // end of method Class1::.cctor

	} // end of class ConsoleApplication43.Class1

	.class private auto ansi ConsoleApplication43.Class2
		extends [mscorlib]System.Object
	{
		// Fields
		.field public static valuetype [mscorlib]System.DateTime TimeStamp

		// Methods
		.method private hidebysig specialname rtspecialname static 
			void .cctor () cil managed 
		{
			// Method begins at RVA 0x20ee
			// Code size 12 (0xc)
			.maxstack 8

			IL_0000: nop
			IL_0001: call valuetype [mscorlib]System.DateTime [mscorlib]System.DateTime::get_Now()
			IL_0006: stsfld valuetype [mscorlib]System.DateTime ConsoleApplication43.Class2::TimeStamp
			IL_000b: ret
		} // end of method Class2::.cctor

		.method public hidebysig specialname rtspecialname 
			instance void .ctor () cil managed 
		{
			// Method begins at RVA 0x20fb
			// Code size 7 (0x7)
			.maxstack 8

			IL_0000: ldarg.0
			IL_0001: call instance void [mscorlib]System.Object::.ctor()
			IL_0006: ret
		} // end of method Class2::.ctor

	} // end of class ConsoleApplication43.Class2

	.class private auto ansi beforefieldinit ConsoleApplication43.Program
		extends [mscorlib]System.Object
	{
		// Methods
		.method private hidebysig static 
			void Main (
				string[] args
			) cil managed 
		{
			// Method begins at RVA 0x2050
			// Code size 118 (0x76)
			.maxstack 1
			.entrypoint
			.locals init (
				[0] valuetype [mscorlib]System.DateTime CS$0$0000
			)

			IL_0000: nop
			IL_0001: ldc.i4 1000
			IL_0006: call void [mscorlib]System.Threading.Thread::Sleep(int32)
			IL_000b: nop
			IL_000c: call valuetype [mscorlib]System.DateTime [mscorlib]System.DateTime::get_Now()
			IL_0011: stloc.0
			IL_0012: ldloca.s CS$0$0000
			IL_0014: constrained. [mscorlib]System.DateTime
			IL_001a: callvirt instance string [mscorlib]System.Object::ToString()
			IL_001f: call void [mscorlib]System.Console::WriteLine(string)
			IL_0024: nop
			IL_0025: ldsflda valuetype [mscorlib]System.DateTime ConsoleApplication43.Class1::TimeStamp
			IL_002a: constrained. [mscorlib]System.DateTime
			IL_0030: callvirt instance string [mscorlib]System.Object::ToString()
			IL_0035: call void [mscorlib]System.Console::WriteLine(string)
			IL_003a: nop
			IL_003b: ldc.i4 1000
			IL_0040: call void [mscorlib]System.Threading.Thread::Sleep(int32)
			IL_0045: nop
			IL_0046: call valuetype [mscorlib]System.DateTime [mscorlib]System.DateTime::get_Now()
			IL_004b: stloc.0
			IL_004c: ldloca.s CS$0$0000
			IL_004e: constrained. [mscorlib]System.DateTime
			IL_0054: callvirt instance string [mscorlib]System.Object::ToString()
			IL_0059: call void [mscorlib]System.Console::WriteLine(string)
			IL_005e: nop
			IL_005f: ldsflda valuetype [mscorlib]System.DateTime ConsoleApplication43.Class2::TimeStamp
			IL_0064: constrained. [mscorlib]System.DateTime
			IL_006a: callvirt instance string [mscorlib]System.Object::ToString()
			IL_006f: call void [mscorlib]System.Console::WriteLine(string)
			IL_0074: nop
			IL_0075: ret
		} // end of method Program::Main

		.method public hidebysig specialname rtspecialname 
			instance void .ctor () cil managed 
		{
			// Method begins at RVA 0x20d2
			// Code size 7 (0x7)
			.maxstack 8

			IL_0000: ldarg.0
			IL_0001: call instance void [mscorlib]System.Object::.ctor()
			IL_0006: ret
		} // end of method Program::.ctor

	} // end of class ConsoleApplication43.Program

}</pre>
</div>
<p>
	 </p>
<p>
	這邊要先說明一下，在.Net裡面有所謂的物件建構函式(.ctor)與型別建構函式(.cctor)。物件建構函式就是我們一般說的建構子，會在建立物件實體時被叫用，用於執行對成員變數的初始化。而型別建構函式則是在類別中有靜態成員變數或是有靜態建構函式時被叫用，用於執行對靜態成員的初始化。</p>
<p>
	 </p>
<p>
	我們可以從上面反組譯出來的MSIL中發現，Class1雖然沒有撰寫靜態建構函式，但是卻有靜態成員變數，且有為其做初始設定。所以這邊程式在編譯後會隱含建立.cctor，用以處理靜態成員變數的初始化。另外注意到MSIL中類別宣告的部分，這邊會被標註一個beforefieldinit旗標，表示這個類別是依據beforefieldinit方式運行，JIT看到beforefieldinit這個旗標後就會知道該方法是不需要檢查靜態建構函式的，藉此避免不必要的性能耗費。而靜態成員的初始設定系統會選擇在最適當的時候執行，實際運行的時間我們無法很精確的掌握，且不保證會在叫用靜態方法或執行個體建構函式之前運行，但系統會確保在實際需要存取靜態欄位前一定會被初始。</p>
<p>
	 </p>
<p>
	而Class2因為有明確的在類別中撰寫靜態建構函式，所以MSIL很精確的建立.cctor，MSIL中類別宣告的部分不會標註beforefieldinit旗標，表示這個類別是依據precise方式運行，靜態成員變數的初始化動作會在對類別成員進行存取時叫用。</p>
<p>
	 </p>
<p>
	除了上面的差異外，注意到Class1與Class2兩者的.cctor還有些許的差異，相較起來採用precise這種方式的.cctor會多一個nop的IL指令。</p>
<p>
	 </p>
<p>
	所以盡量用inline的方式去初始靜態成員變數，避免不必要的靜態建構函式，讓程式採用beforefieldinit運行方式，由系統決定最佳的初始化時機 ，可以取得較佳的效能。</p>
<p>
	 </p>
<p>
	最後來做個簡易的效能測試：</p>
<script src="\images\posts\e9b4d162-717f-4fa6-9f6d-48bdcd8ae97e\5517705.js"></script>
<p>
	 </p>
<p>
	運行結果如下：</p>
<p>
	<img alt="image" border="0" height="192" src="\images\posts\e9b4d162-717f-4fa6-9f6d-48bdcd8ae97e\image_thumb_1.png" style="border-left-width: 0px; border-right-width: 0px; border-bottom-width: 0px; border-top-width: 0px" width="385" /></p>
<p>
	 </p>
<p>
	應該不難看出確實有些影響...</p>
<p>
	 </p>
<h2>
	Link</h2>
<ul>
	<li>
		CA1810: Initialize reference type static fields inline</li>
	<li>
		C#捷徑編程筆記6</li>
	<li>
		關於Type Initializer和BeforeFieldInit的問題，看看大家能否給出正確的解釋</li>
	<li>
		Class|Static Constructor and BeforeFieldInit</li>
	<li>
		關於靜態構造函數和BeforeFieldInit</li>
	<li>
		[你必須知道的.NET]第二十三回：品味細節，深入.NET的類型構造器</li>
	<li>
		對beforefieldinit的理解</li>
	<li>
		C# 型別初始式(Type Initializer) .cctor - 我的Coding之路- 點部落</li>
</ul>
