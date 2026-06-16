---
title: "[C#]Set Windows 7 Progress Bar's State"
slug: "[CSharp]Set Windows 7 Progress Bar's State"
date: "2013-11-06 12:00:00"
description: "要在Win7設定Progressbar的運行狀態，可能是一般運行狀態，可能是暫停狀態，或是錯誤狀態。 我們可以透過SendMessage發送PBM_SETSTATE訊息給ProgressBar，訊息的wParam依需求可帶入PBST_NORMAL、PBST_ERROR、與PBST_PAUSED，"
tags: [CSharp]
---

要在Win7設定Progressbar的運行狀態，可能是一般運行狀態，可能是暫停狀態，或是錯誤狀態。

![image_thumb_4.png](/images/posts/85f5fb35-b5fe-4572-9f96-73518531e017/image_thumb_4.png)

我們可以透過SendMessage發送PBM_SETSTATE訊息給ProgressBar，訊息的wParam依需求可帶入PBST_NORMAL、PBST_ERROR、與PBST_PAUSED，lParam部分則帶入0就可以了。

![image_thumb_3.png](/images/posts/85f5fb35-b5fe-4572-9f96-73518531e017/image_thumb_3.png)

程式撰寫起來會像下面這樣：

```csharp
#region Const
const int PBM_SETSTATE = 0x410;
const int PBST_PAUSE = 0x0003;
const int PBST_ERROR = 0x0002;
const int PBST_NORMAL = 0x0001;
#endregion

#region DllImport
[DllImport("user32.dll", CharSet = CharSet.Auto)]
internal static extern int SendMessage(IntPtr hWnd, int wMsg, int wParam, int lParam);
#endregion

#region Private Method
void SetPaused(ProgressBar progressBar)
{
    SendMessage(progressBar.Handle, PBM_SETSTATE, PBST_PAUSE, 0);
}

void SetError(ProgressBar progressBar)
{
    SendMessage(progressBar.Handle, PBM_SETSTATE, PBST_ERROR, 0);
}

void SetNormal(ProgressBar progressBar)
{
    SendMessage(progressBar.Handle, PBM_SETSTATE, PBST_NORMAL, 0);
}
#endregion
```

這邊用此概念做個簡單的示意範例：

```csharp
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApplication3
{
    public partial class Form1 : Form
    {
        #region Const
        const int PBM_SETPOS = 0x402;
        const int PBM_GETPOS = 0x0408;
        const int PBM_SETSTATE = 0x410;
        const int PBST_PAUSE = 0x0003;
        const int PBST_ERROR = 0x0002;
        const int PBST_NORMAL = 0x0001;
        #endregion

        #region DllImport
        [DllImport("user32.dll", CharSet = CharSet.Auto)]
        internal static extern int SendMessage(IntPtr hWnd, int wMsg, int wParam, int lParam);
        #endregion

        #region Private Method
        void SetPaused(ProgressBar progressBar)
        {
            SendMessage(progressBar.Handle, PBM_SETSTATE, PBST_PAUSE, 0);
        }

        void SetError(ProgressBar progressBar)
        {
            SendMessage(progressBar.Handle, PBM_SETSTATE, PBST_ERROR, 0);
        }

        void SetNormal(ProgressBar progressBar)
        {
            SendMessage(progressBar.Handle, PBM_SETSTATE, PBST_NORMAL, 0);
        }
        #endregion

        public Form1()
        {
            InitializeComponent();
        }

        private void trackBar1_Scroll(object sender, EventArgs e)
        {
            SendMessage(progressBar1.Handle, PBM_SETPOS, trackBar1.Value, 0);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            SetNormal(progressBar1);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            SetPaused(progressBar1);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            SetError(progressBar1);
        }
    }
}
```

當按下不同狀態按鈕，ProgressBar會有不同的呈現。

![image_thumb.png](/images/posts/85f5fb35-b5fe-4572-9f96-73518531e017/image_thumb.png)

![image_thumb_1.png](/images/posts/85f5fb35-b5fe-4572-9f96-73518531e017/image_thumb_1.png)

![image_thumb_2.png](/images/posts/85f5fb35-b5fe-4572-9f96-73518531e017/image_thumb_2.png)

為了方便起見也可以將之整理成擴充方法。

```csharp
public static class ProgressExtension
{
    #region Const
    const int PBM_SETSTATE = 0x410;
    const int PBST_PAUSE = 0x0003;
    const int PBST_ERROR = 0x0002;
    const int PBST_NORMAL = 0x0001;
    #endregion

    #region DllImport
    [DllImport("user32.dll", CharSet = CharSet.Auto)]
    internal static extern int SendMessage(IntPtr hWnd, int wMsg, int wParam, int lParam);
    #endregion

    #region Public Method
    public static void SetNormalState(this ProgressBar progressBar)
    {
        SendMessage(progressBar.Handle, PBM_SETSTATE, PBST_NORMAL, 0);
    }

    public static void SetPauseState(this ProgressBar progressBar)
    {
        SendMessage(progressBar.Handle, PBM_SETSTATE, PBST_PAUSE, 0);
    }

    public static void SetErrorState(this ProgressBar progressBar)
    {
        SendMessage(progressBar.Handle, PBM_SETSTATE, PBST_ERROR, 0);
    }
    #endregion
}
```

使用上會更為方便簡潔。

```csharp
public partial class Form1 : Form
{
    public Form1()
    {
        InitializeComponent();
    }

    private void trackBar1_Scroll(object sender, EventArgs e)
    {
        progressBar1.Value = trackBar1.Value;
    }

    private void button1_Click(object sender, EventArgs e)
    {
        progressBar1.SetNormalState();
    }

    private void button2_Click(object sender, EventArgs e)
    {
        progressBar1.SetPauseState();
    }

    private void button3_Click(object sender, EventArgs e)
    {
        progressBar1.SetErrorState();
    }
}
```

## Link

* Windows 7 Progress Bars in .NET
* PBM_SETSTATE message
