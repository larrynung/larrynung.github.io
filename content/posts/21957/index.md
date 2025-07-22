---
title: "[C#]快速將字串轉換為結構"
slug: "[CSharp]快速將字串轉換為結構"
date: "2011-03-19 09:20:12"
description: "[C#]快速將字串轉換為結構"
tags: [CSharp]
---看到MSDN上請問將一個字串copy到一個結構中最快的方式為何?這篇的發問，做些紀錄：

要將字串快速轉換為結構，首先我們必須要在結構上加些Attribute，像是設定每個欄位所佔用的型態、大小...等：
[StructLayout(LayoutKind.Sequential, CharSet = CharSet.Unicode)]
public struct MyStruct
{
    [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 4)]
    public string fname;
    [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 4)]
    public string lname;
    [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 7)]
    public string phone;
}

在轉換時先透過Marshal.StringToBSTR將字串轉為指標，再透過Marshal.PtrToStructure將指標轉換為指定的結構型態，最後再用Marshal.FreeBSTR把剛剛的指標位置給釋放掉就可以了：

private static T ConvertToStruct(string val)
{
    IntPtr valPoint = Marshal.StringToBSTR(val);
    T ret = (T)Marshal.PtrToStructure(valPoint, typeof(T));
    Marshal.FreeBSTR(valPoint);
    return ret;
}

完整範例如下：

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;
using System.Runtime.InteropServices;

namespace ConsoleApplication20
{
    class Program
    {
        [StructLayout(LayoutKind.Sequential, CharSet = CharSet.Unicode)]
        public struct MyStruct
        {
            [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 4)]
            public string fname;
            [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 4)]
            public string lname;
            [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 7)]
            public string phone;
        }

        private static T ConvertToStruct(string val)
        {
            IntPtr valPoint = Marshal.StringToBSTR(val);
            T ret = (T)Marshal.PtrToStructure(valPoint, typeof(T));
            Marshal.FreeBSTR(valPoint);
            return ret;
        }

        public static void Main()
        {
            MyStruct ms = ConvertToStruct("abcdefgh2223333");
            Console.WriteLine("fname is: {0}", ms.fname);
            Console.WriteLine("lname is: {0}", ms.lname);
            Console.WriteLine("phone is: {0}", ms.phone);         
        }
    }
}

運行後可以發現abcdefgh2223333字串會依照我們在結構欄位所設定的長度自動填入：

## Link

How to copy a String into a struct using C#

請問將一個字串copy到一個結構中最快的方式為何?