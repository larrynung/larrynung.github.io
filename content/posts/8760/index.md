---
title: "[Software]快速清除SVN控管"
date: "2009-06-10 09:14:31"
description: "[Software]快速清除SVN控管"
tags: [Software]
---

在使用SVN做檔案控管時，SVN會在專案目錄下新增個.svn目錄。

![](/images/posts/8760/)

該目錄內記錄著SVN控管所需的資訊。

當我們需要把專案的SVN控管給取消時，最笨的作法是我們必需一層層瀏覽專案目錄，並把專案目錄下的.svn目錄全部給砍掉。

較好的作法是，我們可以撰寫個副檔名為reg的登錄檔。檔案內容如下：
```
Windows Registry Editor Version 5.00
``````
``````
[HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Folder\shell\DeleteSVN]
``````
@="Delete SVN Folders"
``````
```
[HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Folder\shell\DeleteSVN