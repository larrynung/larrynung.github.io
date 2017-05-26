---
title: Ansible - Shell module
date: 2017-05-26 13:25:56
tags: [Ansible]
---

Ansible 的 Shell module 可以用來執行命令。  

<!-- More -->

<br/>


可用的參數如下：  

| parameter | required | default | choices | comments |
|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|
| chdir | no | | | cd into this directory before running the command |
| creates | no | | | a filename, when it already exists, this step will not be run. |
| executable | no | | | change the shell used to execute the command. Should be an absolute path to the executable. |
| free_form | yes | | | The shell module takes a free form command to run, as a string. There's not an actual option named "free form". See the examples! |
| removes | no | | | a filename, when it does not exist, this step will not be run. |
| warn | no | True | | if command warnings are on in ansible.cfg, do not warn about this particular line if set to no/false. |

<br/>


以 Ad-Hoc 模式為例...

<br/>


要讓指定電腦運行指定的命令，可以直接用 -m 指定使用 Shell module，並用 -a 指定命令。  

    ansible <Group> -i <IP>, -m Shell -a "<Command>"
    ansible <Group> -i <Inventory> -m Shell -a "<Command>"

{% asset_img 1.png %}

<br/>


要先切換至指定工作目錄再執行命令，可加帶 chdir 參數指定要切換至的工作目錄。  

{% asset_img 2.png %}

<br/>


要在指定的目錄或檔案存在的時才運行指定的命令，可加帶 creates 參數指定目錄或檔案。  

    ansible <Group> -i <IP>, -m Shell -a "<Command> creates=<FolderOrFile>"
    ansible <Group> -i <Inventory> -m Shell -a "<Command> creates=<FolderOrFile>"

{% asset_img 3.png %}

<br/>


要在指定的目錄或檔案不存在時才運行指定的命令，可加帶 removes 參數指定目錄或檔案。  

    ansible <Group> -i <IP>, -m Shell -a "<Command> removes=<FolderOrFile>"
    ansible <Group> -i <Inventory> -m Shell -a "<Command> removes=<FolderOrFile>"

{% asset_img 4.png %}

<br/>


Link
----
* [shell - Execute commands in nodes. — Ansible Documentation](http://docs.ansible.com/ansible/shell_module.html)