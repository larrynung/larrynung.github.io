---
title: "[C#]Effective C# 條款九： 理解幾個相等判斷之間的關係"
slug: "[CSharp]Effective C# 條款九： 理解幾個相等判斷之間的關係"
date: "2009-10-21 08:27:25"
description: "[C#]Effective C# 條款九： 理解幾個相等判斷之間的關係"
tags: [CSharp]
---

C#提供了四種不同的函式來判斷兩個物件是否相等：

1.ReferenceEquals靜態方法

```csharp
public static bool ReferenceEquals(object left, object right);
```

2.Equals靜態方法

```csharp
public static bool Equals(object left,object right);
```

3.Equals方法

```csharp
public virtual bool Equals(object right);
```

4.運算子==

```csharp
public static bool operator== (MyClass object,MyClass right);
```

前兩個靜態方法我們永遠都不應該去重新定義，後兩個則可視需要去重新定義。

以ReferenceEquals來說，其功能為判斷兩個變數指標是否指向同一物件。也就是判斷兩者的物件參考是否相同。如果兩個指標所指的是同一物件的話，則該方法會返回True值。反之，則傳回False。若是以值類別來看，以ReferenceEquals來比較兩個值類別。或是將一個值類別與自身進行比較。其值皆為False。對於ReferenceEquals來說，.預設的功能已經把該方法該有的功能做得很好了，因此我們不需要對此重新定義。

而Object.Equals靜態方法則是當我們不知道執行階段類型時，所採用的判斷相等的方法。其實現概念如下：

```csharp
public static bool Equals(object left, object right)
{
    //兩個物件參考相等=>return true;
    if (left == right)
        return true;

    //兩個有一個為空=>return false;
    if ((left == null) || (right == null))
        return false;

    //透過left.Equals判斷是否相等
    return left.Equals(right);
}
```

從上述代碼可以看出，當傳入相同的物件參考，該方法會回傳True。而當物件參考不同時，Object.Equals靜態方法會透過叫用left參數的Equals方法來做相等判斷。該方法預設在功能上已經做得很好了，我們也不需對此重新定義。

至於非靜態的Object.Equals方法，當預設的處理方式與我們所預期的不同，可以視需求重新定義。像是値類型在預設的情況下，其Equals方法是叫用基底類別ValueType.Equals來處理的。判斷的動作是在不知道類別成員的狀態下去做的。因此，它是利用.NET的反射機制來達到對應的效果，在效能上的表現並不是很好。所以當建立值類別時，我們都應重新定義ValueType.Equals方法。而另一個需重新定義的情況是，當參考類別不想採用物件參考來判斷是否相等，想改用值類型的判斷方式時，我們也可以重新定義Object.Equals方法。

Object.Equals方法若要重新定義，一般可以遵循下列的順序來實作：
![image_thumb_1.png](/images/posts/11168/image_thumb_1.png)

程式碼實作上會如下：

```csharp
public override bool Equals(object obj)
        {
            //檢查參數是否為null
            if (obj == null)
                return false;

            //檢查是否與自身是相同物件
            if (object.ReferenceEquals(this, obj))
                return true;

            //檢查是否型態相等
            if (this.GetType() != obj.GetType())
                return false;

            //比較內容是否相等
            return CompareMembers(this, obj);
        }
```

若重新定義的類別其Equals方法不是由System.Object或是System.ValueType提供的話，其實作流程會變為下面這樣：
![image_thumb_3.png](/images/posts/11168/image_thumb_3.png)

程式碼實作上會如下：

```csharp
public override bool Equals(object obj)
        {
            //檢查參數是否為null
            if (obj == null)
                return false;

            //檢查是否與自身是相同物件
            if (object.ReferenceEquals(this, obj))
                return true;

            //檢查是否型態相等
            if (this.GetType() != obj.GetType())
                return false;

            //叫用基底類別的Equals方法
            if(!base.Equals(obj))
                return false;

            //比較內容是否相等
            return CompareMembers(this, obj);
        }
```

值得注意的是，當我們重新定義了Equals方法時，GetHashCode方法也要跟著重新定義，如此該類別在雜湊函式才可正常運作。

最後一個Operator==，則是當我們建立值類別時，就應該重新定義。其理由跟上面重新定義ValueType.Equals方法的一樣。
