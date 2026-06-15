---
title: "Tkinter's tkColorChooser"
date: "2013-11-06 12:00:00"
description: "Tkinter's tkColorChooser"
tags: [Python]
---

使用Tkinter中的tkColorChooser，可以為叫出顏色選取對話框。

使用時需先將tkColorChooser package import進來。

```python
import tkColorChooser
```

Import完後就可以開始實際的撰寫程式，在此之前讓我們先來看一下tkColorChooser的函式原型：

```python
tkColorChooser.askcolor(color, options)
```

因為預設選取的顏色較為常用，tkColorChooser.askcolor這邊允許我們直接將預設選取的顏色帶入。

```python
...
print tkColorChooser.askcolor("red")
...
```

除了預設選取的顏色外，tkColorChooser.askcolor也可以透過options參數帶入些其它的設定，像是initialcolor、parent、title。initialcolor一樣是預設選取的顏色、parent是用來指定對話框的父視窗，而title則是設定顏色選取對話框的標題列文字 (依筆者的經驗在Windows下設定並無效果)。

另外要注意到的是回傳值的部分，tkColorChooser.askcolor選取完顏色後對話框關閉會回傳(triple, color)這樣的Tuple。triple這部分是顏色的RGB值，color這部份則是對應的color物件。所以tkColorChooser.askcolor呼叫完所回傳的值會像下面這樣：

![image_thumb_1.png](/images/posts/edb1e98e-d6f7-4e4c-bb31-2c0dc2a0ce8d/image_thumb_1.png)

最後附上筆者在測試時所用的範例：

```python
import tkColorChooser

print tkColorChooser.askcolor(title="test")
print tkColorChooser.askcolor("red")
print tkColorChooser.askcolor(initialcolor="red")
```

在Windows下運行會出現色彩對話框...

![image_thumb.png](/images/posts/edb1e98e-d6f7-4e4c-bb31-2c0dc2a0ce8d/image_thumb.png)

## Link

* 55.3. The tkColorChooser module
