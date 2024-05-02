---
title: "Jenkins - Setup slave nodes"
date: "2018-11-29 23:53:44"
tags: [Jenkins]
---


要設定 Jenkins 的 Slave 節點，先將 Jenkins 切到設定全域安全性。  

<!-- More -->

![1.png](1.png)

<br/>


設定 JNLP agent 要走的 TCP port。  

![2.png](2.png)

<br/>
      

存檔離開。    

![3.png](3.png)

<br/>


然後進到管理節點。  

![4.png](4.png)

<br/>


點選新增節點。  

![5.png](5.png)

<br/>


設定節點名稱後按下 OK 按鈕。

![6.png](6.png)

<br/>


接著進行節點細部設定，像是執行程式數量這邊可以設定要讓該節點運同時運行多少的任務，遠端檔案系統根目錄這邊設定該節點電腦存放必要程式的位置，設定完成按下儲存按鈕。

![7.png](7.png)

<br/>


節點清單中會出現剛所加入的節點，點選該節點。

![8.png](8.png)

<br/>


這邊會提示節點電腦的設置。  

<br/>


這邊可以下載他所提供的 JNLP 檔。    

![9.png](9.png)

<br/>


將下載下來的 JNLP 檔放至 Slave 節點電腦運行，只要 JRE 有安裝就能直接用滑鼠連點開啟運行。  

![10.png](10.png)

<br/>


![11.png](11.png)

<br/>


![12.png](12.png)

<br/>


運行後剛在節點設定那邊所指定的位置就會存放運行必要的檔案。  

![13.png](13.png)

<br/>


Jenkins 節點清單這邊也會看到節點有正常的被連接。  

![14.png](14.png)

<br/>


除了用下載的 JNLP 檔案外，我們也可以用命令的方式啟動 Slave 節點服務。  

![15.png](15.png)

<br/>


![16.png](16.png)

<br/>


如要將 Slave 節點服務註冊成 Windows 服務，可透過 JNLP 檔運行後開出的視窗，點選 [File | Install as a service]  主選單選項。  

![17.png](17.png)

<br/>


然後點選 OK 按鈕做 Windows 服務的註冊。  

![18.png](18.png)

<br/>


![19.png](19.png)

<br/>
