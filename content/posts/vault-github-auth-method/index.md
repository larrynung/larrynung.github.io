---
title: "Vault - GitHub auth method"
date: "2020-01-02 08:28:32"
tags: [Vault]
---


要使用 GitHub 做 Vault 的認證，可用 vault auth enable 帶入 github 啟動 GitHub auth method。  

<!-- More -->

    vault auth enable [-path=$path] github

![1.png](1.png)

</br>


查驗一下是否正常啟用。

  vault auth list

![2.png](2.png)                       

</br>


接著設定 GitHub 的 Organization。  

    vault write auth/github/config organization=$organization

![3.png](3.png)

</br>


設定 GitHub Organization 的 Team，與要使用的 Policy。  

    vault write auth/github/map/teams/$team value=$policy

![4.png](4.png)

</br>


因為用 GitHub 認證，這邊要先準備好 GitHub personal access token。  

![5.png](5.png)

</br>


GitHub personal access token 這邊建立時要給予 read:org 權限。

![6.png](6.png)

</br>


![7.png](7.png)

</br>


![8.png](8.png)

</br>


建立完調用 vault login，帶入 -method 參數指定用 GitHub 登入，並帶入剛建立的 GitHub personal access token 即可。  

    vault login -method=github

![9.png](9.png)

</br>


若後續不再使用，可登回 root。  

    vault login $VAULT_DEV_ROOT_TOKEN_ID

![10.png](10.png)

</br>


撤銷所有透過 GitHub 的登入。  

    vault token revoke -mode path auth/github

![11.png](11.png)

</br>


關閉 GitHub auth method。

    vault auth disable github

![12.png](12.png)

</br>


Link
=====
* [Authentication](https://learn.hashicorp.com/vault/getting-started/authentication)
