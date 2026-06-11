---
title: "[Performance][C#]String.Empty V.S “”"
date: "2009-12-22 08:00:58"
description: "[Performance][C#]String.Empty V.S “”"
tags: [CSharp,Performance]
---

在程式的寫作過程中，我們經常會需要指派空字串。但在.NET的程式語言中，空字串的指派除了指派""，我們也可以指派String.Empty。相信有人對於兩者的差異不甚了解，或是了解卻未實際比較。這邊隨手記錄一下自己做的整理與比較。

整理了網路上流佈的文章，大致上大家普遍認為使用String.Empty來取代""作指派空字串的動作，我們可以獲取較好的效能。

這邊讓我們先來看段實驗，實驗的Code如下： 
                static void Main(string[] args)
        {
            EmptyString1(1);
            EmptyString2(1);
            EmptyString3(1);

            Console.Clear();
            int count = 1000000000;
            for (int idx = 0; idx < 3; ++idx)
            {             
                EmptyString1(count);
                EmptyString2(count);
                EmptyString3(count);
                Console.WriteLine();
            }
        }

        private static void EmptyString1(int count)
        {
            String test;
            Stopwatch sw = Stopwatch.StartNew();
            for (int idx = 0; idx < count; ++idx)
            {
                test = "";
            }
            sw.Stop();
            Console.WriteLine("EmptyString1: " + sw.ElapsedMilliseconds.ToString());
        }

        private static void EmptyString2(int count)
        {
            String test;
            Stopwatch sw = Stopwatch.StartNew();
            for (int idx = 0; idx < count; ++idx)
            {
                test = string.Empty;
            }
            sw.Stop();
            Console.WriteLine("EmptyString2: " + sw.ElapsedMilliseconds.ToString());
        }

        private static void EmptyString3(int count)
        {
            String test;
            Stopwatch sw = Stopwatch.StartNew();
            for (int idx = 0; idx < count; ++idx)
            {
                test = new String(' ',0);
            }
            sw.Stop();
            Console.WriteLine("EmptyString1: " + sw.ElapsedMilliseconds.ToString());
        }

當測試的次數為1000000，其實驗結果如下： 

當測試的次數為10000000，其實驗結果如下： 

當測試的次數為1000000000，其實驗結果如下： 

由以上實驗可以看到String.Empty其實跟""是差不了多少的。這是因為若是使用""來作空字串的指派。程式會在使用時幫我們建立並指派空字串物件，第一次使用時雖然會需要額外的OverHead，但是由於在.NET中有字串池這樣的優化機制，因此這部分的OverHead被降到最小了，當後續再使用相同的字串，系統會自動至字串池取出以建立的來使用，這部份的概念可參閱筆者的[.Net Concept]理解並善用String pool這篇。而使用String.Empty來作空字串的指派動作，由於該屬性是String類別的唯讀靜態屬性，在使用上不會頻繁的建立空字串物件。

再看一下兩者所產生的MSIL有何差異。 

我們可以發現兩者所產生的MSIL幾乎一樣，只有一行有所差異。

雖然String.Empty跟""這兩個設定空字串的方式在效能上幾乎沒有差異，但是筆者認為使用String.Empty較為直白，能的話還是建議使用String.Empty。

## Link

  String.Empty Field 

  [.net]String.Empty與"" 

  What is the difference between String.Empty and “” 

  String.Empty vs "" 

  String.Empty、null和""的区别 

  String.Empty,NULL和""的区别