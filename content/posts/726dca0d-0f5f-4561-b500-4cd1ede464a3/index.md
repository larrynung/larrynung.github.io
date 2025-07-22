---
title: "How to fix HttpListener Access Denied"
date: "2013-11-06 12:00:00"
description: "How to fix HttpListener Access Denied"
---最近開發中的專案程式發生了一些狀況，有的時候安裝完運行就會直接掛掉，無論怎麼重開都無法修復，連用程式去運行除錯也會跟著發生例外錯誤。若是用管理員權限去運行程式卻又可以正常運作，或是將它移除再安裝也有可能就修復了。唯一的線索就是當錯誤發生時用程式除錯可看到問題是在HttpListener.Prefixes.Add這邊會有存取被拒的問題。

這樣的線索我還是有點猜不透，若是存取被拒應該是always發生的，怎麼會有的時候就加的進去？上網查到也有人碰到類似的問題，依據HttpListener Access Denied c# windows 7這篇的討論，看來存取被拒滿像是UAC造成的，要避免這樣的問題只有下netsh http add urlacl命令跟系統註冊，像是下面這樣：

註冊後可再下netsh http show urlacl查閱是否已經跟系統註冊成功。

註冊成功可以在裡面看到剛註冊的url位置。

註冊完畢後，HttpListener.Prefixes.Add就不會有存取被拒的問題了。

若是想要取消註冊，可以用netsh http delete urlacl命令。

這邊要注意的是，netsh這些命令因為要跟系統註冊，還是需要管理者權限，但是我們可以將這動作提到安裝程式這邊去做，由安裝程式要求管理者權限就好了。若是安裝包是用wix去做的，可像下面這樣設定自訂動作：
...

...

...
= 601]]>
= 601]]>
...

...

這樣安裝程式就會在安裝時順便幫我們去做這些處理。

## Link

HttpListener Access Denied c# windows 7

add urlacl (Windows)

delete urlacl (Windows)

設定 HTTP 和 HTTPS