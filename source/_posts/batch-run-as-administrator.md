---
layout: post
title: "Batch - Run as administrator"
date: 2014-01-01 22:36:00
comments: true
tags: Batch
keywords: Batch,Admin,UAC
description: "Batch - Run as administrator"
---

Windows Vista 後的作業系統開始導入 UAC ，在運行某些操作時必須要提升至管理者權限才能繼續。這在程式中只要加上 MetaData 就可以了，但在批次檔中卻沒有比較直接的做法。

<!-- More -->

好在有好心的網友整理好了下面這樣的程式碼片段

```bat
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
```

<br/>

使用時只要將它附加在批次檔的開頭，運行時就會嘗試去提升至管理者的權限。  

這邊筆者稍稍將之做些修改調整...  

```bat
:TryToRunAsAdmin
    set GetAdminScriptFile="%temp%\getadmin.vbs"

    REM  --> Check for permissions
    >nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"

    REM --> If error flag set, we do not have admin.
    if '%errorlevel%' NEQ '0' (
        echo Requesting administrative privileges...
        call:UACPrompt
        set ERRORLEVEL=1
    ) else ( 
        if exist %GetAdminScriptFile% ( del %GetAdminScriptFile% )
        set ERRORLEVEL=0
    )
    goto :eof


:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > %GetAdminScriptFile%
    echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> %GetAdminScriptFile%

    call %GetAdminScriptFile%
    goto :eof
```

<br/>

使用時只要在開頭處加入對應的呼叫與中止的判斷處理即可  

    ...
    call:TryToRunAsAdmin

    if %ERRORLEVEL%==1 exit /B
    ...
    
<br/>

像是下面這樣...  

```bat
@echo off

call:TryToRunAsAdmin

if %ERRORLEVEL%==1 exit /B
    
echo got administrative privileges...
goto :eof

:TryToRunAsAdmin
    set GetAdminScriptFile="%temp%\getadmin.vbs"

    REM  --> Check for permissions
    >nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"

    REM --> If error flag set, we do not have admin.
    if '%errorlevel%' NEQ '0' (
        echo Requesting administrative privileges...
        call:UACPrompt
        set ERRORLEVEL=1
    ) else ( 
        if exist %GetAdminScriptFile% ( del %GetAdminScriptFile% )
        set ERRORLEVEL=0
    )
    goto :eof


:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > %GetAdminScriptFile%
    echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> %GetAdminScriptFile%

    call %GetAdminScriptFile%
    goto :eof
```

<br/>

Link
----
* [BatchGotAdmin](https://sites.google.com/site/eneerge/scripts/batchgotadmin)
