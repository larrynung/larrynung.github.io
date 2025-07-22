---
title: "[C#]Linq在使用Distinct去除重複資料時如何指定所要依據的成員屬性"
slug: "[CSharp]Linq在使用Distinct去除重複資料時如何指定所要依據的成員屬性"
date: "2013-11-06 12:00:00"
description: "[C#]Linq在使用Distinct去除重複資料時如何指定所要依據的成員屬性"
tags: [CSharp]
---最近專案中在用Linq Distinct想要將重複的資料去除時，發現它跟Any之類的方法有點不太一樣，不能很直覺的在呼叫時直接帶入重複資料判斷的處理邏輯，所以當我們要用某個成員屬性做重複資料的判斷時，就必需繞一下路，這邊稍微將處理的方法做個整理並記錄一下。

首先為了方便接下去說明，我們必須先來準備後面會用到的資料類別，這邊一樣用筆者最常用來示範的Person類別，內含兩個成員屬性ID與Name。

public struct Person
{
#region Property
///
/// Gets or sets the ID.
///
/// The ID.
public string ID { get; set; }

///
/// Gets or sets the name.
///
/// The name.
public string Name { get; set; }
#endregion

#region Public Method
///
/// Returns a that represents this instance.
///
///
/// A that represents this instance.
///
public override string ToString()
{
return Name;
}
#endregion

接著準備要用來測試的資料，這邊準備了十一個Person物件，前十個物件的名稱都是Larry，第十一個物件的名稱為LastLarry。期望後面可以透過Distinct將重複的Larry過濾掉。

...
var datas = new List();
int idx = 0;
for (idx = 0; idx (IEnumerable datas)
{
foreach (var data in datas)
{
Console.WriteLine(data.ToString());
}
}

可以看到運行起來並不如我們所預期的，過濾出來的資料跟沒過濾一樣。

為了解決這個問題，我們必須要做個可依照Person.Name去做比較的Compare類別，該Compare類別必須實做IEqualityCompare.Equals與IEqualityCompare.GetHashCode方法，並在呼叫Distinct過濾時將該Compare物件帶入。

...
distinctDatas = datas.Distinct(new PersonCompare());
ShowDatas(distinctDatas);
...
class PersonCompare : IEqualityComparer
{
#region IEqualityComparer Members

public bool Equals(Person x, Person y)
{
return x.Name.Equals(y.Name);
}

public int GetHashCode(Person obj)
{
return obj.Name.GetHashCode();
}

#endregion
}

運行起來就會是我們所期望的樣子。

但是這樣做代表我們每次碰到新的類別就必須要實現對應的Compare類別，用起來十分的不便。因此有人就提出用泛型加上反射的方式做一個共用的Compare類別。

public class PropertyComparer : IEqualityComparer
{
private PropertyInfo _PropertyInfo;

///
/// Creates a new instance of PropertyComparer.
///
/// The name of the property on type T
/// to perform the comparison on.
public PropertyComparer(string propertyName)
{
//store a reference to the property info object for use during the comparison
_PropertyInfo = typeof(T).GetProperty(propertyName,
BindingFlags.GetProperty | BindingFlags.Instance | BindingFlags.Public);
if (_PropertyInfo == null)
{
throw new ArgumentException(string.Format("{0} is not a property of type {1}.", propertyName, typeof(T)));
}
}

#region IEqualityComparer Members

public bool Equals(T x, T y)
{
//get the current value of the comparison property of x and of y
object xValue = _PropertyInfo.GetValue(x, null);
object yValue = _PropertyInfo.GetValue(y, null);

//if the xValue is null then we consider them equal if and only if yValue is null
if (xValue == null)
return yValue == null;

//use the default comparer for whatever type the comparison property is.
return xValue.Equals(yValue);
}

public int GetHashCode(T obj)
{
//get the value of the comparison property out of obj
object propertyValue = _PropertyInfo.GetValue(obj, null);

if (propertyValue == null)
return 0;

else
return propertyValue.GetHashCode();
}

#endregion
}

使用時只要帶入泛型的型態與成原屬性的名稱，就可以產生出需要的Compare物件。

...
distinctDatas = datas.Distinct(new PropertyComparer("Name"));
ShowDatas(distinctDatas);
...

這樣的作法是減少了許多額外的負擔，但是感覺還是少了一條路，用起來也還是必須要建立Compare物件，而且反射也存在著效能的問題，如果每個元素都透過這個Compare去做判斷，感覺處理上也不是很漂亮。所以有人也意識到了這個問題，用擴充方法提供了一條我們比較熟悉的路，可以直接將Lambda帶入以決定元素要怎樣過濾。

public static class EnumerableExtender
{
public static IEnumerable Distinct(this IEnumerable source, Func keySelector)
{
HashSet seenKeys = new HashSet();
foreach (TSource element in source)
{
var elementValue = keySelector(element);
if (seenKeys.Add(elementValue))
{
yield return element;
}
}
}
}

使用上會好寫許多。

...
distinctDatas = datas.Distinct(person => person.Name);
ShowDatas(distinctDatas);
...

若是不想加入額外的類別，我們也可以透過Group方式來達到類似的效果。

distinctDatas = from data in datas
group data by data.Name into g
select g.First();
ShowDatas(distinctDatas);

##
Link

Linq Distinct on a particular Property

Linq Distinct with a single comparison class (and interface)

LINQ Select Distinct on Custom Class Property

A Generic IEqualityComparer for Linq Distinct()