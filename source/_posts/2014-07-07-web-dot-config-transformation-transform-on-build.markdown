---
layout: post
title: "Web.Config Transformation - Transform on build"
date: 2014-07-07 23:19
comments: true
categories: [Web.Config Transformation]
keywords: "Web.Config, Transformation"
description: "Web.Config Transformation - Transform on build"
---

Web.Config Transformation 功能在我們有多個環境需要部署時很方便，但預設只會在發佈時做對應的轉換，因此當我們需要針對特定環境下去排解問題時，就不能很直接的切換 Profile 去做偵錯的動作。  

<!-- More -->

<br/>

若要在建置時也做 Web.Config 的轉換，讓除錯時更為方便。我們可以複製 Web.Config，降之更名為 Web.Base.config，然後卸載並開啟專案檔，將 Web.Base.config 設定為 DependentUpon Web.Config。 

{% codeblock lang:xml %} 
...
<Content Include="Web.Base.config">
<DependentUpon>Web.config</DependentUpon>
</Content>
...
{% endcodeblock %}

<br/>

然後在專案檔中設定建置前用 Microsoft.WebApplication.targets 將 Web.Base.config 套用 Web.$(Configuration).config 的轉換設定產出實際我們需要的 Web.config。 

{% codeblock lang:xml %} 
<Import Project="$(MSBuildExtensionsPath32)\Microsoft\VisualStudio\v11.0\WebApplications\Microsoft.WebApplication.targets" />
<Target Name="BeforeBuild">
<TransformXml Source="Web.Base.config" Transform="Web.$(Configuration).config" Destination="Web.config" />
</Target>
{% endcodeblock %}

<br/>

設定好存檔，將專案檔載回方案檔，以後建置時即會運行轉換的動作。  

除了建置時驅動轉換外，若是想要將 Web.Config Transformation 功能套用到 Web.Config 外的 Config 檔，也可以使用該方法如法泡製。 
