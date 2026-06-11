---
title: "[C#]使用SharpShell實現Shell Icon Overlay功能"
slug: "[CSharp]使用SharpShell實現Shell Icon Overlay功能"
date: "2013-11-06 12:00:00"
description: "[C#]使用SharpShell實現Shell Icon Overlay功能"
tags: [CSharp]
---

有在使用DropBox或是SVN之類的軟體的使用者應該都會注意到，這類型的軟體在透過檔案總管瀏覽時，都會透過icon的變化來明確的告知目前的狀態，既炫又清楚。這樣的功能稱做Shell Icon Overlay，在.NET中我們可以透過SharpShell來輕易的實現這樣的功能。

(因為SharpShell實現這樣的功能過於簡單，筆者就不另行建立範例，直接拿SharpShell裡面的範例來做說明。)

首先我們要先準備好要覆蓋到上面的Icon，用以表示當前的狀態。Icon圖檔建議要內含16×16、24×24 、32×32、48×48、64×64、256×256這幾種尺寸，且背景要透明處理。

因為範例的功能是當檔案是唯獨時附加狀態告知，因此這邊範例準備的圖檔是個大鎖。

圖檔準備好後開始進入程式的編碼。首先要建立個dll的專案，然後添加個類別來告知系統要怎樣覆蓋Icon，以及要用甚麼樣的Icon覆蓋。該類別需繼承至SharpIconOverlayHandler，並覆寫GetPriority、CanShowOverlay、與GetOverlayIcon三個抽象方法。

其中GetPriority是設定處理的優先權，值的範圍需介於0~100之間，0代表優先權最高，100則是最低的優先權，當指定的檔案有多個Shell Icon Overlay可供處理時系統會由此優先權值去做抉擇。

CanShowOverlay則是用來決定系統何時要為我們覆蓋上狀態Icon，因為這範例是唯獨時要附加狀態告知，故這邊會由帶進來的path參數去讀出檔案屬性，當檔案屬性是唯獨時帶回true，若是非唯獨檔案則回傳false。

GetOverlayIcon就更簡單了，很明顯的就是回傳我們要覆蓋上去的狀態Icon，也就是我們一開始準備好的大鎖圖。

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using SharpShell.Interop;
using SharpShell.SharpIconOverlayHandler;

namespace ReadOnlyFileIconOverlayHandler
{
///
/// The ReadOnlyFileIconOverlayHandler is an IconOverlayHandler that shows
/// a padlock icon over files that are read only.
///
[ComVisible(true)]
public class ReadOnlyFileIconOverlayHandler : SharpIconOverlayHandler
{
///
/// Called by the system to get the priority, which is used to determine
/// which icon overlay to use if there are multiple handlers. The priority
/// must be between 0 and 100, where 0 is the highest priority.
///
///
/// A value between 0 and 100, where 0 is the highest priority.
///
protected override int GetPriority()
{
// The read only icon overlay is very low priority.
return 90;
}

///
/// Determines whether an overlay should be shown for the shell item with the path 'path' and
/// the shell attributes 'attributes'.
///
/// The path for the shell item. This is not necessarily the path
/// to a physical file or folder.
/// The attributes of the shell item.
///
/// true if this an overlay should be shown for the specified item; otherwise, false.
///
protected override bool CanShowOverlay(string path, FILE_ATTRIBUTE attributes)
{
try
{
// Get the file attributes.
var fileAttributes = new FileInfo(path);

// Return true if the file is read only, meaning we'll show the overlay.
return fileAttributes.IsReadOnly;
}
catch (Exception)
{
return false;
}
}

///
/// Called to get the icon to show as the overlay icon.
///
///
/// The overlay icon.
///
protected override System.Drawing.Icon GetOverlayIcon()
{
// Return the read only icon.
return Properties.Resources.ReadOnly;
}
}
}

最後記得要為剛撰寫的類別附加ComVisibleAttribute，並為程式加上強命名簽章。

到這邊實現功能所需要的組件已經準備好了。接著我們必須跟系統註冊，透過.NET Framework內建的命令提是字元輸入命令"regasm [ShellIconHandler.dll] /codebase"，告知系統我們有一些自訂的處理動作。(若需要解除註冊，可下命令"regasm [ShellIconHandler.dll] /u")

命令下完後若是輸出畫面沒有任何異常，應該就是成功的完成了註冊的動作。若不夠放心我們也可以透過登錄檔做一下確認，沒意外的話HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\ShellIconOverlayIdentifiers下應該會看到對應的機碼。

若到上述的動作都完成了，我們可以開始測試一下程式的運作是否如我們的預期，這邊我們需要將explorer.exe給關閉重啟，讓我們跟系統註冊的功能能夠生效。

重啟後在檔案總管隨便找個檔案將其改為唯獨狀態，我們可以如預期地看到檔案的Icon被附加了狀態Icon。

## Link


SharpShell

.NET Shell Extensions - Shell Icon Handlers

IMPLEMENTING ICON OVERLAY HANDLERS IN C#