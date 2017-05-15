---
layout: post
title: "Json.Net - Custom Converter"
date: 2015-02-17 07:54:00
comments: true
tags: [Json.NET]
keywords: "Json.NET, Converter"
description: "Json.NET - Custom Converter"
---

Json.Net 用到後面，我們免不了有時會要 Custom Converter 去做序列化的客製動作。  

<!-- More -->

<br/>


使用 Json.Net 要做自定義序列化，我們可以 Custom Json.Net 的 Converter，為此需要建立一個 Converter 類別，將之繼承自 JsonConverter，接著將繼承而來的方法實作即可。  

<br/>


CanConverter 用來決定該型別是否可被該 Converter 處理、WriteJson 用來序列化物件、ReadJson 用來解序列化物件。  

<br/>


像是我們可以像下面這樣做個簡易的 Converter，裡面只是單純的將物件序列化與解序列化。    

```c#
using System;
using Newtonsoft.Json;

namespace LevelUp.Converter
{
    public class ConcreteTypeConverter<TConcrete> : JsonConverter
    {
        public override bool CanConvert( Type objectType)
        {
            return true ;
        }

        public override object ReadJson( JsonReader reader, Type objectType, object existingValue, JsonSerializer serializer)
        {
            return serializer.Deserialize<TConcrete>(reader);
        }

        public override void WriteJson( JsonWriter writer, object value, JsonSerializer serializer)
        {
            serializer.Serialize(writer, value);
        }
    }
}
```

<br/>


當我們在序列化物件時，若物件的成員屬性是 Interface，就可以用來指定序列化與解序列化時實際所要用的型態。  

```c#
[JsonConverter(typeof(ConcreteTypeConverter<DecisionNode[]>))]
IDecisionNode[] Nodes { get ; }
```

<br/>


或者是像下面這段用來處理 Dictionary 的序列話與解序列化的 Converter 程式，裡面會用 JsonWriter 去處理序列化的動作、用 JsonReader 去處理解序列化的動作，寫起來比較複雜些，但可進行比較進階的處理。  

```c#
using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Newtonsoft.Json;

namespace LevelUp.Converter
{
    public class DictionaryConverter<TKey, TValue> : JsonConverter
    {
        #region  Methods
        private static bool TypeImplementsGenericInterface( Type concreteType, Type interfaceType)
        {
            return concreteType.GetInterfaces()
                   .Any(i => i.IsGenericType && i.GetGenericTypeDefinition() == interfaceType);
        }
        public override bool CanConvert( Type objectType)
        {
            return (typeof (IDictionary).IsAssignableFrom(objectType) ||
                    TypeImplementsGenericInterface(objectType, typeof(IDictionary <,>)));
        }

        public override object ReadJson( JsonReader reader, Type objectType, object existingValue, JsonSerializer serializer)
        {
            if (reader.TokenType == JsonToken.None) return null ;

            var dict = new Dictionary<TKey, TValue>();

            reader.Read();

            while (reader.TokenType == JsonToken.StartArray)
            {
                reader.Read();

                var key = serializer.Deserialize<TKey>(reader);

                reader.Read();
                var value = serializer.Deserialize<TValue>(reader);

                reader.Read();
                reader.Read();

                dict.Add(key, value);
            }

            return dict;
        }

        public override void WriteJson( JsonWriter writer, object value, JsonSerializer serializer)
        {
            var dict = value as IDictionary;
            var keys = dict.Keys;
            var values = dict.Values;
            var valueEnumerator = values.GetEnumerator();

            writer.WriteStartArray();
            foreach (var key in keys)
            {
                valueEnumerator.MoveNext();

                writer.WriteStartArray();
                serializer.Serialize(writer, key);
                serializer.Serialize(writer, valueEnumerator.Current);
                writer.WriteEndArray();
            }
            writer.WriteEndArray();
        }
        #endregion  Methods
    }
}
{% endcodeblock%}

<br/>


Link
----
* [JSON.NET Implementing Custom Serialization](http://blog.maskalik.com/asp-net/json-net-implement-custom-serialization/)
