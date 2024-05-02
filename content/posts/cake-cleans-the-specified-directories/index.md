---
title: "Cake - Cleans the specified directories"
date: "2018-11-08 23:18:51"
tags: [Cake]
---


要使用 Cake 清除特定目錄，可以參閱 CleanDirectories 的使用方式。  

<!-- More -->

![1.png](1.png)

<br/>


調用上可以直接帶入目錄的集合，或是目錄的 match pattern。  

<br/>


像是用 match pattern 去清除目錄腳本撰寫起來就會像下面這樣。  

```C#
...
Task("Clean")
    .Does(() =>
{
    CleanDirectories("./**/bin/" + configuration);
    CleanDirectories("./**/obj/" + configuration);
});
...
```

<br/>


Cake 任務運行後。  

![2.png](2.png)

<br/>


![3.png](3.png)

<br/>


指定目錄的檔案就會被清除。  

![4.png](4.png)

<br/>


![5.png](5.png)

<br/>


最後附上完整的 Cake 腳本。

```C#
///////////////////////////////////////////////////////////////////////////////
// ARGUMENTS
///////////////////////////////////////////////////////////////////////////////

var target = Argument("target", "Default");
var configuration = Argument("configuration", "Release");

///////////////////////////////////////////////////////////////////////////////
// SETUP / TEARDOWN
///////////////////////////////////////////////////////////////////////////////

Setup(ctx =>
{
	// Executed BEFORE the first task.
	Information("Running tasks...");
});

Teardown(ctx =>
{
	// Executed AFTER the last task.
	Information("Finished running tasks.");
});

///////////////////////////////////////////////////////////////////////////////
// TASKS
///////////////////////////////////////////////////////////////////////////////

Task("Clean")
    .Does(() =>
{
    CleanDirectories("./**/bin/" + configuration);
    CleanDirectories("./**/obj/" + configuration);
});

Task("Default")
.IsDependentOn("Clean")  
.Does(() => {
});

RunTarget(target);
```

<br/>


Link
----
* [Cake - Reference - Directory Operations](https://cakebuild.net/dsl/directory-operations/)
