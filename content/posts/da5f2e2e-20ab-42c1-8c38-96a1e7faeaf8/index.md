---
title: "Tkinter's place geometry manager"
date: "2013-11-06 12:00:00"
description: "Tkinter's place geometry manager"
tags: [Python]
---

Tkinter在做版面配置有三種方式，place是其中一種。

使用place來做版面配置，我們可以指定元件的絕對位置、絕對大小、相對位置、相對大小...

place方法可以接受anchor、bordermode、x、y、relx、rely、width、height、relwidth、relheight...等參數。

x、y、width、height用來設定元件的絕對位置與絕對大小。

```python
...
lbl = Label(form, text="place test1", bg="red")
lbl.place(x=10, y=10, width=100, height=100)

lbl = Label(form, text="place test2", bg="white")
lbl.place(x=20, y=20)
...
```

relx、rely、height、relwidth則用來設定相對位置與相對大小。相對位置與相對大小是相對於parent來說，其值介在 0.0 與 1.0 中間。所以假設我們要將元件置中，我們可以將anchor設為CENTER，並設定relx為0.5；要將元件置中且元件的寬度相當於parent的一半，我們可以將relx設為0.25，relwidth設為0.5；要將元件靠右放，可以將anchor設為E，relx設為1。其它以此類推...

```python
...
lbl = Label(form, text="place test0", bg="gray")
lbl.place(x=5, y=5, relwidth=1, relheight=1, width=-10, height=-10)
...
lbl = Label(form, text="place test3", bg="yellow")
lbl.place(y=120, relx=0.25 , relwidth=0.5)

lbl = Label(form, text="place test4", bg="yellow")
lbl.place(y=150, anchor=E, relx=1)

lbl = Label(form, text="place test5", bg="yellow")
lbl.place(y=180, relx=0.5, anchor=CENTER)
...
```

最後附上完整的範例程式：

```python
from Tkinter import *

form = Tk()
form.geometry("300x200")

lbl = Label(form, text="place test0", bg="gray")
lbl.place(x=5, y=5, relwidth=1, relheight=1, width=-10, height=-10)

lbl = Label(form, text="place test1", bg="red")
lbl.place(x=10, y=10, width=100, height=100)

lbl = Label(form, text="place test2", bg="white")
lbl.place(x=20, y=20)

lbl = Label(form, text="place test3", bg="yellow")
lbl.place(y=120, relx=0.25 , relwidth=0.5)

lbl = Label(form, text="place test4", bg="yellow")
lbl.place(y=150, anchor=E, relx=1)

lbl = Label(form, text="place test5", bg="yellow")
lbl.place(y=180, relx=0.5, anchor=CENTER)

form.mainloop()
```

運行起來會像下面這樣：

![image_thumb_4.png](/images/posts/da5f2e2e-20ab-42c1-8c38-96a1e7faeaf8/image_thumb_4.png)

## Link

* Layout Managers / Geometry Manager
* The Tkinter Place Geometry Manager
* Python Tkinter place() Method
