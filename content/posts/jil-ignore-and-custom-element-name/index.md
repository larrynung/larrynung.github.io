---
title: "Jil - Ignore amp; Custom Element Name"
date: "2015-10-02 00:11:00"
description: "Jil - Ignore &amp; Custom Element Name"
tags: [Jil]
---


使用 Jil 處理 JSON 時，如果要在序列化時忽略處理某特定屬性，可在其屬性加上 IgnoreDataMemberAttribute，像是下面這樣：  

<!-- More -->


```c#
using System;
using System. Runtime.Serialization ;
using Jil;

namespace ConsoleApplication10
{
    class Program
    {
        static void Main( string[] args )
        {
            var larry = new Person
            {
                Name = "Larry Nung",
                NickName = "Larry"
            };

            Console.WriteLine (JSON. Serialize(larry ));
        }

        public class Person
        {
            [ DataMember]
            public String Name { get; set ; }

            [ IgnoreDataMember]
            public String NickName { get; set ; }
        }
    }
}
```

<br/>


或是帶上 JilDirectiveAttribute，指定 Ignore：  

```c#
using System;
using System. Runtime.Serialization ;
using Jil;

namespace ConsoleApplication10
{
    class Program
    {
        static void Main( string[] args )
        {
            var larry = new Person
            {
                Name = "Larry Nung",
                NickName = "Larry"
            };

            Console.WriteLine (JSON. Serialize(larry ));
        }

        public class Person
        {
            [ JilDirective(false )]
            public String Name { get; set ; }

            [ JilDirective(true )]
            public String NickName { get; set ; }
        }
    }
}
```

{% img /images/posts/JilIgnoreAndCustomElement/1.png %}

<br/>


如果要客製輸出的 Element 名稱，則直接透過 JilDirectiveAttribute 帶入指定的名稱：  

```c#
using System;
using System. Runtime.Serialization ;
using Jil;

namespace ConsoleApplication10
{
    class Program
    {
        static void Main( string[] args )
        {
            var larry = new Person
            {
                Name = "Larry Nung",
                NickName = "Larry"
            };

            Console.WriteLine (JSON. Serialize(larry ));
        }

        public class Person
        {
            [ JilDirective("name" )]
            public String Name { get; set ; }

            [ JilDirective(true )]
            public String NickName { get; set ; }
        }
    }
}
```

{% img /images/posts/JilIgnoreAndCustomElement/2.png %}
