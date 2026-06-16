---
title: "Tkinter's tkFileDialog"
date: "2013-11-06 12:00:00"
description: "要使用Tkinter的tkFileDialog，首先要先將tkFileDialog package import進來。 tkFileDialog 的用法大概像下面這樣，依使用需求呼叫不同的方法，並帶入參數就可以了。"
tags: [Python]
---

要使用Tkinter的tkFileDialog，首先要先將tkFileDialog package import進來。

```python
import tkFileDialog
```

tkFileDialog 的用法大概像下面這樣，依使用需求呼叫不同的方法，並帶入參數就可以了。

```python
tkFileDialog.FunctionName(options)
```

參數的部分可以帶入 title、filetypes、initialdir、initialfile、multiple、parent、defaultextension 等 (視方法不同可帶入的參數可能會有所不同)，分別對應到的是對話框標題、對話框可選擇的檔案類型、初始的目錄、初始的檔案位置、是否支援多選、父視窗、以及預設的附檔名。

```python
...
options = {}
options['filetypes'] = [("allfiles","*"),("text","*.txt")]
options['initialdir'] = "c:\\"
options['multiple'] = True
options['title'] = "tkFileDialog.askopenfilename"
...
```

可以呼叫的方法有askopenfilename、asksaveasfilename、askopenfilenames、askopenfile、askopenfiles、asksaveasfile、與askdirectory。

以askopenfilename來說...

```python
...
options['title'] = "tkFileDialog.askopenfilename"
print tkFileDialog.askopenfilename(**options) or "Without selected!"
...
```

就是我們一般看到的開啟檔案對話框，方法回傳值為選取的檔案位置。

![image_thumb.png](/images/posts/18586e39-cb57-4b05-8a55-5bed5a57adfc/image_thumb.png)

askopenfilenames 也是一般的開啟檔案對話框，等同於askopenfilename加設multiple參數。這個方法在python 2.6後回傳值從陣列變為字串 (也許是前面提到的multiple參數的關係)，所以在取得選取的檔案時我們必須做些處理，可以自行切割，或是透過Tkinter內建的splitlist將字串轉回陣列。

```python
...
options['title'] = "tkFileDialog.askopenfilenames"
print Tk().tk.splitlist(tkFileDialog.askopenfilenames(**options)) or "Without selected!"
...
```

askopenfile 跟askopenfilename類似，也是一般的開啟檔案對話框，只是其回傳值改為File物件，可用來直接進一步存取檔案內容。

```python
...
options['title'] = "tkFileDialog.askopenfile"
fs = tkFileDialog.askopenfile(**options)

if fs:
	print fs.name
else:
	print "Without selected!"
...
```

askopenfiles 也是開啟一般開啟對話框，可供多選並傳回File物件的陣列。

```python
...
options['title'] = "tkFileDialog.askopenfiles"
files = tkFileDialog.askopenfiles(**options)

print files

if files:
	for fs in files:
		print fs.name
else:
	print "Without selected!"
...
```

但這個方法在Python中好像有些問題，所以在運行時會出現錯誤。

![image_thumb_4.png](/images/posts/18586e39-cb57-4b05-8a55-5bed5a57adfc/image_thumb_4.png)

錯誤發生的原因可參閱tkFileDialog.py。就筆者看來可能是因為Python 2.6以後askopenfilenames的回傳值從陣列改為字串，這邊卻未跟著修正...

![image_thumb_7.png](/images/posts/18586e39-cb57-4b05-8a55-5bed5a57adfc/image_thumb_7.png)

此外，tkFileDialog也可以叫出儲存對話框。我們可以改呼叫asksaveasfilename方法，該方法回傳值為選取的檔案名稱。

```python
...
options['title'] = "tkFileDialog.asksaveasfilename"
options['defaultextension'] = '.txt'
del options['multiple']
print tkFileDialog.asksaveasfilename(**options)
...
```

![image_thumb_1.png](/images/posts/18586e39-cb57-4b05-8a55-5bed5a57adfc/image_thumb_1.png)

也可以改呼叫asksaveasfile方法，回傳值會從字串改為File物件，可直接用來寫入檔案內容。

```python
...
del options['filetypes']
del options['defaultextension']
options['title'] = "tkFileDialog.asksaveasfile"

print tkFileDialog.asksaveasfile(**options).name
...
```

若要叫出開啟目錄對話框，可以改呼叫askdirectory方法。

```python
...
options['title'] = "tkFileDialog.askdirectory"
print tkFileDialog.askdirectory(**options)
...
```

![image_thumb_6.png](/images/posts/18586e39-cb57-4b05-8a55-5bed5a57adfc/image_thumb_6.png)

最後附上筆者測試用的完整範例：

```python
from Tkinter import *
import tkFileDialog

options = {}
options['filetypes'] = [("allfiles","*"),("text","*.txt")]
options['initialdir'] = "c:\\"
options['multiple'] = True

options['title'] = "tkFileDialog.askopenfilename"
print tkFileDialog.askopenfilename(**options) or "Without selected!"

options['title'] = "tkFileDialog.askopenfilenames"
print Tk().tk.splitlist(tkFileDialog.askopenfilenames(**options)) or "Without selected!"

options['title'] = "tkFileDialog.askopenfile"
fs = tkFileDialog.askopenfile(**options)

if fs:
	print fs.name
else:
	print "Without selected!"

options['title'] = "tkFileDialog.askopenfiles"
files = tkFileDialog.askopenfiles(**options)

print files

if files:
	for fs in files:
		print fs.name
else:
	print "Without selected!"

options['title'] = "tkFileDialog.asksaveasfilename"
options['defaultextension'] = '.txt'
del options['multiple']
print tkFileDialog.asksaveasfilename(**options)

del options['filetypes']
del options['defaultextension']
options['title'] = "tkFileDialog.asksaveasfile"

print tkFileDialog.asksaveasfile(**options).name

options['title'] = "tkFileDialog.askdirectory"
print tkFileDialog.askdirectory(**options)
```

## Link

* tkFileDialog - Tkinter Wiki
