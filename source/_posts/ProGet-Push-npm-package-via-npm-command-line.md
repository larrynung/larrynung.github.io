---
title: ProGet - Push npm package via npm command line
date: 2017-08-21 13:27:51
tags: [ProGet]
---

要透過 npm 命令上傳 npm 套件到 ProGet 的 npm feed，可在 ProGet 的 npm feed 頁面按下 Add Package 按鈕。  

<!-- More -->

{% asset_img 1.png %}

<br/>


點選 Push via npm (Command line)。  

{% asset_img 2.png %}

<br/>


這邊會告知怎樣使用 npm publish 命令上傳 npm 套件，使用前需點選 configured npm，參閱該連結做些設定。  

{% asset_img 3.png %}

<br/>


{% asset_img 4.png %}

<br/>


像是設定 npm 的 registry 位置。  

    npm set registry <RegistryUrl>

<br/>	


設定 npm registry 使用者帳號，這邊直接使用 ProGet 帳號轉小寫後輸入、輸入密碼。  

    npm adduser
	
{% asset_img 5.png %}

<br/>


再使用 npm publish 將指定的 npm 套件發佈上 Registry。  

    npm publish <NpmPackage>

{% asset_img 6.png %}

<br/>


選取的套件即會上傳到 ProGet 的 npm feed。  

{% asset_img 7.png %}

<br/>


{% asset_img 8.png %}

<br/>