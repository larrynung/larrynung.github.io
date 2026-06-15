---
title: ".NET 4.0 New Feature - 程式碼合約(Code Contracts) (三) Contract.Assert  Contract.Assume"
date: "2010-09-19 12:17:30"
description: ".NET 4.0 New Feature - 程式碼合約(Code Contracts) (三) Contract.Assert & Contract.Assume"
tags: [CSharp]
---

斷言(Assertions)合約主要用於描述某一特定程式點所需滿足的驗證條件，可透過Contract.Assert方法表示，使用上可直接帶入驗證條件：

```csharp
Contract.Assert(this.privateField > 0);
```

除了驗證條件外，斷言合約方法也可以附加帶入驗證錯誤時所要顯示的錯誤訊息。

```csharp
Contract.Assert(this.x == 3, "Why isn't the value of x 3?");
```

該合約只能運行在Debug模式，或是在設定有CONTRACTS_FULL前置編譯器的情況。

![image_thumb.png](/images/posts/17802/image_thumb.png)

方法用途跟Debug.Assert十分類似，舉凡所以可使用Debug.Assert做驗證的地方，都可以使用Contract.Assert替換。唯一的差異只在於Contract.Assert能享有Code Contract所具有的優點。

而至於假定(Assumptions)合約方法，跟Contract.Assert很類似，也是用來描述某一特定程式點所需滿足的驗證條件，可減少不必要的警告訊息。透過Contract.Assume方法表示，使用上可直接帶入驗證條件：

```csharp
Contract.Assume(this.privateField > 0);
```

或是帶入驗證條件與驗證錯誤時所要顯示的錯誤訊息：

```csharp
Contract.Assume(this.x == 3, "Static checker assumed this");
```

介紹到這邊，相信應該都還是無法區別Contract.Assert與Contract.Assume的差異。其實兩者的差異只是在於靜態分析的嚴謹程度，Contract.Assert在使用上會比Contract.Assume來得嚴謹，這邊來看段範例會更清楚些。假設我們撰寫了段程式如下：

```csharp
static void Main(string[] args)
{
   int x = CalculateSomeValues();
   Contract.Assert(x > 0);
}

public static int CalculateSomeValues()
{
    Contract.Ensures(Contract.Result<int>() > 0);
    return 1;
}
```

由於在CalculateSomeValues函式內，已經用後置條件去驗證了函式回傳值，因此在Main裡面的Contract.Assert就可以確定x變數一定會滿足驗證條件，故整個程式在做靜態分析時是會通過驗證的。

而若今天我們的函式並未用後置條件去確保有正確的函式回傳值的話，這樣的程式在Contract.Assert那段就會被檢查出有問題。因為回傳值不確定，這個Assert在靜態分析中就無法被驗證，也就無法確定x變數一定會大於零。

![image_thumb_2.png](/images/posts/17802/image_thumb_2.png)

![image_thumb_1.png](/images/posts/17802/image_thumb_1.png)

這時若仍不想為函式加入後置方法，讓整個驗證更為嚴謹的話，可以使用Contract.Assume來做驗證的動作。

![image_thumb_3.png](/images/posts/17802/image_thumb_3.png)

![image_thumb_4.png](/images/posts/17802/image_thumb_4.png)
