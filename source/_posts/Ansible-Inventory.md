---
title: Ansible - Inventory
date: 2017-05-22 23:44:35
tags: [Ansible]
---

Ansible 的 Inventory 紀錄著主機資訊。  

<!-- More -->

<br/>


裡面存放著要管理的機器位置。  

{% asset_img 1.png %}

<br/>


Ansible 可以透過 Inventory 找到要控制的機器做對應的操控。  

{% asset_img 2.png %}

<br/>


除了最簡單的將機器 IP 寫入 Inventory，若有相近的主機，Inventory 也可以像下面這樣撰寫：   

{% asset_img 3.png %}

<br/>


{% asset_img 4.png %}

<br/>


為了佈署上方便，我們也可以將機器做個群組。  

{% asset_img 5.png %}

<br/>


就可以針對不同群組使用不同的佈署策略。  

{% asset_img 6.png %}

<br/>


此外， Inventory 也支援一些可以設定的參數，像是 ansible_ssh_host、ansible_ssh_port、ansible_ssh_user、ansible_ssh_pass、ansible_sudo_pass、ansible_sudo_exe、ansible_connection、ansible_ssh_private_key_file、ansible_shell_type、ansible_python_interpreter、ansible_ssh_common_args、ansible_sftp_extra_args、ansible_scp_extra_args、ansible_ssh_extra_args、ansible_ssh_pipelining、ansible_ssh_executable、ansible_become、ansible_become_method、ansible_become_user、ansible_become_pass、ansible_shell_executable、ansible_host、ansible_user、ansible_become、ansible_docker_extra_args。  

<br/>


像是這邊筆者設定了 localhost 至 Inventory，但因為 localhost 不需要走 ssh，所以這邊將 ansible_connection 設為 local。  

{% asset_img 7.png %}

<br/>


{% asset_img 8.png %}

<br/>

