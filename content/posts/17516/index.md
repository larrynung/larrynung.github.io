---
title: ".NET 4.0 New Feature - 程式碼合約(Code Contracts) (二) 三大合約"
date: "2010-08-31 10:44:14"
description: ".NET 4.0 New Feature - 程式碼合約(Code Contracts) (二) 三大合約"
tags: [CSharp]
---

程式碼合約內定義許多方便的合約，供開發人員能對開發的程式做些驗證，其中最重要用的也最多的莫過於下面三個合約：

1. 前置條件(Preconditions)
2. 後置條件(Postconditions)
3. 物件非變異(Object Invariants)

### 前置條件(Preconditions)

前置條件合約主要是用來驗證進入方法或是屬性時所必須滿足的需求條件，多用來判斷帶入方法或是屬性的參數值是否符合預期。使用上透過Contract.Requires方法表示，帶入所要驗證的條件就可以了。

像是若要限定帶入方法或屬性的參數x不可為空引用，可以如下撰寫：

```csharp
Contract.Requires(x != null );
```

前置條件合約除了可以帶入驗證條件外，Contract.Requires方法也具備其它多載方法，可附加帶入驗證失敗時所要顯示的訊息，或是透過泛型方法指定當驗證失敗所要丟出的例外(若未特別指定，預設是丟出ContractException例外)。

像是若要限定帶入方法或屬性的參數x不可為空引用，否則丟出ArguementNullException例外，並顯示x is null的訊息，可以如下撰寫：

```csharp
Contract.Requires(x != null, "x is null");
```

若程式中含有先前已撰寫的if-than-throw參數判斷，Code Contract也提供了Contract.EndContractBlock方法，可將其加在舊有的if-than-throw參數判斷後面，如此Code Contract即會將舊有的if-than-throw參數判斷視為前置條件合約處理。像是：

```csharp
if(x == null) throw new ArguementNullException();
Contract.EndContractBlock();
```

### 後置條件(Postconditions)

後置條件合約主要是用來驗證當跳離方法或屬性時所需滿足的需求條件，依用途不同可分為標準後置條件(Normal Postconditions) 、例外後置條件(Exceptional Postconditions)、與特殊後置條件(Special Methods within Postconditions)三種。

標準後置條件是用來驗證方法或屬性正常中止時所需滿足的需求條件，使用上透過 Contract.Ensures 方法表示，帶入所要驗證的條件就可以了。

像是若要限定方法或屬性正常離開時，其成員變數F的值必須要大於零，可以如下撰寫：

```csharp
Contract.Ensures( this .F > 0 );
```

例外後置條件是用來驗證方法或屬性在擲回特定例外狀況時所需滿足的需求條件，使用上透過Contract.EnsuresOnThrow 方法表示，像是：

```csharp
Contract.EnsuresOnThrow( this.F > 0 );
```

特殊後置條件則是指方法傳回值、前置狀態值、與輸出參數這三種輔助後置條件用的語法。

特殊後置條件中的方法傳回值指的是呼叫方法時其所要回傳給呼叫端的返回值，在無傳回值的副程式中無法使用，使用上透過Contract. Result<T>表示。像是：

```csharp
Contract.Ensures(0 < Contract.Result());
```

而特殊後置條件中的前置狀態值所要表示的是一開始進入方法或屬性的值 ，可用 Contract.OldValue<T>(T t) 表示 。像是：

```csharp
void IArray.Insert(int index, Object value){
Contract.Requires(index >= 0);
Contract.Requires(index <= ((IArray)this).Count);
Contract.Ensures(((IArray)this).Count == Contract.OldValue(((IArray)this).Count) + 1);
}
```

這段範例程式清楚的帶出了前置狀態值的用法，使用陣列個數前置狀態值跟目前的陣列個數去比對，看看兩者之間的個數是否差距一，以確保陣列元素真的有加入陣列之中。

需特別注意的是前置狀態值語法在使用上有些限制存在，像是前置狀態值不得參考方法的傳回值與用傳址方式帶入的參數：

```csharp
Contract.OldValue(Contract.Result() + x) // ERROR
```

如數量詞範圍相依於方法傳回值，前置狀態值也不得相依於數量詞的繫結變數：

```csharp
Contract. ForAll (0,Contract. Result(),i => Contract.OldValue(xs[i]) > 3 ); // ERROR
```

還有就是前置狀態值除非是當方法呼叫的索引子或引數使用，否則不得在 ForAll 或 Exists 呼叫中參考匿名委派的參數：

```csharp
Contract. ForAll (0, xs .Length, i => Contract.OldValue(xs[i]) > 3); // OK
Contract. ForAll (0, xs .Length, i => Contract.OldValue(i) > 3 ); // ERROR
```

另外如果前置狀態值的值相依於匿名委派的任何參數，除非此匿名委派是 ForAll 或 Exists 方法的引數，否則前置狀態值不得出現在匿名委派的主體中：

```csharp
Method( ... (T t) => Contract.OldValue(... t ...) ... ); // ERROR
```

至於特殊後置條件中的輸出參數，則是用來表示以傳址方式傳遞的方法參數，可用 Contract.ValueAtReturn<T>(out T t) 表示。像是：

```csharp
public void OutParam(out int x) {
Contract.Ensures(Contract.ValueAtReturn(out x) == 3);
x = 3;
}
```

### 物件非變異(Object Invariants)

物件非變異是用來描述類別執行個體總是需要滿足的不變條件，使用上只要在方法上附加ContractInvariantMethodAttribute 屬性標記，並在方法中使用Contract .Invariant方法做一連串的驗證即可。值得注意的是該方法內只能包含Invariant契约，不得包含任何其它程式碼。

舉個例子來看，若是我們需要撰寫個合約限制MyProperty永遠不得小於零，可以如下撰寫：

```csharp
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
```

這邊我們來反組譯了解一下其運作原理，反組譯後可發現Code Contract偷偷的幫我們在裡面造了兩個私有欄位<MyProperty>k\_backingField與$evaluatingInvariant$。

![clip_image002_2.jpg](/images/posts/17516/clip_image002_2.jpg)

此外，Code Contract也偷偷的幫我們把跟該屬性相關的物件非變異合約條件給放入屬性內，藉此達到物件非變異合約所要實現的功能。

```csharp
public int MyProperty
{
[CompilerGenerated]
get
{
int Contract.Result = this.k__BackingField;
if (!this.$evaluatingInvariant$)
{
__ContractsRuntime.Ensures(Contract.Result >= 0, null, "MyProperty >= 0");
}
return Contract.Result;
}
[CompilerGenerated]
set
{
if (!this.$evaluatingInvariant$)
{
__ContractsRuntime.Requires(value >= 0, null, "MyProperty >= 0");
}
this.k__BackingField = value;
if (!this.$evaluatingInvariant$)
{
}
this.$InvariantMethod$();
}
}
```

到此整個物件非變異合約的運作概念， 想必應該都非常清楚了。這邊額外再帶出一個很有趣的現象，假設今天再為上面的範例程式加一個未使用到的屬性MyProperty1：

```csharp
public int MyProperty { get; set; }
public int MyProperty1 { get; set; }
[ContractInvariantMethod]
void ObjectInvariant()
{
Contract.Invariant(MyProperty >= 0);
}
```

反組譯後可看到有趣的現象，沒用來設定物件非變異的屬性也被加入了對應的私有欄位<MyProperty1>k\_backingField。

`![image_thumb.png](/images/posts/17516/image_thumb.png)`

再看屬性內部的程式，可以發現屬性內部的程式碼也都被調整了，這表示不論屬性是否有用以設定物件非變易，所有屬性都會隨之調整。可以想見當一個類別有很多屬性時，會為所有屬性都增加對應的私有欄位，與做對應屬性程式碼的調整，額外增加的成本以目前的Code Contract來看是有點多的，希望以後這部份能再加以調整優化。

```csharp
public int MyProperty1
{
[CompilerGenerated]
get
{
int Contract.Result = this.k__BackingField;
if (!this.$evaluatingInvariant$)
{
}
return Contract.Result;
}
[CompilerGenerated]
set
{
this.k__BackingField = value;
if (!this.$evaluatingInvariant$)
{
}
this.$InvariantMethod$();
}
}
```
