---
title: "Swashbuckle - Seamlessly adds a swagger to WebApi projects"
date: "2016-10-04 23:46:05"
tags: [Swashbuckle]
---


要在 Web API 加上 Swagger 支援，可以為專案裝上 Swashbuckle 套件。  

<!-- More -->

    Install-Package Swashbuckle

<br/>


![1.png](1.png)

<br/>


安裝完可以看到 App_Start 目錄下會多個 SwaggerConfig.cs 黨，我們需要依需求去做些設定上的調動。

![2.png](2.png)

<br/>


起碼要設定 XML documentation file 的位置，設定只要找到 c.IncludeXmlComments(GetXmlCommentsPath()); 這行，將其註解取消，取消後會看到 GetXmlCommentsPath 這個方法會找不到，這邊需要自己將該方法建立。  

![3.png](3.png)

<br/>


GetXmlCommentsPath 方法在實作上只要將 XML documentation file 位置回傳即可。  

![4.png](4.png)

<br/>


這邊的 XML documentation file 位置可查閱專案屬性這邊的設定。  

![5.png](5.png)

<br/>


設定好後運行將專案運行起來，瀏覽 http://[Domain]/swagger/，沒意外的話就會看到 swagger 頁面。  

![6.png](6.png)

<br/>
