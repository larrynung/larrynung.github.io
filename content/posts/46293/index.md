---
title: "[C#].NET 4.5 New Feature - Regex match with timeout"
slug: "csharp-dotnet-4-5-new-feature-regex-match-with-timeout"
aliases: ["/posts/csharp.net-4.5-new-feature-regex-match-with-timeout/"]
date: "2011-10-25 01:20:13"
description: ".Net 4.5中Regex多了一個內含Timespan的多載版本，該多載版本方法允許開發人員帶入一個TimeSpan指定Timeout的值，當正規表示式比對運行超過指定的時間即中止比對。"
tags: [CSharp]
---

.Net 4.5中Regex多了一個內含Timespan的多載版本，該多載版本方法允許開發人員帶入一個TimeSpan指定Timeout的值，當正規表示式比對運行超過指定的時間即中止比對。

![image_thumb_2.png](/images/posts/46293/image_thumb_2.png)

Timeout的時間除了可以透過上述的多載方法傳入外，也可以透過用AppDomain.SetData設定REGEX_DEFAULT_MATCH_TIMEOUT，可指定預設的Timeout值。當正規表示式在做比對時未帶入指定的Timeout值，系統都會使用設定到AppDomain的Timeout去處理。

```csharp
AppDomain.CurrentDomain.SetData("REGEX_DEFAULT_MATCH_TIMEOUT", TimeSpan.FromSeconds(2));
```

對於Timeout的設定值在設定時也有些限制，像是其值必須大於零，且必須要小於25天，不然在運行時會發出ArgumentOutOfRangeException的例外。

```csharp
isMatch = IsMatch(input, pattern, TimeSpan.FromMilliseconds(0));
isMatch = IsMatch(input, pattern, TimeSpan.FromMilliseconds(-2));
isMatch = IsMatch(input, pattern, TimeSpan.FromDays(25));
```

若是想要不限制Timeout時間，可帶入-1或是Regex.InfiniteMatchTimeout來做為Timeout的設定值。

```csharp
isMatch = IsMatch(input, pattern, Regex.InfiniteMatchTimeout);
isMatch = IsMatch(input, pattern, TimeSpan.FromMilliseconds(-1));
```

設好Timeout後進行正規表示試的比對，當比對時間超過指定的Timeout時間時，系統會發出RegexMatchTimeoutException例外告知，可以從例外中取得比對的字串、比對的Pattern、Timeout值等資訊。(可參閱MSDN中的RegexMatchTimeoutException Class)

![image_thumb.png](/images/posts/46293/image_thumb.png)

完整範例如下：

```csharp
class Program
{
    static void Main(string[] args)
    {
        string input = "The quick brown fox jumps over the lazy dog.";
        string pattern = @"([a-z ]+)*!";
        Boolean isMatch = false;

        AppDomain.CurrentDomain.SetData("REGEX_DEFAULT_MATCH_TIMEOUT", TimeSpan.FromSeconds(2));
        isMatch = IsMatch(input, pattern);

        Console.WriteLine();
        isMatch = IsMatch(input, pattern, TimeSpan.FromSeconds(4));
    }

    static Boolean IsMatch(string input, string pattern)
    {
        try
        {
            return Regex.IsMatch(input, pattern, RegexOptions.None);
        }
        catch (RegexMatchTimeoutException ex)
        {
            // handle exception
            Console.WriteLine("Match timed out!");
            Console.WriteLine("- Timeout interval specified: " + ex.MatchTimeout);
            Console.WriteLine("- Pattern: " + ex.Pattern);
            Console.WriteLine("- Input: " + ex.Input);
        }

        return false;
    }

    static Boolean IsMatch(string input, string pattern, TimeSpan timeout)
    {
        try
        {
            return Regex.IsMatch(input, pattern, RegexOptions.None, timeout);
        }
        catch(ArgumentOutOfRangeException ex)
        {
            Console.WriteLine(ex.Message);
        }
        catch (RegexMatchTimeoutException ex)
        {
            // handle exception
            Console.WriteLine("Match timed out!");
            Console.WriteLine("- Timeout interval specified: " + ex.MatchTimeout);
            Console.WriteLine("- Pattern: " + ex.Pattern);
            Console.WriteLine("- Input: " + ex.Input);
        }

        return false;
    }
}
```

運行結果如下：

![image_thumb_3.png](/images/posts/46293/image_thumb_3.png)

## Link

* RegexMatchTimeoutException Class
* Regular Expressions with Timeout in .NET 4.5
* Regex engine updated to allow timeouts in .NET 4.5
* Regex.IsMatch Method (String, String, RegexOptions, TimeSpan)
* Regex.InfiniteMatchTimeout Field
