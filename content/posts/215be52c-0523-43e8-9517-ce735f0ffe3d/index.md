---
title: "[C#]使用InternetGetConnectedState API偵測目前電腦網路的連線狀態"
slug: "[CSharp]使用InternetGetConnectedState API偵測目前電腦網路的連線狀態"
date: "2013-11-06 12:00:00"
description: "[C#]使用InternetGetConnectedState API偵測目前電腦網路的連線狀態"
tags: [CSharp]
---

有時候我們會有需要為程式加入偵測網路連線的能力，也許是當網路不通時秀些提示，或是將某些程式的功能給停用。這時我們可能會傾向採用NetworkChange.NetworkAddressChanged與NetworkChange.NetworkAvailabilityChanged這兩個事件去偵測網路環境是否有所變動，或者用Timer加Ping的方式去偵測網路是否可以外連。上面兩種方式在.NET程式中還算滿常用的方法，但是以筆者的經驗來說NetworkChange在多網卡環境下運作跟期望的可能會有所出入，而就算事件正常觸發也可能需搭配其它方法偵測網路是否是通的，至於Ping的偵測方式，它需要實際的去送封包偵測，不僅需考慮可能會被封鎖，也要考慮封包傳送的額外負擔，如果能直接跟系統詢問連線狀態一定會比較好一點。所以在做類似的功能時使用InternetGetConnectedState API可能也是一個不錯的選擇，這邊隨手將之稍微紀錄一下。

要使用InternetGetConnectedState API偵測目前電腦網路的連線狀態，首先我們必須要了解一下該API的函式原型。
  BOOL InternetGetConnectedState(
  __out  LPDWORD lpdwFlags,
  __in   DWORD dwReserved
);

從函式原型我們可以看出該API需要兩個參數，一個是帶入來回傳目前網路連線類型的，回傳的值可參閱下表：

另一個則是API保留的參數，直接帶入0就可以了。至於該API的回傳值則是代表電腦網路是否是連線的狀態。

函式原型跟用法都清楚後，我們可以開始實際的使用API，首先為程式加入API的PInvoke宣告：

[DllImport("wininet")]
public static extern bool InternetGetConnectedState(
ref uint lpdwFlags,
uint dwReserved
);

使用時就先宣告個用來回傳的參數，然後將宣告的參數與0帶入該API中即可。

...
uint flags = 0x0;
var isNetworkAvailable = InternetGetConnectedState(ref flags, 0);
...

最後這邊附上一個比較完整的使用範例：

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Runtime.InteropServices;

namespace ConsoleApplication21
{
class Program
{
[DllImport("wininet")]
public static extern bool InternetGetConnectedState(
ref uint lpdwFlags,
uint dwReserved
);

static void Main(string[] args)
{
uint flags = 0x0;

var isNetworkAvailable = InternetGetConnectedState(ref flags, 0);

Console.WriteLine(string.Format("Network available: {0} ({1})", isNetworkAvailable.ToString(), flags.ToString()));
}
}
}

運行後可以看到如下的畫面，代表筆者的電腦目前是有網路連線的，而且網路的連線狀態是INTERNET_RAS_INSTALLED & INTERNET_CONNECTION_LAN。

## Link

  InternetGetConnectedState function 

  InternetGetConnectedState | 男丁格爾's 脫殼玩