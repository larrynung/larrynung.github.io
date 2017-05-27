---
title: Ansible - Copy module
date: 2017-05-27 23:39:53
tags: [Ansible]
---

Ansible 的 Copy module 可以用來處理檔案的複製。  

<!-- More -->

<br/>


可用的參數如下：  

| parameter | required | default | choices | comments |
|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|
| attributes | no | None | | Attributes the file or directory should have. To get supported flags look at the man page for chattr on the target system. This string should contain the attributes in the same order as the one displayed by lsattr. |
| backup | no | no | yes/no | Create a backup file including the timestamp information so you can get the original file back if you somehow clobbered it incorrectly. |
| content | no | | | When used instead of 'src', sets the contents of a file directly to the specified value. This is for simple values, for anything complex or with formatting please switch to the template module. |
| decrypt | no | Yes | Yes/No | This option controls the autodecryption of source files using vault. |
| dest | yes | | | Remote absolute path where the file should be copied to. If src is a directory, this must be a directory too. |
| directory_mode | no | | | When doing a recursive copy set the mode for the directories. If this is not set we will use the system defaults. The mode is only set on directories which are newly created, and will not affect those that already existed. |
| follow | no | no | yes/no | This flag indicates that filesystem links, if they exist, should be followed. |
| force | no | yes | yes/no | the default is yes, which will replace the remote file when contents are different than the source. If no, the file will only be transferred if the destination does not exist. |
| group | no | | | Name of the group that should own the file/directory, as would be fed to chown. |
| mode | no | | | Mode the file or directory should be. For those used to /usr/bin/chmod remember that modes are actually octal numbers (like 0644). Leaving off the leading zero will likely have unexpected results. As of version 1.8, the mode may be specified as a symbolic mode (for example, u+rwx or u=rw,g=r,o=r). |
| owner | no | | | Name of the user that should own the file/directory, as would be fed to chown. |
| remote_src | no | False | True/False | If False, it will search for src at originating/master machine, if True it will go to the remote/target machine for the src. Default is False. Currently remote_src does not support recursive copying. |
| selevel | no | s0 | | Level part of the SELinux file context. This is the MLS/MCS attribute, sometimes known as the range. _default feature works as for seuser. |
| serole | no | | | Role part of SELinux file context, _default feature works as for seuser. |
| setype | no | | | Type part of SELinux file context, _default feature works as for seuser. |
| seuser | no | | | User part of SELinux file context. Will default to system policy, if applicable. If set to _default, it will use the user portion of the policy if available. |
| src | no | | | Local path to a file to copy to the remote server; can be absolute or relative. If path is a directory, it is copied recursively. In this case, if path ends with "/", only inside contents of that directory are copied to destination. Otherwise, if it does not end with "/", the directory itself with all contents is copied. This behavior is similar to Rsync. |
| unsafe_writes | no | | | Normally this module uses atomic operations to prevent data corruption or inconsistent reads from the target files, sometimes systems are configured or just broken in ways that prevent this. One example are docker mounted files, they cannot be updated atomically and can only be done in an unsafe manner. This boolean option allows ansible to fall back to unsafe methods of updating files for those cases in which you do not have any other choice. Be aware that this is subject to race conditions and can lead to data corruption. |
| validate | no | None | | The validation command to run before copying into place. The path to the file to validate is passed in via '%s' which must be present as in the example below. The command is passed securely so shell features like expansion and pipes won't work. |

<br/>


以 Ad-Hoc 模式為例...

<br/>


要將指定檔案複製到指定的電腦，可以直接用 -m 指定使用 Copy module，並用 -a 帶入 src 參數指定來源檔案，以及 dest 參數設定目的檔案。  

    ansible <Group> -i <IP>, -m Copy -a "src=<SourceFile> dest=<DestFile>"
    ansible <Group> -i <Inventory> -m Copy -a "src=<SourceFile> dest=<DestFile>"

{% asset_img 1.png %}

<br/>


要直接將檔案內容寫到指定電腦，可以用 content 參數來設定要寫入的檔案內容。  

    ansible <Group> -i <IP>, -m Copy -a "content=<FileContent> dest=<DestFile>"
    ansible <Group> -i <Inventory> -m Copy -a "content=<FileContent> dest=<DestFile>"

{% asset_img 2.png %}

<br/>


要在指定檔案不存在時才寫檔案，可以將 force 參數設為 false。  

{% asset_img 3.png %}

<br/>


Link
----
* [copy - Copies files to remote locations. — Ansible Documentation](http://docs.ansible.com/ansible/copy_module.html)
