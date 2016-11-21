---
title: SQL Server v.Next - Run the SQL Server Docker image
date: 2016-11-21 13:15:10
tags: [SQL Server v.Next]
---

要使用 Docker 運行 SQL Server v.Next，首先要先確定下列環境需求：  

<!-- More -->

    Docker Engine: 1.8+  
    Disk space: Minimum of 4 GB  
    RAM: Minimum of 4 GB  

<br/>


Docker 引擎需要在 1.8 以上的版本，硬碟空間最小要 4 GB，記憶體最小要有 4GB。  

<br/>


記得要調整設定讓 Docker 吃到 4 GB 的記憶體。  

<br/>


接著將 microsoft/mssql-server-linux 這個 Docker image 拉下來。  

    sudo docker pull microsoft/mssql-server-linux

{% asset_img 1.png %}

<br/>


拉下來後可以像下面這樣將 Container 運行起來，SA_PASSWORD 需要自行修改後帶入。  

	docker run -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=<YourStrong!Passw0rd>' -p 1433:1433 -d microsoft/mssql-server-linux
	
{% asset_img 2.png %}

<br/>


若是要將資料庫的資料保留下來，可以在 Container 運行時加掛資料卷。  

    sudo docker run -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=<YourStrong!Passw0rd>' -p 1433:1433 -v <host directory>:/var/opt/mssql -d microsoft/mssql-server-linux 

<br/>


叫用命令 `docker ps` 查驗是否 Container 有正常運行。  

{% asset_img 3.png %}

<br/>


Container 正常運行後，用剛才運行 Container 的 Port 號以及 SA 密碼即可連到 Docker Container 內的 SQL Server。  

<br/>


Link
----
* [SQL Server v.Next—SQL Server on Linux | Microsoft](https://www.microsoft.com/en-us/sql-server/sql-server-vnext-including-Linux)
* [Run the SQL Server Docker image on Linux, Mac, or Windows - SQL Server vNext CTP1 | Microsoft Docs](https://docs.microsoft.com/zh-tw/sql/linux/sql-server-linux-setup-docker)
* [microsoft/mssql-server-linux - Docker Hub](https://hub.docker.com/r/microsoft/mssql-server-linux/)