---
title: "[VB.NET]SecureString較為安全的加密字串類別"
date: "2010-04-29 02:10:06"
description: "Namespace System.Security Framework 2.0 or Latter SecureString SecureString是.NET 2.0開始提供的加密字串類別，為一較安全的字串處理類別，適合用以保存較為機密或是較為敏感的字串。"
tags: [VB.NET]
---

## Namespace

System.Security

## Framework

2.0 or Latter

## SecureString

SecureString是.NET 2.0開始提供的加密字串類別，為一較安全的字串處理類別，適合用以保存較為機密或是較為敏感的字串。

SecureString內部使用DPAPI對記憶體作加密的動作，存入的資料會自動進行加密的動作，甚至可以使用MakeReadOnly方法讓物件執行個體設為唯讀狀態，避免被進一步修改。

在記憶體層級的保護上，對於該物件執行個體所使用的記憶體會被禁止作複製的動作(除非自行呼叫複製)。

SecureString提供較少的類別成員，像是檢查、比較或轉換等成員皆未提供，有助於防止執行個體值被不慎或惡意公開。此外，也有實作IDisposiable介面，可在不需使用資源時作即時的資源釋放，不像String一樣需等待GC的回收，減少機密資料存在記憶體中的時間，降低被竊取的風險。

## 重要成員

屬性

<table border="1" cellpadding="2" cellspacing="0" width="391"><tbody> <tr> <td valign="top" width="110">名稱</td> <td valign="top" width="279">說明</td> </tr> <tr> <td valign="top" width="110"><a href="http://msdn.microsoft.com/zh-tw/library/system.security.securestring.length(v=VS.90).aspx" target="_blank">Length</a></td> <td valign="top" width="279">取得目前安全字串的長度。</td> </tr> </tbody></table>

方法

<table border="1" cellpadding="2" cellspacing="0" width="389"><tbody> <tr> <td valign="top" width="113">名稱</td> <td valign="top" width="274">說明</td> </tr> <tr> <td valign="top" width="113"><a href="http://msdn.microsoft.com/zh-tw/library/system.security.securestring.appendchar(v=VS.90).aspx" target="_blank">AppendChar</a></td> <td valign="top" width="274">將字元附加至目前安全字串的結尾。</td> </tr> <tr> <td valign="top" width="113"><a href="http://msdn.microsoft.com/zh-tw/library/system.security.securestring.clear(v=VS.90).aspx" target="_blank">Clear</a></td> <td valign="top" width="274">刪除目前安全字串的值。</td> </tr> <tr> <td valign="top" width="113"><a href="http://msdn.microsoft.com/zh-tw/library/system.security.securestring.copy(v=VS.90).aspx" target="_blank">Copy</a></td> <td valign="top" width="274">建立目前安全字串的複本</td> </tr> <tr> <td valign="top" width="113"><a href="http://msdn.microsoft.com/zh-tw/library/system.security.securestring.dispose(v=VS.90).aspx" target="_blank">Dispose</a></td> <td valign="top" width="274">釋放由目前的 <a href="http://msdn.microsoft.com/zh-tw/library/system.security.securestring(v=VS.90).aspx" target="_blank">SecureString</a> 物件使用的所有資源。</td> </tr> <tr> <td valign="top" width="113"><a href="http://msdn.microsoft.com/zh-tw/library/system.security.securestring.insertat(v=VS.90).aspx" target="_blank">InsertAt</a></td> <td valign="top" width="274">將這個安全字串中的字元插入指定索引位置。</td> </tr> <tr> <td valign="top" width="113"><a href="http://msdn.microsoft.com/zh-tw/library/system.security.securestring.isreadonly(v=VS.90).aspx" target="_blank">IsReadOnly</a></td> <td valign="top" width="274">指示這個安全字串是否標示為唯讀。</td> </tr> <tr> <td valign="top" width="113"><a href="http://msdn.microsoft.com/zh-tw/library/system.security.securestring.makereadonly(v=VS.90).aspx" target="_blank">MakeReadOnly</a></td> <td valign="top" width="274">使這個安全字串的文字值成為唯讀。</td> </tr> <tr> <td valign="top" width="113"><a href="http://msdn.microsoft.com/zh-tw/library/system.security.securestring.removeat(v=VS.90).aspx" target="_blank">RemoveAt</a></td> <td valign="top" width="274">從這個安全字串移除位在指定索引位置的字元。</td> </tr> <tr> <td valign="top" width="113"><a href="http://msdn.microsoft.com/zh-tw/library/system.security.securestring.setat(v=VS.90).aspx" target="_blank">SetAt</a></td> <td valign="top" width="274">使用另一個字元，取代位在指定索引位置的現有字元。</td> </tr> </tbody></table>

## 設定字串

```vb
Const testString As String = "Level Up"  '要寫入的字串
Dim secureString As New SecureString
For Each c In testString
    secureString.AppendChar(c)           '使用AppendChar加入SecureString
Next
secureString.MakeReadOnly()              '設定為唯讀狀態
```

## 讀取字串

```vb
'配置 BSTR，並將 Managed SecureString 物件的內容複製到其中。
Dim stringPointer As IntPtr = Marshal.SecureStringToBSTR(secureString)
Try
    '配置 Managed String，並將儲存在 Unmanaged 記憶體的 BSTR 字串複製到其中，並顯示出來。
    Console.WriteLine(Marshal.PtrToStringBSTR(stringPointer))
Finally
    '釋放之前使用 SecureStringToBSTR 方法配置的 BSTR 指標。
    Marshal.ZeroFreeBSTR(stringPointer)
End Try
```

## 清除字串

```vb
Sub Main()
    Dim secureString As New SecureString
    ...
    Console.WriteLine("原字串...")
    PrintSecureString(secureString)
    secureString.Clear()                     '使用Clear清除SecureString字串內容
    Console.WriteLine()
    Console.WriteLine("Clear呼叫後...")
    PrintSecureString(secureString)
End Sub

Public Sub PrintSecureString(ByVal secureString As SecureString)
...
End Sub
```

## 完整範例

該範例主要是參閱How to: Use strings in a secure manner with SecureString class與[Making Strings More Secure兩篇的範例所撰寫。](http://blogs.msdn.com/shawnfa/archive/2004/05/27/143254.aspx)

```vb
Imports System.Security
Imports System.Runtime.InteropServices

Module Module1

    Sub Main()
        Console.WriteLine("Please enter your password to be encrypted:")

        Dim password As SecureString = ReadPassword()

        Console.WriteLine()

        Console.WriteLine("Decripted password:")

        PrintPassword(password)
    End Sub

    Public Function ReadPassword() As SecureString

        Dim password As New SecureString()

        Dim nextKey As ConsoleKeyInfo = Console.ReadKey(True)

        While nextKey.Key <> ConsoleKey.Enter
            If nextKey.Key = ConsoleKey.Backspace Then
                If password.Length > 0 Then
                    password.RemoveAt(password.Length - 1)

                    ' erase the last * as well
                    Console.Write(nextKey.KeyChar)
                    Console.Write(" ")
                    Console.Write(nextKey.KeyChar)
                End If
            Else
                password.AppendChar(nextKey.KeyChar)
                Console.Write("*")
            End If

            nextKey = Console.ReadKey(True)
        End While

        password.MakeReadOnly()
        ' make the password read-only.

        ' return the encrypted password.

        Return password

    End Function

    Public Sub PrintPassword(ByVal password As SecureString)

        ' Uncrypt the password and get a reference to it...

        Dim bstr As IntPtr = Marshal.SecureStringToBSTR(password)

        Try
            ' Printing the uncrypted password...

            Console.WriteLine(Marshal.PtrToStringBSTR(bstr))

        Finally

            Marshal.ZeroFreeBSTR(bstr)

        End Try

    End Sub

End Module
```

![image_thumb_3.png](/images/posts/14918/image_thumb_3.png)

## Link

* SecureString 類別
* SecureString 應用程式範例
* Security Enhancements in the .NET Framework 2.0
* SecureString in .Net 2.0
* How to: Use strings in a secure manner with SecureString class
* Making Strings More Secure
* C# SecureString
