---
title: Azure - Create a Linux VM with Azure Cloud Shell
date: 2019-01-16 23:26:44
tags: [Azure]
---

要使用 Azure Cloud Shell 建立 Linux VM，可以使用 az vm create 命令，用 --name 指定 VM 的名稱、--resource-group 指定資源群組 (Resource groups)、--image 指定 VM 的映像 (e.x. UbuntuLTS)、--location 指定放置的區域、--size 指定 VM 的大小 (處理器速度、記憶體大小...等)、--admin-username 指定 VM 的使用者名稱、--generate-ssh-keys 建立用以登入 VM 的 SSH key。  

<!-- More -->

    az vm create \
      --name $vmName \
      --resource-group $resourceGroup \
      --image $image \
      --location $location \
      --size $size \
      --admin-username $adminUser \
      --generate-ssh-keys

{% asset_img 1.jpg %}

<br/>


當 VM 建立並啟動成功，可以用 az vm get-instance-view 命令查看。  

    az vm get-instance-view \
      --name $vmName \
      --resource-group $resourceGroup \
      --output table

{% asset_img 2.jpg %}

<br/>


Link
----
* [建立虛擬機器 | Microsoft Docs](https://docs.microsoft.com/zh-tw/learn/modules/welcome-to-azure/3-create-a-vm?pivots=linux-cloud)
