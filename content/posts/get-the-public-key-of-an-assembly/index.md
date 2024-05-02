---
title: "Get the Public Key of an Assembly"
date: "2015-02-12 08:02:00"
description: "Get the Public Key of an Assembly"
---


在做 .NET 程式的開發時，有時候我們會需要查閱組件目前簽署的 Public Key 為何 （可能是為了確定組件是否跟我們預期的是同一個，或是要做些 Config 設定，抑或是反射叫用）。這時我們可以直接透過 Visual Studio 安裝時自帶的強命名命令列工具下去查閱，呼叫 SN 命令，帶入 -TP 參數與組件的檔案位置。  

<!-- More -->

    sn.exe -Tp [AssemblyFile]


命令呼叫後會看到類似下面這樣的畫面，告訴你簽署 Public Key 以及 Public Key Token 為何。  

{% img /images/posts/PublicKeyWithAssembly/1.png %}

<br/>


也可進一步將之與 Visual Studio 整合，加入 External Tools，Command 那邊指向 SN.Exe 的位置，Arguments 那邊設定 -Tp $(TargetPath) 就可以了。  

{% img /images/posts/PublicKeyWithAssembly/2.png %}

<br/>


設定完以後就可以直接透過 Visual Studio 的 External Tools 直接觸發查詢當前專案產出的組件。  

{% img /images/posts/PublicKeyWithAssembly/3.png %}

<br/>


Link
----
* [Sn.exe (Strong Name Tool)](https://msdn.microsoft.com/en-us/library/vstudio/k5b5tt23%28v=vs.100%29.aspx)
* [asp.net - How do I find the PublicKeyToken for a particular dll? - Stack Overflow](http://stackoverflow.com/questions/1710935/how-do-i-find-the-publickeytoken-for-a-particular-dll)
* [How to: Create a Tool to Get the Public Key of an Assembly](http://msdn.microsoft.com/en-us/library/office/ee539398(v=office.14).aspx)
* [Getting Public Key Token of Assembly Within Visual Studio - Kirk Evans Blog - Site Home - MSDN Blogs](http://blogs.msdn.com/b/kaevans/archive/2008/06/18/getting-public-key-token-of-assembly-within-visual-studio.aspx)
