---
title: BenchmarkDotNet - Jobs
date: 2017-04-13 22:30:12
tags: BenchmarkDotNet
---

BenchmarkDotNet 的 Job 是用來描述 benchmark 是怎樣運行的。  

<!-- More -->

<br/>


內建的 Job 有：  
- DryJob
- ClrJob
- CoreJob
- MonoJob
- LegacyJitX86Job
- LegacyJitX64
- RyuJitX64Job
- SimpleJob
- LongRunJob
- MediumRunJob
- ShortRunJob
- VeryLongRunJob

<br/>


Job 在使用上只要透過 Attribute 的方式加到要 benchmark 的類別即可。像是這邊想要跑短一點的 benchmark 就可以為 benchmark 類別加掛 ShortRunJobAttribute：    

{% codeblock lang:c# %}
using BenchmarkDotNet.Attributes; 
using BenchmarkDotNet.Attributes.Jobs; 
... 
[ShortRunJob] 
public class ProgramBenchmarker { 
  ... 
}
{% endcodeblock %}

<br/>


運行結果如下：

{% asset_img 1.png %}

