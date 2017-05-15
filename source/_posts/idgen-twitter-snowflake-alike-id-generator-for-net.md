---
layout: post
title: "IdGen - Twitter Snowflake-alike ID generator for .Net"
date: 2016-04-06 21:39:00
comments: true
tags: 
keywords: "IdGen"
description: "IdGen - Twitter Snowflake-alike ID generator for .Net"
---

IdGen 是 ID 產生器套件，可用以產生 Twitter Snowflake-alike 的 ID，具備彈性，支援許多不同的建構方式，支援調整 ID 的結構。  

<!-- More --> 

<br/>


IdGen 產生的 ID 預設有 64 bit，就一個 long 的大小， 由 1 bit 的正負符號， 41 bit 的 Timestamp， 10 bit 的 Generator id， 12 bit 的 Sequence 所組成。  


{% img /images/posts/IdGen/1.png %}

<br/>


使用上要先透過 NuGet 安裝 IdGen 套件。  

{% img /images/posts/IdGen/2.png %}

<br/>


{% img /images/posts/IdGen/3.png %}

<br/>


接著引用 IdGen 命名空間，建立 IdGenerator，然後調用 CreateId() 取得單一 ID，或是調用 Take() 取得多個 ID 即可。  
 
```c#
using IdGen;
...
var generator = GetIdGenerator();
var id = generator.CreateId();
...
var count = 10;
var ids = generator.Take(count);
...
```

<br/>


IdGenerator 的建立方式有幾種，最基本的做法，我們可以透過建構子下去建構，像是帶入 Generator Id 下去建構。  

```c#
...
var generatorID = 0;
var generator = new IdGenerator(generatorID);
...
```

<br/>


或是帶入 EPoch 與 Mask 將 ID 的組成結構改掉，像是這邊帶入的 Mask 即是指定 45 bit 的 Timestamp， 8 bit 的 Generator Id， 10 bit 的 Sequence。  

```c#
...
var gid = short.Parse(Dns.Resolve(Dns.GetHostName()).AddressList[0].ToString().Split('.')[3]);
var mc = new MaskConfig(45, 8, 10);
var generator = new IdGenerator(gid, new DateTime (1970, 1, 1), mc);
...
```

<br/>


第二種建構方式是透過 IdGenerator.CreateMachineSpecificGenerator() 取得該機器用的 Generator，這方法會用 Machine name 的 Hash code 當 Generator id 下去建構 Generator，以期讓每台機器的 Generator 能夠錯開，確保產生的 ID 不會重複。但礙於 ID 的大小，因此 Hash Code 只取了部分值，是不保險的處理方式，只能偶爾偷懶使用，實際使用上還是建議要自己處理。   

```c#
...
var generator = IdGenerator.CreateMachineSpecificGenerator();
...
```

<br/>


第三種建構方式是透過 IdGenerator.CreateThreadSpecificGenerator() 取得該執行緒用的 Generator，當程式只會在一台機器上執行，但會跑再多執行緒的環境下適用。  

```c#
...
var generator = IdGenerator.CreateThreadSpecificGenerator();
...
```

<br/>


最後一種建構方式是透過 Config 建構，可在 Config 檔先做好設定。  

{% codeblock lang:xml %}
<configuration>
  <configSections>
    <section name="idGenSection" type="IdGen.Configuration.IdGeneratorsSection, IdGen" />
  </configSections>

  <idGenSection>
    <idGenerators>
      <idGenerator name="foo" id="123"  epoch="2016-01-02T12:34:56" timestampBits="39" generatorIdBits="11" sequenceBits="13" />
      <idGenerator name="bar" id="987"  epoch="2016-02-01 01:23:00:45" timestampBits="20" generatorIdBits="21" sequenceBits="22" />
      <idGenerator name="baz" id="2047" epoch="2016-02-29"          timestampBits="21" generatorIdBits="21" sequenceBits="21" />
    </idGenerators>
  </idGenSection>

</configuration>
```

<br/>


然後調用 GetFromConfig，帶入 Generator 的名稱。  

```c#
...
var generator = IdGenerator.GetFromConfig("foo");
...
```

<br/>


最後附上完整的測試範例：  

```c#
using System;
using System.Linq;
using System.Net;
using IdGen;

namespace ConsoleApplication32
{
    class Program
    {
        static void Main( string[] args)
        {
            var localIp = short.Parse(Dns .Resolve(Dns .GetHostName()).AddressList[0].ToString().Split('.')[3]);
            var generator = new IdGenerator(localIp);

            Console.WriteLine(generator.CreateId().ToString());

            var ids = generator.Take(100);

            foreach ( var id in ids)
            {
                Console.WriteLine(id.ToString());
            }
        }
    }
}
```

<br/>


運行結果如下：  

{% img /images/posts/IdGen/4.png %}

<br/>


Link
----
* [RobThree/IdGen: Twitter Snowflake-alike ID generator for .Net](https://github.com/RobThree/IdGen)
