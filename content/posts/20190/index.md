---
title: ".NET 4.0 New Feature - IObservablelt;Tgt; & IObserverlt;Tgt;"
date: "2010-12-16 09:00:01"
description: ".NET 4.0 New Feature - IObservable<T> & IObserver<T>"
tags: [CSharp]
---

IObservable<T> & IObserver<T>為一種推入型通知的通用機制，為觀察者模式的實現，在.NET 4.0開始加入到BCL中 ，跟以往IEnumerable與IEnumerator這種拉出型通知的通用機制有所不同。

IEnumerable & IEnumerator這種迭代器模式屬於拉出型通知的通用機制，也就是說資料需由消費者自行從提供者拉出，就像是我們在食堂點餐必需排隊取餐，取餐的速度取決於食堂生產的速度，只要還沒排到或還在準備，我們都只能站在隊伍中繼續等候，待拿到餐點才能離開對伍找位置坐下開動，而IObservable<T> & IObserver<T>這種觀察者模式屬於推入型通知的通用機制，資料可由提供者主動推向給消費者，就像是在餐廳吃飯，我們點好餐點就可以開始聊天或做些其它事情，餐點完成服務員會主動奉上，拿到餐點後我們就可以開始開動。

IObservable<T>為負責傳送通知的類別，是資料的提供者，其具有一個名為Subscribe的Method，提供觀察者訂閱通知，用以通知有觀察者想要接收通知。

```csharp
public interface IObservable<out T>
{
      IDisposable Subscribe(IObserver<T> observer);
}
```

IObserver<T>為負責接收通知的類別 ，為一觀察者，具有三個Method，分別為OnNext方法，用以通知觀察者有新的資料;OnError方法用以通知觀察者有錯誤發生；OnCompleted則用以通知已沒有資料可送，傳送完成。

```csharp
public interface IObserver<in T>
{
    void OnCompleted();
    void OnError(Exception error);
    void OnNext(T value);
}
```

看到這邊不知道大家有沒有發現，其實IObservable<T> & IObserver<T>與IEnumerable & IEnumerator是對偶的存在，IObservable<T>.Subscribe對應到IEnumerable的GetEnumerator，一個是送入觀察者，一個是取出迭代器；IObserver<T>.OnNext跟IEnumerator.Current對應，一個是送入資料，一個是取出資料；IObserver<T>.OnError則是對應到IEnumerator.MoveNext若有問題時會拋出異常；IObserver<T>.OnCompleted與IEnumerator.MoveNext沒有資料時會返回False的行為對應。

這邊要注意一點，若是細看上面的IObservable<T>定義，你可能會發現到有Subscribe，但取消訂閱卻沒有對應的方法，其實這邊微軟在IObservable(Of T).Subscribe 方法有提到"此方法會將參考傳回 [IDisposable](http://msdn.microsoft.com/zh-tw/library/system.idisposable.aspx) 介面。 這可讓觀察者在提供者完成傳送並呼叫訂閱者 [OnCompleted 方法之前取消訂閱 (也就是要停止接收通知)。"，也就是說取消訂閱的動作是透過IObservable<T>.Subscribe回傳的IDisposable去釋放，所以我們可以像下面實作在釋放時能將訂閱取消的類別：](http://msdn.microsoft.com/zh-tw/library/dd782982.aspx)

```csharp
private class Unsubscriber : IDisposable
    {
        private List<IObserver<T>> m_Observers { get; set; }
        private IObserver<T> m_Observer { get; set; }

        public Unsubscriber(List<IObserver<T>> observers, IObserver<T> observer)
        {
            this.m_Observers = observers;
            this.m_Observer = observer;
        }

        public void Dispose()
        {
            if (m_Observer != null && m_Observers.Contains(m_Observer))
            {
                m_Observers.Remove(m_Observer);
            }
        }
    }
```

在訂閱時將取消訂閱用的物件實體回傳，供訂閱者取消訂閱用：

```csharp
public IDisposable Subscribe(IObserver<T> observer)
    {
        if (!m_Observers.Contains(observer))
        {
            m_Observers.Add(observer);
        }
        return new Unsubscriber(m_Observers, observer);
    }
```

這邊實作了一個較完整點的範例：

Observable.CS

```csharp
using System;
using System.Collections.Generic;

public class Observable<T> : IObservable<T>
{
    #region Class
    private class Unsubscriber : IDisposable
    {
        private List<IObserver<T>> m_Observers { get; set; }
        private IObserver<T> m_Observer { get; set; }

        public Unsubscriber(List<IObserver<T>> observers, IObserver<T> observer)
        {
            this.m_Observers = observers;
            this.m_Observer = observer;
        }

        public void Dispose()
        {
            if (m_Observer != null && m_Observers.Contains(m_Observer))
            {
                m_Observers.Remove(m_Observer);
            }
        }
    }
    #endregion

    #region Enum
    enum NotifyType
    {
        Next,
        Completed,
        Error
    }
    #endregion

    #region Var
    private List<IObserver<T>> _observers;
    #endregion

    #region Protected Property
    protected List<IObserver<T>> m_Observers
    {
        get
        {
            if (_observers == null)
                _observers = new List<IObserver<T>>();
            return _observers;
        }
    }
    #endregion

    #region Private Method
    private void NotifyError(Exception error)
    {
        foreach (IObserver<T> observer in m_Observers)
        {
            observer.OnError(error);
        }
    }
    #endregion

    #region Protected Method
    protected void NotifyNext(T obj)
    {
        try
        {
            foreach (IObserver<T> observer in m_Observers)
            {
                observer.OnNext(obj);
            }
        }
        catch (Exception e)
        {
            NotifyError(e);
        }
    }

    protected void NotifyCompleted()
    {
        try
        {
            foreach (IObserver<T> observer in m_Observers)
            {
                observer.OnCompleted();
            }
        }
        catch (Exception e)
        {
            NotifyError(e);
        }
    }
    #endregion

    #region Public Method
    public IDisposable Subscribe(IObserver<T> observer)
    {
        if (!m_Observers.Contains(observer))
        {
            m_Observers.Add(observer);
        }
        return new Unsubscriber(m_Observers, observer);
    }
    #endregion
}
```

Program.CS

```csharp
using System;
using System.Collections.Generic;

namespace ConsoleApplication5
{
    class Program
    {
        static void Main(string[] args)
        {
            BlogViwer guest = new BlogViwer();
            Blog levelUp = new Blog("Level Up", "Larry Nung");
            levelUp.Subscribe(guest);
            levelUp.AddArticle(".NET 4.0 New Feature - Environment.Is64BitProcess & Environment.Is64BitOperatingSystem", "...");
            levelUp.AddArticle("LINQ to CSV library", "...");
            levelUp.AddArticle("[C#][VB.NET]最大公因數 & 最小公倍數", "...");
        }
    }

    class Blog : Observable<string>
    {
        List<string> _articles;
        private List<string> Articles
        {
            get
            {
                if (_articles == null)
                    _articles = new List<string>();
                return _articles;
            }
        }

        public String Name { get; set; }
        public String Owner { get; set; }

        public Blog(String name, string owner)
        {
            this.Name = name;
            this.Owner = owner;
        }

        public void AddArticle(string title, string content)
        {
            string article = title + Environment.NewLine + content;
            Articles.Add(article);
            NotifyNext(article);
        }
    }

    class BlogViwer : IObserver<string>
    {
        public void OnCompleted()
        {
            Console.WriteLine("Completed...");
        }

        public void OnError(Exception error)
        {
            Console.WriteLine("Error...");
        }

        public void OnNext(string value)
        {
            Console.WriteLine(value);
            Console.WriteLine(new string('"', 50));
        }
    }
}
```

執行結果如下：

![image_thumb.png](/images/posts/20190/image_thumb.png)

## Download

ObserverDemo.zip

## Link

* IObserver(Of T) 介面
* IObservable(Of T) 介面
* IObserver and IObservable - A New addition to BCL
