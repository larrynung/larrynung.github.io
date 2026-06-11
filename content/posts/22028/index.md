---
title: "[C#]RaiseEvent Extension Method (一)"
slug: "[CSharp]RaiseEvent Extension Method (一)"
date: "2011-03-23 01:11:00"
description: "[C#]RaiseEvent Extension Method (一)"
tags: [CSharp]
---

今天再調整程式中的事件，又注意到C#的事件實在是很囉唆，每次觸發事件前都要判斷一下事件處理常式是否有繫上，有繫上才能做觸發的動作。這樣的檢查動作隨著事件的增多，重複撰寫相同的邏輯會變得非常的頻繁。而在VB.NET中事件的觸發相較之下就容易得多，不需要自行判斷事件處理常式是否繫上，直接叫用RaiseEvent觸發事件就可以了。因此想說是否可以把這部分工作提出來，試了一下提出來後仍舊運行良好，這邊將其整理成擴充方法：

public static class ObjectExtension

{

    public static void RaiseEvent(this object obj, EventHandler handler, EventArgs e)

    {

        if (handler == null)

            return;

        handler(obj, e);

    }

    public static void RaiseEvent(this object obj, EventHandler handler, TEventArgs e) where TEventArgs : EventArgs

    {

        if (handler == null)

            return;

        handler(obj, e);

    }

}

使用上帶入EventHandler與事件的參數就可以了：

public event EventHandler NameChanged;

...

this.RaiseEvent(NameChanged, EventArgs.Empty);

...

完整程式碼範例：

using System;

using System.Collections.Generic;

using System.Linq;

using System.Text;

namespace ConsoleApplication2

{

    class Program

    {

        static void Main(string[] args)

        {

            Person Larry = new Person();

            Larry.NameChanged += new EventHandler(Larry_NameChanged);

            Larry.;           

        }

        static void Larry_NameChanged(object sender, EventArgs e)

        {

            Console.WriteLine("NameChanged...");

        }

    }

    public static class ObjectExtension

    {

        public static void RaiseEvent(this object obj, EventHandler handler, EventArgs e)

        {

            if (handler == null)

                return;

            handler(obj, e);

        }

        public static void RaiseEvent(this object obj, EventHandler handler, TEventArgs e) where TEventArgs : EventArgs

        {

            if (handler == null)

                return;

            handler(obj, e);

        }

    }

    class Person

    {

        private string _name;

        public string Name

        {

            get

            {

                if (_ null)

                    return string.Empty;

                return _name;

            }

            set

            {

                if (_name != value)

                {

                    _                     

                    this.RaiseEvent(NameChanged, EventArgs.Empty);

                }

            }

        }

        public event EventHandler NameChanged;

    }

}

運行結果：