---
title: "Decode JWT token with jq"
date: "2021-03-20 08:02:06"
---


使用 JWT token 免不了有時會需要解碼看裡面存放的內容，在可以連到外網的環境下，很多網站工具都可以滿足我們的需求，但若是在網路比較受限的環境下，就不能依賴於外網的網站工具了。

<!-- More -->

<br>


這時可考慮使用 jq 命令來做 JWT token 的解碼，使用方式如下:  

    jq -R 'split(".") | .[1] | @base64d | fromjson' <<< "$JWT"

<br>


像是筆者這邊拿了一組 JWT token。  

![1.png](1.png)

<br>


將 JWT token 帶入指令，即可看到 JWT token 解碼後的結果。  

    jq -R 'split(".") | .[1] | @base64d | fromjson' <<< "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"

![2.png](2.png)

<br>


Link
====
* [Decode a JWT via command line](https://gist.github.com/angelo-v/e0208a18d455e2e6ea3c40ad637aac53)
