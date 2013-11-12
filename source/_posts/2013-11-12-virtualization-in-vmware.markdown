---
layout: post
title: "Virtualization in VMware"
date: 2013-11-12 23:27
comments: true
categories: [VMware]
---

在VMware下若欲跑些需要虛擬化的程式，可將VMware的Virtualization功能開啟   

<!--More-->

首先將VMware的Settings對話框開啟，點擊選取Advanced按鈕 

{% img /images/posts/VMwareVirtualization/1.png %}


將Preferred virtualization engine欄位的值設為Intel VT-x with EPT.

{% img /images/posts/VMwareVirtualization/2.png %}


找到對應的.vmx檔將之開啟，將下列內容填入後存檔

    hypervisor.cpuid.v0 = “FALSE”
    mce.enable = “TRUE”
    vhv.enable = “TRUE”


像是下面這樣  
{% img /images/posts/VMwareVirtualization/3.png %}

{% img /images/posts/VMwareVirtualization/4.png %}

{% img /images/posts/VMwareVirtualization/5.png %}


設定完後將虛擬機啟動，就可以在裡面使用虛擬化的功能了，像是Windows Phone的模擬器就可以在VMware內運行良好。

{% img /images/posts/VMwareVirtualization/6.png %}

