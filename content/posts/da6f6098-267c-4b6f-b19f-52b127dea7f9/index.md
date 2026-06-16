---
title: "使用fsutil file createnew快速產生虛胖檔案"
date: "2013-11-06 12:00:00"
description: "在撰寫程式時，依照需求有時候開發人員可能會有需要找一些大檔案來考驗一下程式，看在系統中有很大檔案的情況下是否程式能正常運行。像是在做一些可以查閱檔案資訊的程式時，可能會需要一些較大的檔案來測一下是否會讓程式卡太久，或是做壓縮程式時可能會需要評估一下大檔案壓縮的效能、壓縮比等等。"
---

在撰寫程式時，依照需求有時候開發人員可能會有需要找一些大檔案來考驗一下程式，看在系統中有很大檔案的情況下是否程式能正常運行。像是在做一些可以查閱檔案資訊的程式時，可能會需要一些較大的檔案來測一下是否會讓程式卡太久，或是做壓縮程式時可能會需要評估一下大檔案壓縮的效能、壓縮比等等。

在這樣的需求下比較笨一點的做法是想辦法找到比較大的檔案，多半是從自己或別人的電腦中現有的檔案下手。比較聰明一點可能就是想辦法產生一個假檔使用，透過系統內建的fsutil file createnew我們可以很快速的滿足這樣的需求。

使用fsutil file createnew建立虛胖檔案十分簡單，使用方法如下：

```xml
Usage : fsutil file createnew <filename> <length>
   Eg : fsutil file createnew C:\testfile.txt 1000
```

簡單說在fsutil file createnew後面帶入檔名與檔案大小即可，像是鍵入fsutil file createnew c:\BigFile.txt 4293967295這行命令，可以在C:\下產生名為BigFile.txt的虛胖檔案，其檔案大小為4GB。

![image_thumb_3.png](/images/posts/da6f6098-267c-4b6f-b19f-52b127dea7f9/image_thumb_3.png)

![image_thumb_4.png](/images/posts/da6f6098-267c-4b6f-b19f-52b127dea7f9/image_thumb_4.png)

## Link

* 在Windows中產生任意大小的檔案
* Howto: Generate many files of a particular size in Windows
* 在Windows產生大檔案
* DOS命令大全：Fsutil:文件命令詳解
