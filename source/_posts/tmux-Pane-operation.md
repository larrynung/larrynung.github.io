---
title: tmux - Pane operation
date: 2019-03-29 22:01:27
tags: [tmux]
---

tmux 的 Pane 可將一個 Terminal 視窗切成多個區塊。  

<!-- More -->

<br/>


使用前先進入 tmux。

    tmux

{% asset_img 1.jpg %}

<br/>


要進行水平切割可按熱鍵 Ctrl + b，再按下 %。

{% asset_img 2.jpg %}

<br/>


要進行垂直切割可按熱鍵 Ctrl + b，再按下 "。

{% asset_img 3.jpg %}

<br/>


要在不同的 Pane 切換，可按下熱鍵 Ctrl + b，再按下對應的方向鍵。  

{% asset_img 4.jpg %}

<br/>


要將當前 Pane 關閉，可輸入 exit 命令，或是按下熱鍵 Ctrl + b，再按下 x。  

{% asset_img 5.jpg %}

<br/>


{% asset_img 6.jpg %}

<br/>


熟悉 Pane 的操作，我們就可以依不同的使用情境做適當的切割，讓 Terminal 的使用上更方便。

<br/>


像是一邊運行命令一邊查閱資源使用的狀況。  

{% asset_img 7.jpg %}
