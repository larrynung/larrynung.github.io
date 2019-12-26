---
title: Vault - Secrets engines
date: 2019-12-25 08:01:19
tags: [Vault]
---

Vault 的 Secure engine 可以是 AWS、Database、Github... 等。

<!-- More -->

</br>


資料會進哪個 Secret engine 是看 Path，像是預設開啟 kv 這個 Secret engine 在 secret 這個 Path，我們可以直接用 secret/$name 這樣的方式指定存放的位置。  

</br>


若指定的位置無對應的 Secret engine，因為無 Secret engine 可以服務，因此會報錯。

    vault write foo/bar a=b

{% asset_img 1.png %}

</br>


Secret engine 可使用 vault secrets enable 加帶 Secret engine name自行啟用，如果啟用的 Path 跟 Secret engine name 不同，可加帶 -path 參數指定。

    vault secrets enable [-path=$path] $secret-engine

</br>


像是這邊筆者起了一個 kv 的 Secret engine 在 kv 這個 Path。  

    vault secrets enable -path=kv kv

{% asset_img 2.png %}

</br>


查驗 Secret engine 列表，可看到確實已經啟用。

    vault secrets list

{% asset_img 3.png %}

</br>


實際操作寫入測試。  

    vault write kv/my-secret value="s3c(eT"

{% asset_img 4.png %}

</br>


    vault write kv/hello target=world

{% asset_img 5.png %}

</br>


    vault write kv/airplane type=boeing class=787

{% asset_img 6.png %}

</br>


新啟動的 Secret engine 應該會能正常的運作。  

    vault list kv

{% asset_img 7.png %}

</br>


若要關閉，可用 vault secrets disable 加帶 Path 關閉。

    vault secrets disable $path

</br>


像是...

    vault secrets disable kv/

{% asset_img 8.png %}

</br>


查驗 Secure engine 列表，應可看到確實被停用。  

    vault secrets list

{% asset_img 9.png %}

</br>


Link
====
* [Secrets Engines](https://learn.hashicorp.com/vault/getting-started/secrets-engines)
