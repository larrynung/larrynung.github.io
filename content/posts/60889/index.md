---
title: "[C#][WPF]WPF程式接收視窗訊息"
slug: "[CSharp][WPF]WPF程式接收視窗訊息"
date: "2011-12-06 01:15:51"
description: "[C#][WPF]WPF程式接收視窗訊息"
tags: [CSharp,WPF]
---
WinForm程式可以透過覆寫Window.WndProc去接收視窗訊息，而在WPF程式中的處理方法跟WinForm程式有些出入，首先必須要繫上SourceInitialized事件。
public MainWindow()
{
InitializeComponent();
this.SourceInitialized += new EventHandler(MainWindow_SourceInitialized);
}

在被繫上SourceInitialized事件的事件處理常式中將WndProc函式繫上。

void MainWindow_SourceInitialized(object sender, EventArgs e)
{
IntPtr hwnd = new WindowInteropHelper(this).Handle;
HwndSource.FromHwnd(hwnd).AddHook(new HwndSourceHook(WndProc));
}

在WndProc函式我們就可以收到視窗訊息並做些自己想要的處理。

IntPtr WndProc(IntPtr hwnd, int msg, IntPtr wParam, IntPtr lParam, ref bool handled)
{
switch (msg)
{
...
}
return IntPtr.Zero;
}

完整的範例程式如下：

using System;
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
///
/// Interaction logic for MainWindow.xaml
///
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
}

## Link

Attaching to WndProc in WPF