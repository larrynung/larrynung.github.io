---
title: "WPF - Binding a ListView to DataTable"
date: "2014-02-07 10:23:00"
description: "WPF - Binding a ListView to DataTable"
tags: [WPF]
---


要在 WPF 中將 DataTable binding 到 ListView 上，我們主要有幾種做法…  

<!-- More -->

像是把 DataTable 轉型成 IListSource 後，叫用 GetList 方法，並將回傳值塞進 ListView 的 ItemSource 屬性  

    lvTable.ItemsSource = ((IListSource)dt).GetList();


或是直接將 DataTable 的 DefaultView 塞進 ListView 的 ItemSource 屬性  

    lvTable.ItemsSource = dt.DefaultView;


XAML 這邊我們只要直接將 DataTable 的 Column 繫上 ListView 內 Grid Column 的 DisplayMemberBinding 就可以了。  

以個簡單的例子來看，假設我們要繫結的表單長的像下面這樣：  

```c#
var dt = new DataTable();
dt.Columns.Add( "Key");
dt.Columns.Add( "Value");

dt.Rows.Add( new object[] { "Key1", "Value1"});
dt.Rows.Add( new object[] { "Key2", "Value2"});

...

lvTable.ItemsSource = dt.DefaultView;
```


那麼 XAML 這邊就會是像這個樣子  

```xml
<ListView x :Name="lvTable" Margin="0">
  <ListView.View>
    <GridView>
      <GridViewColumn Header ="Key" DisplayMemberBinding ="{Binding Key}"/>
      <GridViewColumn Header ="Value" DisplayMemberBinding="{Binding Value}"/>
    </GridView>
  </ListView.View>
</ListView>
```


你也可以像下面這樣稍微包裝一下，將 ListView 的 ItemSource 與 DefaultView 繫結...

```xml
<ListView x :Name="lvTable" Margin="0" ItemsSource="{Binding DefaultView}">
  <ListView.View>
    <GridView>
      <GridViewColumn Header ="Key" DisplayMemberBinding ="{Binding Key}"/>
      <GridViewColumn Header ="Value" DisplayMemberBinding="{Binding Value}"/>
    </GridView>
  </ListView.View>
</ListView>
```

這樣在 Binding 時只要直接塞 DataTable 給 ListView 就好了...  

    lvTable.DataContext = dt;
