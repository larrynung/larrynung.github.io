---
title: Ansible - Inventory
date: 2017-05-22 23:44:35
tags: [Ansible]
---

Ansible 的 Inventory 是 Ansible 的主機清單，紀錄著要被管理的主機資訊。  

<!-- More -->

<br/>


最簡單的設置方式就是直接將要被管理的主機 IP 逐一寫入。  

{% asset_img 1.png %}

<br/>


Ansible 就可以透過 Inventory 找到要控制的機器做對應的操控。  

{% asset_img 2.png %}

<br/>


若有多台相近 IP 或相近網址的主機，Inventory 也可以用中括號來設定範圍值，便於設定與後續的管理。  

{% asset_img 3.png %}

<br/>


{% asset_img 4.png %}

<br/>


在比較複雜的環境下，為了佈署上的方便，我們也可以在 Inventory 中將機器做群組。  

{% asset_img 5.png %}

<br/>


這樣可針對不同群組套用不同的佈署策略。  

{% asset_img 6.png %}

<br/>


此外， Inventory 也支援一些可以設定的參數，可參閱下表。  

| Parameter | Description | 
|:-------------:|:-------------:|
| ansible_connection | Connection type to the host. This can be the name of any of ansible’s connection plugins. SSH protocol types are smart, ssh or paramiko. The default is smart. Non-SSH based types are described in the next section. |
| ansible_host | The name of the host to connect to, if different from the alias you wish to give to it. |
| ansible_port | The ssh port number, if not 22 |
| ansible_user | The default ssh user name to use. |
| ansible_ssh_pass | The ssh password to use (never store this variable in plain text; always use a vault. See Variables and Vaults) |
| ansible_ssh_private_key_file | Private key file used by ssh. Useful if using multiple keys and you don’t want to use SSH agent. |
| ansible_ssh_common_args | This setting is always appended to the default command line for sftp, scp, and ssh. Useful to configure a ProxyCommand for a certain host (or group). |
| ansible_sftp_extra_args | This setting is always appended to the default sftp command line. |
| ansible_scp_extra_args | This setting is always appended to the default scp command line. |
| ansible_ssh_extra_args | This setting is always appended to the default ssh command line. |
| ansible_ssh_pipelining | Determines whether or not to use SSH pipelining. This can override the pipelining setting in ansible.cfg. |
| ansible_ssh_executable | This setting overrides the default behavior to use the system ssh. This can override the ssh_executable setting in ansible.cfg. |
| ansible_become | Equivalent to ansible_sudo or ansible_su, allows to force privilege escalation |
| ansible_become_method | Allows to set privilege escalation method |
| ansible_become_user | Equivalent to ansible_sudo_user or ansible_su_user, allows to set the user you become through privilege escalation |
| ansible_become_pass | Equivalent to ansible_sudo_pass or ansible_su_pass, allows you to set the privilege escalation password (never store this variable in plain text; always use a vault. See Variables and Vaults) |
| ansible_shell_type | The shell type of the target system. You should not use this setting unless you have set the ansible_shell_executable to a non-Bourne (sh) compatible shell. By default commands are formatted using sh-style syntax. Setting this to csh or fish will cause commands executed on target systems to follow those shell’s syntax instead. |
| ansible_python_interpreter | The target host python path. This is useful for systems with more than one Python or not located at /usr/bin/python such as *BSD, or where /usr/bin/python is not a 2.X series Python. We do not use the /usr/bin/env mechanism as that requires the remote user’s path to be set right and also assumes the python executable is named python, where the executable might be named something like python2.6. |
| ansible_shell_executable | This sets the shell the ansible controller will use on the target machine, overrides executable in ansible.cfg which defaults to /bin/sh. You should really only change it if is not possible to use /bin/sh (i.e. /bin/sh is not installed on the target machine or cannot be run from sudo.). |
| ansible_docker_extra_args | Could be a string with any additional arguments understood by Docker, which are not command specific. This parameter is mainly used to configure a remote Docker daemon to use. |

<br/>


像是這邊筆者設定了 localhost 至 Inventory，但因為 localhost 不需要走 ssh，所以這邊將 ansible_connection 設為 local。  

{% asset_img 7.png %}

<br/>


{% asset_img 8.png %}

<br/>

