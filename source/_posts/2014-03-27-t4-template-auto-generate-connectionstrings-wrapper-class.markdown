---
layout: post
title: "T4 template - Auto generate ConnectionString's wrapper class"
date: 2014-03-27 23:28
comments: true
categories: [T4]
keywords: "T4, ConnectionString, Strong Type"
description: "T4 template - Auto generate ConnectionString's wrapper class"
---

在 .Net 程式中要使用資料庫的連線字串，多半我們會將資料庫的連線字串設定在 Config 檔中，然後透過 ConfigurationManager.ConnectionStrings 帶入對應的 Key 去將之取出來使用。  

<!-- More -->

<br/>

用這樣的撰寫方式，連線字串名稱打錯無法立即的被意識到，連線字串名稱調動時也很容易漏改，造成系統運行時的錯誤。因此有的人會將連線字串這邊再包一層，透過這層物件的屬性去取得連線字串，將連線字串的修改都在這層處理，減少人為造成的錯誤。 

<br/>

然而這樣的做法並無法完全解決問題，因為多包的那層還是人工下去做的，仍舊是無法避免連線名稱鍵錯的問題，連線字串變動時仍是會有改錯的可能。故這邊筆者嘗試使用 T4 template，讀取專案的 config 檔，動態產生強型別物件，提供連線字串給系統使用。 

<br/>

首先我們要為專案加入一個 t4 template 檔。 

<br/>

然後將其程式碼替換成下面這樣。

{% codeblock lang:c# %}
<#@ template debug="false" hostspecific="True" language="C#" #>
<#@ assembly name="EnvDTE" #>
<#@ assembly name="System.Core.dll" #>
<#@ assembly name="System.Configuration" #>
<#@ assembly name="System.Xml" #>
<#@ import namespace="System.Collections.Generic" #>
<#@ import namespace="System.Configuration" #>
<#@ import namespace="EnvDTE" #>
<#@ import namespace="System.Xml" #>
<#@ output extension=".cs" #>
using System.Configuration;

public class ConnectionStrings
{
<#
       var configFile = new ExeConfigurationFileMap();
       configFile.ExeConfigFilename = GetConfigPath();
       var config = System.Configuration.ConfigurationManager.OpenMappedExeConfiguration(configFile, ConfigurationUserLevel.None);
       var connectionStrings = config.ConnectionStrings.ConnectionStrings;
       foreach (ConnectionStringSettings connectionString in connectionStrings)
       {
#>
       public static string <#= connectionString.Name#>
       {
              get
              {
                     return ConfigurationManager.ConnectionStrings["<#= connectionString.Name#>"].ConnectionString;
              }
       }
<#
  }
#>
}

<#+
private EnvDTE.Project GetCurrentProject()
{
       var hostServiceProvider = (IServiceProvider)this.Host;
       
       if (hostServiceProvider == null)
           throw new Exception("Host property returned unexpected value (null)");
       
       EnvDTE.DTE dte = (EnvDTE.DTE)hostServiceProvider.GetService(typeof(EnvDTE.DTE));
       if (dte == null)
           throw new Exception("Unable to retrieve EnvDTE.DTE");
       
       Array activeSolutionProjects = (Array)dte.ActiveSolutionProjects;
       if (activeSolutionProjects == null)
           throw new Exception("DTE.ActiveSolutionProjects returned null");
       
       EnvDTE.Project dteProject = (EnvDTE.Project)activeSolutionProjects.GetValue(0);
       if (dteProject == null)
           throw new Exception("DTE.ActiveSolutionProjects[0] returned null");
       
       return dteProject;
}

private string GetProjectPath()
{
       EnvDTE.Project project = GetCurrentProject();
    System.IO.FileInfo info = new System.IO.FileInfo(project.FullName);
    return info.Directory.FullName;
}

private string GetConfigPath()
{
       EnvDTE.Project project = GetCurrentProject();
    foreach (EnvDTE.ProjectItem item in project.ProjectItems)
    {
              // if it is the app.config file, then open it up
        if (string.Compare(item.Name, "App.config", true) == 0)
        {
            return GetProjectPath() + "\\" + item.Name;
        }
       
        // if it is the web.config file, then open it up
        if (string.Compare(item.Name, "Web.config", true) == 0)
        {
            return GetProjectPath() + "\\" + item.Name;
        }
    }
    return "";
}
#>
{% endcodeblock %}

<br/>

存檔運行，沒意外的話應該可以看到對應的強型別物件被產生了出來。

<Br/>

在系統中我們就可直接透過該強型別物件去取得連線字串，像是假設有個名為 Oracle 的 ConnectionString，就可像下面這樣取用。

{% codeblock lang:c# %}
var connectionString = ConnectionStrings.Oracle;
...
{% endcodeblock %}

<br/>

如果後續 config 內的連線字串有所增減，或是連線字串的名稱有所更動，可直接在該 t4 template 上按下滑鼠右鍵，在彈出的滑鼠右鍵快顯選單中點選 Run custom tool 這個滑鼠右鍵選單選項，讓 t4 template 重新產生對應的強型別物件就可以了。
