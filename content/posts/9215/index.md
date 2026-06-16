---
title: "[C#]Effective C# 條款一： 使用屬性代替公有欄位"
slug: "[CSharp]Effective C# 條款一： 使用屬性代替公有欄位"
date: "2009-07-08 12:38:19"
description: "為何要用屬性來替代公有欄位主要有下列幾項原因： 符合物件導向封裝概念 支援資料繫結 具修改彈性 符合物件導向封裝概念 屬性是對取得/修改內部數據的方法的一種擴展，從表面看來就像是數據成員，但內部卻是以方法實現。"
tags: [CSharp]
---

![image_thumb.png](/images/posts/9215/image_thumb.png)

為何要用屬性來替代公有欄位主要有下列幾項原因：

1. 符合物件導向封裝概念
2. 支援資料繫結
3. 具修改彈性

## 符合物件導向封裝概念

屬性是對取得/修改內部數據的方法的一種擴展，從表面看來就像是數據成員，但內部卻是以方法實現。

在程式編譯後，編譯器在把程式編譯成MSIL時，會自動把屬性中的get區塊與set區塊編譯成兩個分離的方法。所以使用屬性能穫得函式的全部好處。

讓我們來看一下簡單的例子。假設今天有個People的類別，內含一個Name屬性，該屬性可讀可寫。

```
class People
{
    string Name { get; set; }
}
```

程式編譯後我們透過SDK內建的IL Disassembler工具查看MSIL。

![image_thumb_4.png](/images/posts/9215/image_thumb_4.png)

我們可以發現Name屬性在MSIL中已不復可見，取而代之的是MSIL中多了兩個Method，一個是get_name、一個是set_name，這兩個方法分別對應至本來屬性的get與set區塊。

![image_thumb_3.png](/images/posts/9215/image_thumb_3.png)

## 支援資料繫結

.NET中的資料繫結只支援屬性，並不支援公有欄位。這是因為資料繫結機制用反射來實作時只尋找類別的屬性。而之所以不支援公有欄位，主要是因為公有欄位把數據成員直接鋪暴露給外界較不符合物件導向的封裝原則。

## 具修改彈性

使用屬性在修改上也較一般公有欄位更具彈性。試想當程式中類別的公有欄位被頻繁的使用，則當我們要增加判斷防止公有欄位值為空時，我們勢必需要把散在程式中所有用到的地方都加上判斷才行。同樣的情況對於屬性來說，我們只需在屬性的get區塊增加判斷即可。

```
class People
{
    private string _name;
    public string Name
    {
        get
        {
            if (_name == null)
                return string.Empty;
            return _name;
        }
        set
        {
            _name = value;
        }
    }
}
```

若是日後要改成多執行緒程式，使用屬性也會比使用公有欄位容易來得修改。只要在get與set區塊中加入lock即可。

```
class People
{
    private string _name;
    public string Name
    {
        get
        {
            lock (this)
            {
                if (_name == null)
                    return string.Empty;
                return _name;
            }
        }
        set
        {
            lock (this)
            {
                _name = value;
            }
        }
    }
}
```

除此之外，使用屬性對於事件的增加也較為容易。

```
class People
{
    public event EventHandler NameChanging;
    public event EventHandler NameChanged;
```

```
    private string _name;
    public string Name
    {
        get
        {
            if (_name == null)
                return string.Empty;
            return _name;
        }
        set
        {
            if (_name != value)
            {
                NameChanging(this, new EventArgs());
                _name = value;
                NameChanged(this, new EventArgs());
            }
        }
    }
}
```

## 注意事項

雖然屬性與公有欄位在使用上看起來是一樣的，但不代表可以先寫成公有欄位以後有需要再改成屬性，因為公有欄位與屬性所編譯出的MSIL是不同的，因此若把公有欄位改為屬性，所有使用到本來公有欄位的程式都必需重新編譯，兩者以二進制的層級來看並非是兼容的。
