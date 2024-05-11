---
title: "[C#][WPF]WPF程式接收視窗訊息"
slug: "[CSharp][WPF]WPF程式接收視窗訊息"
date: "2011-12-06 01:15:51"
description: "[C#][WPF]WPF程式接收視窗訊息"
tags: [CSharp,WPF]
---

<p>WinForm程式可以透過覆寫Window.WndProc去接收視窗訊息，而在WPF程式中的處理方法跟WinForm程式有些出入，首先必須要繫上SourceInitialized事件。</p>  <div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:d1e70b86-84b8-48d6-b766-255fd696e0e0" class="wlWriterSmartContent"><pre name="code" class="c#">public MainWindow()
{
    InitializeComponent();
    this.SourceInitialized += new EventHandler(MainWindow_SourceInitialized);
}</pre></div>

<p> </p>

<p>在被繫上SourceInitialized事件的事件處理常式中將WndProc函式繫上。</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:79c6440c-3e85-4af8-b68a-18f4a949708b" class="wlWriterSmartContent"><pre name="code" class="c#">void MainWindow_SourceInitialized(object sender, EventArgs e)
{
    IntPtr hwnd = new WindowInteropHelper(this).Handle;
    HwndSource.FromHwnd(hwnd).AddHook(new HwndSourceHook(WndProc));
}</pre></div>

<p> </p>

<p>在WndProc函式我們就可以收到視窗訊息並做些自己想要的處理。</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:9e190f54-df70-400e-afeb-b6cb5461161e" class="wlWriterSmartContent"><pre name="code" class="c#">IntPtr WndProc(IntPtr hwnd, int msg, IntPtr wParam, IntPtr lParam, ref bool handled)
{
    switch (msg)
    { 
        ...
    }
    return IntPtr.Zero;
}</pre></div>

<p> </p>

<p>完整的範例程式如下：</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:ce31c25d-79f7-4e6f-9dfc-f92eeb4dcd7b" class="wlWriterSmartContent"><pre name="code" class="c#">using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.Windows.Interop;

namespace WpfApplication2
{
    /// &lt;summary&gt;
    /// Interaction logic for MainWindow.xaml
    /// &lt;/summary&gt;
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            this.SourceInitialized += new EventHandler(MainWindow_SourceInitialized);
        }

        void MainWindow_SourceInitialized(object sender, EventArgs e)
        {
            IntPtr hwnd = new WindowInteropHelper(this).Handle;
            HwndSource.FromHwnd(hwnd).AddHook(new HwndSourceHook(WndProc));
        }

        IntPtr WndProc(IntPtr hwnd, int msg, IntPtr wParam, IntPtr lParam, ref bool handled)
        {
            switch (msg)
            { 
                //...
            }
            return IntPtr.Zero;
        }
    }
}</pre></div>

<p> </p>

<h2>Link</h2>

<ul>
  <li>Attaching to WndProc in WPF</li>
</ul>
