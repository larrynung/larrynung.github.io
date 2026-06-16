---
title: "[VB.NET]Control Mouse Actions with the mouse_event API"
slug: "vbnet-control-mouse-actions-with-the-mouse-event-api"
aliases: ["/posts/15365/"]
date: "2010-05-21 12:07:12"
description: "函式原型 參數 參數名稱 說明 dwFlags 指示滑鼠動作 dx x座標 (dwFlags有設MOUSEEVENTF_ABSOLUTE時，該座標為絕對座標) dy y座標 (dwFlags有設MOUSEEVENTF_ABSOLUTE時，"
tags: [VB.NET]
---

函式原型

```c
VOID WINAPI mouse_event(
  __in  DWORD dwFlags,
  __in  DWORD dx,
  __in  DWORD dy,
  __in  DWORD dwData,
  __in  ULONG_PTR dwExtraInfo
);
```

參數

<table border="1" cellpadding="2" cellspacing="0" width="497"><tbody>
<tr>
<td valign="top" width="91">參數名稱</td>
<td valign="top" width="404">說明</td>
</tr>
<tr>
<td valign="top" width="91"><em>dwFlags</em></td>
<td valign="top" width="404">指示滑鼠動作</td>
</tr>
<tr>
<td valign="top" width="91">dx</td>
<td valign="top" width="404">x座標 (dwFlags有設MOUSEEVENTF_ABSOLUTE時，該座標為絕對座標)</td>
</tr>
<tr>
<td valign="top" width="91">dy</td>
<td valign="top" width="404">y座標 (dwFlags有設MOUSEEVENTF_ABSOLUTE時，該座標為絕對座標)</td>
</tr>
<tr>
<td valign="top" width="91">dwData</td>
<td valign="top" width="404">dwFlags為MOUSEEVENTF_HWHEEL時，該值代表捲軸捲動的量。
        <br/>
<br/>dwFlags為MOUSEEVENTF_XDOWN或MOUSEEVENTF_XUP時，該值可為XBUTTON1 (&amp;H0001)或XBUTTON2 (&amp;H0002)。

        <br/>
<br/>當dwFlags不為MOUSEEVENTF_HWHEEL、

        <br/>MOUSEEVENTF_XDOWN或MOUSEEVENTF_XUP，該值為0。</td>
</tr>
<tr>
<td valign="top" width="91">dwExtraInfo</td>
<td valign="top" width="404">An additional value associated with the mouse event. An application calls <strong>GetMessageExtraInfo</strong> to obtain this extra information.</td>
</tr>
</tbody></table>

API宣告

```vb
Declare Sub mouse_event Lib "user32" Alias "mouse_event" (ByVal dwFlags As Integer, ByVal dx As Integer, ByVal dy As Integer, ByVal dwData As Integer, ByVal dwExtraInfo As Integer)
```

簡易使用類別整理如下

```vb
Public Class MouseControler

    Private Declare Function mouse_event Lib "user32.dll" Alias "mouse_event" (ByVal dwFlags As MouseEvent, ByVal dX As Int32, ByVal dY As Int32, ByVal dwData As Int32, ByVal dwExtraInfo As Int32) As Boolean

    <Flags()> _
    Enum MouseEvent
        None
        AbsoluteLocation = &H8000
        LeftButtonDown = &H2
        LeftButtonUp = &H4
        Move = &H1
        MiddleButtonDown = &H20
        MiddleButtonUp = &H40
        RightButtonDown = &H8
        RightButtonUp = &H10
        Wheel = &H800
        WheelDelta = 120
        XButtonDown = &H100
        XButtonUp = &H200
    End Enum

#Region "Public Shared Method"
    Public Shared Sub LeftButtonDown()
        LeftButtonDown(0, 0, False)
    End Sub

    Public Shared Sub LeftButtonDown(ByVal x As Integer, ByVal y As Integer, Optional ByVal absolateLocation As Boolean = True)
        mouse_event(MouseEvent.LeftButtonDown Or If(absolateLocation, MouseEvent.AbsoluteLocation, MouseEvent.None), x, y, 0, 0)
    End Sub

    Public Shared Sub LeftButtonUp()
        LeftButtonUp(0, 0, False)
    End Sub

    Public Shared Sub LeftButtonUp(ByVal x As Integer, ByVal y As Integer, Optional ByVal absolateLocation As Boolean = True)
        mouse_event(MouseEvent.LeftButtonUp Or If(absolateLocation, MouseEvent.AbsoluteLocation, MouseEvent.None), x, y, 0, 0)
    End Sub

    Public Shared Sub LeftButtonClick()
        LeftButtonClick(0, 0, False)
    End Sub

    Public Shared Sub LeftButtonClick(ByVal x As Integer, ByVal y As Integer, Optional ByVal absolateLocation As Boolean = True)
        LeftButtonDown(x, y, absolateLocation)
        LeftButtonUp(x, y, absolateLocation)
    End Sub

    Public Shared Sub LeftButtonDoubleClick()
        LeftButtonDoubleClick(0, 0, False)
    End Sub

    Public Shared Sub LeftButtonDoubleClick(ByVal x As Integer, ByVal y As Integer, Optional ByVal absolateLocation As Boolean = True)
        LeftButtonClick(x, y, absolateLocation)
        LeftButtonClick(x, y, absolateLocation)
    End Sub

    Public Shared Sub MiddleButtonDown()
        MiddleButtonDown(0, 0, False)
    End Sub

    Public Shared Sub MiddleButtonDown(ByVal x As Integer, ByVal y As Integer, Optional ByVal absolateLocation As Boolean = True)
        mouse_event(MouseEvent.MiddleButtonDown Or If(absolateLocation, MouseEvent.AbsoluteLocation, MouseEvent.None), x, y, 0, 0)
    End Sub

    Public Shared Sub MiddleButtonUp()
        MiddleButtonUp(0, 0, False)
    End Sub

    Public Shared Sub MiddleButtonUp(ByVal x As Integer, ByVal y As Integer, Optional ByVal absolateLocation As Boolean = True)
        mouse_event(MouseEvent.MiddleButtonUp Or If(absolateLocation, MouseEvent.AbsoluteLocation, MouseEvent.None), x, y, 0, 0)
    End Sub

    Public Shared Sub MiddleButtonClick()
        MiddleButtonClick(0, 0, False)
    End Sub

    Public Shared Sub MiddleButtonClick(ByVal x As Integer, ByVal y As Integer, Optional ByVal absolateLocation As Boolean = True)
        MiddleButtonDown(x, y, absolateLocation)
        MiddleButtonUp(x, y, absolateLocation)
    End Sub

    Public Shared Sub MiddleButtonDoubleClick()
        MiddleButtonDoubleClick(0, 0, False)
    End Sub

    Public Shared Sub MiddleButtonDoubleClick(ByVal x As Integer, ByVal y As Integer, Optional ByVal absolateLocation As Boolean = True)
        MiddleButtonClick(x, y, absolateLocation)
        MiddleButtonClick(x, y, absolateLocation)
    End Sub

    Public Shared Sub RightButtonDown()
        RightButtonDown(0, 0, False)
    End Sub

    Public Shared Sub RightButtonDown(ByVal x As Integer, ByVal y As Integer, Optional ByVal absolateLocation As Boolean = True)
        mouse_event(MouseEvent.RightButtonDown Or If(absolateLocation, MouseEvent.AbsoluteLocation, MouseEvent.None), x, y, 0, 0)
    End Sub

    Public Shared Sub RightButtonUp()
        RightButtonUp(0, 0, False)
    End Sub

    Public Shared Sub RightButtonUp(ByVal x As Integer, ByVal y As Integer, Optional ByVal absolateLocation As Boolean = True)
        mouse_event(MouseEvent.RightButtonUp Or If(absolateLocation, MouseEvent.AbsoluteLocation, MouseEvent.None), x, y, 0, 0)
    End Sub

    Public Shared Sub RightButtonClick()
        RightButtonClick(0, 0, False)
    End Sub

    Public Shared Sub RightButtonClick(ByVal x As Integer, ByVal y As Integer, Optional ByVal absolateLocation As Boolean = True)
        RightButtonDown(x, y, absolateLocation)
        RightButtonUp(x, y, absolateLocation)
    End Sub

    Public Shared Sub RightButtonDoubleClick()
        RightButtonDoubleClick(0, 0, False)
    End Sub

    Public Shared Sub RightButtonDoubleClick(ByVal x As Integer, ByVal y As Integer, Optional ByVal absolateLocation As Boolean = True)
        RightButtonClick(x, y, absolateLocation)
        RightButtonClick(x, y, absolateLocation)
    End Sub

    Public Shared Sub Wheel(ByVal scrollValue As Integer)
        mouse_event(MouseEvent.Wheel, 0, 0, scrollValue, 0)
    End Sub

#End Region

End Class
```

## Link

* mouse_event Function
* pinvoke.net: mouse_event (user32)
* 用Mouse_event（）来控制鼠标操作
* Simulate a mouse click in a program
