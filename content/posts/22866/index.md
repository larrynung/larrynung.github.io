---
title: "[.NET Concept]集合與字串類型的屬性和方法應避免回傳null"
date: "2011-04-16 03:14:05"
description: "在撰寫程式時，最常撰寫的成員型態應該就屬集合與字串這兩種，很多開發人員對這兩種回傳型態的屬性與方法並未特別的注意，因兩種型態都是參考型態別，有時在實作上直接把null回傳出去。其實當回傳型態為這兩種型態時，我們應避免直接以null當作回傳的值，而是應該回傳空的字串或是空的集合。"
tags: [.NET Concept]
---

在撰寫程式時，最常撰寫的成員型態應該就屬集合與字串這兩種，很多開發人員對這兩種回傳型態的屬性與方法並未特別的注意，因兩種型態都是參考型態別，有時在實作上直接把null回傳出去。其實當回傳型態為這兩種型態時，我們應避免直接以null當作回傳的值，而是應該回傳空的字串或是空的集合。像是:

```
class Person
{
    #region Var
    private string _name;
    private IEnumerable<CreditCard> _creditCards;
    #endregion
```

```
    #region Property
    public string Name
    {
        get
        {
            if (_name == null)
                return string.Empty;
            return _name;
        }
    }
```

```
    public IEnumerable<CreditCard> CreditCards
    {
        get
        {
            if (_creditCards == null)
                return new CreditCard[0];
            return _creditCards;
        }
    }
    #endregion
}
```

這是個很簡單卻也很重要的撰寫概念，若在撰寫時能遵照此概念，如此使用者不會混淆於哪些成員屬性與方法可能為null，在使用上也可直接用字串長度或是集合的元素數量直接判斷是否為空值，而不需事先判斷是否為null，因此程式撰寫會變得簡潔，可讀性跟著提升，間接的也減少了NullReferenceException發生的機率。

這概念在MSDN的陣列用法方針這篇也有提到

![image_thumb.png](/images/posts/22866/image_thumb.png)

在.Net Framework中也隨處可見此概念的實現，稍有留心就能參透此概念。有興趣的可以嚐試看看.Net Framework BCL中的集合與字串型態成員是否都可以直接判斷空值，是否不需判斷是否為null。

## Link

* [How to return an array – null or empty?](http://ray.jez.net/how-to-return-an-array-null-or-empty/)
* [陣列用法方針](http://msdn.microsoft.com/zh-tw/library/k2604h5s(v=VS.90).aspx)
