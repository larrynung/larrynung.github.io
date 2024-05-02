---
title: "Drone - Integrate with GitHub"
date: "2017-09-07 06:37:49"
tags: [Drone, GitHub]
---


要將 GitHub 與 GitHub 整合，需要先在 GitHub 建立 Application。  

<!-- More -->

<br/>


切到 GitHub 設定頁面。  

![1.png](1.png)

<br/>


切到 [Developer settings | OAuth Apps]。  

![2.png](2.png)

<br/>


創建新的 Applcation。  

![3.png](3.png)

<br/>


填寫 Application 的名稱、Drone 的位置、Application 的描述、Drone 的認證位置 （http://[DroneUrl]/api/auth/github.com），按下 Register application 按鈕繼續。  

![4.png](4.png)

<br/>


指定的 Application 即會建立。  

![5.png](5.png)

<br/>


開啟 Drone 的配置文件，設定連接 GitHub Application 需要的 client 與 secret。  

    vi /etc/drone/drone.toml 

![6.png](6.png)

<br/>


重啟 Drone 服務再次瀏覽 Drone 服務頁面即可。  

<br/>


![7.png](7.png)

<br/>


Link
----
* [How to Setup Drone on Ubuntu/Debian - FoxuTech](https://foxutech.com/how-to-setup-drone/)
* [如何在 linux 上配置持續集成服務 - Drone - 壹讀](https://read01.com/4ARPAo.html#.WbB7aNMjHVo)
