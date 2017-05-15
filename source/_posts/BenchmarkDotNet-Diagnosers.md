---
title: BenchmarkDotNet - Diagnosers
date: 2017-04-13 23:09:09
tags: BenchmarkDotNet
---

Diagnoser 可以附加到 benchmark 上，並獲取一些有用的資訊。像是內建的 MemoryDiagnoser 就可以幫我們獲取記憶體資訊。    

<!-- More -->

<br/>


使用上只要透過 Attribute 的方式加到要 benchmark 的類別即可。像是下面這樣：  

```c#
using BenchmarkDotNet.Attributes; 
using BenchmarkDotNet.Configs; 
using BenchmarkDotNet.Diagnosers; 
... 
[MemoryDiagnoser] 
public class ProgramBenchmarker { 
  ... 
}
```

<br/>


或是透過 config 的方式設定也可以。  

```c#
using BenchmarkDotNet.Attributes; 
using BenchmarkDotNet.Configs; 
using BenchmarkDotNet.Diagnosers; 
... 
[Config(typeof(Config))] 
public class ProgramBenchmarker { 
  private class Config : ManualConfig { 
    public Config() { 
      Add(MemoryDiagnoser.Default); 
    } 
  } 
  ... 
}
```

<br/>


運行起來會看到多了 Allocated 欄位，顯示配置的記憶體量。  

{% asset_img 1.png %}

<br/>
