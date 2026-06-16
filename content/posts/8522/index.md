---
title: "[C#][VB.NET]壓縮.NET程式的記憶體用量"
slug: "csharp-vbnet-壓縮-dotnet-程式的記憶體用量"
aliases: ["/posts/csharpvb.net壓縮.net程式的記憶體用量/"]
date: "2009-05-22 09:37:21"
description: ".NET程式的記憶體用量一直以來都是程式設計師所關注的焦點。因為.NET程式必需載入.NET Framework的關係，記憶體用量動輒就至少10MB以上。 對於觀察敏銳的人來說，相信應該都有注意到某個奇特的現象，那就是當我們把程式視窗縮小至工具列時，記憶體就會驟減。"
tags: [CSharp,VB.NET]
---

.NET程式的記憶體用量一直以來都是程式設計師所關注的焦點。因為.NET程式必需載入.NET Framework的關係，記憶體用量動輒就至少10MB以上。

![image_thumb.png](/images/posts/8522/image_thumb.png)

對於觀察敏銳的人來說，相信應該都有注意到某個奇特的現象，那就是當我們把程式視窗縮小至工具列時，記憶體就會驟減。

![image_thumb_1.png](/images/posts/8522/image_thumb_1.png)

這現象好像是因為作業系統會把虛擬內存轉為物理內存的關係。大多數觀察到這現象的人都會利用把應用程式縮小來壓縮程式的記憶體用量。但這樣做起來有點笨拙，站在使用者的觀點來看也是怪怪的，甚至會造成使用者使用上的不便。

其實同樣的效果，我們也可以透過SetProcessWorkingSetSize API來達到。

**API宣告方式**

VB.NET

```
Private Declare Auto Function SetProcessWorkingSetSize Lib "kernel32.dll" _
(ByVal procHandle As IntPtr, ByVal min As Int32, ByVal max As Int32) As Boolean
```

C#

```
[DllImport ("kernel32.dll")]
static extern Boolean SetProcessWorkingSetSize(IntPtr procHandle, Int32 min, Int32 max) ;
```

**使用方式**

VB.NET

```
SetProcessWorkingSetSize(Process.GetCurrentProcess().Handle, -1, -1)
```

C#

```
SetProcessWorkingSetSize(Process.GetCurrentProcess().Handle, -1, -1);
```

## 範例程式

**範例界面**

![image17_thumb.png](/images/posts/8522/image17_thumb.png)

**範例程式碼**

VB.NET

```
Public Class Form1

#Region "Declare"
    Private Declare Auto Function SetProcessWorkingSetSize Lib "kernel32.dll" (ByVal procHandle As IntPtr, ByVal min As Int32, ByVal max As Int32) As Boolean
#End Region

#Region "Private Method"
    Private Sub CompressMemory()
        SetProcessWorkingSetSize(Process.GetCurrentProcess().Handle, -1, -1)
    End Sub
#End Region

#Region "Event Process"
    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
        CompressMemory()
    End Sub
#End Region
End Class
```

C#

```
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Runtime.InteropServices;
using System.Diagnostics;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        [DllImport ("kernel32.dll")]
        static extern Boolean SetProcessWorkingSetSize(IntPtr procHandle, Int32 min, Int32 max) ;

        public Form1()
        {
            InitializeComponent();
        }

        private void CompressMemory()
        {
            SetProcessWorkingSetSize(Process.GetCurrentProcess().Handle, -1, -1);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            CompressMemory();
        }
    }
}
```
