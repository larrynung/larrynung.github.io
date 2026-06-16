---
title: "[C#]Convert Arabic Numerals to Chinese Numerals"
slug: "csharp-convert-arabic-numerals-to-chinese-numerals"
aliases: ["/posts/csharp阿拉伯數字轉國字/"]
date: "2009-11-03 06:02:00"
description: "看到Rico的[C#][WinForm]如何將數字轉為國字又手癢了一下，也試著寫了一段程式，隨手記錄一下。 基本上要作數字轉國字，大致上有兩種方法： 用現成的函式庫，像是Microsoft Visual Studio International Feature Pack。"
tags: [CSharp]
---

看到Rico的[C#][WinForm]如何將數字轉為國字又手癢了一下，也試著寫了一段程式，隨手記錄一下。

基本上要作數字轉國字，大致上有兩種方法：

* 用現成的函式庫，像是[Microsoft Visual Studio International Feature Pack。](http://www.microsoft.com/downloads/details.aspx?displaylang=zh-tw&FamilyID=7d1df9ce-4aee-467f-996e-bec826c5daa2)
* 土法煉鋼自己做

下方為我寫的土法煉鋼程式：

```csharp
static string GetChineseNumber(int number)
{
    string[] chineseNumber = { "零", "一", "二", "三", "四", "五", "六", "七", "八", "九" };
    string[] unit = { "", "十", "百", "千", "萬", "十萬", "百萬", "千萬", "億", "十億", "百億", "千億", "兆", "十兆", "百兆", "千兆" };
    StringBuilder ret = new StringBuilder();
    string inputNumber = number.ToString();
    int idx = inputNumber.Length;
    bool needAppendZero = false;
    foreach (char c in inputNumber)
    {
        idx--;
        if (c > '0')
        {
            if (needAppendZero)
            {
                ret.Append(chineseNumber[0]);
                needAppendZero = false;
            }
            ret.Append(chineseNumber[(int)(c - '0')] + unit[idx]);
        }
        else
            needAppendZero = true;
    }
    return ret.Length == 0 ? chineseNumber[0] : ret.ToString ();
}
```

使用範例：

```csharp
for (int num = 0; num < 100; num++)
    Console.WriteLine(GetChineseNumber(num));
```

執行結果：

![image_thumb.png](/images/posts/11396/image_thumb.png)

## Link

* [C#][WinForm]如何將數字轉為國字
