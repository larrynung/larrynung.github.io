---
title: LiteDB - Query data
date: 2017-12-18 23:08:26
tags: [LiteDB]
---

要取得 LiteDB 內的資料，首先需先將 LiteDB 開啟，取得對應的 Collection，調用 Collecion.FindAll 即可取得 Collection 內所有的資料。  

<!-- More -->

```C#
...
using (var db = new LiteDatabase(dbFile))
{
  var collection = db.GetCollection<T>(collectionName);
  ...
  var collectionItems = collection.FindAll();
  ...
}
```

<br/>


```C#
using System;

namespace LiteDB.Demo8
{
    class Program
    {
        static void Main(string[] args)
        {
            using (var db = new LiteDatabase("Person.db"))
            {
                var persons = db.GetCollection<Person>("persons"); 

                foreach (var person in persons.FindAll())
                {
                    Console.WriteLine(person.NickName);
                }
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


要找尋滿足特定條件的資料的話，可以調用 Collection.Find 方法，並用 Lambda 帶入要過濾的條件。  

```C#
...
using (var db = new LiteDatabase(dbFile))
{ 
  var collection = db.GetCollection<T>(collectionName);
  ...
  var collectionItems = collection.Find(item => filter(item));
  ...
}
```

<br/>


```C#
using System;

namespace LiteDB.Demo8
{
    class Program
    {
        static void Main(string[] args)
        {
            using (var db = new LiteDatabase("Person.db"))
            {
                var persons = db.GetCollection<Person>("persons"); 

                foreach (var person in persons.Find(item => item.ID < 10))
                {
                    Console.WriteLine(person.NickName);
                }
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


如果要過濾的資料只有單筆的話，可以調用 Collection.FindOne 方法。  

```C#
...
using (var db = new LiteDatabase(dbFile))
{ 
  var collection = db.GetCollection<T>(collectionName);
  ...
  var collectionItem = collection.FindOne(item => filter(item));
  ...
}
```

<br/>


```C#
using System;

namespace LiteDB.Demo8
{
    class Program
    {
        static void Main(string[] args)
        {
            using (var db = new LiteDatabase("Person.db"))
            {
                var persons = db.GetCollection<Person>("persons"); 

                var larry = persons.FindOne(item => item.ID == 1);
                Console.WriteLine(larry.NickName);
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


要過濾出指定索引資料的話，可帶入要抓取資料的索引值去調用 Collection.FindById。  


```C#
...
using (var db = new LiteDatabase(dbFile)) 
{ 
  var collection = db.GetCollection<T>(collectionName); 
  ...
  var collectionItem = collection.FindById(itemIdx);
  ...
}
```

<br/>


```C#
using System;

namespace LiteDB.Demo8
{
    class Program
    {
        static void Main(string[] args)
        {
            using (var db = new LiteDatabase("Person.db"))
            {
                var persons = db.GetCollection<Person>("persons"); 

                var larry = persons.FindById(1);
                Console.WriteLine(larry.NickName);
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
