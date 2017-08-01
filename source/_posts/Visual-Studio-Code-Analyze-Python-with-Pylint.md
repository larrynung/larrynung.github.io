---
title: Visual Studio Code - Analyze Python with Pylint
date: 2017-04-24 23:45:28
tags: [Visual Studio Code, Python]
---

要在 Visual Studio Code 中開發 Python 並使用 Pylint 進行程式碼的分析，Visual Studio Code 要先安裝 Python 的套件，完成 Python 開發環境的設定。   

<!-- More -->

<br/>


然後安裝 Pylint，不同環境有不同的安裝方式，因為筆者用的是 Mac，所以是用 pip 安裝。 

<br/> 


沒有 pip 的話要先進行安裝。    

{% asset_img 1.png %}

<br/>


開啟 Visual Studio Code 運行 Python 程式，Visual Studio Code 偵測到 Pylint 沒安裝的話會彈出通知，並提供安裝的按鈕。  

{% asset_img 2.png %}

<br/>


點選安裝的按鈕，安裝命令會帶到 TERMINAL 視窗調用。  

{% asset_img 3.png %}

<br/>


如果有權限問題的話，還是需要自己調整命令後再調用。  

{% asset_img 4.png %}

<br/>


安裝好後就可以支援 Python 的分析。  

{% asset_img 5.png %}

<br/>


Link
----
* [Pylint - code analysis for Python | www.pylint.org](https://www.pylint.org/)
