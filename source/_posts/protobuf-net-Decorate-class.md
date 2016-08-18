---
title: protobuf-net - Decorate class
date: 2016-08-18 12:39:58
tags: protobuf-net
---

protobuf-net 要設定類別怎樣被序列化與解序列化有三種方式‧  

<!-- More -->

<br/>

像是使用 protobuf-net 提供的 Attribute，類別上用 ProtoContractAttribute、Property 上用 ProtoMemberAttribute‧  

{% codeblock lang:c# %}
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
{% endcodeblock %}

<br/>


如果有繼層的類別可以透過 ProtoIncludeAttribute 設定。  

{% codeblock lang:c# %}
[ProtoContract] 
[ProtoInclude(10, typeof(Male))] 
[ProtoInclude(11, typeof(Female))] 
class Person { 
    [ProtoMember(1)] 
    public string Name { get; set; }
} 

[ProtoContract] 
class Male : Person { } 

[ProtoContract] 
class Female : Person { }
{% endcodeblock %}

<br/>


ProtoContractAttribute 這邊還有提供些設定，像是 SkipConstructor 可以讓類別解序列化時不需要有建構子、ImplicitFields 可以設定全部的欄位或是屬性都序列化解序列化。  

{% codeblock lang:c# %}
[ProtoContract(SkipConstructor = true, ImplicitFields = ImplicitFields.AllFields)] 
class Person { 
    public string Name { get; set; } 
    public Person(string name) { 
        Name = name; 
    } 

    [ProtoAfterDeserialization] 
    void Validate() {
        if (string.IsNullOrEmpty(Name)) 
            throw new Exception("Empty name"); 
    } 
}
{% endcodeblock %}

<br/>


除了 protobuf-net 提供的 Attribute 外，protobuf-net 也提供 .NET Framework 內建的 DataContractAttribute。  

{% codeblock lang:c# %}
[DataContract] 
class Person { 
    [DataMember(Order = 1)] 
    public string Name { get; set; } 
}
{% endcodeblock %}

<br/>


如果不想用 Attribute 的方式設定，也可以透過 RuntimeTypeModel 設定。  

{% codeblock lang:c# %}
class Person { 
    public string Name { get; set; } 
} 
…
RuntimeTypeModel.Default
    .Add(typeof(Person), false); 
    .Add(1, "Name");
{% endcodeblock %}