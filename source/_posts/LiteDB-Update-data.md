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

                var larry = new Person
                {
                    Name = "Larry Nung",
                    NickName = "Larry"
                };

                persons.Insert(larry);

                larry.NickName = "Larry Nung";
                persons.Update(larry);

                
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
