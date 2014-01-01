---
layout: post
title: "Batch - Run as administrator"
date: 2014-01-01 22:36
comments: true
categories: Batch
keywords: Batch,Admin,UAC
description: "Batch - Run as administrator"
---

Windows Vista 後的作業系統開始導入 UAC ，在運行某些操作時必須要提升至管理者權限才能繼續。這在程式中只要加上 MetaData 就可以了，但在批次檔中卻沒有比較直接的做法。

<!-- More -->

好在有好心的網友整理好了下面這樣的程式碼片段

{% codeblock lang:bat %}
:: BatchGotAdmin
:-------------------------------------
REM --> Check for permissions
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"

REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
echo Requesting administrative privileges...
goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\getadmin.vbs"

"%temp%\getadmin.vbs"
exit /B

:gotAdmin
if exist "%temp%\getadmin.vbs" ( del "%temp%\getadmin.vbs" )
pushd "%CD%"
CD /D "%~dp0"
:--------------------------------------
{% endcodeblock %}


使用時只要將它附加在批次檔的開頭，運行時就會嘗試去提升至管理者的權限。

Link
----
* [BatchGotAdmin](https://sites.google.com/site/eneerge/scripts/batchgotadmin)
