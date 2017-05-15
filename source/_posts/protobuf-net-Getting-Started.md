---
title: protobuf-net - Getting Started
date: 2016-08-16 13:32:20
tags: protobuf-net
---

使用 protobuf-net，首先要參照 protobuf-net library，接著設定要用來做序列化或解序列化用的類別，設定完後就可以用 protobuf-net 來序列化或解序列化。  

<!-- More -->

{% asset_img 1.png %}

<br/>


protobuf-net library 透過 NuGet 引用即可。  

{% asset_img 2.png %}

<br/>


{% asset_img 3.png %}

<br/>


接著準備用來做序列化或解序列化用的類別，類別可透過 Attribute 的方式決定怎樣序列化或解序列化。  

{% codeblock lang:C# %}
[ProtoContract] 
class Person { 
    [ProtoMember(1)] 
    public int Id {get;set;}
    [ProtoMember(2)] 
    public string Name {get;set:} 
    [ProtoMember(3)] 
    public Address Address {get;set;} 
} 

[ProtoContract] 
class Address { 
    [ProtoMember(1)] 
    public string Line1 {get;set;} 
    [ProtoMember(2)] 
    public string Line2 {get;set;} 
}
```

<br/>


序列化時只要調用 Serializer.Serialize 帶入 Stream 與要序列化的物件。  

{% codeblock lang:C# %}
var person = new Person { 
    Id = 12345, Name = "Fred", 
    Address = new Address { 
        Line1 = "Flat 1", 
        Line2 = "The Meadows" 
    } 
}; 
using (var file = File.Create("person.bin")) { 
    Serializer.Serialize(file, person); 
}
```

<br/>


解序列化時調用 Serializer.Deserialize 帶入 Stream，並用泛型指定解序列化回來的型態即可。  

{% codeblock lang:C# %}
Person newPerson; 
using (var file = File.OpenRead("person.bin")) { 
    newPerson = Serializer.Deserialize<Person>(file); 
}
```

<br/>


Link
----
* [mgravell/protobuf-net: Protocol Buffers library for idiomatic .NET](https://github.com/mgravell/protobuf-net)