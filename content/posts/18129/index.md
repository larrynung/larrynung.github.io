---
title: "[C#]使用WM_SYSCOMMAND訊息控制螢幕模式切換"
slug: "[CSharp]使用WM_SYSCOMMAND訊息控制螢幕模式切換"
date: "2010-10-05 10:03:15"
description: "[C#]使用WM_SYSCOMMAND訊息控制螢幕模式切換"
tags: [CSharp]
---

要控制螢幕的開啟、關閉，可透SendMessage發送WM_SYSCOMMAND訊息，wParam參數傳入SC_MONITORPOWER，lParam參數則傳入螢幕的模式。

  參數方面參閱WM_SYSCOMMAND Message，裡面清楚的帶出WM_SYSCOMMAND為0x0112、SC_MONITORPOWER為0xF170、與其對應的lParam。      

使用上就像下面這樣：
  
        [DllImport("user32.dll")]
        private static extern int SendMessage(int hWnd, int Msg, int wParam, int lParam);
 
        const int SC_MONITORPOWER = 0xF170;
        const int WM_SYSCOMMAND = 0x0112;
        ...
        SendMessage(-1,  WM_SYSCOMMAND, SC_MONITORPOWER , -1);
        SendMessage(-1,  WM_SYSCOMMAND, SC_MONITORPOWER , 1);
        SendMessage(-1,  WM_SYSCOMMAND, SC_MONITORPOWER , 2);

這邊為方便後續使用，將程式整理成類別，有需要的自行取用。
  
public static class MonitorControler
    {
        [DllImport("user32.dll")]
        private static extern int SendMessage(int hWnd, int Msg, int wParam, int lParam);

        const int SC_MONITORPOWER = 0xF170;
        const int WM_SYSCOMMAND = 0x0112;
        //const int SC_SCREENSAVE = 0xF140;
        
        public enum MonitorMode : int
        {
            MONITOR_ON = -1,
            MONITOR_STANBY = 1,
            MONITOR_OFF
        }

        public static void ChangeMonitorState(MonitorMode mode)
        {
            SendMessage(-1, WM_SYSCOMMAND, SC_MONITORPOWER, (int)mode);
        }

        public static void MonitorOff()
        {
            ChangeMonitorState(MonitorMode.MONITOR_OFF);
        }

        public static void MonitorOn()
        {
            ChangeMonitorState(MonitorMode.MONITOR_ON);
        }

        public static void MonitorStandBy()
        {
            ChangeMonitorState(MonitorMode.MONITOR_STANBY);
        }
    }

## Link
     WM_SYSCOMMAND Message