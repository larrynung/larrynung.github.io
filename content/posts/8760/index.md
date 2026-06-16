---
title: "[Software]Quickly Remove SVN Source Control"
slug: "software-quickly-remove-svn-source-control"
aliases: ["/posts/8760/"]
date: "2009-06-10 09:14:31"
description: "在使用SVN做檔案控管時，SVN會在專案目錄下新增個.svn目錄。 該目錄內記錄著SVN控管所需的資訊。 當我們需要把專案的SVN控管給取消時，最笨的作法是我們必需一層層瀏覽專案目錄，並把專案目錄下的.svn目錄全部給砍掉。 較好的作法是，我們可以撰寫個副檔名為reg的登錄檔。"
tags: [Software]
---

在使用SVN做檔案控管時，SVN會在專案目錄下新增個.svn目錄。

![image_thumb_2.png](/images/posts/8760/image_thumb_2.png)

該目錄內記錄著SVN控管所需的資訊。

當我們需要把專案的SVN控管給取消時，最笨的作法是我們必需一層層瀏覽專案目錄，並把專案目錄下的.svn目錄全部給砍掉。

較好的作法是，我們可以撰寫個副檔名為reg的登錄檔。檔案內容如下：

```
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Folder\shell\DeleteSVN]
@="Delete SVN Folders"

[HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Folder\shell\DeleteSVN\command]
@="cmd.exe /c \"TITLE Removing SVN Folders in %1 && COLOR 07 && FOR /r \"%1\" %%f IN (.svn) DO RD /s /q \"%%f\" \""
```

編寫完畢後，用滑鼠連點兩下，把機碼登錄。

![image_thumb_5.png](/images/posts/8760/image_thumb_5.png)

![image_thumb_4.png](/images/posts/8760/image_thumb_4.png)

登錄完後按下滑鼠右鍵即會看到"Delete SVN Folders"選項。

![image_thumb_1.png](/images/posts/8760/image_thumb_1.png)

按下滑鼠選單後，即會開始清除SVN控管資訊。以後透過這新增的滑鼠選項即可快速輕鬆的清除SVN控管。
