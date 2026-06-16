---
title: "Tkinter's grid geometry manage"
date: "2013-11-06 12:00:00"
description: "Tkinter在做版面配置有三種方式，grid是其中一種。 使用grid來做版面配置，我們可以指定元件的要放在哪一行、哪一列、占用幾行、占用幾列...等。 grid方法可以接受column、columnspan、row 、rowspan…"
tags: [Python]
---

Tkinter在做版面配置有三種方式，grid是其中一種。

使用grid來做版面配置，我們可以指定元件的要放在哪一行、哪一列、占用幾行、占用幾列...等。

grid方法可以接受column、columnspan、row 、rowspan 、padx、pady、ipadx、ipady、sticky...等參數。

column、columnspan、row 、rowspan用來設定元件要放在Grid的哪行哪列，以及要占用的行列數。

```python
...
Entry(form).grid(row=0, column=0)
Entry(form).grid(row=0, column=1, rowspan=2)
Entry(form).grid(row=1, column=0)
Entry(form).grid(row=2, column=0, columnspan=2)
...
```

sticky可設定元件要怎樣對齊，若是要靠左對齊可以設定W、靠右對齊可以設定E、靠上對齊設定N、靠下對齊設定S。要讓元件左右伸展，可設定WE；要讓元件上下左右都可以伸展，則設定NEWS。

```python
...
Entry(form).grid(row=0, sticky=W+E)
Entry(form).grid(row=1, sticky="WE")
Entry(form).grid(row=2, sticky="NEWS")
...
```

padx、pady、ipadx、ipady跟我們一般認知的margin與padding沒什麼兩樣，一個是外部的邊界，一個是內部的邊界(也可參閱筆者Tkinter's pack geometry manager這篇的說明)。

```python
...
Button(form, text="GO").grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky=W+E+S+N)
...
```

grid在使用上可以不用是先宣告行列數，只要呼叫grid時帶入行列，Tkinter就會自動幫我們長出。預設長出的欄位是不具縮放功能的，因此我們在調整視窗時，欄位是不會跟著縮放的。如要進行欄位縮放的調整，我們可以透過TK.columnconfigure與TK.rowconfigure這兩個方法下去設定，帶入對應的行列數以及weight值就可以了，weight值為1代表可進行縮放，反之則否。

```python
...
form = Tk()
...
form.columnconfigure(0, weight=0)
form.columnconfigure(1, weight=1)
form.rowconfigure(0, weight=0)
form.rowconfigure(1, weight=0)
form.rowconfigure(2, weight=1)
...
```

最後附上完整的測試範例：

```python
from Tkinter import *

form = Tk()

form.columnconfigure(0, weight=0)
form.columnconfigure(1, weight=1)
form.rowconfigure(0, weight=0)
form.rowconfigure(1, weight=0)
form.rowconfigure(2, weight=1)

Label(form, text="First").grid(row=0, sticky=W)
Label(form, text="Second").grid(row=1, sticky=W)

Entry(form).grid(row=0, column=1, sticky=W+E)
Entry(form).grid(row=1, column=1, sticky=W+E)

Button(form, text="GO").grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky=W+E+S+N)

form.mainloop()
```

運行的結果如下：

![image_thumb.png](/images/posts/41f12d29-128f-4377-a12b-daa9fdf1a35d/image_thumb.png)

前面Label顯示的字樣會靠左對其，右側輸入框的寬度會填滿剩下的空間。下方的按鈕四周會留個5單位，且會占滿下方剩餘的空間。

![image_thumb_1.png](/images/posts/41f12d29-128f-4377-a12b-daa9fdf1a35d/image_thumb_1.png)

## Link

* Layout Managers / Geometry Manager
* The Tkinter Grid Geometry Manager
* Grid layout manager demonstration.
* Tkinter Geometry Managers
