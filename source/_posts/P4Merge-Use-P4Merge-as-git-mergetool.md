---
title: P4Merge - Use P4Merge as git mergetool
date: 2017-09-19 23:23:01
tags: [P4Merge, Git]
---

要將 P4Merge 與 Git 整合，使用 P4Merge 去做 Merge，可以加入 Merge tool 設定。   

<!-- More -->

    git config --global merge.tool p4merge

{% asset_img 1.png %}

<br/>


設定 P4Merge 檔案的位置。  

    git config --global mergetool.p4merge.path [P4MergeFileLocation]

{% asset_img 2.png %}

<br/>


或是直接開啟 global configuration file 編輯也可以。  

    [merge]
    	tool = p4merge
    [mergetool "p4merge"]
    	path = C:\\Program Files\\Perforce\\p4merge.exe

{% asset_img 3.png %}

<br/>


設定好後就可以使用 P4Merge 在 git 做 Merge。  

    git mergetool

{% asset_img 4.png %}

<br/>


{% asset_img 5.png %}

<br/>


{% asset_img 6.png %}

<br/>


Link
----
* [Setup p4merge as difftool and mergetool on Windows](https://gist.github.com/dgoguerra/8258007)
* [Git for Windows tip: Use P4Merge as mergetool – danlimerick](https://danlimerick.wordpress.com/2011/06/19/git-for-window-tip-use-p4merge-as-mergetool/)
