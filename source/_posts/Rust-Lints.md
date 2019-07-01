---
title: Rust - Lints
date: 2019-07-01 08:30:00
tags: [Rust]
---

Rust 內建程式碼分析功能，在編譯時會針對程式碼進行分析。  

<!-- More -->

</br>


分析出來的問題分為 allow、warn、deny、forbid 這幾個等級。  

</br>


allow 是被允許的問題，預設是不會顯示的，若有需要可手動將它轉成其它等級。  

</br>


像是下面這樣的程式。  

{% asset_img 1.png %}

</br>


在編譯時可帶入 -W、-D、-F 將指定的 allow 等級問題轉為 warn、deny、forbid 等級，這樣就可以在編譯時看到問題。  

    rust -W $issue
    rust -D $issue
    rust -F $issue

{% asset_img 2.png %}

</br>


如果是 allow 等級以外的問題，直接編譯就可以偵測到。  

</br>


像是 warn。  

{% asset_img 3.png %}

</br>


{% asset_img 4.png %}

</br>


deny...

{% asset_img 5.png %}

</br>


{% asset_img 6.png %}

</br>


或是 forbid。

</br>


如要轉換問題等級，出了用上面提到的命令參數外，也可以透過 attribute 的方式指定。  

{% asset_img 7.png %}

</br>


{% asset_img 8.png %}

</br>


{% asset_img 9.png %}

</br>


{% asset_img 10.png %}

</br>


Link
====
* [Lint levels - The rustc book](https://doc.rust-lang.org/rustc/lints/levels.html)
