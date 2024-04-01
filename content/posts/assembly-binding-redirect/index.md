---
title: "Assembly Binding Redirect"
date: "2015-03-03 07:48:00"
description: "Assembly Binding Redirect"
---


在開發上有時我們會需要將組件版本導向，可能是因為不同專案用到不同版本的相依組件，或是基於某些原因要將某個組件用特定版本替換。這時我們可以透過 Assembly Binding Redirect 來做到這件事。  

<!-- More -->

<br/>


Assembly Binding Redirect 可在電腦或是應用程式層級進行組件的導向，這邊以應用程式層級的導向做個簡單的介紹。  

<br/>


首先，Config 檔內必須在 `configurationuntime` 節點下加入 assemblyBinding 節點，其 xmlns 屬性需指定字串 "urn:schemas-microsoft-com:asm.v1"。  

```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
	...
	<runtime>
		<assemblyBinding xmlns="urn:schemas-microsoft-com:asm.v1">...</assemblyBinding>
	</runtime>
	...
</configuration>
``` 

<br/>


若要限定特定 .NET Framework 版本的組件才做導向，可加上 appliesTo 屬性，並指定 .NET Framework 的版本。像是要指定只對 .NET 3.5 的組件導向的話可下面這樣編寫：  

```xml 
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
	...
	<runtime>
		<assemblyBinding xmlns="urn:schemas-microsoft-com:asm.v1" appliesTo="v3.5">...</assemblyBinding>
	</runtime>
	...
</configuration>
```

<br/>


接著在 assemblyBinding 下我們需加上 assemblyIdentity 節點，用以指定所要導向的組件。像是要導向 Json.NET 組件的話就會像下面這樣：  

```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
	...
	<runtime>
		<assemblyBinding xmlns="urn:schemas-microsoft-com:asm.v1">
			<dependentAssembly>
				<assemblyIdentity name="Newtonsoft.Json" publicKeyToken="30AD4FE6B2A6AEED" culture="neutral" />
				...
			</dependentAssembly>
		</assemblyBinding>
	</runtime>
	...
</configuration>
```

<br/>


最後在 assemblyBinding 下再加上 bindingRedirect 節點，用以指定要從哪個版本導向哪個版本就可以了。  

```xml
<?xml version="1.0" encoding="UTF-8"?>
<runtime>
	<assemblyBinding xmlns="urn:schemas-microsoft-com:asm.v1">
		<dependentAssembly>
			<assemblyIdentity name="Newtonsoft.Json" publicKeyToken="30AD4FE6B2A6AEED" culture="neutral" />
			<!--<bindingRedirect oldVersion="5.0.7.0" newVersion="6.0.0.0" />-->
			<bindingRedirect oldVersion="0.0.0.0-6.0.0.0" newVersion="6.0.0.0" />
		</dependentAssembly>
	</assemblyBinding>
</runtime>
```

<br/>

Link
----
* [重新導向組件版本](https://msdn.microsoft.com/zh-tw/library/7wd6ex19(v=vs.110\).aspx)
* [<bindingRedirect> 項目](https://msdn.microsoft.com/zh-tw/library/eftw1fys(v=vs.110\).aspx)
* [Introduction to Versioning and BindingRedirect - Thottam R. Sriram - Site Home - MSDN Blogs](http://blogs.msdn.com/b/thottams/archive/2007/01/30/introduction-to-versioning-and-bindingredirect.aspx)
