---
title: Ansible - APT module
date: 2017-05-26 23:30:25
tags: [Ansible]
---

Ansible 的 APT module 可以用來管理 APT 套件。  

<!-- More -->

<br/>


可用的參數如下：  

| parameter | required | default | choices | comments |
|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|
| allow_unauthenticated | no | no | yes/no | Ignore if packages cannot be authenticated. This is useful for bootstrapping environments that manage their own apt-key setup. |
| autoremove | no | | yes/no | If yes, remove unused dependency packages for all module states except build-dep. It can also be used as the only option. |
| cache_valid_time | no | | | Update the apt cache if its older than the cache_valid_time. This option is set in seconds. |
| deb | no | | | Path to a .deb package on the remote machine.If :// in the path, ansible will attempt to download deb before installing. (Version added 2.1) | 
| default_release | no | | | Corresponds to the -t option for apt and sets pin priorities |
| dpkg_options | no | force-confdef,force-confold | | Add dpkg options to apt command. Options should be supplied as comma separated list |
| force | no | no | yes/no | If yes, force installs/removes. |
| install_recommends | no | | yes/no | Corresponds to the --no-install-recommends option for apt. yes installs recommended packages. no does not install recommended packages. By default, Ansible will use the same defaults as the operating system. Suggested packages are never installed. |
| name | no | | | A package name, like foo, or package specifier with version, like foo=1.0. Name wildcards (fnmatch) like apt* and version wildcards like foo=1.0* are also supported. Note that the apt-get commandline supports implicit regex matches here but we do not because it can let typos through easier (If you typo foo as fo apt-get would install packages that have "fo" in their name with a warning and a prompt for the user. Since we don't have warnings and prompts before installing we disallow this. Use an explicit fnmatch pattern if you want wildcarding) |
| only_upgrade | no | | | Only upgrade a package if it is already installed. |
| purge | no | | yes/no | Will force purging of configuration files if the module state is set to absent. |
| state | no | present | latest/absent/present/build-dep | Indicates the desired package state. latest ensures that the latest version is installed. build-dep ensures the package build dependencies are installed. |
| update_cache | no | | yes/no | Run the equivalent of apt-get update before the operation. Can be run as part of the package installation or as a separate step. |
| upgrade | no | no | no/yes/safe/full/dist | If yes or safe, performs an aptitude safe-upgrade.If full, performs an aptitude full-upgrade.If dist, performs an apt-get dist-upgrade.Note: This does not upgrade a specific package, use state=latest for that. |

<br/>


以 Ad-Hoc 模式為例...

<br/>


要讓指定電腦透過 APT 安裝指定套件最新的版本，可以直接用 -m 指定使用 APT module，並用 -a 帶入 name 參數指定要安裝的 APT 套件，並將 state 參數設為 latest，指定安裝最新的版本。  

    ansible <Group> -i <IP>, -m apt -a "name=<Package> state=latest"
    ansible <Group> -i <Inventory> -m apt -a "name=<Package> state=latest"

{% asset_img 1.png %}

<br/>


要透過 APT 移除指定套件的話，可用 name 參數指定所要移除的 APT 套件，並將 state 參數設為 absent。  

    ansible <Group> -i <IP>, -m apt -a "name=<Package> state=absent"
    ansible <Group> -i <Inventory> -m apt -a "name=<Package> state=absent"

{% asset_img 2.png %}

<br/>


Link
----
* [apt - Manages apt-packages — Ansible Documentation](http://docs.ansible.com/ansible/apt_module.html)
