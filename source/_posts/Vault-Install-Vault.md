---
title: Vault - Install Vault
date: 2019-12-18 22:09:54
tags: [Vault]
---

要安裝 Vault 可到[這邊](https://www.vaultproject.io/downloads.html)下載對應系統的檔案。  

<!-- More -->

{% asset_img 1.png %}

</br>


像是筆者用 Android 手機在玩，所以是下載 ARM 版本的檔案。

    wget https://releases.hashicorp.com/vault/1.3.0/vault_1.3.0_linux_arm64.zip

{% asset_img 2.png %}

</br>



下載下來後解壓縮。  

    unzip vault_1.3.0_linux_arm64.zip

{% asset_img 3.png %}

</br>


就可以直接使用解壓縮出來的二進制檔案操作。  

    vault

{% asset_img 4.png %}

</br>


Link
====
* [Installing Vault](https://learn.hashicorp.com/vault/getting-started/install)
