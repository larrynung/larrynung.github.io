---
title: "Hello, Tkinter"
date: "2013-11-06 12:00:00"
description: "Hello, Tkinter"
tags: [Python]
---

Tkinter是Python的GUI套件，骨子裡為Tcl/TK的封裝，因此透過Tkinter撰寫UI，我們可以讓程式在不同的平台上運行。

	Tkinter使用前我們可以先將Tkinter package import，並呼叫Tkinter._test方法，驗證一下開發環境。

import Tkinter 

Tkinter._test()

	若開發環境是OK的，我們應該可以看到像下面這樣的視窗介面。

	開發環境OK後，可以開始撰寫UI程式的部分。

	透過Tkinter進行程式的撰寫，大概要follow下面這樣的架構。首先要將Tkinter package import進來，import進來後宣告並設定TK物件(可以想成我們一般所說的視窗)，TK物件宣告完成後接著進其他控制項的宣告與設定，用控制項兜出我們想要的視窗樣子，最後呼叫TK物件的mainloop方法啟動訊息迴圈就可以了。

from Tkinter import *

form = Tk()
...
form.mainloop()

	以一個簡單的HelloWorld範例程式來說，程式實際寫起來會像下面這樣：

from Tkinter import *

form = Tk()
form.title("HelloWorld Demo")
form.geometry("300x200")

lbl = Label(form, text="Hello, world!")
lbl.pack()

form.mainloop()

	可以看到這邊如上面所述，會先將Tkinter package import，然後宣告TK物件，設定視窗的標題為"HelloWorld Demo"、視窗的大小為300x200，接著這邊宣告了一個Label控制項，裡面顯示著"Hello,world!"字樣，會內嵌在視窗裡面，最後呼叫TK.mainloop啟動訊息迴圈。

	所以這個HelloWorld範例程式運行起來會像下面這樣：

## 
	Link

		Hello, Tkinter