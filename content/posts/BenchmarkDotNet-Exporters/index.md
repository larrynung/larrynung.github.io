---
title: "BenchmarkDotNet - Exporters"
date: "2017-04-14 13:42:20"
tags: [BenchmarkDotNet]
---


Exporter 會將 benchmark 的結果輸出成不同的格式。  

<!-- More -->

<br/>


內建可使用的 Exporter 有：  
- HtmlExporter
- CsvExporter
- MarkdownExporter
- AsciiDocExporter
- CsvMeasurementsExporter
- PlainExporter
- JsonExporter

<br/>


使用上只要透過 Attribue 掛上 benchmark 類別即可：

```c#
using BenchmarkDotNet.Attributes.Exporters;
…
[AsciiDocExporter] 
[CsvMeasurementsExporter] 
[PlainExporter] 
[JsonExporter] 
public class ProgramBenchmarker { 
  …
}
```

<br/>



或是透過 config 的方式設定也可以。

```c#
using BenchmarkDotNet.Configs; 
using BenchmarkDotNet.Exporters; 
using BenchmarkDotNet.Exporters.Csv; 
using BenchmarkDotNet.Exporters.Json; 
…
[Config(typeof(Config))] 
public class ProgramBenchmarker { 
  private class Config : ManualConfig { 
    public Config() { 
      Add(AsciiDocExporter.Default); 
      Add(CsvMeasurementsExporter.Default); 
      Add(PlainExporter.Default); 
      Add(JsonExporter.Default); 
    } 
  } 
  …
}
```

<br/>
預設輸出的檔案會被放置於 `.\BenchmarkDotNet.Artifactsesults` 下°  

<br/>


HtmlExporter 的輸出會像這樣：

![1.png](1.png)

<br/>


MarkdownExporter 的輸出會像這樣：

![2.png](2.png)

<br/>


CsvExporter 的輸出會像這樣：

![3.png](3.png)

<br/>


AsciiDocExporter 的輸出會像這樣：

![4.png](4.png)

<br/>


CsvMeasurementsExporter 的輸出會像這樣：

![5.png](5.png)

<br/>


PlainExporter 的輸出會像這樣：

![6.png](6.png)

<br/>


JsonExporter 的輸出會像這樣：

![7.png](7.png)

<br/>
