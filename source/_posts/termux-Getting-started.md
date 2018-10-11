---
title: termux - Getting started
date: 2018-10-11 17:08:50
tags: [termux]
---

要使用 termux，首先需透過 Google Play 商店或是 F-Droid 下載安裝。  

<!-- more -->

</br>


安裝後點選 termux 圖示啟動。  

{% asset_img 1.jpg %}

</br>


termux 啟動後會看到如下終端機畫面，終端機畫面上會提供一些參考的資源，以及套件管理的常用操作。  

{% asset_img 2.jpg %}

</br>


為了使用較新的套件，這邊可先進行更新。  

    apt update && apt upgrade

{% asset_img 3.jpg %}

</br>


為了便於使用 termux 在操作上也做了些巧思，像是長按螢幕可叫出選單，便於複製貼上。

{% asset_img 4.jpg %}

</br>


MORE... 內也有些功能可供使用，像是 Kill process 可終止目前的 process (輸入 exit 離開也可以)、Help 可直接開啟 termux wiki。  

{% asset_img 5.jpg %}

</br>


上音量鍵是特殊鍵，可做的功能有...  

'''
Volume Up+E → Escape key
Volume Up+T → Tab key
Volume Up+1 → F1 (and Volume Up+2 → F2, etc)
Volume Up+0 → F10
Volume Up+B → Alt+B, back a word when using readline
Volume Up+F → Alt+F, forward a word when using readline
Volume Up+X → Alt+X
Volume Up+W → Up arrow key
Volume Up+A → Left arrow key
Volume Up+S → Down arrow key
Volume Up+D → Right arrow key
Volume Up+L → | (the pipe character)
Volume Up+H → ~ (the tilde character)
Volume Up+U → _ (underscore)
Volume Up+P → Page Up
Volume Up+N → Page Down
Volume Up+. → Ctrl+\ (SIGQUIT)
Volume Up+V → Show the volume control
Volume Up+Q → Show extra keys view
'''

</br>


像是上音量鍵加按 e，等同按下 ESC。  

</br>


上音量鍵加按 1，等同按下 F1。  

</br>


上音量鍵加按 q，可開關 termux 提供的額外鍵盤列，常用的確鍵盤功能都會在上面，像是 ESC、HOME、END、TAB 等，可以考慮直接安裝其它套鍵盤軟體，或是使用藍芽鍵盤，這樣就不一定要開啟。  

{% asset_img 6.jpg %}

</br>


下音量鍵是 CTRL，可做的功能有...

'''
Ctrl+A → Move cursor to the beginning of line
Ctrl+C → Abort (send SIGINT to) current process
Ctrl+D → Logout of a terminal session
Ctrl+E → Move cursor to the end of line
Ctrl+K → Delete from cursor to the end of line
Ctrl+L → Clear the terminal
Ctrl+Z → Suspend (send SIGTSTP to) current process
Ctrl+alt+C → Open new session (only work in Hacker's Keyboard)
'''

</br>


像是下音量鍵加按 c，等同按下 CTRL + C。  

</br>


如果要起多個 session 操作或是要叫出鍵盤，可在 termux 上從最左側往右滑，開啟左側選單。  

{% asset_img 7.jpg %}

</br>


按下 KEYBOARD 會帶出鍵盤。  

</br>


按下 NEW SESSION 會開啟新的 session，session 的切換可直接點選上方的 session，若有需要也可以在上方的 session 長按，幫 session 命名。  

</br>


Link
----
* [Touch Keyboard](https://wiki.termux.com/wiki/Touch_Keyboard)
