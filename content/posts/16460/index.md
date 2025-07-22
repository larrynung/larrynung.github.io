---
title: "[C#]使用Win32 API為編輯框與下拉方塊加上提示字串"
slug: "[CSharp]使用Win32 API為編輯框與下拉方塊加上提示字串"
date: "2010-07-08 11:03:48"
description: "[C#]使用Win32 API為編輯框與下拉方塊加上提示字串"
tags: [CSharp]
---

Windows在XP與2003開始對單行編輯框支援顯示提示字串的功能，在Vista與2008以後下拉方塊也開始有了支援，多半這樣的功能被用在搜尋框上。像是Windows Live Mail、Windows 7等的搜尋框就是很好的例子。

## 為編輯框加上提示字串
 
要為編輯框加上提示字串，首先我們必須先了解EM_SETCUEBANNER訊息，該訊息是用來設定編輯框要用來顯示的提示字串，其隨之帶入SendMessage的兩個參數wParam與lParam分別簡述如下：
 WParam 當編輯框獲得焦點時是否顯示提示字串   
True=>當編輯框獲得焦點仍舊顯示提示字串   
False=>當編輯框獲得焦點時提示字串就消失  
 
 lParam  
要顯示的提示字串

對EM_SETCUEBANNER訊息的用法有了了解之後，使用SendMessage對編輯框發送EM_SETCUEBANNER訊息，並帶入對應的參數就可以了。就像下面這樣：
 [DllImport("user32.dll", CharSet = CharSet.Auto)]
private static extern Int32 SendMessage(IntPtr hWnd, int msg, int wParam, [MarshalAs(UnmanagedType.LPWStr)] string lParam);
...
const int EM_SETCUEBANNER = 0x1501;
...
SendMessage(this.Handle, EM_SETCUEBANNER, 0, "提示字串");

也可以整理成控制項重複使用：

    public class CueTextBox : TextBox
    {
        [DllImport("user32.dll", CharSet = CharSet.Auto)]
        private static extern Int32 SendMessage(IntPtr hWnd, int msg, int wParam, [MarshalAs(UnmanagedType.LPWStr)] string lParam);

        const int EM_SETCUEBANNER = 0x1501;

        private string _cueText;

        [Localizable(true)]
        public string CueText
        {
            get
            {
                if (_cueText == null)
                    return string.Empty;
                return _cueText;
            }
            set
            {
                _cueText = value;
                updateCue();
            }
        }

        private void updateCue()
        {
            SendMessage(this.Handle, EM_SETCUEBANNER, 0, CueText);
        }
    }

使用上只要放至表單，接著設置CueText屬性就可以了。

## 為下拉方塊加入提示字串

要為下拉方塊加上提示字串，首先我們必須先了解CB_SETCUEBANNER訊息，該訊息是用來設定下拉方塊要用來顯示的提示字串，其隨之帶入SendMessage的兩個參數wParam與lParam分別簡述如下：
wParam
必須為0

lParam

要顯示的提示字串

使用上一樣只要對下拉方塊發送CB_SETCUEBANNER訊息就可以了：

[DllImport("user32.dll", CharSet = CharSet.Auto)]
private static extern Int32 SendMessage(IntPtr hWnd, int msg, int wParam, [MarshalAs(UnmanagedType.LPWStr)] string lParam);
...
const int CB_SETCUEBANNER = 0x1703;
...
SendMessage(this.Handle, CB_SETCUEBANNER0, "提示字串");

## Link

Search box 
Is there a way to do default text with a WinForms textbox? 
EM_SETCUEBANNER Message 
CB_SETCUEBANNER Message
The Missing .NET #1: Cue Banners in Windows Forms (EM_SETCUEBANNER, Text Prompt) 
[VB.NET]设置TextBox的提示文字