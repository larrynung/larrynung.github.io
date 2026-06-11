---
title: "Recursive ContainerFromItem"
date: "2013-11-06 12:00:00"
description: "Recursive ContainerFromItem"
tags: [CSharp]
---

在使用WPF的TreeView時，透過ItemContainerGenerator.ContainerFromItem找尋特定的TreeViewItem，只能找到第一層的節點。第二層以後的節點必須要透過遞迴下去找尋，像是下面這樣：

public DependencyObject ContainerFromItemItems(Control itemsControl, object value)
{
var dp = itemsControl.ItemContainerGenerator.ContainerFromItem(value);

if (dp != null)
return dp;

foreach (var item in itemsControl.Items)
{
var currentTreeViewItem = itemsControl.ItemContainerGenerator.ContainerFromItem(item);

var childDp = ContainerFromItem(currentTreeViewItem as ItemsControl, value);

if (childDp != null)
return childDp;
}
return null;
}

為方便後續使用，這邊筆者稍微整理了一些擴充方法，有需要的自行取用：

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows;
using System.Windows.Controls;

public static class ItemsControlExtension
{
public static DependencyObject ContainerFromItem(this ItemsControl itemsControl, object value)
{
var dp = itemsControl.ItemContainerGenerator.ContainerFromItem(value);

if (dp != null)
return dp;

foreach (var item in itemsControl.Items)
{
var currentTreeViewItem = itemsControl.ItemContainerGenerator.ContainerFromItem(item);

var childDp = ContainerFromItem(currentTreeViewItem as ItemsControl, value);

if (childDp != null)
return childDp;
}
return null;
}

public static T ContainerFromItem(this ItemsControl itemsControl, object value) where T : class
{
return ContainerFromItem(itemsControl, value) as T;
}
}

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows;
using System.Windows.Controls.Primitives;

public static class SelectorExtension
{
public static DependencyObject ContainerFromSelectedItem(Selector selector)
{
var selectedItem = selector.SelectedItem;

if (selectedItem == null)
return null;

return selector.ContainerFromItem(selectedItem);
}

public static T ContainerFromSelectedItem(Selector selector) where T : class
{
return ContainerFromSelectedItem(selector) as T;
}
}

using System.Windows;
using System.Windows.Controls;

public static class TreeViewExtension
{
public static void ClearSelection(this TreeView treeview)
{
var selectedItem = ContainerFromSelectedItem(treeview);

if (selectedItem == null) return;

selectedItem.IsSelected = false;

}

public static DependencyObject ContainerFromSelectedItem(this TreeView treeview)
{
var selectedItem = treeview.SelectedItem;

if (selectedItem == null)
return null;

return treeview.ContainerFromItem(selectedItem);
}

public static T ContainerFromSelectedItem(this TreeView treeview) where T : class
{
return ContainerFromSelectedItem(treeview) as T;
}
}