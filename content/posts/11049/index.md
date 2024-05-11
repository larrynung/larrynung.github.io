---
title: "[C#]Effective C# 條款六： 明辨值類型與參考類型的使用場合"
slug: "[CSharp]Effective C# 條款六： 明辨值類型與參考類型的使用場合"
date: "2009-10-14 09:01:03"
description: "[C#]Effective C# 條款六： 明辨值類型與參考類型的使用場合"
tags: [CSharp]
---

<p>
	在C++中，所有類型都被定義為值類型，但可以自行選擇建立他們的參考形式；在JAVA中，所有自定義的類別都為參考類型。而在C#中，我們必須在設計類型的時候決定類型的型態。且必須清楚了解這個決定的後果，因為後期的更改會導致許多程式碼在不經意間出現錯誤。</p>
<p>
	 </p>
<p>
	值類型與參考類型的抉擇，應依照類型的責任與期望的使用方式，去選擇適合的類型。值類型不支援多型，適合儲存供應用程式操作的數據、與較小的輕量級類別。參考類型支援多型，適用於定義應用程式的行為、與建構整個類層級。</p>
<p>
	 </p>
<p>
	讓我們先來看段程式：</p>
<div class="wlWriterEditableSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:16919efb-5b5f-4661-a6ca-8a357b00c51e" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c#:nocontrols" name="code">
	private MyData _myData;
public MyData GetData()
{
    return _myData;
}

MyData data= GetData();</pre>
</div>
<p>
	 </p>
<p>
	 </p>
<p>
	 </p>
<p>
	這邊如果MyData是值類型，返回值將複製一份到data所在的空間。但是，如果MyData是參考類型，則會把內部變數的參考曝露給外界，造成外界的變動連帶影響類別內部的變數。這樣的程式具備著一定的風險，也違反了類別封裝的原則。但如果把上面代碼做點調整：</p>
<div class="wlWriterEditableSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:2d1c5263-91e3-4c47-9de6-3f16c5347fd3" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c#:nocontrols" name="code">
	private MyData _myData;
public MyData GetData()
{
    return _myData.Clone() as MyData;
}

MyData data= GetData();</pre>
</div>
<p>
	 </p>
<p>
	 </p>
<p>
	 </p>
<p>
	此時返回值將會是物件副本。雖然這麼寫可避免直接把類別的內部變數曝露給外界，但卻會產生額外不必要的負擔(複製物件與型別檢查的成本)。同樣的我們也可以改用介面來當返回值傳遞：</p>
<div class="wlWriterEditableSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:b0c6a03c-2ceb-4154-afea-d2dc9e23c105" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c#:nocontrols" name="code">
	private MyData _myData;
public IMyInterface GetData()
{
    return _myData as IMyInterface 
}

IMyInterface data= GetData();</pre>
</div>
<p>
	 </p>
<p>
	 </p>
<p>
	 </p>
<p>
	 </p>
<p>
	使用介面，可以避免直接返回內部變數，透過介面所預先定義的契約來存取控制，達到類似的效果。</p>
<p>
	 </p>
<p>
	接著我們來釐清一下不同類型在記憶體中的儲存狀態。先來看一下程式碼片段：</p>
<div class="wlWriterEditableSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:fe6276c3-2d0c-4002-9b2e-9f2498eae46a" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c#:nocontrols" name="code">
	public class C
{
    private MyType _a = new MyType();
    private MyType _b = new MyType();
}

C var = new C();</pre>
</div>
<p>
	 </p>
<p>
	如果MyType為值類型，則建置一個物件C需要一次的記憶體配置，其大小為MyType類別的兩倍大。如果是參考類型，則需要三次的記憶體配置：一次用於物件C，大小為8Byte (假設為32位元)；兩次用於物件C中所包含的MyType(_a與_b)。</p>
<p>
	 </p>
<p>
	再看一段程式碼來加深概念：</p>
<div class="wlWriterEditableSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:367bb88d-b67c-491b-b872-640c0c3ee110" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c#:nocontrols" name="code">
	MyType[] var = new MyType[100];</pre>
</div>
<p>
	 </p>
<p>
	 </p>
<p>
	如果MyType為值類型，則只需一次的記憶體配置，其大小為MyType類別的100倍大。如果為參考類型，其陣列變數宣告就需要一次記憶體配置(此時陣列成員的值仍為null)。若要初始化每個陣列元素，總共需做101次記憶體配置(陣列變數1次+陣列元素100次)。因此值類型在效能上會優於參考類型，相較於參考類型來說，也較少的零碎記憶體空間。</p>
<p>
	 </p>
<p>
	類型的抉擇是ㄧ項很重要的決定，必須在一開始就決定好。若是一開始沒有確認清楚，後續變換類型將會造成很大的影響。像是假設今天我們做一個薪資管理的程式，使用值類型來做：</p>
<div class="wlWriterEditableSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:22ff516d-ff45-4463-a97e-389a5b7e2cda" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c#:nocontrols" name="code">
	public struct Employee
{
    private string _name;
    private int _ID;
    private decimal _salary;

    public void Pay(BankAccount b)
    {
        b.Balance -= _salary;
    }
}</pre>
</div>
<p>
	 </p>
<p>
	 </p>
<p>
	而後來由於需求變更，我們希望系統能提供不同種類的員工，因此把它改為參考類型：</p>
<div class="wlWriterEditableSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:2306668c-7e6b-4c01-9f2e-5805ac66a4d5" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c#:nocontrols" name="code">
	public class Employee
{
    private string _name;
    private int _ID;
    private decimal _salary;

    public void Pay(BankAccount b)
    {
        b.Balance -= _salary;
    }
}</pre>
</div>
<p>
	 </p>
<p>
	 </p>
<p>
	 </p>
<p>
	這樣一改，本來系統的程式可能就會出錯。像下面這段程式碼，就會從一次性獎金發放，變為永久性的調薪。</p>
<div class="wlWriterEditableSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:15a182e6-38b6-4f53-a685-7edc8c53a71a" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c#:nocontrols" name="code">
	Employee e = Employees.Find("CEO");
e.Salary += Bonus;
e.Pay(CEOBankAccount);</pre>
</div>
<p>
	 </p>
<p>
	 </p>
<p>
	 </p>
<p>
	總體來說，值類型在記憶體的管理上具有較好的效率：較少的零碎空間，較少的記憶體垃圾，以及較少的間接存取。更重要的是，值類型傳遞的是物件副本,可避免內部成員的參考曝露給外界的風險。而其缺點在於只具有有限的物件導向特性，少了繼承的特性。</p>
<p>
	 </p>
<p>
	作者在這邊也提出了值類型的判斷依據，供大家參考。如果以下問題都是Yes，則應該使用值類型。</p>
<ol>
	<li>
		該類型的主要職責是否用於儲存數據？</li>
	<li>
		該類型的公用接口是否完全由一些數據成員存取屬性定義？</li>
	<li>
		是否確信該類型永遠不會有子類別？</li>
	<li>
		是否確信該類型永遠不可能具有多型？</li>
</ol>
