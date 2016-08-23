---
title: protobuf-net - Serialize/DeSerialize data
date: 2016-08-23 23:52:16
tags:
---

protobuf-net 預設只支援序列化至 stream，或是自 stream 姐序列化回物件。使用上就是透過 Serializer.Serialize 帶入 stream 與物件，帶入的物件就會被序列化至 stream，呼叫 Serializer.Deserialize，帶入 stream，泛型型態設定為指定的類別型態，就可以自 stream 解序列化回指定型態的物件。  

<!-- More -->

{% codeblock lang:c# %}
private static void SerializeToStream<T>(T obj, Stream stream) { 
    Serializer.Serialize(stream, obj); 
} 

private static T DeSerializeFromStream<T>(Stream stream) { 
    return Serializer.Deserialize<T>(stream); 
}
{% endcodeblock %}

<br/>


如果要序列化為字串，可以將物件先序列化到 stream，然後將他轉成 Base 64 的字串。解序列化反向操作即可。  

{% codeblock lang:sql %}
private static string SerializeToText<T>(T obj) { 
    using (var ms = new MemoryStream(1024)) { 
        SerializeToStream(obj, ms); 
        return Convert.ToBase64String(ms.ToArray());
    } 
} 

private static T DeSerializeFromText<T>(string text) { 
    var buffer = Convert.FromBase64String(text); 
    using (var ms = new MemoryStream(buffer)) { 
        return DeSerializeFromStream<T>(ms); 
    } 
}
{% endcodeblock %}

<br/>


序列化到檔案的話，就是開啟檔案串流，將物件序列化到檔案串流即可。解序列化一樣反向操作。  

{% codeblock lang:c# %}
public virtual void SerializeToFile<T>(T obj, String file, Int32 bufferSize = 1024) { 
    using (var fs = File.Open(file, FileMode.Create, FileAccess.Write)) { 
        using (var bs = new BufferedStream(fs, bufferSize)) { 
            SerializeToStream(obj, bs); 
            bs.Flush(); 
        } 
    } 
} 
public virtual T DeSerializeFromFile<T>(String file, Int32 bufferSize) { 
    using (var fs = File.Open(file, FileMode.Open, FileAccess.Read, FileShare.ReadWrite)) { 
        using (var bs = new BufferedStream(fs, bufferSize)) { 
            return DeSerializeFromStream<T>(bs); 
        } 
    } 
}
{% endcodeblock %}
