---
title: "Tkinter.TK"
date: "2013-11-06 12:00:00"
description: "Tkinter.TK"
tags: [Python]
---

前面筆者在Hello, Tkinter這篇簡單的示範了一下最基本的Tkinter程式要如何撰寫。這邊進一步紀錄一下如何透過Tkinter.TK類別去設定與控制我們的程式視窗。

	在設定前記得要先將Tkinter package import進來，import進來後宣告，我們才可以進行設定的動作。

from Tkinter import *
form = Tk()

	要設定視窗上的標題，可以叫用TK.title方法，帶入視窗標題所要顯示的字串。

form.title("Tkinter.TK Demo")

	要設定視窗標題前的小圖示，可叫用TK.iconbitmap方法，帶入視窗標題前要顯示的小圖示檔案位置。

form.iconbitmap('Icon.ico')

	要設定視窗的背景顏色，可叫用TK.configure方法，帶入視窗的背景顏色。

form.configure(background='black')
form.configure(background='#888888')

	要設定視窗是否可以縮放，可以叫用TK.resizable方法。第一個帶入的參數是用來指定寬度大小是否可供縮放調整、第二個則是用來指定高度大小是否可供縮放調整。

form.resizable(False, False)

	要設定視窗啟動時的大小與位置，可以叫用TK.geometry方法，帶入特定的格式字串(寬x長+左位移+右位移)。像是"300x200+10+10"就是在(10,10)這個位置建立大小的視窗。這邊若有需要也可以只指定視窗大小，或是視窗的位置，像是"300x200"與"+10+10"。

form.geometry("300x200+10+10")

	要設定視窗最小的縮放大小，可以叫用TK.minsize方法，帶入視窗最小可接受的寬度與高度。

form.minsize(300, 200)

	要設定視窗最大的縮放大小，可以叫用TK.maxsize方法，帶入視窗最大可接受的寬度與高度。

form.maxsize(600, 400)

	要將視窗變成ToolWindow Style，可以呼叫TK.attributes("-toolwindow", 1)。

form.attributes("-toolwindow", 1) 

	要將視窗設為置頂視窗，可以呼叫TK.attributes("-topmost", 1)。

form.attributes("-topmost", 1) 

	要在啟動時最大化，可以呼叫TK.state("zoomed")。

form.state("zoomed")

	要最小化可以呼叫TK.iconify方法。

form.iconify()

	要還原最小化可以呼叫TK.deiconify方法。

form.deiconify()

	最後實際來看個完整的使用範例：

from Tkinter import *

form = Tk()

form.title("Tkinter.TK Demo")
form.geometry("300x200+10+10")
form.iconbitmap('Icon.ico')
#form.resizable(False, False)
form.minsize(300, 200)
form.maxsize(600, 400)
#form.attributes("-toolwindow", 1) 
form.attributes("-topmost", 1) 
#form.state("zoomed")
#form.iconify()
#form.deiconify()
form.configure(background='black')

form.mainloop()

	運行起來會像下面這樣：

## 
	Link

		Toplevel Window Methods