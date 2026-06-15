---
title: "[C#]Json.NET - Reducing Serialized JSON Size"
date: "2013-11-06 12:00:00"
description: "[C#]Json.NET - Reducing Serialized JSON Size"
tags: [CSharp]
---

筆者在[C#]Json.NET - A high performance Json library這篇簡單的帶過了一下JSON.NET這個序列化函式庫，基本的操作只要理解那篇大概都不成問題，但最近在使用上JSON.NET又碰到一個問題，就是有時候沒有資料並不是總是不要序列化，所以我們不能帶上JsonIgnoreAttribute去總是忽略它，而是必須要做些特殊的判斷，像是欄位有時候會是Null或是空的集合，這時候我們序列化傳送也只是增加無謂的資料量，因此我們必須做些對此做些處理。

接下來筆者以[[C#]Json.NET - A high performance Json library這篇的例子來做個簡單的說明，假設我們有個Person類別長得像下面這樣：](http://www.dotblogs.com.tw/larrynung/archive/2012/04/05/71295.aspx)

```csharp
public class Person
{
	public String Name { get; set; }

	public String NickName { get; set; }

	public DateTime Birthday { get; set; }

	public int Age
	{
		get
		{
			return (int)((DateTime.Now - Birthday).TotalDays / 365);
		}
	}
}
```

裡面的NickName成員屬性就是個很好的例子，若NickName是忽略不序列化，那我們永遠無法從其它的地方推斷回來，它並不是跟Age這個成員屬性一樣可以透過推算所以可以直接忽略，但是若不做任何處理，當值為Null時它序列化出來的資訊也沒甚麼意義。

```csharp
...
DateTime date = DateTime.Now;

Person Larry = new Person
{
	Name = "Larry Nung",
	Birthday = new DateTime(1980,4,19)
};

var json = JsonConvert.SerializeObject(Larry, Formatting.Indented);

Console.WriteLine(json);
```

![image_thumb_1.png](/images/posts/0edc4d5e-da98-40f0-8cb5-a9de9b74dc4e/image_thumb_1.png)

這時可以在成員屬性上加上JsonPropertyAttribute，並指定NullValueHandling的處理，像是：

```csharp
...
[JsonProperty(NullValueHandling = NullValueHandling.Ignore)]
public String NickName { get; set; }
...
```

當成員屬性的值為Null時，序列化出來的結果就會被自動忽略掉。

![image_thumb_2.png](/images/posts/0edc4d5e-da98-40f0-8cb5-a9de9b74dc4e/image_thumb_2.png)

套用這個屬性可以解決掉大多參考型態的成員屬性的問題，但是當成員屬性的型態為字串或是集合時就不完全適用，因為集合成員屬性可能不為Null但是是空的，而字串成員屬性可能不為Null但是是空字串。

```csharp
...
Person Larry = new Person
{
    Name = "Larry Nung",
    NickName = "",
    Birthday = new DateTime(1980, 4, 19)
};
...
```

這樣的情況下序列出來的資料也是沒有什麼意義。

![image_thumb.png](/images/posts/0edc4d5e-da98-40f0-8cb5-a9de9b74dc4e/image_thumb.png)

為了徹底解決這樣的問題，我們可以設定序列化的條件，像是為類別加上個名為ShowSerializeXXX的成員方法，用以決定什麼時候應該要序列化名為XXX的成員屬性。

```csharp
[JsonObject(MemberSerialization.OptIn)]
public class Person
{
    ...

    [JsonProperty(NullValueHandling = NullValueHandling.Ignore)]
    public String NickName { get; set; }

   ...

    public bool ShouldSerializeNickName()
    {
        return !string.IsNullOrEmpty(NickName);
    }
}
```

又或者你不想要去更動到用來序列化的類別那邊，我們也可以加個ContractResolver類別，在CreateProperty方法裡面去決定要怎樣判斷是否要序列化，並將該類別的物件實體在序列化時帶入也可以。

```csharp
public class ShouldSerializeContractResolver : DefaultContractResolver
{
    public new static readonly ShouldSerializeContractResolver Instance = new ShouldSerializeContractResolver();

    protected override JsonProperty CreateProperty(MemberInfo member, MemberSerialization memberSerialization)
    {
        JsonProperty property = base.CreateProperty(member, memberSerialization);

        if (property.DeclaringType == typeof(Person) && property.PropertyName == "NickName")
        {
            property.ShouldSerialize =
              instance =>
              {
                  Person e = (Person)instance;
                  return !string.IsNullOrEmpty(e.NickName);
              };
        }

        return property;
    }
}
...
var json = JsonConvert.SerializeObject(Larry, Formatting.Indented, new JsonSerializerSettings
{
        ContractResolver = new ShouldSerializeContractResolver()
});
```

運行起來就會發現這些沒意義的序列化資料都被濾掉了。

![image_thumb_2.png](/images/posts/0edc4d5e-da98-40f0-8cb5-a9de9b74dc4e/image_thumb_2.png)

## Link

* Conditional Property Serialization
* Reducing Serialized JSON Size
