---
title: "GitLab - Install GitLab Runner on Windows"
date: "2018-01-21 10:32:01"
tags: [GitLab]
---


要在 Windows 使用 GitLab Runner，可至 [Install GitLab Runner on Windows - GitLab Documentation](https://docs.gitlab.com/runner/install/windows.html) 這邊下載 GitLab Runner。   

<!-- More -->

![1.png](1.png)
 
<br/>


下載後可視需要變更檔名，像是改為 gitlab-runner。然後帶入 install 調用命令，即可進行 GitLab Runner 服務的安裝。  

    gitlab-runner install

![2.png](2.png)

<br/>


![3.png](3.png)

<br/>


GitLab Runner 服務安裝好後，可帶入 start 調用命令，啟動 GitLab Runner 服務。  

    gitlab-runner start

![4.png](4.png)

<br/>


![5.png](5.png)

<br/>


若不在使用 GitLab Runner，可帶入 stop 調用命令，停用 GitLab Runner 服務。  

    gitlab-runner stop

![6.png](6.png)

<br/>


![7.png](7.png)

<br/>


然後帶入 uninstall 調用命令，將 GitLab Runner 服務移除。  

    gitlab-runner uninstall

![8.png](8.png)

<br/>


Link
====
* [GitLab Runner - GitLab Documentation](https://docs.gitlab.com/runner/)
* [Install GitLab Runner on Windows - GitLab Documentation](https://docs.gitlab.com/runner/install/windows.html)
