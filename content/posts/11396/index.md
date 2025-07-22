---
title: "[C#]阿拉伯數字轉國字"
slug: "[CSharp]阿拉伯數字轉國字"
date: "2009-11-03 06:02:00"
description: "[C#]阿拉伯數字轉國字"
tags: [CSharp]
---

看到Rico的[C#][WinForm]如何將數字轉為國字又手癢了一下，也試著寫了一段程式，隨手記錄一下。  

基本上要作數字轉國字，大致上有兩種方法：
     用現成的函式庫，像是Microsoft Visual Studio International Feature Pack。     土法煉鋼自己做    

下方為我寫的土法煉鋼程式：
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

使用範例：

              for (int num = 0; num < 100; num++)
                Console.WriteLine(GetChineseNumber(num));

執行結果：

## Link

  [C#][WinForm]如何將數字轉為國字