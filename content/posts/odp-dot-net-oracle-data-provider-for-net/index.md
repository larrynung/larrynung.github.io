---
title: "ODP.NET - Oracle Data Provider for .NET"
date: "2014-04-06 23:52:00"
description: "ODP.NET - Oracle Data Provider for .NET"
tags: [ODP.NET, CSharp]
---


要用 C# 存取 Oracle，通常我們會使用 ODP.NET。  

<!-- More -->

<br/>

ODP.NET 目前有 x86、 x64 與 Managed 三個版本可供使用。  

<br/>

Managed 版本為純 .NET 的解決方案，具備位元適應性， 能兼容於 x86 與 x64 的環境，可不安裝 Oracle client 使用，只是目前尚未支援 UDT 操作。  

<br/>

x86 與 x64 版本的 ODP.NET 不具位元適應性，需依運行環境使用正確的組件，且需安裝對應的 Oracle client，或是將會用到的 Oracle client 組件一併發佈，使用起來較 Managed 的麻煩，但能使用完整的功能。  

<br/>

不論選用哪個版本做開發，使用前都需先將組件加入參考，這邊可直接透過 NuGet 安裝對應的套件。  

{% img /images/posts/ODP.NET/1.png %}

<br/>

{% img /images/posts/ODP.NET/2.png %}

<br/>

{% img /images/posts/ODP.NET/3.png %}

<br/>

{% img /images/posts/ODP.NET/4.png %}

<br/>

組件載入後，程式撰寫起來跟一般的 ADO.NET 程式沒什麼兩樣。  

<br/>

首先要先建立資料庫的連線。  

```c#
using(var conn = new OracleConnection(connstring))
{
    ...
}
```

<br/>

接著將建立的資料庫連線開啟。
  
```c#
conn.Open();
```

<br/>

再來建立所要運行的命令。

```c#
using (var comm = new OracleCommand(sql, conn))
{
    ...
}
```

<br/>

運行命令做對應的資料庫存取動作。  

```c#
using(var rdr = comm.ExecuteReader())
{
    ...
}
```

<br/>

最後將命令釋放並關閉資料庫連線。  

<br/>

所以以呼叫一個簡單的 Select 命令來說，程式寫起來會像下面這樣：  

```c#
void DisplayAllTable(string connectionString)
{
    using(var conn = new OracleConnection(connectionString))
    {
        conn.Open();
        var sql ="select distinct owner from sys.all_objects order by owner";
        using(var comm = new OracleCommand(sql, conn))
        {
            using(var rdr = comm.ExecuteReader())
            {
                while(rdr.Read())
                {
                    Console.WriteLine(rdr.GetString(0));
                }
            }
        }
    }
}
```

<br/>

呼叫一個 StoredProcedure 會像下面這樣：  

```c#
void ExecuteStoredProcedure(string connectionString, string storedProcedure, OracleParameter[] parameters)
{
    using(var cn = new OracleConnection(connectionString))
    {
        cn.Open();

        using(var cmd = new OracleCommand(storedProcedure, cn))
        {
            cmd.CommandType = CommandType.StoredProcedure;

            cmd.Parameters.AddRange(parameters);
            cmd.ExecuteNonQuery();
        }
    }
}
```
