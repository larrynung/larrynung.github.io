---
title: "Visual Studio 2013 RC New Feature - XAML Editor's Go To Definition"
date: "2013-11-06 12:00:00"
description: "Visual Studio 2013 RC New Feature - XAML Editor's Go To Definition"
---

Visual Studio 2013 RC在XAML編輯區這邊開始支援Go To Definition，Go To Definition不再只有程式碼編輯區可以使用。

	若是在內建的元件型別上使用Go To Definition...

	Visual Studio會開啟物件瀏覽器並自動幫我們帶到該元件型別上。

	如果是在內建元件的屬性上使用Go To Definition。

	物件瀏覽器視窗會更進一步的帶到該屬性上面。

	自訂的元件這邊一樣可以支援Go To Definition功能。

	如果是在元件型別的上方使用Go To Definition，因為是自訂的元件，所以我們的專案中會有XAML檔與CS檔，Visual Studio會不知道你想要移至哪個定義，所以會都列出讓我們自行選取。

	如果在自訂元件的成員上使用Go To Definition。

	因為目標明確，所以會直接的帶到成員的定義位置。

	除了內建的元件以及自訂的元件外，Resource這邊也支援Go To Definition，

	像是Static Resource...

	或是Dynamic Resource...Go To Definition功能在上面都運行良好