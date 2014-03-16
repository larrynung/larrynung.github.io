---
layout: post
title: "WPF - Refresh / Update WPF controls"
date: 2014-03-16 22:29
comments: true
categories: [WPF] 
keywords: WPF, Refresh
description: "WPF - Refresh / Update WPF controls"
---


相信大家都知道若要釋放些資源去讓畫面得以更新，若不將運算處理切離主執行緒，我們可能會偷懶用 DoEvents 來做。然而， DoEvents 這個方法的功用只是釋放資源，而釋放出的資源為誰所用，這部分我們無法掌控。因此釋放出的資源可能會被拿去做不相干的處理，造成效能嚴重低落。 

<!-- More -->

<br/> 

在 WinForm 的世界裡，這樣的問題比較好處理，因為有許多現成的方法可以指定特定元件去做更新，像是 Update、Refresh、或是 Invalidate。 

<br/> 

在 WPF 的世界裡，我們沒現有的方法可以直接叫用，只能用些小技巧兜出類似的功能。像是將下面這段擴充方法加入…  

{% codeblock lang:c# %}
public static class ExtensionMethods
{
   private static Action EmptyDelegate = delegate() { }; 
   public static void Refresh(this UIElement uiElement)
   {
      uiElement.Dispatcher.Invoke(DispatcherPriority.Render, EmptyDelegate);
   }
}
{% endcodeblock %}

<br/>

程式在撰寫時就可以像下面這樣直接透過 UI 元件觸發更新。 

    control.Refresh();

<br/>

Link
----
* [Refresh / Update WPF controls](http://geekswithblogs.net/NewThingsILearned/archive/2008/08/25/refresh--update-wpf-controls.aspx)
