---
title: LiteDB - Insert data
date: 2017-12-17 22:53:59
tags: [LiteDB]
---

要將資料塞入 LiteDB，需先準備一個用來存放資料的 Model，該 Model 跟一般的 Model 一樣，不需要加掛特殊的 Attribute，只需要為 Model 加上一個 ID 的數值屬性，讓 LiteDB 用以識別資料。  

<!-- More -->

```C#
public class MyModel
{
    public int ID { get; set; }
    ...
}    
```

<br/>


再來準備要塞入的資料，ID 值不用填，LiteDB 會自行填入。  

```C#
var collectionItem = new T()
{
  ...
};
```

<br/>


最後將 LiteDB 開啟，取得對應的 Collection，用 Collection.Insert 將資料塞入即可。  

```C#
…
using (var db = new LiteDatabase(dbFile)) 
{ 
  var collection = db.GetCollection<T>(collectionName); 
  ...
  collection.Insert(collectionItem); 
} 
```

<br/>


程式撰寫起來會像下面這樣：

```C#
using System;

namespace LiteDB.Demo1
{
    class Program
    {
        static void Main(string[] args)
        {
            using (var db = new LiteDatabase("Person.db"))
            {
                var persons = db.GetCollection<Person>("persons");
                
                var larry = new Person
                {
                    Name = "Larry Nung",
                    NickName = "Larry"
                };
                
                persons.Insert(larry);
            }
        }
    }

    public class Person
    {
        public int ID { get; set; }
        public String Name { get; set; }
        public String NickName { get; set; }
    }
}
```

<br/>


運行起來會將資料寫入指定的 LiteDB。  

{% asset_img 1.png %}

<br/>


除了單筆的塞值，Collection.Insert 也允許塞入多筆資料，只要調用 Collection.Insert 時帶入資料的集合即可。  

```C#
using System;
using System.Diagnostics;
using System.Linq;

namespace LiteDB.Demo3
{
    class Program
    {
        static void Main(string[] args)
        {
            using (var db = new LiteDatabase("Person.db"))
            {
                var persons = db.GetCollection<Person>("persons");
                var count = 1000000;
                var data = Enumerable.Range(1, count).Select(item => new Person
                {
                    Name = "Larry Nung " + item,
                    NickName = "Larry " + item
                }).ToArray();
                persons.Insert(data);
            }
        }
    }

    public class Person
    {
        public int ID { get; set; }
        public String Name { get; set; }
        public String NickName { get; set; }
    }
}
```

<br/>


除了 Collection.Insert，也可以使用 Collection.InsertBulk 塞入多筆資料，調用 Collection.InsertBulk 並帶入資料的集合與批次的大小，資料就會依指定的批次大小批次塞入。  

```C#
…
using (var db = new LiteDatabase(dbFile)) 
{ 
  var collection = db.GetCollection<T>(collectionName); 

  collection.InsertBulk(data, batchSize); 
} 
```

<br/>


像是下面這樣：

```C#
using System;
using System.Diagnostics;
using System.Linq;

namespace LiteDB.Demo3
{
    class Program
    {
        static void Main(string[] args)
        {
            using (var db = new LiteDatabase("Person.db"))
            {
                var persons = db.GetCollection<Person>("persons");
                var count = 1000000;
                var data = Enumerable.Range(1, count).Select(item => new Person
                {
                    Name = "Larry Nung " + item,
                    NickName = "Larry " + item
                }).ToArray();
                persons.InsertBulk(data);
            }
        }
    }

    public class Person
    {
        public int ID { get; set; }
        public String Name { get; set; }
        public String NickName { get; set; }
    }
}
```