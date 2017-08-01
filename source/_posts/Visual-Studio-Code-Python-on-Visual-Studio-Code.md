---
title: Visual Studio Code - Python on Visual Studio Code
date: 2017-04-09 23:08:40
tags: [Visual Studio Code, Python]
---

要在 Visual Studio Code 使用 Python，可安裝 Visual Studio Code 的 Python 套件。  

<!-- More -->

{% asset_img 1.png %}

<br/>


套件安裝完按下熱鍵打開 Command Palette (Windows 為 `Ctrl+ Shift + P`， OS X 為`CMD + SHIFT + P`)，搜尋並運行 `Tasks: Configure Task Runner`。 

{% asset_img 2.png %}

<br/>


接著選取 `TypeScript - tsconfig.json`。  

{% asset_img 3.png %}

<br/>


修改 tasks.json 設定，command 設為 python、args 設為 `${file}`、showOutput 設為 always。  

{% asset_img 4.png %}

<br/>


設定修改完存檔，按下熱鍵運行 `Tasks: Run Build Task` (Windows 為 `Ctrl+ Shift + B`， OS X 為`CMD + SHIFT + B`)，即可運行 Python 程式。  

{% asset_img 5.png %}

<br/>


Link
----
* [Python with Visual Studio Code](https://code.visualstudio.com/docs/languages/python)
* [[Python] 使用 Visual Studio Code 作為開發環境](http://oranwind.org/python-vscode/)
