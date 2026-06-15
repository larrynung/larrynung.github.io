---
title: "Brahma Command Line Parser"
date: "2010-11-16 12:34:12"
description: "Brahma Command Line Parser"
tags: [CSharp]
---
在研究Brahma這個C#開源的Linq To GPU函式庫時，發現在Brahma網站上有釋出用來解析命令列參數的程式碼片段，稍微玩了一下，隨手做個記錄。

程式碼片段可在Code Snippets下載，透過程式碼片段管理員將其匯入至本機的Visual Studio中，程式碼片段如下：

#region CommandLine Arguments Parser

/* Simple commandline argument parser written by Ananth B.
http://www.ananthonline.net */
static class CommandLine
{
public class Switch // Class that encapsulates switch data.
{
public Switch(string name, Action> handler, string shortForm)
{
Handler = handler;
ShortForm = shortForm;
}

public Switch(string name, Action> handler)
{
Handler = handler;
ShortForm = null;
}

public string Name
{
get;
private set;
}
public string ShortForm
{
get;
private set;
}
public Action> Handler
{
get;
private set;
}

public int InvokeHandler(string[] values)
{
Handler(values);
return 1;
}
}

/* The regex that extracts names and comma-separated values for switches
in the form ([="value 1",value2,...])+ */
private static readonly Regex ArgRegex =
new Regex(@"(?[^=\s]+)=?((?\""?)(?(?(quoted)[^\""]+|[^,]+))\""?,?)*",
RegexOptions.Compiled | RegexOptions.CultureInvariant |
RegexOptions.ExplicitCapture | RegexOptions.IgnoreCase);

private const string NameGroup = "name"; // Names of capture groups
private const string ValueGroup = "value";

public static void Process(this string[] args, Action printUsage, params Switch[] switches)
{
/* Run through all matches in the argument list and if any of the switches
match, get the values and invoke the handler we were given. We do a Sum()
here for 2 reasons; a) To actually run the handlers
and b) see if any were invoked at all (each returns 1 if invoked).
If none were invoked, we simply invoke the printUsage handler. */
if ((from arg in args
from Match match in ArgRegex.Matches(arg)
from s in switches
where match.Success &&
((string.Compare(match.Groups[NameGroup].Value, s.Name, true) == 0) ||
(string.Compare(match.Groups[NameGroup].Value, s.ShortForm, true) == 0))
select s.InvokeHandler(match.Groups[ValueGroup].Value.Split(','))).Sum() == 0)
printUsage(); // We didn't find any switches
}
}

#endregion

該程式碼片段結合擴充方法、Linq、與正規表示式等技術去實現解析命令列參數的功能，解析時會去比對設定的Switch命令類別，藉此將命令列參數解析後帶入給對應的命令去處理。

使用時直接在傳入的命令列參數上呼叫Process

args.Process(顯示命令使用說明的函式，命令處理類別集合);

其中命令處理類別在建構時需帶入命令名稱、命令對應處理函式、命令縮寫。

new CommandLine.Switch (命令名稱,命令對應處理函式,命令縮寫);

使用上會像下面這樣：

args.Process(printUsage,new CommandLine.Switch []{
new CommandLine.Switch ("-Command1",Command1,"-cmd1")
});

static void Command1(IEnumerable args)
{
...
}

static void printUsage()
{
...
}

這邊直接來看個簡單的使用範例：

static void Main(string[] args)
{

args.Process(printUsage,new CommandLine.Switch []{
new CommandLine.Switch ("-MessageBox",MessageBoxCommand,"-mbx"),
new CommandLine.Switch ("-ConsoleWriteLine",ConsoleWriteLineCommand,"-cw")
});
}

static void printUsage()
{
Console.WriteLine("測試解析命令列參數用命令");
Console.WriteLine();
Console.WriteLine("-MessageBox or -mbx: 彈出對話方塊");
Console.WriteLine("-ConsoleWriteLine or -cw: 顯示主控台訊息");
}

static void MessageBoxCommand(IEnumerable args)
{
System.Windows.Forms.MessageBox.Show(args.FirstOrDefault());
}

static void ConsoleWriteLineCommand(IEnumerable args)
{
Console.WriteLine(args.FirstOrDefault());
}

以這範例來看，若在命令列參數帶入-cw=test的話：

帶入參數-mbx=test的話：

不帶任何參數或是非合法的參數的話：

使用起來感覺程式還算十分清楚好維護，在撰寫上也很容易上手，但是彈性上卻稍嫌不足，像是命令名稱與值要用等號隔開、名稱與值中間不能有空格、無法處理不合法參數...等等，使用上這邊要特別注意一下。

##
Download

CommandLineParser.zip

##
Link

Code Snippets