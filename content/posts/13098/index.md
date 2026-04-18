---
title: "[VS 2010]Generate From Usage"
date: "2010-01-18 11:57:57"
description: "[VS 2010]Generate From Usage"
tags: [Visual Studio]
---

## Introduction

Generate From Usage是VS2010的新功能，其能讓使用者先使用類別與成員，事後再去定義它。這種特性對於TDD的開發方式特別有幫助、因為我們可以在撰寫單元測試的同時，利用Generate From Usage功能產生對應的程式框架。透過Generate From Usage產生程式的同時，焦點仍會保持在原本的程式編輯視窗，使用上十分方便。

Generate From Usage在使用上我們可以透過把滑鼠移至小波浪下的小底線，或是把焦點設到波浪處後，按下熱鍵Ctrl+.。

接著在彈出的圖示上按下滑鼠左鍵，並在快顯選單中選取所需使用的功能即可。

除此之外，也可以在小波浪處按下滑鼠右鍵，移至[Generate]，並選取所需使用的功能。

若選用New Type…，則會彈出Generate New Type視窗，提供進階的設定。

## Generate Class

當宣告物件的類別在專案中找不到時，我們可透過Generate From Usage的Generate Class來替我們產生。

使用後，專案會自動幫我們產生類別檔   
 
```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Generate_From_Usage
{
    class Person
    {
    }
}
```

## Generate Property

當物件的屬性不存在時，我們可透過Generate From Usage的Generate Property來替我們產生。

使用後，會幫我們產生對應的屬性

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Generate_From_Usage
{
    class Person
    {
        public string Name { get; set; }
    }
}
```

若要產生靜態的屬性，我們可以透過"類別.屬性名稱"來作Generate Property

使用後，靜態的屬性就產生了

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Generate_From_Usage
{
    class Person
    {
        public string Name { get; set; }
        public static string StaticProperty { get; set; }
    }
}
```

## Generate Field

當物件的欄位不存在時，我們可透過Generate From Usage的Generate Field來替我們產生。

使用後，會幫我們產生對應的欄位

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Generate_From_Usage
{
    class Person
    {
        private string _name;
        public string Name { get{return _name;} set; }
    }
}
```

若要產生靜態的欄位，我們可以像下圖這般作Generate Field

使用後，靜態的欄位就產生了   

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Generate_From_Usage
{
    class Person
    {
        private string _name;
        private static string _staticField;
        public string Name { get{return _name;} set; }

        public static string StaticProperty { get { return _staticField; } set; }
    }
}
```

也可以透過"類別.欄位名稱"來作Generate Field

同樣的，我們也可以產生靜態的欄位，只是存取範圍不同而已。

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Generate_From_Usage
{
    class Person
    {
        private string _name;
        private static string _staticField;
        public static string StaticField;
        public string Name { get{return _name;} set; }

        public static string StaticProperty { get { return _staticField; } set; }
    }
}
```

## Generate Constructer

當物件的建構子不存在時，我們可透過Generate From Usage的Generate Constructer來替我們產生。

使用後，會幫我們產生對應的建構子   

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Generate_From_Usage
{
    class Person
    {
        private string Name;
        private int Yesr;

        public Person(string Name, int Yesr)
        {
            // TODO: Complete member initialization
            this.Name = Name;
            this.Yesr = Yesr;
        }
    }
}
```

## Generate Method

當物件的方法不存在時，我們可透過Generate From Usage的Generate Method來替我們產生。

使用後，會幫我們產生對應的方法   

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Generate_From_Usage
{
    class Person
    {
        internal void SayHello()
        {
            throw new NotImplementedException();
        }
    }
}
```

若要產生靜態的方法，我們可以像下圖這般作Generate Method

使用後，靜態的方法就產生了   

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Generate_From_Usage
{
    class Person
    {
        internal void SayHello()
        {
            throw new NotImplementedException();
        }

        internal static void StaticSayHello()
        {
            throw new NotImplementedException();
        }
    }
}
```

## Link
VS 2010 Generate From UsageGenerate From UsageWalkthrough: TDD Support with the Generate From Usage FeatureGenerate From Usage in Visual Studio 2010Walkthrough: TDD Support with the Generate From Usage Feature in VS 2010 (Lisa Feigenbaum)HDI Video: Generate from Usage in Visual Studio 2010 with Karen LiuHow Do I Use Generate from Usage in Visual Studio 2010?