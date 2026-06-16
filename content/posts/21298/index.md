---
title: "Implementing the IEnumerable & IEnumerator Interfaces"
slug: "implementing-the-ienumerable-ienumerator-interfaces"
aliases: ["/posts/21298/"]
date: "2011-02-09 07:15:52"
description: "實作IEnumerable & IEnumerator介面最主要的好處是該類別能被foreach直接遍巡處理，有鑒於網路上存在許多IEnulerable & IEnumerator介面的實作方式跟個人的理解有所出入，這邊將個人的理解稍作了整理。"
tags: [CSharp]
---

實作IEnumerable & IEnumerator介面最主要的好處是該類別能被foreach直接遍巡處理，有鑒於網路上存在許多IEnulerable & IEnumerator介面的實作方式跟個人的理解有所出入，這邊將個人的理解稍作了整理。

IEnumerator介面的組成成員如下，內含有Current屬性與MoveNext、Reset兩個方法。

```csharp
public interface IEnumerator
{
    object Current { get; }
    bool MoveNext();
    void Reset();
}
```

```

```

其中Current成員方法可用以取得目前遍巡到的項目。在MSDN上有清楚的提到當列舉索引在第一個項目之前，或是最後一個項目之後，也就是說當列舉索引是不合法時會拋出InvalidOperationException例外。

```

```

因此在MSDN的範例中會像下面這樣撰寫，直接將索引位置的資料回傳，並利用try/catch欄截索引錯誤的例外，當例外發生時改丟InvalidOperationException例外。

```csharp
public object Current
    {
        get
        {
            try
            {
                return _people[position];
            }
            catch (IndexOutOfRangeException)
            {
                throw new InvalidOperationException();
            }
        }
    }
```

MoveNext方法可將索引位置往前推至下個項目，並回傳是否還有可遍巡的元素。

```csharp
public bool MoveNext()
    {
        position++;
        return (position < _people.Length);
    }
```

```

```

Reset方法則是將索引位置移回到遍巡開始前，也就是回到第一個元素前。

```csharp
public void Reset()
    {
        position = -1;
    }
```

IEnumerable介面的組成成員如下，只有內含一個GetEnumerator方法。

```csharp
public interface IEnumerable
{
    IEnumerator GetEnumerator();
}
```

```

```

GetEnumerator方法呼叫後會回傳IEnumerator介面的物件實體，在該方法的實作常常會被誤用，舉個例子來說，有的教學會直接將類別同時實作IEnumerable與IEnumerator這兩個介面，然後實作該方法時直接像是下面這樣：

```csharp
public IEnumerator GetEnumerator()
    {
        return this;
    }
```

```

```

這樣的作法會有問題，因為遍巡完後索引並不會自動再次初始，故當第二次遍巡時就會發生異常。且這時物件的實體也只有一份，索引也只有一份，同時間給不同的執行緒去遍巡可能也會發生錯亂的情況。

這樣的問題若有注意到MSDN的範例寫法，其實會發現MSDN上的範例已經避開了。MSDN的範例兩個介面是用不同類別去實作，PeopleEnum為列舉People用的迭代器類別，透過People.GetEnumerator可以取得PeopleEnum的迭代器物件實體，該物件實體每次叫用GetEnumerator都會去產生，故皆為不同的物件實體，且各自含有各自的索引，故可免除上述的問題。

```csharp
public IEnumerator GetEnumerator()
    {
        return new PeopleEnum(_people);
    }
```

```

```

若想要將兩個介面實作在同一個類別上，我們也可以參考MSDN的範例，開ㄧ個建構子讓GetEnumerator方法產生物件副本回傳。

```csharp
public class PersonCollection : IEnumerable,IEnumerator
    {
        ...
        public PersonCollection(Person[] list)
        {
            _peoples = list;
        }
       ...
        public IEnumerator GetEnumerator()
        {
            return new PersonCollection(_peoples);
        }
    }
```

完整範例如下：

```csharp
{
        static void Main(string[] args)
        {

            PersonCollection persons = new PersonCollection ( new Person[]{new Person("Larry")});
            foreach (Person person in persons)
            {
                Console.WriteLine(person.Name);
            }
            foreach (Person person in persons)
            {
                Console.WriteLine(person.Name);
            }
        }
    }

      public class Person {
          public string Name { get; set; }

          public Person(string name)
          {
              this.Name = name;
          }
    }

    public class PersonCollection : IEnumerable,IEnumerator
    {
        private Person[] _peoples;
        private int position = -1;

        public PersonCollection(Person[] list)
        {
            _peoples = list;
        }

        public bool MoveNext()
        {
            position++;
            return (position < _peoples.Length);
        }

        public void Reset()
        {
            position = -1;
        }

        public object Current
        {
            get
            {
                try
                {
                    return _peoples[position];
                }
                catch (IndexOutOfRangeException)
                {
                    throw new InvalidOperationException();
                }
            }
        }

        public IEnumerator GetEnumerator()
        {
            return new PersonCollection(_peoples);
        }
    }
```

## Link

* When IEnumerator.Reset() method is called ? - Stack Overflow
* IEnumerable 介面
* IEnumerator 介面
