---
title: ".NET 4.0 New Feature - 程式碼合約(Code Contracts) (二) 三大合約"
date: "2010-08-31 10:44:14"
description: ".NET 4.0 New Feature - 程式碼合約(Code Contracts) (二) 三大合約"
tags: [CSharp]
---程式碼合約內定義許多方便的合約，供開發人員能對開發的程式做些驗證，其中最重要用的也最多的莫過於下面三個合約：
前置條件(Preconditions) 後置條件(Postconditions) 物件非變異(Object Invariants)

### 前置條件(Preconditions)

前置條件合約主要是用來驗證進入方法或是屬性時所必須滿足的需求條件，多用來判斷帶入方法或是屬性的參數值是否符合預期。使用上透過Contract.Requires方法表示，帶入所要驗證的條件就可以了。

像是若要限定帶入方法或屬性的參數x不可為空引用，可以如下撰寫：

Contract.Requires(x != null );

前置條件合約除了可以帶入驗證條件外，Contract.Requires方法也具備其它多載方法，可附加帶入驗證失敗時所要顯示的訊息，或是透過泛型方法指定當驗證失敗所要丟出的例外(若未特別指定，預設是丟出ContractException例外)。

像是若要限定帶入方法或屬性的參數x不可為空引用，否則丟出ArguementNullException例外，並顯示x is null的訊息，可以如下撰寫：

Contract.Requires(x != null, "x is null");

若程式中含有先前已撰寫的if-than-throw參數判斷，Code Contract也提供了Contract.EndContractBlock方法，可將其加在舊有的if-than-throw參數判斷後面，如此Code Contract即會將舊有的if-than-throw參數判斷視為前置條件合約處理。像是：

if(x == null) throw new ArguementNullException();
Contract.EndContractBlock();

### 後置條件(Postconditions)

後置條件合約主要是用來驗證當跳離方法或屬性時所需滿足的需求條件，依用途不同可分為標準後置條件(Normal Postconditions) 、例外後置條件(Exceptional Postconditions)、與特殊後置條件(Special Methods within Postconditions)三種。

標準後置條件是用來驗證方法或屬性正常中止時所需滿足的需求條件，使用上透過 Contract.Ensures 方法表示，帶入所要驗證的條件就可以了。

像是若要限定方法或屬性正常離開時，其成員變數F的值必須要大於零，可以如下撰寫：

Contract.Ensures( this .F > 0 );

例外後置條件是用來驗證方法或屬性在擲回特定例外狀況時所需滿足的需求條件，使用上透過Contract.EnsuresOnThrow 方法表示，像是：

Contract.EnsuresOnThrow( this.F > 0 );

特殊後置條件則是指方法傳回值、前置狀態值、與輸出參數這三種輔助後置條件用的語法。

特殊後置條件中的方法傳回值指的是呼叫方法時其所要回傳給呼叫端的返回值，在無傳回值的副程式中無法使用，使用上透過Contract. Result表示。像是：

Contract.Ensures(0 ());

而特殊後置條件中的前置狀態值所要表示的是一開始進入方法或屬性的值 ，可用 Contract.OldValue(T t) 表示 。像是：

void IArray.Insert(int index, Object value){
Contract.Requires(index >= 0);
Contract.Requires(index () + x) // ERROR

如數量詞範圍相依於方法傳回值，前置狀態值也不得相依於數量詞的繫結變數：                               

Contract. ForAll (0,Contract. Result(),i => Contract.OldValue(xs[i]) > 3 ); // ERROR

還有就是前置狀態值除非是當方法呼叫的索引子或引數使用，否則不得在 ForAll 或 Exists 呼叫中參考匿名委派的參數：                               

Contract. ForAll (0, xs .Length, i => Contract.OldValue(xs[i]) > 3); // OK
Contract. ForAll (0, xs .Length, i => Contract.OldValue(i) > 3 ); // ERROR

另外如果前置狀態值的值相依於匿名委派的任何參數，除非此匿名委派是 ForAll 或 Exists 方法的引數，否則前置狀態值不得出現在匿名委派的主體中：

Method( ... (T t) => Contract.OldValue(... t ...) ... ); // ERROR

至於特殊後置條件中的輸出參數，則是用來表示以傳址方式傳遞的方法參數，可用 Contract.ValueAtReturn(out T t) 表示。像是：

public void OutParam(out int x) {
Contract.Ensures(Contract.ValueAtReturn(out x) == 3);
x = 3;
}

### 物件非變異(Object Invariants)

物件非變異是用來描述類別執行個體總是需要滿足的不變條件，使用上只要在方法上附加ContractInvariantMethodAttribute 屬性標記，並在方法中使用Contract .Invariant方法做一連串的驗證即可。值得注意的是該方法內只能包含Invariant契约，不得包含任何其它程式碼。

舉個例子來看，若是我們需要撰寫個合約限制MyProperty永遠不得小於零，可以如下撰寫：

public int MyProperty { get; set; }

[ContractInvariantMethod]
void ObjectInvariant()
{
Contract.Invariant(MyProperty >= 0);
}
public int MyProperty { get; set; }

[ContractInvariantMethod]
void ObjectInvariant()
{
Contract.Invariant(MyProperty >= 0);
}

這邊我們來反組譯了解一下其運作原理，反組譯後可發現Code Contract偷偷的幫我們在裡面造了兩個私有欄位k_backingField與$evaluatingInvariant$。
<img src="\images\posts\17516