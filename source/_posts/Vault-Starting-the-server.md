---
title: Vault - Starting the server
date: 2019-12-19 07:15:01
tags: [Vault]
---

Vault 安裝後可調用 Vault server 命令起服務試試，這邊可加帶 -dev 參數起 Dev server。  

<!-- More -->

    vault server -dev

{% asset_img 1.png %}

</br>


服務啟用後注意到特別變色的區塊，裡面有 Vault server 的位置與 Root token。  

</br>


可複製新開 Terminal 後貼上，設定 VAULT_ADDR。  

    export VAULT_ADDR='http://127.0.0.1:8200'

{% asset_img 2.png %}

</br>


以及 VAULT_DEV_ROOT_TOKEN_ID。  

    export VAULT_DEV_ROOT_TOKEN_ID="$token_id"

{% asset_img 3.png %}

</br>


設定完後調用 vault status 命令測試看看，沒意外的話應該可以正常連到 Vault server，並將 Vault server 的資訊顯示出來。  

    vault status

{% asset_img 4.png %}

</br>


Link
====
* [Starting the Server](https://learn.hashicorp.com/vault/getting-started/dev-server)
