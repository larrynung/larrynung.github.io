---
title: "[C#]實作UDP Broadcast的傳送與接收"
slug: "[CSharp]實作UDP Broadcast的傳送與接收"
date: "2013-11-06 12:00:00"
description: "最近筆者想要利用廣播封包做些處理，稍微研究了一下，這篇簡單的做個紀錄。 若要發送UDP Broadcast，我們可以像下面這樣建立ProtocolType為Udp的Socket物件實體，呼叫SetSocketOption做些設定，"
tags: [CSharp]
---

最近筆者想要利用廣播封包做些處理，稍微研究了一下，這篇簡單的做個紀錄。

若要發送UDP Broadcast，我們可以像下面這樣建立ProtocolType為Udp的Socket物件實體，呼叫SetSocketOption做些設定，並向IPAddress.Broadcast位置發送我們想要送出的廣播資料。

```csharp
private static void BroadcastMessage(string message, int port)
{
	BroadcastMessage(Encoding.ASCII.GetBytes(message), port);
}

private static void BroadcastMessage(byte[] message, int port)
{
	using (var sock = new Socket(AddressFamily.InterNetwork, SocketType.Dgram,
	 ProtocolType.Udp))
	{
		sock.EnableBroadcast = true;
		sock.SetSocketOption(SocketOptionLevel.Socket, SocketOptionName.Broadcast, true);

		var iep = new IPEndPoint(IPAddress.Broadcast, port);

		sock.SendTo(message, iep);
	}
}
```

在接收廣播封包這邊，一樣我們要建立ProtocolType為Udp的Socket物件實體，將Socket綁定在IPAddress.Any位置，並用Socket.ReceiveFrom接收廣播的訊息。

```csharp
		private void ReceiveBroadcastMessage(Action<EndPoint, string> receivedAction, int port)
		{
			ReceiveBroadcastMessage((ep, data) =>
			{
				var stringData = Encoding.ASCII.GetString(data);
				receivedAction(ep, stringData);
			}, port);
		}

		private void ReceiveBroadcastMessage(Action<EndPoint, byte[]> receivedAction, int port)
		{
			using (var sock = new Socket(AddressFamily.InterNetwork,
 SocketType.Dgram, ProtocolType.Udp))
			{
				var ep = new IPEndPoint(IPAddress.Any, port) as EndPoint;
				sock.Bind(ep);

				while (true)
				{
					var buffer = new byte[1024];
					var recv = sock.ReceiveFrom(buffer, ref ep);

					var data = new byte[recv];

					Array.Copy(buffer, 0, data, 0, recv);

					receivedAction(ep, data);

					Thread.Sleep(500);
					Application.DoEvents();
				}
			}
		}
```

最後附上完整的程式碼範例：

```csharp
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApplication8
{
	public partial class Form1 : Form
	{
		public Form1()
		{
			InitializeComponent();
		}

		private void button1_Click(object sender, EventArgs e)
		{
			BroadcastMessage("This is a test message", 9051);
		}

		private void Form1_Load(object sender, EventArgs e)
		{
			backgroundWorker1.RunWorkerAsync();
		}

		private void backgroundWorker1_DoWork(object sender, DoWorkEventArgs e)
		{
			ReceiveBroadcastMessage((EndPoint ep, string data) =>
			{
				this.Invoke((MethodInvoker)delegate()
				{
					listBox1.Items.Add(string.Format("received: {0} from: {1}",
							   data, ep.ToString()));
				});
			}, 9051);
		}

		private static void BroadcastMessage(string message, int port)
		{
			BroadcastMessage(Encoding.ASCII.GetBytes(message), port);
		}

		private static void BroadcastMessage(byte[] message, int port)
		{
			using (var sock = new Socket(AddressFamily.InterNetwork, SocketType.Dgram,
			 ProtocolType.Udp))
			{
				sock.EnableBroadcast = true;
				sock.SetSocketOption(SocketOptionLevel.Socket, SocketOptionName.Broadcast, true);

				var iep = new IPEndPoint(IPAddress.Broadcast, port);

				sock.SendTo(message, iep);
			}
		}

		private void ReceiveBroadcastMessage(Action<EndPoint, string> receivedAction, int port)
		{
			ReceiveBroadcastMessage((ep, data) =>
			{
				var stringData = Encoding.ASCII.GetString(data);
				receivedAction(ep, stringData);
			}, port);
		}

		private void ReceiveBroadcastMessage(Action<EndPoint, byte[]> receivedAction, int port)
		{
			using (var sock = new Socket(AddressFamily.InterNetwork,
 SocketType.Dgram, ProtocolType.Udp))
			{
				var ep = new IPEndPoint(IPAddress.Any, port) as EndPoint;
				sock.Bind(ep);

				while (true)
				{
					var buffer = new byte[1024];
					var recv = sock.ReceiveFrom(buffer, ref ep);

					var data = new byte[recv];

					Array.Copy(buffer, 0, data, 0, recv);

					receivedAction(ep, data);

					Thread.Sleep(500);
					Application.DoEvents();
				}
			}
		}
	}
}
```

運行結果如下：

![image_thumb.png](/images/posts/a44f65e7-9075-4b7e-b907-d044875b3e5b/image_thumb.png)

## Link

* IP Multicasting in C#
* [C#] 傳送與接收UDP廣播封包
