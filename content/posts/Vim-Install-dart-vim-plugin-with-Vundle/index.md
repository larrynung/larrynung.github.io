---
title: "Vim - Install dart-vim-plugin with Vundle"
date: "2019-06-21 16:17:07"
tags: [Vim, Dart]
---


使用 Vim 撰寫 Dart，可透過 Vundle 安裝 dart-vim-plugin 套件。  

<!-- More -->

</br>


開啟 ~/.vimrc 檔。  

    vim ~/.vimrc

</br>


設定 Vundle 與 dart-vim-plugin。  

```
...
set nocompatible
filetype off                               
set rtp+=~/.vim/bundle/Vundle.vim

call vundle#begin()
Plugin 'VundleVim/Vundle.vim'
Plugin 'dart-lang/dart-vim-plugin'
call vundle#end()
filetype plugin indent on
...
```

![1.png](1.png)

</br>


然後調用命令進行 Vim plugin 的安裝。  

    vim +PluginInstall +qall

![2.png](2.png)

</br>


![3.png](3.png)

</br>


安裝好後 Dart 程式碼會支援 Highlight。  

</br>


也支援排版的功能。  

    :DartFmt

![4.png](4.png)

</br>


![5.png](5.png)

</br>


甚至是程式碼的分析。  

    :DartAnalyzer

![6.png](6.png)

</br>


![7.png](7.png)
