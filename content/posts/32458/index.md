---
title: "[C#]取得網卡的IPV6位置"
slug: "[CSharp]取得網卡的IPV6位置"
date: "2011-08-02 01:18:13"
description: "[C#]取得網卡的IPV6位置"
tags: [CSharp]
---
最近有個需求是要取得本地端的IPV6位置，若用IPHostEntry去取AddressList，回傳的IP位置內沒有IPV6的位置資訊，因此換個方法改透過System.Net.NetworkInformation.NetworkInterfaceType下去取所有的網卡資訊，再從網卡資訊內去擷取IPV6的位置資訊，這邊隨筆將之記錄一下。
```
private static IEnumerable GetLocalIPV6IP()
{
return (from adapter in NetworkInterface.GetAllNetworkInterfaces()
where adapter .NetworkInterfaceType == NetworkInterfaceType.Ethernet
from AddressInfo in adapter.GetIPProperties().UnicastAddresses.OfType()
where AddressInfo.Address.AddressFamily == System.Net.Sockets.AddressFamily.InterNetworkV6
let ipAddress = AddressInfo.Address.ToString()
select ipAddress);
}
```
完整範例如下：
```
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Net.NetworkInformation;

namespace ConsoleApplication13
{
class Program
{
static void Main(string[] args)
{
foreach (var ip in GetLocalIPV6IP())
{
Console.WriteLine(ip);
}
}

private static IEnumerable GetLocalIPV6IP()
{
return (from adapter in NetworkInterface.GetAllNetworkInterfaces()
where adapter .NetworkInterfaceType == NetworkInterfaceType.Ethernet
from AddressInfo in adapter.GetIPProperties().UnicastAddresses.OfType()
where AddressInfo.Address.AddressFamily == System.Net.Sockets.AddressFamily.InterNetworkV6
let ipAddress = AddressInfo.Address.ToString()
select ipAddress);
}
}
}
```
運行結果：

![image_thumb.png](/images/posts/32458/image_thumb.png)