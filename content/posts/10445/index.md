---
title: "[.NET Concept][Security].NET程式保護機制概述"
date: "2009-09-05 11:54:24"
description: "相信大家都知道，.NET程式為了跨平台、跨語言，在架構中特別導入了CLR，用來運行中繼碼。程式在透過編譯器編譯過後會被編譯成MSIL，有點類似JAVA的Bytecode，同屬兩階段編譯。因此.NET跟JAVA程式一樣，寫出來的程式很容易從中繼碼被反推回去原程式碼(就是所謂的反組譯)。"
tags: [.NET Concept,Security]
---

相信大家都知道，.NET程式為了跨平台、跨語言，在架構中特別導入了CLR，用來運行中繼碼。程式在透過編譯器編譯過後會被編譯成MSIL，有點類似JAVA的Bytecode，同屬兩階段編譯。因此.NET跟JAVA程式一樣，寫出來的程式很容易從中繼碼被反推回去原程式碼(就是所謂的反組譯)。甚至能從MSIL反推回不同的語言。

最常見的反組譯方式有透過.NET Framework SDK內所附的IL Disassembler、.NET Explorer、Anakrino、.NET Reflector等工具來進行反組譯的動作。其中又以[.NET Reflector](http://www.red-gate.com/products/reflector/)最為強大，只要簡單的[載入組件]→[選取慣用的語言]→[點選反組譯]，不需要任何技術背景，只要簡單的幾個步驟，程式碼就完整的呈現在你的眼前。除此之外[.NET Reflector還有許多的外掛模組，像是把反組譯出來的程式轉為專案檔等。好用到幾乎是有組件就等於有程式碼的地步。也由於反組譯工具的猖獗，程式的保護對.NET程式來說就顯得隔外的重要。](http://www.red-gate.com/products/reflector/)

而就我目前所知，.NET程式的保護方式大概有幾種

1. 混淆保護
2. 內核級加密保護
3. 硬體保護

## 混淆保護

混淆保護主要的功能就是增加有心人解碼的難度。通常有幾種作法：

**1.用無意義的字串來取代本來的程式碼字串**

像是GetValue()=>AAA()

**2.耗費程式效能加入一些不會影響結果的程式讓返組譯變得困難**

像是

```csharp
for(int i=0;i<100;i++);  //不影響結果
```

或

```csharp
for(int i=0;i<100;i++){
    int a = i+1;    //不影響結果
    Console.WriteLine(i.ToString());

    //不影響結果
    if(i == a){
        Console.WriteLine("Some Thing Error!!");
    }
}
```

**3.加入一些冗贅的運算**

```csharp
int a = 10;
```

改為

```csharp
int b = 2;
int c = 5;
int a = b * c;
```

值得注意的是，使用混淆保護的程式仍是可以使用反組譯工具看到混淆後的MSIL，且很容易被有心人反推回去的，只是增加了反推的難度而已。

微軟自帶的Dotfuscator Community Edition好像已經有現成反推回去的程式在網路上流佈，像水瓶大介紹的DF Stack就是一例。

## 內核級加密保護

若採用內核級加密來保護，使用反組譯工具去看MSIL時。會顯示不是CLR程式，無法看到反組譯過後的程式碼。有比混淆稍微安全些的感覺。類似的軟體有MaxToCode、XeonCode。

## 硬體保護

硬體保護方面，有[聖天狗](http://www.safenet-inc.com/products/sentinel/hardware_keys.asp)、[Aladdin](http://www.aladdin.com/)等硬體加密鎖。多半這類產品除了本身會提供API可以讓程式呼叫做保護的動作外，也會附上基本的混淆與程式加密功能。

## Conclusion

在.NET保護這塊我涉略不深，只能做初步的介紹。這邊我要順帶一提，其實我們用來反組譯的[.NET Reflector](http://www.red-gate.com/products/reflector/)工具在加密上算是還做的不錯。畢竟本身就是反組譯用的工具，在這方面會有一定的程度，網路上也有許多相關研究。有興趣的可以從該工具的保護機制著手研究。像是[Reflector保護方法初探](http://www.cnblogs.com/smalldust/archive/2006/07/17/452724.html)等，還有很多篇，請自行打上關鍵字Reflector 保護，Google一下就有了。

## Link

* [MSDN大內高手專欄 - To De or Not to De?](http://www.microsoft.com/taiwan/msdn/columns/DoNet/ToDeoNottoDe.htm)
* [DF Stack 1.0 - .NET 的反混淆器?](http://www.dotblogs.com.tw/chhuang/archive/2008/03/18/1783.aspx)
* [DF Stack](http://www.dfstack.com/)
* [Reflector保護方法初探](http://www.cnblogs.com/smalldust/archive/2006/07/17/452724.html)
