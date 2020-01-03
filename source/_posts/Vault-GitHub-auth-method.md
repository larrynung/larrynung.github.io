---
title: Vault - GitHub auth method
date: 2020-01-02 08:28:32
tags: [Vault]
---

要使用 GitHub 做 Vault 的認證，可用 vault auth enable 帶入 github 啟動 GitHub auth method。  

<!-- More -->

    vault auth enable [-path=$path] github

{% asset_img 1.png %}

</br>


查驗一下是否正常啟用。

  vault auth list

{% asset_img 2.png %}                       

</br>


接著設定 GitHub 的 Organization。  

    vault write auth/github/config organization=$organization

{% asset_img 3.png %}

</br>


設定 GitHub Organization 的 Team，與要使用的 Policy。  

    vault write auth/github/map/teams/$team value=$policy

{% asset_img 4.png %}

</br>


因為用 GitHub 認證，這邊要先準備好 GitHub personal access token。  

{% asset_img 5.png %}

</br>


GitHub personal access token 這邊建立時要給予 read:org 權限。

{% asset_img 6.png %}

</br>


{% asset_img 7.png %}

</br>


{% asset_img 8.png %}

</br>


建立完調用 vault login，帶入 -method 參數指定用 GitHub 登入，並帶入剛建立的 GitHub personal access token 即可。  

    vault login -method=github

{% asset_img 9.png %}

</br>


若後續不再使用，可登回 root。  

    vault login $VAULT_DEV_ROOT_TOKEN_ID

{% asset_img 10.png %}

</br>


撤銷所有透過 GitHub 的登入。  

    vault token revoke -mode path auth/github

{% asset_img 11.png %}

</br>


關閉 GitHub auth method。

    vault auth disable github

{% asset_img 12.png %}

</br>


Link
=====
* [Authentication](https://learn.hashicorp.com/vault/getting-started/authentication)
