---
layout: post
title: "[C#]Json.NET - Reducing Serialized JSON Size"
date: 2013-11-06 12:00:00
comments: true
tags: 
description: "[C#]Json.NET - Reducing Serialized JSON Size"
---
<p>筆者在[C#]Json.NET - A high performance Json library</a>這篇簡單的帶過了一下JSON.NET這個序列化函式庫，基本的操作只要理解那篇大概都不成問題，但最近在使用上JSON.NET又碰到一個問題，就是有時候沒有資料並不是總是不要序列化，所以我們不能帶上JsonIgnoreAttribute去總是忽略它，而是必須要做些特殊的判斷，像是欄位有時候會是Null或是空的集合，這時候我們序列化傳送也只是增加無謂的資料量，因此我們必須做些對此做些處理。</p>  <p> </p>  <p>接下來筆者以<a href="http://www.dotblogs.com.tw/larrynung/archive/2012/04/05/71295.aspx">[C#]Json.NET - A high performance Json library這篇的例子來做個簡單的說明，假設我們有個Person類別長得像下面這樣：</p>  <div id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:5bd6629c-0188-45bc-8797-73d95d395f30" class="wlWriterSmartContent" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px"><pre name="code" class="c#">public class Person
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
}</pre></div>

<p> </p>

<p>裡面的NickName成員屬性就是個很好的例子，若NickName是忽略不序列化，那我們永遠無法從其它的地方推斷回來，它並不是跟Age這個成員屬性一樣可以透過推算所以可以直接忽略，但是若不做任何處理，當值為Null時它序列化出來的資訊也沒甚麼意義。</p>

<div id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:e67030e2-6fa2-4dcb-8a13-5a7905c31707" class="wlWriterSmartContent" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px"><pre name="code" class="c#">...
DateTime date = DateTime.Now;

Person Larry = new Person
{
	Name = "Larry Nung",
	Birthday = new DateTime(1980,4,19)
};

var json = JsonConvert.SerializeObject(Larry, Formatting.Indented);

Console.WriteLine(json);</pre></div>

<p> </p>

<p><img style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" border="0" alt="image" src="\images\posts\0edc4d5e-da98-40f0-8cb5-a9de9b74dc4e\image_thumb_1.png" width="353" height="192" /> </p>

<p> </p>

<p>這時可以在成員屬性上加上JsonPropertyAttribute，並指定NullValueHandling的處理，像是：</p>

<div id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:bd62deb2-2fa8-4439-9fc7-a8da10560ff0" class="wlWriterSmartContent" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px"><pre name="code" class="c#">...
[JsonProperty(NullValueHandling = NullValueHandling.Ignore)]
public String NickName { get; set; }
...</pre></div>

<p> </p>

<p>當成員屬性的值為Null時，序列化出來的結果就會被自動忽略掉。</p>

<p><img style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" border="0" alt="image" src="\images\posts\0edc4d5e-da98-40f0-8cb5-a9de9b74dc4e\image_thumb_2.png" width="353" height="176" /> </p>

<p> </p>

<p>套用這個屬性可以解決掉大多參考型態的成員屬性的問題，但是當成員屬性的型態為字串或是集合時就不完全適用，因為集合成員屬性可能不為Null但是是空的，而字串成員屬性可能不為Null但是是空字串。</p>

<div id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:407defe1-5102-44a9-8843-7b952e14c176" class="wlWriterSmartContent" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px"><pre name="code" class="c#">...
Person Larry = new Person
{
    Name = "Larry Nung",
    NickName = "",
    Birthday = new DateTime(1980, 4, 19)
};
...</pre></div>

<p> </p>

<p>這樣的情況下序列出來的資料也是沒有什麼意義。</p>

<p><img style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" border="0" alt="image" src="\images\posts\0edc4d5e-da98-40f0-8cb5-a9de9b74dc4e\image_thumb.png" width="377" height="192" /> </p>

<p> </p>

<p>為了徹底解決這樣的問題，我們可以設定序列化的條件，像是為類別加上個名為ShowSerializeXXX的成員方法，用以決定什麼時候應該要序列化名為XXX的成員屬性。</p>

<div id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:62623a0c-5089-481d-ae2d-fa24b34278bf" class="wlWriterSmartContent" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px"><pre name="code" class="c#">    [JsonObject(MemberSerialization.OptIn)]
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
    }</pre></div>

<p> </p>

<p>又或者你不想要去更動到用來序列化的類別那邊，我們也可以加個ContractResolver類別，在CreateProperty方法裡面去決定要怎樣判斷是否要序列化，並將該類別的物件實體在序列化時帶入也可以。</p>

<div id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:bb354b85-9aa4-4dac-a8b5-e1cc9c40732f" class="wlWriterSmartContent" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px"><pre name="code" class="c#">    public class ShouldSerializeContractResolver : DefaultContractResolver
    {
        public new static readonly ShouldSerializeContractResolver Instance = new ShouldSerializeContractResolver();

        protected override JsonProperty CreateProperty(MemberInfo member, MemberSerialization memberSerialization)
        {
            JsonProperty property = base.CreateProperty(member, memberSerialization);

            if (property.DeclaringType == typeof(Person) &amp;&amp; property.PropertyName == "NickName")
            {
                property.ShouldSerialize =
                  instance =&gt;
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
 
</pre></div>

<p> </p>

<p>運行起來就會發現這些沒意義的序列化資料都被濾掉了。</p>

<p><img style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" border="0" alt="image" src="\images\posts\0edc4d5e-da98-40f0-8cb5-a9de9b74dc4e\image_thumb_2.png" width="353" height="176" /> </p>

<p> </p>

<h2>Link</h2>

<ul>
  <li>Conditional Property Serialization </li>

  <li>Reducing Serialized JSON Size </li>
</ul>