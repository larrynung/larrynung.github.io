---
title: "[C#]Enable UAC Shield icons and run as administrator"
slug: "[CSharp]Enable UAC Shield icons and run as administrator"
date: "2011-11-23 01:20:05"
description: "[C#]Enable UAC Shield icons and run as administrator"
tags: [CSharp]
---

在Win7中常會看到某些程式中會有個按鈕，按鈕上會有個盾牌的圖示，按下後能提升存取權限。這邊紀錄一下這樣的功能要怎樣實現。

首先是盾牌的圖示，實作時不是自己去換按鈕的圖片，而是要對Button發送BCM_SETSHIELD(0x0000160C)的Message，訊息發送時lParam參數帶1或0去決定是否顯示盾牌圖示。這邊需注意的是因為這功能在vista以前不提供，所以必須做些處理，另外則是這功能必須要將按鈕的FlatStyle設為System，運行後才會有效果。

```c
#region Const
const int BCM_SETSHIELD = 0x0000160C;
#endregion

#region Private Method
private static bool AtLeastVista()
{
    return (Environment.OSVersion.Platform == PlatformID.Win32NT && Environment.OSVersion.Version.Major >= 6);
}

private static void SetButtonShield(Button btn, bool showShield)
{
    if (!AtLeastVista())
        return;

    btn.FlatStyle = FlatStyle.System;
    SendMessage(new HandleRef(btn, btn.Handle), BCM_SETSHIELD, IntPtr.Zero, showShield ? new IntPtr(1) : IntPtr.Zero);
}
#endregion
```

提升權限的部分則是透過Process去實現RunAs功能，比較要注意的是要帶入當下執行檔的位置，並將Verb設為runas。

```csharp
ProcessStartInfo psi = new ProcessStartInfo
     {
         Arguments = "-justelevated",
         ErrorDialog = true,
         ErrorDialogParentHandle = form.Handle,
         FileName = Application.ExecutablePath,
         Verb = "runas"
     };
```

這邊筆者方便後續使用，將其整理為擴充方法。

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Runtime.InteropServices;
using System.Diagnostics;

public static class ButtonExtension
{
    #region DllImport
    [DllImport("shell32.dll", EntryPoint = "#680", CharSet = CharSet.Unicode)]
    private static extern bool IsUserAnAdmin();

    [DllImport("user32.dll", CharSet = CharSet.Unicode)]
    private static extern IntPtr SendMessage(HandleRef hWnd, UInt32 Msg, IntPtr wParam, IntPtr lParam);
    #endregion

    #region Const
    const int BCM_SETSHIELD = 0x0000160C;
    #endregion

    #region Private Method
    private static bool AtLeastVista()
    {
        return (Environment.OSVersion.Platform == PlatformID.Win32NT && Environment.OSVersion.Version.Major >= 6);
    }

    private static void SetButtonShield(Button btn, bool showShield)
    {
        if (!AtLeastVista())
            return;

        btn.FlatStyle = FlatStyle.System;
        SendMessage(new HandleRef(btn, btn.Handle), BCM_SETSHIELD, IntPtr.Zero, showShield ? new IntPtr(1) : IntPtr.Zero);
    }

    private static Form GetWindowForm(Control control)
    {
        Control parent = control.Parent;

        if (parent == null)
            return null;

        if(parent is Form)
            return parent as Form;

        return GetWindowForm(parent);
    }
    #endregion

    #region Public Method
    public static void EnableShieldIcon(this Button button)
    {
        SetButtonShield(button, true);
    }

    public static void EnableRunAsProcess(this Button button)
    {
        button.Click -= new EventHandler(button_RunAsProcess);
        button.Click += new EventHandler(button_RunAsProcess);
    }
    #endregion

    #region Event Process
    private static void button_RunAsProcess(object sender, EventArgs e)
    {
        Button button = sender as Button;
        Form form = GetWindowForm(button);

        if (form == null)
            return;

        ProcessStartInfo psi = new ProcessStartInfo
        {
            Arguments = "-justelevated",
            ErrorDialog = true,
            ErrorDialogParentHandle = form.Handle,
            FileName = Application.ExecutablePath,
            Verb = "runas"
        };
        try
        {
            Process.Start(psi);
            form.Close();
        }
        catch (Exception ex)
        {
            MessageBox.Show(ex.Message);
        }
    }
    #endregion
}
```

使用時對Button去設定EnableShieldIcon與EnableRunAsProcess就可以了。

```csharp
private void Form1_Load(object sender, EventArgs e)
{
    button1.EnableShieldIcon();
    button1.EnableRunAsProcess();
}
```

運行後就會看到盾牌圖示，點擊按鈕也會將權限提升。

![image_thumb.png](/images/posts/59216/image_thumb.png)

## Link

* Shield icons, UAC, and process elevation in .NET on Windows 2000, XP, Vista, and 7
* User Account Control
* Windows Vista 控制項的增強功能
* BCM_SETSHIELD message
