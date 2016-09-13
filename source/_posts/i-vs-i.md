---
title: ++i vs i++
date: 2016-09-10 22:44:54
tags:
---

i++ 與 ++i 如果在不影響結果的情況下使用，像是在 for 迴圈的遞增條件下，兩者最主要的差異是在於 i++ 會多一個堆疊的耗費。  

<!-- More -->

<br/>


這邊以一個簡單的例子來看：  

{% codeblock lang:c# %}
var i = 0;
var a = i++;
{% endcodeblock %}

<br/>


對應的 IL 如下：  

{% codeblock lang:IL %}
IL_0000:  nop         
IL_0001:  ldc.i4.0    
IL_0002:  stloc.0     // i
IL_0003:  ldloc.0     // i
IL_0004:  dup         
IL_0005:  ldc.i4.1    
IL_0006:  add         
IL_0007:  stloc.0     // i
IL_0008:  stloc.1     // a
IL_0009:  ret        
{% endcodeblock %}

<br/>


整個運作是會先將堆疊內放置一個 0，然後將堆疊內的 0 取出放到區域變數 i，再將 i 的值放到堆疊內，這時堆疊內的值還是 0。

{% asset_img 1.png %}

<br/>


然後將堆疊內的 0 複製一份放至堆疊，這時堆疊內的值為 00。  

{% asset_img 2.png %}

<br/>


接著將 1 放入堆疊，堆疊內的值變為 001。  

{% asset_img 3.png %}

<br/>


再來從堆疊內取出兩個值相加後放回堆疊，堆疊內的值變為 01。  

{% asset_img 4.png %}

<br/>


最後將堆疊內的值取出依序塞給區域變數 i 與 a。  

{% asset_img 5.png %}

<br/>


可以看到這樣的處理最多需要的堆疊大小為 3。  

<br/>


再來來看 ++i，一樣用個間單的例子來看：    

{% codeblock lang:c# %}
var i = 0;
var a = ++i;
{% endcodeblock %}

<br/>


其對應的 IL 如下：  

{% codeblock lang:IL %}
IL_0000:  nop         
IL_0001:  ldc.i4.0    
IL_0002:  stloc.0     // i
IL_0003:  ldloc.0     // i
IL_0004:  ldc.i4.1    
IL_0005:  add         
IL_0006:  dup         
IL_0007:  stloc.0     // i
IL_0008:  stloc.1     // a
IL_0009:  ret   
{% endcodeblock %}

<br/>


整個運作是會先將堆疊內放置一個 0，然後將堆疊內的 0 取出放到區域變數 i，再將 i 的值
放到堆疊內，這時堆疊內的值還是 0。

{% asset_img 6.png %}

<br/>


接著會在堆疊放置一個 1，這時堆疊內的值為 01。  

{% asset_img 7.png %}

<br/>


再來從堆疊內取出兩個值相加後放回堆疊，堆疊內的值變為 1。  

{% asset_img 8.png %}

<br/>


然後複製堆疊頂端的值，此時堆疊內的值為 11。  

{% asset_img 9.png %}

<br/>


最後將堆疊內的值取出依序塞給區域變數 i 與 a。  

{% asset_img 10.png %}

<br/>


這樣的處理最多需要的堆疊大小為 2。  

<br/>


所以使用 i++ 會比使用 ++i 多一點點的 Overhead。  
