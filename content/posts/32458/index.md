---
title: "[C#]取得網卡的IPV6位置"
date: "2011-08-02 01:18:13"
description: "[C#]取得網卡的IPV6位置"
tags: [CSharp]
---

<p>
	最近有個需求是要取得本地端的IPV6位置，若用IPHostEntry去取AddressList，回傳的IP位置內沒有IPV6的位置資訊，因此換個方法改透過System.Net.NetworkInformation.NetworkInterfaceType下去取所有的網卡資訊，再從網卡資訊內去擷取IPV6的位置資訊，這邊隨筆將之記錄一下。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:de6a2bca-86a5-4168-8eba-8bac17310e0b" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c#" name="code">
        private static IEnumerable&lt;String&gt; GetLocalIPV6IP()
        {
            return (from adapter in NetworkInterface.GetAllNetworkInterfaces()                   
                    where adapter .NetworkInterfaceType ==  NetworkInterfaceType.Ethernet 
                    from AddressInfo in adapter.GetIPProperties().UnicastAddresses.OfType&lt;UnicastIPAddressInformation&gt;()
                    where AddressInfo.Address.AddressFamily == System.Net.Sockets.AddressFamily.InterNetworkV6                    
                    let ipAddress = AddressInfo.Address.ToString()
                    select ipAddress);
        }</pre>
</div>
<p>
	 </p>
<p>
	完整範例如下：</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:ad61bda0-e3d7-419d-9109-77a7a6e963e6" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c#" name="code">
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

        private static IEnumerable&lt;String&gt; GetLocalIPV6IP()
        {
            return (from adapter in NetworkInterface.GetAllNetworkInterfaces()                   
                    where adapter .NetworkInterfaceType ==  NetworkInterfaceType.Ethernet 
                    from AddressInfo in adapter.GetIPProperties().UnicastAddresses.OfType&lt;UnicastIPAddressInformation&gt;()
                    where AddressInfo.Address.AddressFamily == System.Net.Sockets.AddressFamily.InterNetworkV6                    
                    let ipAddress = AddressInfo.Address.ToString()
                    select ipAddress);
        }
    }
}</pre>
</div>
<p>
	 </p>
<p>
	運行結果：</p>
<p>
	<img alt="image" border="0" height="159" src="\images\posts\32458\image_thumb.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="409" /></p>
