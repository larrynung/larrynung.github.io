---
title: "Vim - Display line numbers"
date: "2018-10-20 23:56:45"
description: "Vim 預設 Line number 是關閉的。 如有需要將開啟 Vim 的設定檔。 vi ~/.vimrc 在設定檔內加上設定開啟 Line number。 set number 再次進入 Vim 就會看到 Line number 已被開啟。"
tags: [Vim]
---

Vim 預設 Line number 是關閉的。

![1.jpg](1.jpg)

如有需要將開啟 Vim 的設定檔。

vi ~/.vimrc

![2.jpg](2.jpg)

在設定檔內加上設定開啟 Line number。

set number

![3.jpg](3.jpg)

再次進入 Vim 就會看到 Line number 已被開啟。

![4.jpg](4.jpg)

如果只是暫時要開關 Line number，可以不用修改到設定檔。

可以直接輸入命令暫時開啟。

set number

![5.jpg](5.jpg)

set nu

![6.jpg](6.jpg)

或是直接輸入命令暫時關閉。

set nonumber

![7.jpg](7.jpg)

set nonu

![8.jpg](8.jpg)

Link
----
* [Display line numbers](http://vim.wikia.com/wiki/Display_line_numbers)