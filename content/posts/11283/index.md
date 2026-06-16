---
title: "[C#]透過API移除表單的控制功能表方塊中的功能表項目"
slug: "csharp-透過api移除表單的控制功能表方塊中的功能表項目"
aliases: ["/posts/csharp透過api移除表單的控制功能表方塊中的功能表項目/"]
date: "2009-10-26 08:30:24"
description: "Introduction 看到了rico寫的[C#][WinForm]如何關閉表單\"X\"這篇文章，覺得還滿好玩的。又是一個沒玩過的寫法。在處理上也不難，只要透過GetSystemMenu.aspx)與RemoveMenu.aspx)這兩個簡單的API，就可以達到關閉視窗的關閉按鈕的效果了。"
tags: [CSharp]
---

## Introduction

看到了rico寫的[C#][WinForm]如何關閉表單"X"這篇文章，覺得還滿好玩的。又是一個沒玩過的寫法。在處理上也不難，只要透過[GetSystemMenu](http://msdn.microsoft.com/en-us/library/ms647985(VS.85).aspx)與[RemoveMenu](http://msdn.microsoft.com/en-us/library/ms647994(VS.85).aspx)這兩個簡單的API，就可以達到關閉視窗的關閉按鈕的效果了。這邊隨手記錄一下。

## 透過API移除表單的控制功能表方塊中的功能表項目

欲使用API移除表單的控制功能表方塊中的功能表項目，只需透過[GetSystemMenu](http://msdn.microsoft.com/en-us/library/ms647985(VS.85).aspx) API取得SystemMenu的Handle，再把取得的SystemMenu Handle與要關閉的功能選單索引當作參數，傳進RemoveMenu API即可。
![image_thumb_1.png](/images/posts/11283/image_thumb_1.png)

API詳細的使用方式可參考[GetSystemMenu](http://msdn.microsoft.com/en-us/library/ms647985(VS.85).aspx)與[RemoveMenu](http://msdn.microsoft.com/en-us/library/ms647994(VS.85).aspx)的MSDN說明文件。值得注意的是，RemoveMenu方法第二個參數所帶的索引值，為SystemMenu選單項目的索引。預設的系統選單畫面如下：
![image_thumb.png](/images/posts/11283/image_thumb.png)

其索引值如下：

<table border="1" cellpadding="2" cellspacing="0" width="400"><tbody> <tr> <td valign="top" width="200">功能表項目</td> <td valign="top" width="200">索引值</td> </tr> <tr> <td valign="top" width="200">Restore</td> <td valign="top" width="200">0</td> </tr> <tr> <td valign="top" width="200">Move</td> <td valign="top" width="200">1</td> </tr> <tr> <td valign="top" width="200">Size</td> <td valign="top" width="200">2</td> </tr> <tr> <td valign="top" width="200">Minimize</td> <td valign="top" width="200">3</td> </tr> <tr> <td valign="top" width="200">Maximize</td> <td valign="top" width="200">4</td> </tr> <tr> <td valign="top" width="200">Seperator</td> <td valign="top" width="200">5</td> </tr> <tr> <td valign="top" width="200">Close</td> <td valign="top" width="200">6</td> </tr> </tbody></table>

了解了實作方法，我們可以把此功能整理成如下類別：

```csharp
public class SystemMenuController
{
    [DllImport("user32.dll")]
    private static extern int GetSystemMenu(Int32 hWnd, Int32 bRevert);
    [DllImport("user32.dll")]
    private static extern int RemoveMenu(Int32 hMenu, Int32 nPosition, Int32 wFlags);

    const Int32 MF_BYPOSITION = 1024;//&H400

    public enum SystemMenuItemType
    {
        Restore,
        Move,
        Size,
        Min,
        Max,
        Seperator,
        Close
    }

   public static void RemoveSystemMenuItem(Form form, SystemMenuItemType menuItem)
    {
        RemoveMenu(GetSystemMenu(form.Handle.ToInt32(), 0),(int)menuItem, MF_BYPOSITION);
    }
    public static void RemoveRestoreSystemMenuItem(Form form)
    {
        RemoveSystemMenuItem(form, SystemMenuItemType.Restore);
    }

    public static void RemoveMoveSystemMenuItem(Form form)
    {
        RemoveSystemMenuItem(form, SystemMenuItemType.Move);
    }

    public static void RemoveSizeSystemMenuItem(Form form)
    {
        RemoveSystemMenuItem(form, SystemMenuItemType.Size);
    }

    public static void RemoveMinSystemMenuItem(Form form)
    {
        RemoveSystemMenuItem(form, SystemMenuItemType.Min);
    }

    public static void RemoveMaxSystemMenuItem(Form form)
    {
        RemoveSystemMenuItem(form, SystemMenuItemType.Max);
    }

    public static void RemoveSeperatorSystemMenuItem(Form form)
    {
        RemoveSystemMenuItem(form, SystemMenuItemType.Seperator);
    }

    public static void RemoveCloseSystemMenuItem(Form form)
    {
        RemoveSystemMenuItem(form, SystemMenuItemType.Close);
    }
}
```

使用上可以直接叫用，像這樣：

```csharp
SystemMenuController.RemoveCloseSystemMenu(this);
```

也可以把它整理成擴充方法：

```csharp
public static class SystemMenuExtendMethod
{
    [DllImport("user32.dll")]
    private static extern int GetSystemMenu(Int32 hWnd, Int32 bRevert);
    [DllImport("user32.dll")]
    private static extern int RemoveMenu(Int32 hMenu, Int32 nPosition, Int32 wFlags);

    const Int32 MF_BYPOSITION = 1024;//&H400

    public enum SystemMenuItemType
    {
        Restore,
        Move,
        Size,
        Min,
        Max,
        Seperator,
        Close
    }

    public static void RemoveSystemMenuItem(this Form form, SystemMenuItemType menuItem)
    {
        RemoveMenu(GetSystemMenu(form.Handle.ToInt32(), 0), (int)menuItem, MF_BYPOSITION);
    }

    public static void RemoveRestoreSystemMenuItem(this Form form)
    {
        RemoveSystemMenuItem(form, SystemMenuItemType.Restore);
    }

    public static void RemoveMoveSystemMenuItem(this Form form)
    {
        RemoveSystemMenuItem(form, SystemMenuItemType.Move);
    }

    public static void RemoveSizeSystemMenuItem(this Form form)
    {
        RemoveSystemMenuItem(form, SystemMenuItemType.Size);
    }

    public static void RemoveMinSystemMenuItem(this Form form)
    {
        RemoveSystemMenuItem(form, SystemMenuItemType.Min);
    }

    public static void RemoveMaxSystemMenuItem(this Form form)
    {
        RemoveSystemMenuItem(form, SystemMenuItemType.Max);
    }

    public static void RemoveSeperatorSystemMenuItem(this Form form)
    {
        RemoveSystemMenuItem(form, SystemMenuItemType.Seperator);
    }

    public static void RemoveCloseSystemMenuItem(this Form form)
    {
        RemoveSystemMenuItem(form, SystemMenuItemType.Close);
    }

}
```

在使用上會更為方便：

```csharp
private void Form1_Load(object sender, EventArgs e)
{
    this.RemoveCloseSystemMenuItem();
}
```

## 運行效果

值得注意的是，透過API移除不同的功能表項目，會對程式造成不一樣的效果。這邊我們可以大致了解一下。

當移除了Restore功能表項目，系統功能表選單項目會少了Restore選項。當視窗放到最大後，視窗的右上角的按鈕仍舊會跟一般的視窗放大後一樣。

![image_thumb_4.png](/images/posts/11283/image_thumb_4.png)

但按下中間的還原按鈕卻會沒有效果。

移除Move功能表項目，視窗會變得無法搬移。

移除Size功能表項目時，當滑鼠移至視窗邊緣，滑鼠游標仍會像一般視窗一樣變為可調整的游標圖示。

![image_thumb_5.png](/images/posts/11283/image_thumb_5.png)

但若真的試圖調整視窗大小，會發現調整大小的功能已經喪失。

若移除的是Minimize或是Maximize功能表選單。在視窗的外觀上無差異，視窗右上角的按鈕仍舊存在。只是在按下視窗上對應的功能按鈕時會變得無任何效果。

而若是移除Close功能表項目。在視窗右上角我們可以看到按鈕會變為灰階，且不可用滑鼠按下關閉。

![image_thumb_6.png](/images/posts/11283/image_thumb_6.png)

## Link

1. [C#][WinForm]如何關閉表單"X"
2. 如何移除表單的控制功能表方塊中的功能表項目
