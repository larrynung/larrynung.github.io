---
title: 'C# 7.0 - Throw expressions'
date: 2017-03-10 23:47:25
tags: [CSharp, CSharp 7.0]
---

C# 7.0 開始支援	Throw expressions。  

<!-- More -->

<br/>


三元運算中可以視需要直接丟出 exception。  

{% codeblock lang:C# %}
...
this.FirstName = firstName == null ? throw new ArgumentNullException(nameof(firstName)) : firstName;
...
{% endcodeblock %}

<br/>


?? 運算式中也可以直接丟出 exception。  

{% codeblock lang:C# %}
...
this.LastName = lastName ?? throw new ArgumentNullException(nameof(lastName));
...
{% endcodeblock %}

<br/>


Expression bodied member 也可以丟出 exception。  

{% codeblock lang:C# %}
...
public override string ToString() => throw new NotImplementedException();
...
{% endcodeblock %}

<br/>


最後附上完整的測試範例：  

{% codeblock lang:C# %}
    class Program
    {
        static void Main(string[] args)
        {
            var person = new Person("Larry", "Nung");
            Console.WriteLine(person.ToString());
        }
    }
    struct Person
    {
        public string FirstName { get; set; }
        public string LastName { get; set; }

        public Person(string firstName, string lastName)
        {
            this.FirstName = firstName == null ? throw new ArgumentNullException(nameof(firstName)) : firstName;
            this.LastName = lastName ?? throw new ArgumentNullException(nameof(lastName));
        }

        public override string ToString() => throw new NotImplementedException();
    }
{% endcodeblock %}

<br/>


Link
=====
* [What’s New in C# 7.0 | .NET Blog](https://blogs.msdn.microsoft.com/dotnet/2016/08/24/whats-new-in-csharp-7-0/)
