---
title: "[C#]RaiseEvent Extension Method (二)"
slug: "[CSharp]RaiseEvent Extension Method (二)"
date: "2011-08-17 06:52:51"
description: "[C#]RaiseEvent Extension Method (二)"
tags: [CSharp]
---

<p>前面[C#]RaiseEvent Extension Method (一)這篇介紹了如何用擴充方法來簡化C#事件的觸發動作，最近在做觸發事件時，又看到了一個引起我關注的重點，那就是有時候我們在初始化事件的參數時費了很大的耗費，準備觸發事件時，透過OnXXX去觸發事件，結果發現事件並未被繫上，整個事件觸發的動作就不做了，那麼前面所作的參數準備不就是不必要的耗費?</p>  <div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:796b6322-7c7f-414f-a857-058cb926f0c0" class="wlWriterSmartContent"><pre name="code" class="c#">...
Var e = new MyEventArgs() {...};
...
OnMyEvent(e);
...</pre></div>

<p> </p>

<p>當然這樣的問題可以在觸發事件的地方用if判別去避開，但這樣就會讓程式在維護與閱讀上的困難度上升，筆者在[.Net Concept]理解事件的宣告方式與用法這篇有對此做詳細的描述，這邊不多做解釋。</p>

<p> </p>

<p>因為有上面的原因，筆者又花了一點時間將擴充方法做了些改進，增加兩個多載版本，使其能帶入初始化事件參數的方法，如此在事件未繫上時就不會做初始的動作。</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:33072e43-cc87-49b1-9abf-cb470b9744cb" class="wlWriterSmartContent"><pre name="code" class="c#">    public static class ObjectExtension
    {
        public static void RaiseEvent(this object obj, EventHandler handler, EventArgs e)
        {
            RaiseEvent(obj, handler, () =&gt; e);
        }

        public static void RaiseEvent(this object obj, EventHandler handler, Func&lt;EventArgs&gt; func)
        {
            if (handler == null)
                return;
            handler(obj, func());
        }

        public static void RaiseEvent&lt;TEventArgs&gt;(this object obj, EventHandler&lt;TEventArgs&gt; handler, TEventArgs e) where TEventArgs : EventArgs
        {
            RaiseEvent(obj, handler, () =&gt; e);
        }

        public static void RaiseEvent&lt;TEventArgs&gt;(this object obj, EventHandler&lt;TEventArgs&gt; handler,Func&lt;TEventArgs&gt; func) where TEventArgs : EventArgs
        {
            if (handler == null)
                return;
            handler(obj, func());
        }
    }</pre></div>

<p> </p>

<p>使用上透過Lambda的輔助也十分的好上手。</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:c777dac3-4232-475c-bbde-cf174b56ad37" class="wlWriterSmartContent"><pre name="code" class="c#">this.RaiseEvent(MyEvent, () =&gt; new MyEventArgs() 
{
	//Init EventArgs
	... 
 });</pre></div>

<p> </p>

<p>完整的範例程式如下：</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:bc7ec8ff-e9e1-4c2d-839f-3c72f9d90990" class="wlWriterSmartContent"><pre name="code" class="c#">using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ConsoleApplication14
{
    class Program
    {
        static void Main(string[] args)
        {
            Person Larry = new Person();
            Larry.NameChanged += new EventHandler&lt;NameEventArgs&gt;(Larry_NameChanged);
            Larry.Name = "Larry";
        }
        static void Larry_NameChanged(object sender, NameEventArgs e)
        {
            Console.WriteLine(string.Format("NameChanged to {0}", e.Name));
        }
    }
    public static class ObjectExtension
    {
        public static void RaiseEvent(this object obj, EventHandler handler, EventArgs e)
        {
            RaiseEvent(obj, handler, () =&gt; e);
        }

        public static void RaiseEvent(this object obj, EventHandler handler, Func&lt;EventArgs&gt; func)
        {
            if (handler == null)
                return;
            handler(obj, func());
        }

        public static void RaiseEvent&lt;TEventArgs&gt;(this object obj, EventHandler&lt;TEventArgs&gt; handler, TEventArgs e) where TEventArgs : EventArgs
        {
            RaiseEvent(obj, handler, () =&gt; e);
        }

        public static void RaiseEvent&lt;TEventArgs&gt;(this object obj, EventHandler&lt;TEventArgs&gt; handler,Func&lt;TEventArgs&gt; func) where TEventArgs : EventArgs
        {
            if (handler == null)
                return;
            handler(obj, func());
        }
    }

    class NameEventArgs : EventArgs
    {
        public string Name { get; set; }
    }

    class Person
    {
        private string _name;
        public string Name
        {
            get
            {
                if (_name == null)
                    return string.Empty;
                return _name;
            }
            set
            {
                if (_name != value)
                {
                    _name = value;
                    this.RaiseEvent(NameChanged, () =&gt; new NameEventArgs() { Name = value });
                }
            }
        }
        public event EventHandler&lt;NameEventArgs&gt; NameChanged;
    }

}</pre></div>

<p> </p>

<p>運行的結果如下：</p>

<p><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" src="\images\posts\33368\image_thumb.png" width="353" height="191" /></p>
