---
title: "Vault - Token authentication"
date: "2019-12-27 08:11:53"
tags: [Vault]
---


Vault 支援 Token 認證方式，在 Vault server 啟動後會顯示 Root token，可直接取用。  

<!-- More -->

</br>


也可以透過 vault token create 命令建立新的 token 使用。

    vault token create

![1.png](1.png)

</br>


Token 的相關資訊可用 vault token lookup 帶入 Token 查驗。

    vault token lookup $token

![2.png](2.png)

</br>


Token 取得後可用 vault login 帶入 Token 登入。  

    vault login $token

![3.png](3.png)

</br>


若要註銷 Token，可用 vault token revoke 帶入 Token。  

    vault token revoke $token

![4.png](4.png)

</br>


Token 註銷後不得使用，無法查驗 Token 資訊。  

![5.png](5.png)

</br>


也無法用來登入。  

![6.png](6.png)

</br>


Link
=====
* [Authentication](https://learn.hashicorp.com/vault/getting-started/authentication)
