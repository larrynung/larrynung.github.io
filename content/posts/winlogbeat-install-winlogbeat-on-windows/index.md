---
title: "Winlogbeat - Install Winlogbeat on Windows"
date: "2017-06-04 23:52:14"
tags: [Winlogbeat]
---


要在 Windows 下使用 Winlogbeat，可先至官網下載下來解壓縮。

<!-- More -->

<br/>


裡面比較會要用到的檔案有 winlogbeat.exe、install-service-winlogbeat.psl、uninstall-service-winlogbeat.psl 與 winlogbeat.yml。


![1.png](1.png)

<br/>



winlogbeat.yml 是 Winlogbeat 的設定檔，設定完後直接點擊 winlogbeat.exe 就會開始作用。

<br/>



也可以執行 install-service-winlogbeat.psl 註冊成 Windows 服務，讓 Winlogbeat 在背景服務。


![2.png](2.png)

<br/>



Windows 服務註冊完後記得將服務啟動才有效果。


![3.png](3.png)

<br/>



做到這邊 Winlogbeat 就能依照設定正常的傳送 Windows Event Logs。

<br/>



若有需要後續也可執行 uninstall-service-winlogbeat.psl 將 Winlogbeat 的 Windows 服務移除。


![4.png](4.png)

<br/>


Link
----
* [Download Winlogbeat • Ship Windows Event Logs | Elastic](https://www.elastic.co/downloads/beats/winlogbeat)
