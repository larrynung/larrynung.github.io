---
layout: post
title: "ASP.NET - Disable View State"
date: 2014-09-23 07:28:00
comments: true
categories: [ASP.NET]
keywords: "ASP.NET, View State"
description: "ASP.NET - Disable View State"
---

禁用 View State 有幾種方式。若要將所有頁面都禁用，我們可以在 Web.Config 內的 system.web 加入 pages 的 element，並將其 enableViewState attribute 設為 false。  

<!-- More -->

{% codeblock lang:xml %}
...
<system.web>
...
<pages enableViewState= "false"/>
...
</system.web>
...
{% endcodeblock %}


若要在單一頁面禁用，可以在該檔案最前面加入...  

{% codeblock lang:xml %}
<%@ Page EnableViewState= "true" ViewStateMode= "Disabled" .. . %>
...
{% endcodeblock %}


若要指定單一控制項禁用，可直接為控制項加上 EnableViewState attribute，並將其值設為 false...  

{% codeblock lang:xml %}
...
<asp:GridView ID= "gdvCustomers" runat= "server" DataSourceID= "mySqlDataSource" AllowPaging="True" EnableViewState ="false"/>
...
{% endcodeblock %}


若要針對單一控制項啟用，頁面上其餘的控制項禁用，可以像下面這樣處理...  

{% codeblock lang:xml %}
<%@ Page EnableViewState= "true" ViewStateMode= "Disabled" .. . %>
...
<asp:GridView ID= "gdvCustomers" runat= "server" DataSourceID= "mySqlDataSource" AllowPaging="True" ViewStateMode= "Enabled"/>
...
{% endcodeblock %}
