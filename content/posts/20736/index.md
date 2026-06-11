---
title: "使用反射(Reflection)實現應用程式擴充元件機制"
date: "2011-01-11 02:42:52"
description: "使用反射(Reflection)實現應用程式擴充元件機制"
tags: [CSharp]
---

身為程式開發人員不能避免的時常會需要因應客戶的需求下去為元件做些客制或擴充，有些應用程式為了讓程式便於處理這部分的需求會為應用程式加上擴充的機制，這樣的擴充機制能讓應用程式很輕鬆的達到大部分的擴充需求，也能將此機制開出讓有此需求的用戶能自行依自己處理擴充的動作。實作應用程式擴充元件機制在.NET有許多的作法，這邊將介紹如何透過反射(Reflection)技術來實作這樣的機制。

要使用反射來實作應用程式擴充元件機制，首先必須了解的是透過反射機制能讓我們動態的在執行階段了解整個組件的構成，組件裡有哪些參考，組件裡有哪些類別，類別裡有哪些方法、屬性、建構子...等，且能夠動態的依據需求建立物件實體、取得設定物件屬性、呼叫物件的方法。故整個擴充元件機制其實就只是透過反射去找出能使用的擴充元件類別，將找到的擴充元件類別動態建立出物件實體，依據需求可能再運行必要的方法或設定些必要的屬性。在實作擴充元件機制時多半我會依照需求下去定義擴充元件必須實作的介面，甚至依需要會在建立個被擴充的宿主介面傳入擴充元件介面讓擴充元件介面取得宿主資訊，再透過反射去找尋組件中有哪些類別是實作擴充元件介面，建立其物件實體做擴充。基本上使用反射來實作應用程式擴充元件機制就是依上面所述的下去做就可以了，只是介面的部分需要依個人需求自行下去設計。

這邊來看個實作範例，範例程式可至larrynung / ReflectionPluginDemo下載。該範例由三個專案構成，PlugIn.Core主要為擴充元件機制所需要的介面與基礎控制；PlugIn.Host為主要的運行介面，也是主要要被擴充的專案；PlugIn.Module為擴充元件專案，放置要用來擴充的擴充元件。

在PlugIn.Core專案中，首先會定義宿主介面：

public interface IHost
{
PlugInController PlugInAgent { get; }
}

這邊的範例中，我在宿主介面裡面放入了用來控制擴充元件的處理類別PlugInController，會利用反射機制找尋組件中的擴充元件類別，動態將擴充元件類別建立物件實體，並把宿主物件參考指派給擴充元件物件實體：

public class PlugInController
{
private IHost _host;

public IHost Host
{
get
{
return _host;
}
set
{
_host = value;
}
}

public PlugInController(IHost host)
{
this.Host = host;
}

IModule GetModule(Assembly asm, string fullTypeName)
{
Type t = asm.GetType(fullTypeName);
IModule module = null;
if (!(t.IsNotPublic || t.IsAbstract))
{
object objInter true);

if (objInterface != null)
{
module = asm.CreateInstance(t.FullName) as IModule;
module.Host = Host;
return module;
}
}
return null;
}

IModule GetModule(Assembly asm, Type moduleType)
{
return GetModule(asm, moduleType.FullName);
}

public IModule[] GetModules(Assembly asm)
{
List modules = new List();
IModule module = null;
foreach (Type t in asm.GetTypes())
{
module = GetModule(asm, t);

if (module != null)
modules.Add(module);
}
return modules.ToArray ();
}

public IModule[] GetModules(string assemblyFile)
{
if (!File.Exists(assemblyFile))
throw new FileNotFoundException();
return GetModules(Assembly.LoadFile(assemblyFile));
}

public IModule[] GetModulesFromDirectory(string directoryPath)
{
List modules = new List();
foreach (string file in Directory.GetFiles(directoryPath,"*.dll"))
modules.AddRange (GetModules(file));
return modules.ToArray ();
}
}

在擴充元件介面的定義上，這邊我是簡單的設定了擴充原件的名稱、宿主的物件參考、與擴充元件所要運行的動作：

public interface IModule
{
String Name { get; }
IHost Host { get; set; }
void Execute();
}

介面定義好以後，PlugIn.Module專案會實作一個簡單的擴充元件SubModule，這個擴充元件只是一個簡單的視窗表單，運行後會被當為宿主的MDI子視窗：

public class SubModule:IModule
{
private Form _view;
private IHost _host;

protected Form m_View
{
get
{
if (_view == null)
_view = new MainForm() { MdiParent = Host as Form };
return _view;
}
}

#region IModule 成員

public string Name
{
get
{
return "SubModule";
}
}

public IHost Host
{
get
{
return _host;
}
set
{
_host = value;
}
}

public void Execute()
{
m_View.Show();
}

#endregion
}

接著在PlugIn.Host專案中，宿主類別會將當前目錄下所有的擴充元件名稱放置功能選單中的模組選單，並允許使用者點選特定模組運行。

public partial class MainForm : Form, IHost
{
public MainForm()
{
InitializeComponent();
foreach (IModule module in PlugInAgent.GetModulesFromDirectory(Environment.CurrentDirectory))
模組MToolStripMenuItem.DropDownItems.Add(module.Name,null,Module_Click).Tag = module;
}

void Module_Click(object sender, EventArgs e)
{
((sender as ToolStripMenuItem).Tag as IModule).Execute();
}

...

#region IHost 成員

private PlugInController _plugInAgent;

public PlugInController PlugInAgent
{
get
{
if (_plugInAgent == null)
_plugInAgent = new PlugInController(this);
return _plugInAgent;
}
}

#endregion
}

運行結果如下：