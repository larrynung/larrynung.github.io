---
title: tmux - Getting started
date: 2019-03-27 07:26:06
tags: [tmux]
---

tmux 在 Ubuntu 可透過 apt-get 安裝。  

<!-- More -->

    apt-get install tmux

{% asset_img 1.jpg %}

<br/>


安裝完可查閱版本確認安裝是否正常。  

    tmux -V

{% asset_img 2.jpg %}

<br/>


使用方式可帶入 --help 參數查詢。  

    tmux --help

{% asset_img 3.jpg %}

<br/>


若要較詳細的使用說明，可使用 man 查閱。  

    man tmux

{% asset_img 4.jpg %}

<br/>

{% asset_img 5.jpg %}

<br/>


在使用上需先調用命令進入 tmux。  

    tmux

{% asset_img 6.jpg %}

<br/>

{% asset_img 7.jpg %}

<br/>


進入 tmux 後即可對 panel/session/window 做些管控。  

<br/>


要離開 tmux 的話調用 exit 命令即可。    

    exit

{% asset_img 8.jpg %}

<br/>

{% asset_img 9.jpg %}
