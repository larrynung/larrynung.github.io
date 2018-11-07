---
title: Cake - Build with MSBuild
date: 2018-11-08 00:09:34
tags: [Cake]
---

要使用 Cake 透過 MSBuild 建置方案，可以參閱 Cake 內使用 MSBuild 的方式。  

<!-- More -->

{% asset_img 1.png %}

<br/>


調用上就是帶入方案檔即可，如有需要設定在帶入設定值而已。  

<br/>


所以建置的腳本寫起來會像下面這樣，先帶入方案檔的位置找到對應的方案檔，遍尋方案檔調用 MSBuild，如有需要則加帶設定，像是是否要將緊告示為錯誤、或是設定是要建置 Debug 或是 Release 等。  

```C#
var solutions = GetFiles("../**/*.sln");
...
Task("Build")
.Does(() => {
	foreach(var solution in solutions)
    {
		...
		MSBuild(solution, settings =>
            settings.SetPlatformTarget(PlatformTarget.MSIL)
                .WithProperty("TreatWarningsAsErrors","true")
                .WithTarget("Build")
                .SetConfiguration(configuration));
	}
});
...
```

<br/>


Cake 任務運行後。  

{% asset_img 2.png %}

</br>


輸出目錄就會看到建置出來的檔案。  

{% asset_img 3.png %}

</br>


{% asset_img 4.png %}

</br>


最後附上完整的 Cake 腳本。  

```C#
var solutions = GetFiles("../**/*.sln");

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

Task("Build")
.Does(() => {
	foreach(var solution in solutions)
    {
		Information("Building {0}", solution);
		MSBuild(solution, settings =>
            settings.SetPlatformTarget(PlatformTarget.MSIL)
                .WithProperty("TreatWarningsAsErrors","true")
                .WithTarget("Build")
                .SetConfiguration(configuration));
	}
});

Task("Default")
.IsDependentOn("Build")   
.Does(() => {
});

RunTarget(target);
```

<br/>


Link
----
* [Cake - Reference - MSBuild](https://cakebuild.net/dsl/msbuild/)
