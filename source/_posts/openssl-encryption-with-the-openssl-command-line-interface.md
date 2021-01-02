---
title: "OpenSSL - Encryption with the OpenSSL Command-Line Interface"
date: 2021-01-01 20:34:52
tags: [OpenSSL]
---

要使用 OpenSSL CLI 進行加密，可先透過命令列帶入參數 -help 查閱一下 OpenSSL enc 的使用方式。  

<!-- More -->

    openssl enc -help

{% asset_img 1.png %}

</br>


常用的參數有 -aes-256-cbc 指定使用 AES 256 CBC 加密、-base64 參數指定經過 Base64 處理、-p 參數指定印出 salt/key/iv、-k 參數指定要用來加密金鑰、-nosalt 指定加密時不加 salt。  

</br>


像是要將 "hello" 透過 AES 256 CBC 加密、加密金鑰用 "world"、透過 Base64 處理的話，可像下面這樣調用。  

    echo "hello" | openssl enc -aes-256-cbc -base64 -p -k world

{% asset_img 2.png %}

</br>


如果不加 salt，可加帶 -nosalt 參數。  

    echo "hello" | openssl enc -aes-256-cbc -base64 -p -k world -nosalt

{% asset_img 3.png %}

</br>


Link
====
* [The Developer Toolbox: Encryption/Decryption with the OpenSSL Command-Line Interface | Jungle Disk Blog](https://www.jungledisk.com/blog/2018/06/04/the-developer-toolbox-encryption-decryption-with-openssl-command-line-interface/)
