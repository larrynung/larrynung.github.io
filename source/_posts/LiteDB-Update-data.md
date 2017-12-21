---
title: LiteDB - Update data
date: 2017-12-18 06:48:44
tags: [LiteDB]
---

要將 LiteDB 內的資料更新，需先將 LiteDB 開啟，取得 Collection，取得 Collection 內的元素，更新元素的屬性值後，再用 Collection.Update 將資料更新回 LiteDB 即可。  

<!-- More -->

```C#
…
using (var db = new LiteDatabase(dbFile)) 
{ 
  var collection = db.GetCollection<T>(collectionName); 
  ...
  collectionItem.Property = newValue;
  collection.Update(collectionItem); 
} 
```

<br/>



像是下面這個範例就會將資料寫入，將塞入的資料做個變更。  

```C#
using System;

namespace LiteDB.Demo2
{
    class Program
    {
        static void Main(string[] args)
        {
            using (var db = new LiteDatabase("Person.db"))
            {
                var persons = db.GetCollection<Person>("persons");

                var firstPerson = collection.FindById(1);

                firstPerson.Name = "Larry Nung";
                firstPerson.NickName = "Larry";
                persons.Update(firstPerson);
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


若是要更新為全新的資料，也可以建立個資料物件指定 ID 將之替換。  

```C#
using System;

namespace LiteDB.Demo2
{
    class Program
    {
        static void Main(string[] args)
        {
            using (var db = new LiteDatabase("Person.db"))
            {
                var persons = db.GetCollection<Person>("persons");

                persons.Update(1, new Person()
                {
                    Name = "Larry Nung",
                    NickName = "Larry Nung"
                });
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


```C#
using System;

namespace LiteDB.Demo2
{
    class Program
    {
        static void Main(string[] args)
        {
            using (var db = new LiteDatabase("Person.db"))
            {
                var persons = db.GetCollection<Person>("persons");

                persons.Update(new Person()
                {
                    ID = 1,
                    Name = "Larry Nung",
                    NickName = "Larry Nung"
                });
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