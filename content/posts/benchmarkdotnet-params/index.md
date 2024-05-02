---
title: "BenchmarkDotNet - Params"
date: "2017-04-17 23:44:13"
tags: [BenchmarkDotNet]
---


使用 BenchmarkDotNet 時若需要設定欄位或是屬性的值，可以使用 ParamsAttribute 指定，像是下面這樣：  

<!-- More -->

```c#
using BenchmarkDotNet.Attributes;
... 
public class ProgramBenchmarker { 
  [Params(100, 200)] 
  public int Parameter { get; set; } 
  protected Program m_Program { get; set; } = new Program(); 
  [Benchmark] 
  public void Test() { 
    m_Program.Test(); 
  } 
}
```

<br/>


運行時即會依序將指定的值帶入欄位或屬性下去量測。  

![1.png](1.png)

<br/>
