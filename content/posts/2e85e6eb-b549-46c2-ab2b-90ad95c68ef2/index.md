---
title: "啟動BusyBox內建的FTP Server"
date: "2013-11-06 12:00:00"
tags: [網樂通]
description: "要啟動BusyBox內建的FTP Server，我們需要先孰悉tcpsvd與ftpd這兩個命令。 tcpsvd可以建立TCP socket，並將它bind在某個ip跟port，或是bind在某個程式上面。"
---

要啟動BusyBox內建的FTP Server，我們需要先孰悉tcpsvd與ftpd這兩個命令。

tcpsvd可以建立TCP socket，並將它bind在某個ip跟port，或是bind在某個程式上面。

![screenshot(65)_thumb.png](/images/posts/2e85e6eb-b549-46c2-ab2b-90ad95c68ef2/screenshot%2865%29_thumb.png)

ftpd則是Anonymous FTP server，它不做身分的驗證，所以啟動後我們使用Guest就可以直接連上去。ftpd它可透過設定inetd.conf去啟動服務，或是搭配tcpsvd來做運行。

![screenshot(66)_thumb.png](/images/posts/2e85e6eb-b549-46c2-ab2b-90ad95c68ef2/screenshot%2866%29_thumb.png)

這兩個命令理解了後，我們實際來啟動服務測試看看。呼叫命令tcpsvd 0 21 ftpd -w /root將服務啟動，設定FTP的port為21，使用者可上傳檔案至FTP，以及FTP檔案的存放位置在/root下。

![screenshot(67)_thumb.png](/images/posts/2e85e6eb-b549-46c2-ab2b-90ad95c68ef2/screenshot%2867%29_thumb.png)

命令呼叫後，命令列會被卡住，表示FTP服務正在運行。若想中止運行的FTP服務，可以按下熱鍵Ctrl + C將運行中斷。

若是想要啟動FTP Server卻又不想要卡住命令列，可以在命令後面加一個"&"，這樣命令呼叫後就會由新的instance去執行，命令列不會被卡住。

![screenshot(71)_thumb.png](/images/posts/2e85e6eb-b549-46c2-ab2b-90ad95c68ef2/screenshot%2871%29_thumb.png)

只不過以這樣的命令運行，我們必須要透過Kill Process的方式來終止運行的FTP服務。

![screenshot(72)_thumb.png](/images/posts/2e85e6eb-b549-46c2-ab2b-90ad95c68ef2/screenshot%2872%29_thumb.png)

在FTP服務運行時，我們可以在瀏覽器上輸入機器的網址，前面的通訊協定記得改用ftp，嘗試做FTP的連線看看。

![screenshot(68)_thumb.png](/images/posts/2e85e6eb-b549-46c2-ab2b-90ad95c68ef2/screenshot%2868%29_thumb.png)

瀏覽器找到FTP服務後會詢問登入的身分，記得剛開始時筆者就有提到這是Anonymous FTP server，所以這邊直接用Guest身分登入。

![screenshot(69)_thumb.png](/images/posts/2e85e6eb-b549-46c2-ab2b-90ad95c68ef2/screenshot%2869%29_thumb.png)

沒意外的話我們應該可以像下面這樣看到FTP Server內的資料。

![screenshot(70)_thumb.png](/images/posts/2e85e6eb-b549-46c2-ab2b-90ad95c68ef2/screenshot%2870%29_thumb.png)
