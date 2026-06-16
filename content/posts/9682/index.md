---
title: "[C#][VB.NET]擴充方法 (Extension Method)"
slug: "[CSharp][VB.NET]擴充方法 (Extension Method)"
date: "2009-07-26 02:10:46"
description: "Introduction 擴充方法(Extension Method)是.NET 3.5所提供的新語法，簡單的來說它的功能就是讓開發人員將自訂的功能加入至已定義的資料型別中。可讓您撰寫可呼叫的方法，就如同是現有型別的執行個體方法一樣。"
tags: [VB.NET, CSharp]
---

## Introduction

擴充方法(Extension Method)是.NET 3.5所提供的新語法，簡單的來說它的功能就是讓開發人員將自訂的功能加入至已定義的資料型別中。可讓您撰寫可呼叫的方法，就如同是現有型別的執行個體方法一樣。不需建立新的衍生型別 (Derived Type)、重新編譯、或是修改原始型別的程式碼。

## Support

* .NET Framework 3.5 (C# 3.0或是VB.NET 9.0都有支援)

## C#定義步驟

1. 定義靜態類別用以包含擴充方法。
2. 加入靜態方法，第一個參數會指定方法進行作業的型別，前面必須加上 this 修飾詞。

![image_thumb_14.png](/images/posts/9682/image_thumb_14.png)

**程式範例**![image_thumb.png](/images/posts/9682/image_thumb.png)

## VB.NET定義步驟

1. 建立模組存放擴充方法
2. 匯入System.Runtime.CompilerServices命名空間
3. 撰寫要加入的擴充方法以一般方式宣告方法，第一個參數的型別必須是您要擴充的資料型別、且方法前面必需加上Extension屬性。

```

```

程式範例

> 在定義擴充方法上，VB.NET與C#的寫法稍微有異。像是VB.NET的擴充方法必需寫在模組內、方法前面必需加上Extension屬性。不過基本上寫擴充方法都是要用靜態函式、第一個參數是要擴充的物件類別，其實並無太大的差異。

## 使用步驟

當幫欲擴充的類別設定完擴充方法，要使用擴充方法時只需匯入該擴充方法的命名空間，就可以像一般實體的方法一樣直接透過物件執行個體叫用。步驟如下：

1. 匯入擴充方法所在的命名空間
2. 透過被擴充的執行個體使用擴充方法

![image_thumb_13.png](/images/posts/9682/image_thumb_13.png)

簡單的使用範例如下：

**C#**

![image_thumb_2.png](/images/posts/9682/image_thumb_2.png)

**VB.NET**

![image_thumb_4.png](/images/posts/9682/image_thumb_4.png)

擴充方法也能針對列舉型別作擴充，像是：

**C#**

```csharp
enum Grade
{
    APlus,
    A,
    B,
    C,
    D
}

public static class EnumExtension
{
    public static string GetName(this Enum e)
    {
        return Enum.GetName(e.GetType(), e);
    }
}

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine(Grade.APlus.GetName());
    }
}
```

**VB.NET**

```vb
Imports System.Runtime.CompilerServices

Enum Grade
    APlus
    A
    B
    C
    D
End Enum

Module Module1
    Sub Main()
        Console.WriteLine(Grade.APlus.GetName)
    End Sub
End Module

Module EnumExtension
    <Extension()> _
    Public Function GetName(ByVal e As [Enum]) As String
        Return [Enum].GetName(e.GetType, e)
    End Function
End Module
```

值得注意的是，以往我們在使用一般實體方法時，若物件參考為NULL，則呼叫實體方法就會發生NullReferenceException的例外。而若叫用的是擴充方法，就算物件參考為NULL也能正常運作，就像下面這樣：

**C#**

```csharp
public static class EnumExtension
{
    public static bool IsNull(this string str)
    {
        return str == null;
    }
}

class Program
{
    static void Main(string[] args)
    {
        string str = null;
        Console.WriteLine(str.IsNull().ToString());
    }
}
```

**VB.NET**

```vb
Imports System.Runtime.CompilerServices

Module Module1

    Sub Main()
        Dim str As String = Nothing
        Console.WriteLine(str.IsNull().ToString())
    End Sub

End Module

Module StringExtension
    <Extension()> _
    Public Function IsNull(ByVal str As String) As Boolean
        Return str Is Nothing
    End Function
End Module
```

之所以會這樣是因為擴充方法是透過靜態方法所達成的，在編譯時編譯器自動會幫我們用對應的靜態方法呼叫來替換，因此在使用上不會有多餘的負擔，且就算物件參考為NULL，也可以呼叫擴充方法。

## 優先順序

<table border="1" cellpadding="2" cellspacing="0" width="100%"><tbody>
<tr>
<td bgcolor="#ffff00" valign="top" width="100%">
<p>下文摘自MSDN</p>
</td>
</tr>
</tbody></table>

當具有相同簽章的兩個擴充方法都在範圍內而且可存取時，將會叫用具有較高優先順序的擴充方法。擴充方法優先順序是根據用來將方法帶入範圍的機制所決定。下列清單從最高到最低，列出優先順序階層。

1. 在目前的模組內定義的擴充方法。
2. 在目前的命名空間或任何父代之資料型別內定義的擴充方法，其子命名空間的優先順序高於父代命名空間。
3. 在目前檔案之型別匯入內定義的擴充方法。
4. 在目前檔案之命名空間匯入內定義的擴充方法。
5. 在專案層級的型別匯入內定義的擴充方法。
6. 在專案層級的命名空間匯入內定義的擴充方法。

如果優先順序無法解決模稜兩可 (Ambiguity) 的問題，則可以使用完整名稱來指定您正要呼叫的方法。如果之前範例中的 Print 方法是在StringExtensions 這個模組中定義，則完整名稱為 StringExtensions.Print(example)，而不是 example.Print()。

> 簡單的說來就是當編譯器遇到方法呼叫時，會先在本身型別的方法中尋找相符項目。如果找不到相符項目，則會搜尋任何針對型別定義的擴充方法，並繫結至找到的第一個擴充方法。其搜尋的順序如上MSDN所述，當依此順序叫用到的擴充方法非所想要呼叫的話，可直接叫用該靜態方法來解決。

##

## 最佳作法

<table border="1" cellpadding="2" cellspacing="0" width="100%"><tbody>
<tr>
<td bgcolor="#ffff00" valign="top" width="100%">
<p>下文摘自MSDN</p>
</td>
</tr>
</tbody></table>

擴充方法可提供方便且功能強大的方法，讓您擴充現有的型別。不過，若要順利使用這些方法，您必須考量幾個重點。這些考量重點主要是針對類別庫的作者，但也可能影響使用擴充方法的應用程式。

一般來說，您加入至未擁有之型別的擴充方法，會比加入至所控制之型別的擴充方法來得更不安全。在您未擁有的類別中可能會發生干擾擴充方法的情形。

* 如果存在的可存取執行個體成員都具有與呼叫端陳述式之引數相容的簽章，而沒有從引數到參數所需要的縮小轉換，則擴充方法會偏好使用執行個體方法。因此，如果將適當的執行個體方法加入至類別，您所依賴的現有擴充成員可能變成無法使用。
* 擴充方法的作者無法避免其他程式設計人員撰寫相衝突的擴充方法，而這些擴充方法的優先順序甚至可能高於原始的擴充方法。
* 您可以將擴充方法放置在自己的命名空間中，即可增進其強度。您程式庫的消費者接著就能併入或排除命名空間，或者選擇程式庫中其他不同的命名空間。
* 特別在您未擁有介面或類別時，擴充介面可能比擴充類別更不安全。介面中的變更會影響實作該介面的每個類別。因此，作者較不希望在介面中加入或變更方法。不過，如果類別實作兩個介面，而這兩個介面有簽章相同的擴充方法，就看不到任一個擴充方法。
* 擴充最特定的型別。在型別階層中，如果選取會從中衍生許多其他型別的型別，則可能會引入執行個體方法的各種層面，或者其他可能與您的擴充方法相衝突的擴充方法。

## Conclusion

雖然擴充方法給予了我們許多的便利，但在使用上光擴充方法能讓我們做的我個人是覺得有限，畢竟無法做到為現有類別增加變數儲存額外資料。若能再來個擴充屬性、擴充事件，我想在使用上會更具變化的彈性。

## Link

* Huan-Lin 學習筆記-C# 筆記：擴充方法
* Sophie: KISS.NET-何謂擴充方法 (Extension method )？
* MSDN Library-擴充方法 (C# 程式設計手冊)
* MSDN Library-擴充方法 (Visual Basic)
* MSDN Library-HOW TO：實作和呼叫自訂擴充方法 (C# 程式設計手冊)
* MSDN Library-HOW TO：建立列舉型別的新方法 (C# 程式設計手冊)
* MSDN Library-HOW TO：撰寫擴充方法 (VB.NET)
* MSDN Library-HOW TO：呼叫擴充方法 (VB.NET)
* MSDN 教學短片-如何使用擴充方法替一個既存的資料型別加入自訂功能 (VB.NET)
* MSDN 教學短片-如何使用擴充方法替一個既存的資料型別加入自訂功能 (C#)
