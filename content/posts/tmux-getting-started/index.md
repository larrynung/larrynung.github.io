---
title: "tmux - Getting started"
date: "2019-03-27 07:26:06"
tags: [tmux]
---


tmux 在 Ubuntu 可透過 apt-get 安裝。  

<!-- More -->

    apt-get install tmux

![1.jpg](1.jpg)

<br/>


安裝完可查閱版本確認安裝是否正常。  

    tmux -V

![2.jpg](2.jpg)

<br/>


使用方式可帶入 --help 參數查詢。  

    tmux --help

![3.jpg](3.jpg)

<br/>


若要較詳細的使用說明，可使用 man 查閱。  

    man tmux

![4.jpg](4.jpg)

<br/>

![5.jpg](5.jpg)

<br/>


在使用上需先調用命令進入 tmux。  

    tmux

![6.jpg](6.jpg)

<br/>

![7.jpg](7.jpg)

<br/>


進入 tmux 後即可對 panel/session/window 做些管控。  

<br/>


要離開 tmux 的話調用 exit 命令即可。    

    exit

![8.jpg](8.jpg)

<br/>

![9.jpg](9.jpg)
