---
title: "[C#]Command Line Parser Library"
slug: "[CSharp]Command Line Parser Library"
date: "2013-11-06 12:00:00"
description: "[C#]Command Line Parser Library"
tags: [CSharp]
---

前陣子為程式加上命令列參數去啟動除錯的功能，先暫時套用筆者之前看到的Brahma Command Line Parser來做到這個需求，用了一陣子還是覺得卡手卡腳的，明明只想帶個簡單的參數進去，卻因為用的solution變得必須要帶較為複雜的參數。因此還是花了一下時間用Command Line Parser Library將他重寫，這篇筆者就稍微簡單的紀錄一下Command Line Parser Library的使用方式。

Command Line Parser Library這個函式庫主要是輔助開發人員做命令列參數的處理，可以很輕鬆的為程式加上完整的命令列參數支援，可適用於：

* CSharp 3.0+
* .NET Framework 2.0+
* Mono Profile 2.1+

(依筆者的經驗，雖然相容於.NET 2.0，但預設抓下來的是.NET 4.0的組件，若有需要需自行下載程式碼編譯使用)

使用前須先下載組件並將其加入參考。這邊我們可透過NuGet直接安裝。

![image_thumb.png](/images/posts/f70bafcb-8353-4c5a-be03-40fa5f3396b3/image_thumb.png)

![image_thumb_1.png](/images/posts/f70bafcb-8353-4c5a-be03-40fa5f3396b3/image_thumb_1.png)

組件加入參考後，我們必須為程式碼加入CommandLine命名空間，若是有要使用HelpText的話，CommandLine.Text命名空間也需加入。

```csharp
using CommandLine;
using CommandLine.Text;
```

接著我們要為命令列參數建立一個對應的處理類別，為每個命令列參數加上對應的成員屬性，並為其加上CommandLineParser內建的Attribute，帶入參數的short name、lone name、help text...，用以告訴CommandLineParser要怎樣去處理這樣的參數。

```csharp
public class Options
{
	...
	[Option("i", "input", Required = true, HelpText = "Input file to read.")]
	public string InputFile { get; set; }

	[OptionArray("o", "output", HelpText = "The output files to generate.")]
	public string[] OutputFiles { get; set; }

	[OptionList("k", "keywords", Separator = ':', HelpText = "Specify keywords to search the text, separated by a colon.")]
	public List<string> Keywords { get; set; }

	[ValueList(typeof(List<string>), MaximumElements = 3)]
	public List<string> Items { get; set; }
	...
}
```

命令列參數對應的類別設定好後，我們就可以像下面這樣在程式起來時去解析帶進程式的命令列參數。簡單來說，這邊就只要建立出命令列參數對應類別的物件實體，然後交給CommandLineParser.ParseArguments去解析就可以了，回傳值會明確的告知命令列參數解析成功與否，若是命令列參數解析成功，這邊帶進去的命令列參數對應類別的物件實體，它的成員屬性就會被填入對應的值，所以我們可以在命令列參數解析成功後依其值做對應的處理。

```csharp
...
var options = new Options();
ICommandLineParser parser = new CommandLineParser();
if (parser.ParseArguments(args, options))
{
	...
}
...
```

命令列參數對應的類別其成員屬性可以套用的Attribute有OptionAttribute、OptionArrayAttribute、OptionListAttribute、與ValueListAttribute，可視命令列參數使用的方式套用不同的Attribute。OptionAttribute表示參數Key與值是一對一的情況。OptionArrayAttribute表示參數Key與值是一對多，且多個值之間是用空格分隔。OptionListAttribute跟OptionArrayAttribute一樣是表示參數Key與值是一對多的關係，但各值之間的分隔可自行定義。所以像是上面的例子，我們就可以像下面這樣的帶入命令列參數：

![image_thumb_4.png](/images/posts/f70bafcb-8353-4c5a-be03-40fa5f3396b3/image_thumb_4.png)

解析後我們可以看到像下面這樣帶入的值都被解析並設置到對應的成員屬性。

![image_thumb_5.png](/images/posts/f70bafcb-8353-4c5a-be03-40fa5f3396b3/image_thumb_5.png)

另外還有個比較特別的ValueListAttribute可以套用，可用於值不需要跟參數Key對應的狀況。像是上面的例子，我們也可以像下面這樣的帶入命令列參數：

![image_thumb_6.png](/images/posts/f70bafcb-8353-4c5a-be03-40fa5f3396b3/image_thumb_6.png)

值一樣會被正確的解析並設置到對應的成員屬性。

![image_thumb_7.png](/images/posts/f70bafcb-8353-4c5a-be03-40fa5f3396b3/image_thumb_7.png)

介紹到這邊，我們已經足夠讓程式加上命令列參數的功能了，但仍舊有點不夠完善，因為我們還沒做到顯示命令列參數的使用說明這部分。若要為程式加上命令列參數的使用說明，我們可以在命令列參數對應的類別連帶增加一個GetUsage方法，並為其加上HelpOptionAttribute。

```csharp
	public class Options
	{
                                ...

		[HelpOption]
		public string GetUsage()
		{
                                	...
		}
	}
```

GetUsage方法主要是回傳命令列參數的使用說明，我們可以自行用程式去兜出我們想要顯示的命令列參數使用說明。

```csharp
[HelpOption]
public string GetUsage()
{
	var usage = new StringBuilder();
	...
	return usage.ToString();
}
```

也可以利用CommandLineParser.Text.HelpText來輔助我們拼湊，像是下面這樣建置出HelpText類別的物件實體，設定Heading、Copyright...等等，再依需求自行用HelpText.AddPreOptionsLine加上自己要附加的訊息，最後用HelpText.AddOptions(this)讓HelpText自行用成員屬性上Attribute帶入的HelpText去兜出命令列參數部分的說明。

```csharp
public string GetUsage()
{
	var help = new HelpText
	{
		Heading = new HeadingInfo(Application.ProductName, Application.ProductVersion),
		Copyright = new CopyrightInfo(Application.CompanyName, 2013),
		AdditionalNewLineAfterOption = true,
		AddDashesToOption = true
	};

	help.AddPreOptionsLine(" ");
	help.AddPreOptionsLine("CommandLine parser library demo...");

	help.AddPreOptionsLine(" ");
	help.AddPreOptionsLine(string.Format("Usage: {0} [options]", Path.GetFileName(Application.ExecutablePath)));

	help.AddPreOptionsLine(" ");
	help.AddPreOptionsLine("options:");
	help.AddOptions(this);
	return help;
}
```

```csharp
private string GetAssemblyCopyright()
{
	var attributes = Assembly.GetExecutingAssembly().GetCustomAttributes(typeof(AssemblyCopyrightAttribute), false);
	if (attributes.Length == 0)
		return "";
	return ((AssemblyCopyrightAttribute)attributes[0]).Copyright;
}

[HelpOption]
public string GetUsage()
{
	var help = new HelpText
	{
		Heading = new HeadingInfo(Application.ProductName, Application.ProductVersion),
		Copyright = GetAssemblyCopyright(),
		AdditionalNewLineAfterOption = true,
		AddDashesToOption = true
	};

	help.AddPreOptionsLine(" ");
	help.AddPreOptionsLine("CommandLine parser library demo...");

	help.AddPreOptionsLine(" ");
	help.AddPreOptionsLine(string.Format("Usage: {0} [options]", Path.GetFileName(Application.ExecutablePath)));

	help.AddPreOptionsLine(" ");
	help.AddPreOptionsLine("options:");
	help.AddOptions(this);
	return help;
}
```

此外也可以透過CommandLineParser的AutoBuild功能讓程式自行去兜，只要在AssemblyInfo.cs中設定AssemblyInformationVersionAttribute、AssemblyLicenseAttribute以及AssemblyUsageAttribute。

```csharp
[assembly: AssemblyInformationalVersionAttribute("1.0")]
[assembly: AssemblyLicense(
  " ",
  "CommandLine parser library demo...")]
[assembly: AssemblyUsage(
  " ",
  "Usage: ConsoleApplication8.exe [options]",
  " ",
  "options:")]
```

然後在GetUsage方法中呼叫HelpText.AutoBuild(this)就可以了。

```csharp
[HelpOption]
public string GetUsage()
{
	return HelpText.AutoBuild(this);
}
```

雖然命令列參數的使用說明這邊CommandLineParser提供了三種方法給開發人員，但是依筆者的來看，目前只有第二種方法比較彈性，建議使用第二種方法。

GetUsage撰寫好後，我們要開始來作呈現這塊，這邊可以在解析時自行呼叫處理，可能是秀在主控台，或是秀在彈出的對話框上面。

```csharp
var options = new Options();
ICommandLineParser parser = new CommandLineParser();
if (parser.ParseArguments(args, options))
{
	...
}
else
	Console.WriteLine(options.GetUsage());
```

如果程式是主控台程式，也不需要特別自行處理的話，可以在ParseArguments時帶入Console.Error讓它自行輸出到主控台上。

```csharp
var options = new Options();
ICommandLineParser parser = new CommandLineParser();
if (parser.ParseArguments(args, options, Console.Error))
{
	...
}
```

也可以用CommandLineParser.Default取得預設的CommandLineParser，或是建立CommandLineParser時在CommandLineParserSettings的建構子中帶入Console.Error，都可以達到一樣的效果。

```csharp
var options = new Options();
ICommandLineParser parser = CommandLineParser.Default;
if (parser.ParseArguments(args, options))
{
	...
}
```

運行起來我們可以看到主控台可以秀出如下這般的命令列參數使用說明。

![image_thumb_3.png](/images/posts/f70bafcb-8353-4c5a-be03-40fa5f3396b3/image_thumb_3.png)

最後這邊附上比較完整的使用範例：

```csharp
using CommandLine;
using CommandLine.Text;
using System;
using System.Collections.Generic;
using System.IO;
using System.Reflection;
using System.Windows.Forms;
namespace ConsoleApplication8
{
	class Program
	{
		static void Main(string[] args)
		{
			var options = new Options();
			ICommandLineParser parser = new CommandLineParser();
			if (parser.ParseArguments(args, options, Console.Error))
			{
				//DO something
			}
		}

		public class Options
		{
			[Option("i", "input", Required = true, HelpText = "Input file to read.")]
			public string InputFile { get; set; }

			[OptionArray("o", "output", HelpText = "The output files to generate.")]
			public string[] OutputFiles { get; set; }

			[OptionList("k", "keywords", Separator = ':', HelpText = "Specify keywords to search the text, separated by a colon.")]
			public List<string> Keywords { get; set; }

			[ValueList(typeof(List<string>), MaximumElements = 3)]
			public List<string> Items { get; set; }

			private string GetAssemblyCopyright()
			{
				var attributes = Assembly.GetExecutingAssembly().GetCustomAttributes(typeof(AssemblyCopyrightAttribute), false);
				if (attributes.Length == 0)
					return "";
				return ((AssemblyCopyrightAttribute)attributes[0]).Copyright;
			}

			[HelpOption]
			public string GetUsage()
			{
				var help = new HelpText
				{
					Heading = new HeadingInfo(Application.ProductName, Application.ProductVersion),
					Copyright = GetAssemblyCopyright(),
					AdditionalNewLineAfterOption = true,
					AddDashesToOption = true
				};

				help.AddPreOptionsLine(" ");
				help.AddPreOptionsLine("CommandLine parser library demo...");

				help.AddPreOptionsLine(" ");
				help.AddPreOptionsLine(string.Format("Usage: {0} [options]", Path.GetFileName(Application.ExecutablePath)));

				help.AddPreOptionsLine(" ");
				help.AddPreOptionsLine("options:");
				help.AddOptions(this);
				return help;
			}
		}
	}
}
```

## Link

* Command Line Parser Library
