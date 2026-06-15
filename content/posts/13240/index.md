---
title: "[C#][VB.NET]FullScreen the winform"
slug: "[CSharp][VB.NET]FullScreen the winform"
date: "2010-01-24 12:00:24"
description: "[C#][VB.NET]FullScreen the winform"
tags: [VB.NET,CSharp]
---

在.NET程式中，若想要把視窗設為全螢幕，我們可以很簡單的透過FormBorderStyle與WindowState兩個屬性來完成。只要把視窗的FormBorderStyle屬性設為None，並把WindowState屬性設為Maximized，視窗就會變為全螢幕顯示。程式碼如下：

C#

```csharp
frm.FormBorderStyle = FormBorderStyle.None;
frm.WindowState = FormWindowState.Maximized;
```

VB.NET

```vb
frm.FormBorderStyle = FormBorderStyle.None
frm.WindowState = FormWindowState.Maximized
```

但在我的電腦使用，當把視窗最大化後在全螢幕的話，效果會不如我所預期。也許是全螢幕功能要由非最大化切到最大化時才會觸發，因此這邊我把程式改為下面這樣：

C#

```csharp
frm.FormBorderStyle = FormBorderStyle.None;
frm.WindowState = FormWindowState.Normal;
frm.WindowState = FormWindowState.Maximized;
```

VB.NET

```vb
frm.FormBorderStyle = FormBorderStyle.None
frm.WindowState = FormWindowState.Normal
frm.WindowState = FormWindowState.Maximized
```

若要把表單從全螢幕還原，我們也只要把上面設定的兩個屬性調回即可。

C#

```csharp
frm.FormBorderStyle = FormBorderStyle.Sizable;
frm.WindowState = FormWindowState.Normal;
```

VB.NET

```vb
frm.FormBorderStyle = FormBorderStyle.Sizable
frm.WindowState = FormWindowState.Normal
```

為了方便使用，我把它整理程了擴充方法，程式碼如下：

C#

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Collections.Specialized;

static class FullScreenExtension
{
    #region Struct
    struct FullScreenData
    {
        public FormBorderStyle FormBorderStyle { get; set; }
        public FormWindowState WindowState { get; set; }

        public FullScreenData(FormBorderStyle formBorderStyle, FormWindowState windowState):this()
        {
            this.FormBorderStyle = formBorderStyle;
            this.WindowState = windowState;
        }
    }
    #endregion

    #region Var
    private static Dictionary<Form, FullScreenData> _fullScreenDataPool;
    #endregion

    #region Private Property
    private static Dictionary<Form, FullScreenData> m_FullScreenDataPool
    {
        get
        {
            if (_fullScreenDataPool == null)
                _fullScreenDataPool = new Dictionary<Form, FullScreenData>();
            return _fullScreenDataPool;
        }
    }

    #endregion

    #region Public Method
    public static void FullScreen(this Form frm)
    {
        if (m_FullScreenDataPool.ContainsKey(frm))
            return;
        m_FullScreenDataPool.Add(frm, new FullScreenData(frm.FormBorderStyle,frm.WindowState));
        frm.FormBorderStyle = FormBorderStyle.None;
        frm.WindowState = FormWindowState.Normal;
        frm.WindowState = FormWindowState.Maximized;
    }

    public static void UnFullScreen(this Form frm)
    {
        if (!m_FullScreenDataPool.ContainsKey(frm))
            return;
        FullScreenData fd = m_FullScreenDataPool[frm];
        frm.WindowState = fd.WindowState;
        frm.FormBorderStyle = fd.FormBorderStyle;
        m_FullScreenDataPool.Remove(frm);
    }
    #endregion
}
```

VB.NET

```vb
Imports System.Runtime.CompilerServices

Module FullScreenExtension

#Region "Structure"
    Structure FullScreenData
        Private _formBorderStyle As FormBorderStyle
        Private _windowState As FormWindowState

        Public Property FormBorderStyle() As FormBorderStyle
            Get
                Return _formBorderStyle
            End Get
            Set(ByVal value As FormBorderStyle)
                _formBorderStyle = value
            End Set
        End Property

        Public Property WindowState() As FormWindowState
            Get
                Return _windowState
            End Get
            Set(ByVal value As FormWindowState)
                _windowState = value
            End Set
        End Property

        Sub New(ByVal formBorderStyle As FormBorderStyle, ByVal windowState As FormWindowState)
            With Me
                .FormBorderStyle = formBorderStyle
                .WindowState = windowState
            End With
        End Sub
    End Structure
#End Region

#Region "Var"
    Private _fullScreenDataPool As Dictionary(Of Form, FullScreenData)
#End Region

#Region "Private Property"
    Private ReadOnly Property m_FullScreenDataPool() As Dictionary(Of Form, FullScreenData)
        Get
            If _fullScreenDataPool Is Nothing Then
                _fullScreenDataPool = New Dictionary(Of Form, FullScreenData)
            End If
            Return _fullScreenDataPool
        End Get
    End Property
#End Region

#Region "Public Method"
    <Extension()> _
    Sub FullScreen(ByVal frm As Form)
        If m_FullScreenDataPool.ContainsKey(frm) Then
            Return
        End If
        With frm
            m_FullScreenDataPool.Add(frm, New FullScreenData(.FormBorderStyle, .WindowState))
            .FormBorderStyle = FormBorderStyle.None
            .WindowState = FormWindowState.Normal
            .WindowState = FormWindowState.Maximized
        End With
    End Sub

    <Extension()> _
    Sub UnFullScreen(ByVal frm As Form)
        If Not m_FullScreenDataPool.ContainsKey(frm) Then
            Return
        End If
        With frm
            Dim fd As FullScreenData = m_FullScreenDataPool(frm)
            .WindowState = fd.WindowState
            .FormBorderStyle = fd.FormBorderStyle
            m_FullScreenDataPool.Remove(frm)
        End With
    End Sub
#End Region

End Module
```

使用上就可像下面這樣呼叫：

C#

```csharp
using System;
using System.Windows.Forms;

namespace FullScreenExtensionDemo
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnFullScreen_Click(object sender, EventArgs e)
        {
            this.FullScreen();

        }

        private void btnUnFullScreen_Click(object sender, EventArgs e)
        {
            this.UnFullScreen();
        }

    }
}
```

VB.NET

```vb
Public Class FullScreenExtensionDemo

    Private Sub btnFullScreen_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnFullScreen.Click
        Me.FullScreen()
    End Sub

    Private Sub btnUnFullScreen_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnUnFullScreen.Click
        Me.UnFullScreen()
    End Sub
End Class
```
