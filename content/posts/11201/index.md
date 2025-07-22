---
title: "[C#]Effective C# 條款十一： 優先採用foreach迴圈"
slug: "[CSharp]Effective C# 條款十一： 優先採用foreach迴圈"
date: "2009-10-22 08:41:07"
description: "[C#]Effective C# 條款十一： 優先採用foreach迴圈"
tags: [CSharp]
---

C#中的foreach迴圈並不僅僅是do…while或是for迴圈的變形。它會與.NET框架中的集合接口做緊密的結合，在編譯時為我們最佳化程式碼。除此之外foreach使用上也具備較高的相容性。

	讓我們先來看三種迴圈的寫法：

	1.foreach迴圈寫法  

	int[] foo = new int[100];
foreach(int i in foo)
    Console.WriteLine(i.ToString());

	2.for迴圈寫法

	int[] foo = new int[100];
for(int index=0;index<foo.Length;index++)
    Console.WriteLine(foo[index].ToString());

	3.for迴圈寫法 (結束條件提到迴圈外)

	int[] foo = new int[100];
int len = foo.Length;
for(int index=0;index<len;index++)
    Console.WriteLine(foo[index].ToString());

	據作者所述，第一個迴圈的寫法，在.NET1.1以後的版本，其效率最佳，程式碼也最少。而第三個迴圈寫法是最慢的，因為這樣刻意的把結束條件提出迴圈外，會阻礙JIT編譯器移除迴圈內的範圍檢查，讓JIT編譯器編譯成下面這樣：

	int[] foo = new int[100];
int len = foo.Length;
for(int index=0;index<len;index++){
    if(index<foo.Length)
        Console.WriteLine(foo[index].ToString());
    else
        throw new IndexOutOfRangeException();
}

	在.NET 1.0以前，使用foreach效率上會較差，因為JIT編譯器會把程式編譯成下面這樣：

	IEnumerator it = foo.GetEnumerator();
while(it.MoveNext())
{
   int i = (int) it.Current;
   Console.WriteLine(i.ToString());
}

	這樣的程式會產生裝箱與拆箱，因此在效能上會有不良的影響。但在.NET 1.1以後的版本，JIT編譯器會把程式編譯成下面這樣：

	int[] foo = new int[100];
for(int index=0;index<foo.Length;index++)
    Console.WriteLine(foo[index].ToString());

	所以我們可以得知，使用foreach來處理迴圈，編譯器會幫我們自動產生最佳的程式碼，程式也較短較易閱讀。

	不過經實際實驗，當撰寫了如下測試程式：

	static void Main(string[] args)
        {
            int[] foo = new int[100];
            int len = foo.Length;

            foreach (int i in foo)
                Console.WriteLine(i.ToString());

            for (int index = 0; index < len; index++)
                Console.WriteLine(foo[index].ToString());

            for (int index = 0; index < foo.Length; index++)
                Console.WriteLine(foo[index].ToString());
        }

	用Reflector反組譯工具來查看，該段程式被編譯後是幾乎不變的。

	這邊就留待個人自己去評估。

	除效能外，foreach迴圈在使用上也具備較高的相容性。不論巡覽的陣列其上下限是多少，foreach迴圈總是能正確的運行。在多維陣列上，不論陣列維度維多少，使用foreach迴圈都能幫我們巡覽所有陣列元素。就算本來使用的是陣列，後來因需求變更為使用集合類別，使用foreach迴圈，程式都不需做任何的修改。

	綜合以上論點，在撰寫巡覽迴圈元素的程式時，我們應該優先考慮使用foreach迴圈寫法。因其可獲得較好的效能與較高的相容性，也可提升開發速度與可讀性。