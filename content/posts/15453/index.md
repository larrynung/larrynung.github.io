---
title: "[VB.NET]Win32 Color lt;=gt; .NET Color"
date: "2010-05-26 10:05:38"
description: "[VB.NET]Win32 Color <=> .NET Color"
tags: [VB.NET]
---

要做Win32 Color與.NET Color的互轉，可以自行轉換，也可以透過.NET Framework內建的ColorTranslator類別來做轉換。

若要自行轉換，首先必須了解到兩者在格式上的差異。Win32 Color在格式上儲存的順序為BGR，而.NET Color在格式上儲存順序則為RGB，依此調換儲存內容的順序即可做出兩者的轉換。

因此，.NET Color => Win32 Color可以像下面這般實作：
      Public Function GetColorFromWin32Color(ByVal win32Color As Integer) As Color
        Dim r As Integer = win32Color And &HFF
        Dim g As Integer = (win32Color >> 8) And &HFF
        Dim b As Integer = (win32Color >> 16) And &HFF
        Return Color.FromArgb(r, g, b)
    End Function

Win32 Color => .NET Color則可以如下這般實作：

    Public Function GetWin32ColorFromColor(ByVal color As Color) As Integer
        Return (CInt(color.B) << 16) Or (CInt(color.G) << 8) Or color.R
    End Function

而若要使用.NET Framework內建的ColorTranslator類別來做轉換，可參閱MSDN文件中ColorTranslator.FromWin32 方法與ColorTranslator.ToWin32 方法，直接帶入所需的參數呼叫函式即可。像是下面這樣：

Dim color As Color = Drawing.Color.White
Dim win32Color As Integer = ColorTranslator.ToWin32(color)
color = ColorTranslator.FromWin32(win32Color)