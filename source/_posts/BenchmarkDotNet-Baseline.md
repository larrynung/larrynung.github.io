---
title: BenchmarkDotNet - Baseline
date: 2017-04-18 00:07:59
tags: [BenchmarkDotNet]
---

BenchmarkDotNet 如果要指定量測比較的標準，可在 BenchmarkAttribute 設定 Baseline 為 true，指定的量測方法即會被視為量測的標準，後續的量測則會跟該量測標準做比較。  

<!-- More -->

<br/>


像是下面這段程式：  

```c#
using System.Threading; 
using BenchmarkDotNet.Attributes; 
... 
public class ProgramBenchmarker { 
  protected Program m_Program { get; set; } = new Program(); 
  [Benchmark(Baseline = true)] 
  public void Test1() { 
    m_Program.Test(); 
    Thread.Sleep(10); 
  } 
  [Benchmark] 
  public void Test2() { 
    m_Program.Test(); 
    Thread.Sleep(20); 
  } 
}
```

<br/>


運行起來會看到設為基準的量測方法其 Scaled 值為 1，而另外一個量測方法其時間耗費大約為基準量測方法的兩倍，所以其 Scaled 值為 2。  

{% asset_img 1.png %}

<br/>
