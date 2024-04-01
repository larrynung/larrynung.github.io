---
title: "'HomeBrew - Error: homebrew-core is a shallow clone.'"
date: "2021-01-05 00:04:10"
tags: [HomeBrew]
---


使用 HomeBrew 如果出現 "Error: homebrew-core is a shallow clone." 錯誤。  

<!-- More -->

![1.png](1.png)

</br>


可照著命令列的提示帶入。  

    git -C /usr/local/Homebrew/Library/Taps/homebrew/homebrew-core fetch --unshallow
    git -C /usr/local/Homebrew/Library/Taps/homebrew/homebrew-cask fetch --unshallow

![2.png](2.png)

</br>


即可修復該問題。  

![3.png](3.png)
