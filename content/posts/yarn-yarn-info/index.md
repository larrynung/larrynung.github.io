---
title: "Yarn - Yarn info"
date: "2017-07-09 18:56:33"
tags: [Yarn]
---


Yarn info 命令可用來查閱套件的資訊。  

<!-- More -->

<br/>


可以直接用 yarn info 帶上指定的套件名稱查閱指定套件的資訊。  

    yarn info <PackageName>

![1.png](1.png)

<br/>


若要查閱指定版本的套件資訊，也可以在套件名稱後面用小老鼠加帶套件版本。  

    yarn info <PackageName>@<PackageVersion>

![2.png](2.png)

<br/>


要查閱指定的套件資訊的話，可以再多帶上套件資訊的名稱。

    yarn info <PackageName> <InfoName>

<br/>


像是可以查閱套件的名稱。  

    yarn info <PackageName> name

![3.png](3.png)

<br/>


查閱套件的描述。  

    yarn info <PackageName> description

![4.png](4.png)

<br/>


查閱套件的依賴。  

    yarn info <PackageName> dependencies

![5.png](5.png)

<br/>


查閱套件的建立與修改時間。  

    yarn info <PackageName> time

![6.png](6.png)

<br/>


查閱套件的說明文件。  

    yarn info <PackageName> readme

![7.png](7.png)

<br/>


若是要用程式去擷取套件的資訊，也可以加帶 --json 改用 JSON 格式顯示。  

    yarn info <PackageName> --json

![8.png](8.png)

<br/>


Link
----
* pyarn info | Yarn](https://yarnpkg.com/en/docs/cli/info)
