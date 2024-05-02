---
title: "Blazor - Getting started"
date: "2019-07-02 07:09:35"
tags: [Blazor]
---


要運行 Blazor，可先安裝 .Net Code 3.0 SDK，然後安裝 Blazor 範本。  

<!-- More -->

    dotnet new -i Microsoft.AspNetCore.Blazor.Templates::3.0.0-preview6.19307.2

</br>


再來透過範本建立 client 程式。  

    dotnet new blazor -o $project

![1.png](1.png)

</br>


或是 Server side 程式。  

    dotnet new blazorserverside -o $application

![2.png](2.png)

</br>


透過範本建立好後將程式運行起來。  

    dotnet run

![3.png](3.png)

</br>


透過瀏覽器訪問 http://localhost:5000 或是 https://localhost:5001，即可看到 Blazor 運行起來的樣子。  

![4.png](4.png)

</br>


![5.png](5.png)

</br>


![6.png](6.png)
