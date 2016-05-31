---
layout: post
title: "Change color in batch file"
date: 2013-11-12 23:55:00
comments: true
tags: [Batch]
---

要在批次檔中設定顯示的顏色,我們可以像下面這樣撰寫批次檔  

<!--More-->

{% codeblock lang:bat %}
@ECHO off
SETLOCAL EnableDelayedExpansion
for /F "tokens=1,2 delims=#" %%a in ('"prompt #$H#$E# & echo on & for %%b in (1) do rem"') do (
  set "DEL=%%a"
)

#==========
#Main Action
#===========

goto :eof



:AppendColorText
echo off
<nul set /p ".=%DEL%" > "%~2"
findstr /v /a:%1 /R "^$" "%~2" nul
del "%~2" > nul 2>&1
goto :eof


:AppendColorTextLine
echo off
call :AppendColorText %~1 %~2
Echo.
goto :eof
{% endcodeblock %}


筆者在這邊宣告了兩個Method可以直接叫用,一個是AppendColorText,一個是AppendColorTextLine,差異只在於是否要做換行的動作

需要叫用時可像下面這樣呼叫 

    call :AppendColorText [TextColor] [DisplayText]
    call :AppendColorTextLine [TextColor] [DisplayText]


第一個參數帶入要顯示的顏色,第二個參數帶入要顯示的字串就可以了  

顯示的顏色部分由兩個顏色代碼所組成,前面的顏色代碼代表背景色,後面的顏色代碼代表前景色,顏色的代碼可參閱下表  

    0 = 黑色
    1 = 藍色
    2 = 綠色
    3 = 藍綠色
    4 = 紅色
    5 = 紫色
    6 = 黃色
    7 = 白色
    8 = 灰色
    9 = 淡藍色
    A = 淡綠色
    B = 淡藍綠色
    C = 淡紅色
    D = 淡紫色
    E = 淡黃色
    F = 亮白色


所以實際用起來會像下面這樣  

    call :AppendColorTextLine 0C "黑底紅字"


最後附上比較完整的使用範例

{% codeblock lang:bat %}
@ECHO off
SETLOCAL EnableDelayedExpansion
for /F "tokens=1,2 delims=#" %%a in ('"prompt #$H#$E# & echo on & for %%b in (1) do rem"') do (
  set "DEL=%%a"
)

#==========
#Main Action
#===========
call :AppendColorTextLine 0C "黑底紅字"
call :AppendColorTextLine 02 "黑底綠字"
call :AppendColorTextLine 70 "白底黑字"
call :AppendColorTextLine 71 "白底藍字"

pause

goto :eof



:AppendColorText
echo off
<nul set /p ".=%DEL%" > "%~2"
findstr /v /a:%1 /R "^$" "%~2" nul
del "%~2" > nul 2>&1
goto :eof


:AppendColorTextLine
echo off
call :AppendColorText %~1 %~2
Echo.
goto :eof
{% endcodeblock %}


運行結果如下

{% img /images/posts/ChangeColorInBatchFile/1.png %}
