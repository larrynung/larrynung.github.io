---
title: "[C#]取得滑鼠游標所指到的視窗及其Process Name"
slug: "[CSharp]取得滑鼠游標所指到的視窗及其Process Name"
date: "2011-06-19 10:24:43"
description: "[C#]取得滑鼠游標所指到的視窗及其Process Name"
tags: [CSharp]
---

最近在開發的案子常會需要使用到前面介紹的小工具(Process Manager)，但畢竟只是先隨便處理一下，在使用時要增加過濾的Process只能透過滑鼠拖曳左邊的Process到右邊，或是透過手動輸入Process Name的方式去設定，使用上總是十分的不便。這一兩天抽空下去調整了一下，想將其改為能用類似Spy++的拖曳箭靶去新增過濾的Process，將箭靶拖到想要過濾的Process視窗上面，就自動的帶出其Process Name，使用起來感覺會更加容易些。

![](\images\posts\29121\image_thumb.png)

![](\images\posts\29121\image_thumb_1.png)

這樣的功能在實作上就會碰到一些難題，像是要怎樣才能找到滑鼠游標指到的視窗，以及要怎樣才能取得其Process Name。

第一個問題我們可以透過WindowFromPoint API下去處理，帶入滑鼠游標當前位置，該API就會返回視窗的Handle。
```
#region DllImport
[DllImport("user32.dll")]
static extern IntPtr WindowFromPoint(Point point);
#endregion
...
var handle = WindowFromPoint(MousePosition);
```
取得了視窗的Handle後，第二個問題就可透過遍尋所有的Process，找到MainWindowHandle跟上面取出的視窗Handle一樣的Process。
```
var handle = WindowFromPoint(MousePosition);
ProcessName = (from item in Process.GetProcesses()
where item.MainWindowHandle == handle
select item.ProcessName).FirstOrDefault();
```