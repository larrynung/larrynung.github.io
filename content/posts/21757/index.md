---
title: "[C#]More Effective C# 條款四十九： 考慮為大型物件使用弱引用"
slug: "[CSharp]More Effective C# 條款四十九： 考慮為大型物件使用弱引用"
date: "2011-03-09 10:08:11"
description: "[C#]More Effective C# 條款四十九： 考慮為大型物件使用弱引用"
tags: [CSharp]
---

<p>
	在.Net的世界中，物件的引用可被分為強引用與弱引用兩種。所謂的強引用指的就是我們一般在使用的物件引用方式。我們可將這種物件引用視為一個釘子，牢牢的釘在物件實體上面，只要物件實體仍有被強引用給參考，該物件實體就會被固定的死死的，不能被GC給回收，因這樣的引用特性是很強烈的，故稱之為強引用。</p>
<p>
	 </p>
<p>
	而弱引用則是相對於強引用來說，弱引用沒有像強引用一樣強烈的引用特性，可被細分為短弱引用與長弱引用兩種。長與短的區別在於物件終結後是否還能被引用。短弱引用在物件被終結或回收後，其引用則會自動失效。而長弱引用則只有回收後，其引用才會失效，僅管物件已被終結，只要垃圾收集器尚未將該物件實體給回收，則都還可使用該引用。弱引用的概念可以將其想成是用根細長的繩子綁住物件實體一般，雖然有繫住，可是一扯就斷。故被弱引用所參考到的物件實體只要未被強引用給參考，所引用的物件實體跟一般的記憶體垃圾一樣都可被GC給回收，不同的是弱引用在回收之前仍能透過引用去取回物件，另一個則是垃圾收集器會對弱引用做些額外的處理，會增加垃圾的負擔，也會讓弱引用的回收機率變得比記憶體垃圾還低。</p>
<p>
	 </p>
<p>
	這種物件引用方式特別適用與大型且僅偶爾會使用的物件，因為這種物件若是使用強引用成員變數，會讓一大塊記憶體長時間被系統所佔用，若使用強引用區域變數，則每次執行皆會生成一大塊記憶體垃圾。而採用弱引用來改寫，會有點類似快取的意味存在，在偶爾特別頻繁的使用下，程式能重用之前所建立的物件實體，而在長時間沒使用的狀況下，物件實體又可以被垃圾收集器給回收，減少記憶體的耗費。</p>
<p>
	 </p>
<p>
	使用上我們可以透過System.WeakReference類別來撰寫弱引用，透過判斷WeakReference.Target是否為null來確定物件是否被垃圾收集器給回收，簡單的使用範例如下：</p>
<pre>
</pre>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:0375a160-1701-4d8f-838f-e4889756ddd1" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c#" name="code">
        static WeakReference _objectCache;

        private static WeakReference m_ObjectCache
        {
            get
            {
                if (_objectCache == null)
                    _objectCache = new WeakReference(null);
                return _objectCache;
            }
        }

        private static Object m_Cache
        {
            get
            {
                if (m_ObjectCache.Target == null)
                    m_ObjectCache.Target = CreateBigObj();
                return m_ObjectCache.Target;
            }
        }

        static void Main(string[] args)
        {
            Console.WriteLine(m_Cache);
            Console.WriteLine(m_Cache);
            GC.Collect();
            Console.WriteLine(m_Cache);
        }
        ...</pre>
</div>
<p>
	 </p>
<p>
	值得注意的是，弱引用並不適用於實作有IDisposable介面的類別，因為當IDisposable.Dispose方法被叫用時，物件所使用的非托管資源會被釋放，不易於被重用。就算沒有這樣的問題，你也不知何時要呼叫弱引用的Dispose方法。</p>
