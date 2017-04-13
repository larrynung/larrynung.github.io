---
title: BenchmarkDotNet - Columns
date: 2017-04-13 22:41:21
tags: BenchmarkDotNet
---

BenchmarkDotNet 允許透過設定去變更 Summary Table 的 Column。  

<!-- More -->

<br/>


內建可使用的 Column 有：  
- NamespaceColumn
- MedianColumn
- MinColumn
- MaxColumn
- RankColumn

<br/>


使用上只要透過 Attribue 掛上 benchmark 類別即可：

{% codeblock lang:c# %}
using BenchmarkDotNet.Attributes.Columns;
…
[NamespaceColumn] 
[MedianColumn] 
[MinColumn] 
[MaxColumn] 
[RankColumn]
[RankColumn(NumeralSystem.Roman)] 
[OrderProvider(SummaryOrderPolicy.FastestToSlowest)] 
public class ProgramBenchmarker { 
  …
}
{% endcodeblock %}

<br/>


運行起來就會在 Summary Table 看到設定的欄位。  

{% asset_img 1.png %}

<br/>


如果要加的欄位是未內建的，可透過 Config 與 TagColumn。像是這邊筆者想要加個 HashCode Column，其值為方法的 Hash 值，就可以像下面這樣撰寫：  

{% codeblock lang:c# %}
using BenchmarkDotNet.Attributes; 
using BenchmarkDotNet.Columns; 
using BenchmarkDotNet.Configs; 
…
[Config(typeof(Config))] 
public class ProgramBenchmarker { 
  private class Config : ManualConfig { 
    public Config() { 
      Add(new TagColumn("HashCode", item => item.GetHashCode().ToString())); 
    } 
  } 
    …
}
{% endcodeblock %}

<br/>


程式運行結果如下：  

{% asset_img 2.png %}

<br/>


不過這樣用 TagColumn 的撰寫方式在重用上比較不易，若有需要可進一步撰寫一個實作 IColumn 的自定義 Column 類別。像是下面這樣： 

{% codeblock lang:c# %}
using BenchmarkDotNet.Columns; 
using BenchmarkDotNet.Reports; 
using BenchmarkDotNet.Running;
…
public class HashCodeColumn : IColumn { 
  public string ColumnName { get; } = "HashCode"; 
  public HashCodeColumn() { } 
  public bool IsDefault(Summary summary, Benchmark benchmark) => false; 
  public string GetValue(Summary summary, Benchmark benchmark) => benchmark.Target.Method.Name.GetHashCode().ToString(); 
  public bool IsAvailable(Summary summary) => true; 
  public bool AlwaysShow => true; 
  public ColumnCategory Category => ColumnCategory.Custom; 
  public string Id { get; } = "1"; 
  public int PriorityInCategory { get; } = 0; 
  public override string ToString() => ColumnName; 
}
{% endcodeblock %}

<br/>


有自定義的 Column 類別，使用上就只要建立實體後透過 Config 設定即可。  

{% codeblock lang:c# %}
…
[Config(typeof(Config))] 
public class ProgramBenchmarker { 
  private class Config : ManualConfig { 
    public Config() { 
      Add(new HashCodeColumn())); 
    } 
  } 
    …
}
{% endcodeblock %}
  
