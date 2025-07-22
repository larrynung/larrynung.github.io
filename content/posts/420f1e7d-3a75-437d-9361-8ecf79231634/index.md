---
title: ".NET 4.0 New Feature - 程式碼合約(Code Contracts) (一) 概念與簡介"
date: "2013-11-06 12:00:00"
description: ".NET 4.0 New Feature - 程式碼合約(Code Contracts) (一) 概念與簡介"
tags: [CSharp]
---程式碼合約(Code Contracts)是.NET Framework 4.0的新功能，它是微軟對契約式編程(Design by contract)概念所提出的一種解決方案，主要由前置條件(Preconditions)、後置條件(Postconditions)、與物件非變異(Object Invariants)這三大契約所構成，可以很容易的為程式碼加入驗證程式碼，降低程式的錯誤發生率，提高程式的品質，也可以整合單元測試，減少單元測試的工作量，甚至整合文件產生器，讓產出的程式文檔更為詳細。

在使用程式碼合約前，首先我們需先至Contracts - Microsoft Research下載並安裝Code Contract套件，才可以啟用Code Contract功能，這是因為Code Contract套件包內除了會附上一些文件、範例、Visual Studio外掛外，還會附含二進位重寫器CCRewrite。

其中Visual Studio外掛可在Visual Studio屬性頁設定Code Contract參數，決定是否啟用執行階段驗證、是否啟用靜態驗證、Code Contract啟用範圍、與一些相關的設定。

至於二進位重寫器CCRewrite則是整個執行階段驗證的核心，能動態對組件進行調整，達到執行階段驗證的功能。

這邊來看個例子會更為清楚。我們撰寫了一道方法如下：

void Test(List array, int index, object value)
{
Contract.Requires(index >= 0);
Contract.Ensures(array.Count == Contract.OldValue(array.Count) + 1);
array.Insert(index, value);
}

方法中內含前置條件與後置條件，編譯後用Reflactor開啟，可發現方法在有啟動Code Contract執行階段驗證的情況下，程式碼會被改為如下這般：

private void Test(List array, int index, object value)
{
List Contract.Old(array);
int Contract.Old(Count);
__ContractsRuntime.Requires(index >= 0, null, "index >= 0");
try
{
Contract.Old(array) = array;
}
catch (Exception exception1)
{
if (exception1 == null)
{
throw;
}
}
try
{
Contract.Old(Count) = array.Count;
}
catch (Exception exception2)
{
if (exception2 == null)
{
throw;
}
}
array.Insert(index, value);
if (__ContractsRuntime.insideContractEvaluation <= 4)
{
try
{
__ContractsRuntime.insideContractEvaluation++;
__ContractsRuntime.Ensures(Contract.Old(array).Count == (Contract.Old(Count) + 1), null, "array.Count == Contract.OldValue(array.Count) + 1");
}
finally
{
__ContractsRuntime.insideContractEvaluation--;
}
}
}

從上面這段範例就可以很清楚的了解到，當啟用了Code Contract執行階段驗證，Code Contract套件包內含的二進位重寫器CCRewrite會偷偷的在程式碼編譯過後依合約的不同進行對應的微調，像是紀錄進入方法與屬性當下的初始值，與調換驗證合約至正確的位置等。

## 組件

程式碼合約雖是.NET Framework 4.0的新功能，但其實只是在4.0以後把它從Microsoft Research專案給整合到.NET Framework中，因此要在.NET Framework 4.0以前使用仍舊是可以的，但需注意到在不同環境條件下，我們必需參考使用不同的組件。
環境 參考組件 .NET Framework 4.0以前 %PROGRAMFILES%/Microsoft/Contracts/PublicAssemblies/Microsoft.Contracts.dll .NET Framework 4.0以後 已含進mscorlib.dll中，無需特別加入參考。 Windows Phone 7 %PROGRAMFILES%/Microsoft/Contracts/PublicAssemblies/Silverlight3/Microsoft.Contracts.dll

## 命名空間

System.Diagnostics.Contracts

## 功能

使用Code Contracts主要可讓我們享有下列四項特點：
提升自動測試程度 靜態驗證 執行階段驗證 文件產生

### 提升自動測試程度
使用有支援Code Contracts的自動測試程式，可依照程式中的Code Contracts設定，自動產生出有意義的單元測試，減少單元測試撰寫的工作量 。像是微軟的Pex就是有支援Code Contracts的自動測試程式，有興趣的可以到Pex for fun網站進行體驗，該網站允許使用者自行撰寫程式，或是使用網站上現有的程式範例來做測試(可透過點選左上方的[Show Anothor Puzzle]按鈕切換程式範例)。只要選取完要使用的語言，程式準備妥當後按下[Ask Pex!]按鈕，下方即會顯示偵測到要用來帶入測試的數值與預期結果，再進一步點選，可在下方看到產生的單元測試程式碼。

### 靜態驗證

靜態驗證功能只在專業版的Code Contract才支援。該功能能在編譯階段檢查隱含合約及明確合約，可判斷合約違規與否，甚至進一步給予建議。

像下圖就是啟動了隱含合約的靜態檢查功能，Code Contract會在編譯時偵測程式，並在輸出對話框建議要加上判別是否為空引用或是參數範圍檢查之類的前置條件。
<img src="\images\posts\420f1e7d-3a75-437d-9361-8ecf79231634