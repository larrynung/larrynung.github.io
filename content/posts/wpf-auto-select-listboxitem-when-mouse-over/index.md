---
title: "WPF - Auto select ListBoxItem when mouse over"
date: "2014-01-22 13:30:00"
description: "WPF - Auto select ListBoxItem when mouse over"
tags: [WPF]
---


在使用 WPF 的 ListBoxItem，若有要在滑鼠游標經過時自動選取的需求，可以為 ListBoxItem 套用像下面這樣的Style：  

<!-- More -->

```xml
<ListBox.Resources>
<Style BasedOn="{StaticResource {x:Type ListBoxItem}}"
TargetType="{x:Type ListBoxItem}">
<Style.Triggers>
<DataTrigger Binding="{Binding IsMouseOver,
RelativeSource={RelativeSource Self}}"
Value="True">
<Setter Property="IsSelected" Value="True" />
</DataTrigger>
</Style.Triggers>
</Style>
</ListBox.Resources>
```

<br/>

這個 Style 只是很簡單的透過 DataTrigger 去偵測 ListBoxItem 的 IsMouseOver屬性值，當屬性值為True時觸發，透過 Setter 將 ListBoxItem 的 IsSelected 屬性值設為True。  

Style 套上後，滑鼠游標移動過去，就會自動將  ListBoxItem 給選取起來。  
