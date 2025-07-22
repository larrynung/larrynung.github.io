---
title: "Tkinter's tkMessageBox"
date: "2013-11-06 12:00:00"
description: "Tkinter's tkMessageBox"
tags: [Python]
---

要使用Tkinter的MessageBox，首先要先將tkMessageBox package import進來。

import tkMessageBox

	tkMessageBox的用法大概像下面這樣，依使用需求呼叫不同的方法，並帶入訊息視窗的標題、內文、以及一些額外的參數就可以了。

tkMessageBox.FunctionName(title, message [, options])

	可以呼叫的方法有showinfo...

tkMessageBox.showinfo("showinfo demo", "Info")

	showwarning...

tkMessageBox.showwarning("showwarning demo", "Warning")

	showerror...

tkMessageBox.showerror("showerror demo", "Error")

	這些是用來提示使用者訊息用的訊息框，另外也有用來詢問使用者動作的訊息框。像是askquestion...

tkMessageBox.askquestion("askquestion demo", "Sure?!")

	askokcancel...

tkMessageBox.askokcancel("askokcancel demo", "OK?! CANCEL?!")

	askyesno...

tkMessageBox.askyesno("askyesno demo", "Yes?! No?!")

	以及askretrycancel...

tkMessageBox.askretrycancel("askretrycancel demo", "Retry?! Cancel?!")

	在使用這種用來詢問使用者動作的訊息框時，我們可以帶入default參數下去指定預設選取的對話框按鈕。像是下面這樣：

tkMessageBox.askquestion("askquestion demo", "Sure?!")
tkMessageBox.askokcancel("askokcancel demo", "OK?! CANCEL?!", default = "ok")
tkMessageBox.askyesno("askyesno demo", "Yes?! No?!", default = "no")
tkMessageBox.askretrycancel("askretrycancel demo", "Retry?! Cancel?!", default = "cancel")

	若是要知道使用者選取的結果，我們可以直接接方法的回傳值，除了askquest是回傳yes/no外，其它的方法在按下OK或是Yes按鈕時是回傳True，按下No與Cancel按鈕是回傳False。

print "askquestion's dialogresult: %s" % tkMessageBox.askquestion("askquestion demo", "Sure?!")
print "askokcancel's dialogresult: %s" % tkMessageBox.askokcancel("askokcancel demo", "OK?! CANCEL?!", default = "ok")
print "askyesno's dialogresult: %s" % tkMessageBox.askyesno("askyesno demo", "Yes?! No?!", default = "no")
print "askretrycancel's dialogresult: %s" % tkMessageBox.askretrycancel("askretrycancel demo", "Retry?! Cancel?!", default = "cancel")

	最後附上完整的測試範例：

import tkMessageBox

tkMessageBox.showinfo("showinfo demo", "Info")
tkMessageBox.showwarning("showwarning demo", "Warning")
tkMessageBox.showerror("showerror demo", "Error")

print "askquestion's dialogresult: %s" % tkMessageBox.askquestion("askquestion demo", "Sure?!")
print "askokcancel's dialogresult: %s" % tkMessageBox.askokcancel("askokcancel demo", "OK?! CANCEL?!", default = "ok")
print "askyesno's dialogresult: %s" % tkMessageBox.askyesno("askyesno demo", "Yes?! No?!", default = "no")
print "askretrycancel's dialogresult: %s" % tkMessageBox.askretrycancel("askretrycancel demo", "Retry?! Cancel?!", default = "cancel")

## 
	Link

		Standard Dialogs
	
		Python Tkinter tkMessageBox
	
		Tkinter 8.5 reference: a GUI for Python