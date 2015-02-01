---
layout: post
title: "PostSharp - Automatically Implementing INotifyPropertyChanged"
date: 2015-02-01 21:01
comments: true
categories: [PostSharp]
keywords: "PostSharp, INotifyPropertyChanged"
description: "PostSharp - Automatically Implementing INotifyPropertyChanged"
---

要用 PostSharp 自動實作 INotifyPropertyChanged，在安裝完 PostSharp 擴充套件後，我們可以在類別上直接按下右鍵，在彈出的滑鼠右鍵快顯選單中，選取 `Implement INotifyPropertyChanged` 選單選項。  

<!-- More -->

{% img /images/posts/PostSharpINotifyPropertyChangedImplement/1.png %}

<br/>


接著 PostSharp 擴充套件會帶出精靈視窗，這邊直接 Next。  

{% img /images/posts/PostSharpINotifyPropertyChangedImplement/2.png %}

<br/>


這邊進度會跑一陣子，因為 PostSharp 會將缺少的參考幫我們加入專案，並將修改套到我們的程式碼。  

{% img /images/posts/PostSharpINotifyPropertyChangedImplement/3.png %}

<br/>


進度跑完後按下 Finish 按鈕結束精靈視窗即可。  

{% img /images/posts/PostSharpINotifyPropertyChangedImplement/4.png %}

<br/>


回過頭來看一下我們的專案，可以發現缺少的 PostSharp 參考被加入專案，且我們的類別上面被加上了 NotifyPropertyChanged 的 Attribute (可參閱 [NotifyPropertyChangedAttribute Class](http://doc.postsharp.net/t_postsharp_patterns_model_notifypropertychangedattribute)，套上這 Attribute 會讓該類別及其子類都實作 INotifyPropertyChanged)。  

{% img /images/posts/PostSharpINotifyPropertyChangedImplement/5.png %}

<br/>


到這邊已經用 PostSharp 幫我們自動實作完 INotifyPropertyChanged 了，若有需要可將滑鼠移至類別上再次進行確認，沒意外的話就會看到確實已經套用完成(若沒有這畫面可能是因為資料還未更新完成，可嘗試重建專案看看)。  

{% img /images/posts/PostSharpINotifyPropertyChangedImplement/6.png %}

<br/>


若再次用反射進行解析。  

{% codeblock lang:c# %} 
using System;
using System. Collections.Generic ;
using System. Linq;
using System. Text;
using PostSharp. Patterns.Model ;


namespace ConsoleApplication32
{
    class Program
    {
        static void Main( string[] args )
        {
            var blog = new Blog ("LevelUp", "http://larrynung.github.io" );


            foreach (var @interface in blog .GetType() .GetInterfaces())
                Console.WriteLine (@interface. Name);
        }
    }


    [ NotifyPropertyChanged ]
    public class Blog
    {
        public string Name { get; set ; }
        public string Url { get; set ; }
        public Blog (string name, string url)
        {
            this.Name = name;
            this.Url = url;
        }
    }
}
{% endcodeblock%}


可看到該介面確實已經實作。  

{% img /images/posts/PostSharpINotifyPropertyChangedImplement/7.png %}

<br/>

最後一提，上述介紹的是用精靈介面下去操作，若不想使用精靈介面亦可，只要留意透過精靈介面對專案造成了什麼影響就會知道了。簡單的說只要引用 PostSharp.Patterns.Model 套件，並將類別加上 NotifyPropertyChangedAttribute 即可。  

<br/>


Link
----
* [Walkthrough: Automatically Implementing INotifyPropertyChanged](http://doc.postsharp.net/inotifypropertychanged-add)
* [NotifyPropertyChangedAttribute Class](http://doc.postsharp.net/t_postsharp_patterns_model_notifypropertychangedattribute)
