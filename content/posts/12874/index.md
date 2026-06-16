---
title: "[VB.NET]Convert Between ASCII String and Hex String"
slug: "vbnet-convert-between-ascii-string-and-hex-string"
aliases: ["/posts/12874/"]
date: "2010-01-06 09:26:50"
description: "ASCII要轉Hex，可透過ToString函式帶入\"X2\"，或是用Hex函式。因此ASCII String轉Hex String可寫成： 而Hex要轉ASCII，可在前面帶入\"&h\"字串，轉成int後再轉為char。"
tags: [VB.NET]
---

ASCII要轉Hex，可透過ToString函式帶入"X2"，或是用Hex函式。因此ASCII String轉Hex String可寫成：

```vb
Public Function AsciiStringToHexString(ByVal asciiString As String) As String
    Dim ascii() As Byte = System.Text.Encoding.Default.GetBytes(asciiString)
    Dim count As Integer = ascii.Length
    Dim hexArray(count - 1) As String
    For idx As Integer = 0 To count - 1
        hexArray(idx) = ascii(idx).ToString("x2")
    Next
    Return String.Join(" ", hexArray)
End Function
```

而Hex要轉ASCII，可在前面帶入"&h"字串，轉成int後再轉為char。因此Hex String轉ASCII String可寫成:

```vb
Public Function HexStringToAsciiString(ByVal hexString As String) As String
    Dim array() As String = hexString.Split(New Char() {" "c}, StringSplitOptions.RemoveEmptyEntries)
    For idx As Integer = 0 To array.Length - 1
        array(idx) = Chr(CInt(String.Format("&h{0}", array(idx))))
    Next
    Return String.Join(String.Empty, array)
End Function
```

## 程式範例

範例介面

![image_thumb.png](/images/posts/12874/image_thumb.png)

完整範例如下：

```vb
Public Class Form1

    Public Function AsciiStringToHexString(ByVal asciiString As String) As String
        Dim ascii() As Byte = System.Text.Encoding.Default.GetBytes(asciiString)
        Dim count As Integer = ascii.Length
        Dim hexArray(count - 1) As String
        For idx As Integer = 0 To count - 1
            hexArray(idx) = ascii(idx).ToString("x2")
        Next
        Return String.Join(" ", hexArray)
    End Function

    Public Function HexStringToAsciiString(ByVal hexString As String) As String
        Dim array() As String = hexString.Split(New Char() {" "c}, StringSplitOptions.RemoveEmptyEntries)
        For idx As Integer = 0 To array.Length - 1
            array(idx) = Chr(CInt(String.Format("&h{0}", array(idx))))
        Next
        Return String.Join(String.Empty, array)
    End Function

    Private Sub tbxASCII_TextChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles tbxASCII.TextChanged
        If Me.ActiveControl Is sender Then
            tbxHex.Text = AsciiStringToHexString(tbxASCII.Text)
        End If
    End Sub

    Private Sub tbxHex_TextChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles tbxHex.TextChanged
        If Me.ActiveControl Is sender Then
            tbxASCII.Text = HexStringToAsciiString(tbxHex.Text)
        End If
    End Sub
End Class
```
