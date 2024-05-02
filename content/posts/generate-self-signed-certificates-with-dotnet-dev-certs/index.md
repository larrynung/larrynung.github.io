---
title: "Generate self-signed certificates with dotnet dev-certs"
date: "2021-03-11 07:26:47"
---


dotnet dev-certs 提供 https 命令可供自產 HTTPS 開發憑證。  

<!-- More -->

    dotnet dev-certs --help

![1.png](1.png)

<br>


使用方式如下圖所示。  

    dotnet dev-certs https --help

![2.png](2.png)

<br>


最簡單的就是不帶任何參數直接使用 dotnet dev-certs 的 https 命令去產生並安裝 HTTPS 開發憑證。  

    dotnet dev-certs https

![3.png](3.png)

<br>


![4.png](4.png)

<br>


產生完可以用 dotnet dev-certs 的 https 命令加帶 --check 參數確認。  

    dotnet dev-certs https --check

![5.png](5.png)

<br>


狀態碼為 0 即表示成功。  

    echo $?

![6.png](6.png)

<br>


若要移除安裝的 HTTPS 開發憑證，可使用 dotnet dev-certs 的 https 命令並加帶 --clean 參數。  

    dotnet dev-certs https --clean

![7.png](7.png)

<br>


再次確認 HTTPS 開發憑證的安裝狀態。  

    dotnet dev-certs https --check

![8.png](8.png)

<br>


這時就會拿到狀態碼 6，表示並未安裝 HTTPS 開發憑證。  

    echo $?

![9.png](9.png)

<br>


如要匯出 HTTPS 開發憑證，可使用 dotnet dev-certs 的 https 命令，加帶 -ep 參數指定匯出的 HTTPS 開發憑證所要存放的檔案位置，加帶 -p 參數指定匯出的 HTTPS 開發憑證私鑰密碼。  

    dotnet dev-certs https -ep $file -p $password

![10.png](10.png)

<br>


![11.png](11.png)

<br>


匯出後 HTTPS 開發憑證會被放置在指定的位置。  

    ls $file

![12.png](12.png)

<br>


Link
====
* [如何使用 .NET Core 2.1 內建的 dev-certs 命令管理開發環境的自簽憑證 | The Will Will Web](https://blog.miniasp.com/post/2018/08/04/Configuring-HTTPS-using-NET-Core-SDK-21)
* [Generate Self-Signed Certificates Overview - .NET | Microsoft Docs](https://docs.microsoft.com/en-us/dotnet/core/additional-tools/self-signed-certificates-guide)
