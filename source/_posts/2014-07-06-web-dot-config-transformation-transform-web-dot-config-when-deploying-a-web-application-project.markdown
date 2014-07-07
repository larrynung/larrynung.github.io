---
layout: post
title: "Web.Config Transformation - Transform Web.config When Deploying a Web Application Project"
date: 2014-07-06 19:27
comments: true
categories: ["Web.Config Transformation"]
keywords: "Web.Config, Transformation"
description: "Web.Config Transformation - Introduction"
---

Web.Config Transformation 允許開發人員依照特定的語法設定部署時 Web.Config 所要做的轉換動作，像是移除除錯設定、或是連線字串。該功能在 Visual Studio 2012 開始整進 Visual Studio，若要在 Visual Studio 2010 使用，需為 Visual Studio 加裝 [Visual Studio Web Publish Update](http://msdn.microsoft.com/en-us/library/jj161045\(v=vs.110\).aspx) 套件。 

<!-- More -->

在使用上，當我們用 Visual Studio 建立一個 Web 專案，預設就會幫我們建好 Debug 跟 Release 最基本的轉換設定。以預設的設定來說，Debug 沒作任何的轉換動作，而 Release 會將 Web.Config 中除錯的設定拔除。

{% codeblock lang:xml %}
  ...
  <system.web>
    <compilation xdt:Transform="RemoveAttributes(debug)" />
  ...
{% endcodeblock %}


我們可以參閱 Release 的轉換設定檔，設定檔內的註解會稍稍提示使用的方式，以及說明文件的位置，確實參閱後做些基本的設定應該都不成問題。  

{% codeblock lang:xml %}
<?xml version="1.0" encoding="utf-8"?>
<!-- 有關使用 web.config 轉換的詳細資訊，請造訪 http://go.microsoft.com/fwlink/?LinkId=125889 -->

<configuration xmlns:xdt="http://schemas.microsoft.com/XML-Document-Transform">
  <!--
    在下面的範例中，"SetAttributes" 轉換只會在 "Match" 定位程式找到
    值為 "MyDB" 的屬性 "name" 時，才將 "connectionString" 的值變
    更為使用 "ReleaseSQLServer"。
    
    <connectionStrings>
      <add name="MyDB"
        connectionString="Data Source=ReleaseSQLServer;Initial Catalog=MyReleaseDB;Integrated Security=True"
        xdt:Transform="SetAttributes" xdt:Locator="Match(name)"/>
    </connectionStrings>
  -->
  <system.web>
    <compilation xdt:Transform="RemoveAttributes(debug)" />
    <!--
      在下面的範例中，"Replace" 轉換將會取代 web.config 檔案
      的整個 <customErrors> 區段。
      請注意，因為在 <system.web> 節點之下
      只有一個 customErrors 區段，所以不需要使用 "xdt:Locator" 屬性。
      
      <customErrors defaultRedirect="GenericError.htm"
        mode="RemoteOnly" xdt:Transform="Replace">
        <error statusCode="500" redirect="InternalError.htm"/>
      </customErrors>
    -->
  </system.web>
</configuration>
{% endcodeblock %}


轉換的語法不會太複雜，只要知道 Locator 與 Transform 的用法就可以了。 Locator 用來選取要做轉換的項目(若不指定則由 Transform 隱含指定)， Transform 則是用來設定要對選取的項目進行哪種轉換。簡單來說 Web.Config Transformation 也就只是使用 Locator 選取後透過 Transform 將設定值轉換成我們所預期的值。

像是連線字串的轉換，就只要像下面這樣設定。一樣是加入 `configuration/connectionStrings/add` 節點去設定連線字串，就像是一般我們在 Web.Config 內做的那樣。只不過要在節點上附加 Locator 與 Transform 屬性，指定如果 match 的到連線字串的 name，才套用這邊設定的 connectionString 屬性值。  

{% codeblock lang:xml %}
    ...
    <connectionStrings>
      <add name="SQLServer"
        connectionString="Data Source=ReleaseSQLServer;Initial Catalog=MyReleaseDB;Integrated Security=True"
        xdt:Transform="SetAttributes" xdt:Locator="Match(name)"/>
    </connectionStrings>
    ...
{% endcodeblock %}

如果是 appSettings 的設定的轉換，也是一樣的設定方式。加入 `configuration/appSettings/add` 節點，節點的設定方式如同在一般的 Web.Config 設定，將預期的值帶入。接著附加 Locator 與 Transform 屬性，指定 match 到 ket 時套用 value 值。
{% codeblock lang:xml %}
  ...
  < appSettings>
    < add key="Bolg" value="Level Up" xdt:Transform="SetAttributes " xdt:Locator=" Match(key)"/>
    < add key="Site" value="http://larrynung.github.com" xdt:Transform="SetAttributes " xdt:Locator=" Match(key)"/>
  </ appSettings>
  ...
{% endcodeblock %}

簡單的使用方式大概就是這樣。再進階一點就要細看 Locator 的 Condition、 Match、 XPath 語法，以及 Transform 的 Replace、 Insert 、 InsertBefore 、 InsertAfter 、 Remove 、 RemoveAll 、 RemoveAttributes 、 SetAttributes 語法。若有需求或是有研究的興趣，可自行參閱 MSDN 的說明。  

Link
----
* [Visual Studio Web Publish Update](http://msdn.microsoft.com/en-us/library/jj161045\(v=vs.110\).aspx)
* [Web 應用程式專案部署的 Web.config 轉換語法](http://msdn.microsoft.com/zh-tw/library/dd465326\(VS.100\).aspx)
* [Web Deployment: Web.Config Transformation - .NET Web Development and Tools Blog - Site Home - MSDN Blogs](http://blogs.msdn.com/b/webdev/archive/2009/05/04/web-deployment-web-config-transformation.aspx)
* [Visual Studio 2010 單鍵發行簡單使用 Web.Release.config | demo小鋪](http://demo.tc/Post/661)
