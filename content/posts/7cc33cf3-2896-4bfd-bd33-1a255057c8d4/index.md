---
title: "如何在Linux環境下設定命令別名"
date: "2013-11-06 12:00:00"
description: "如何在Linux環境下設定命令別名"
---

Linux系統內建許多的命令列指令，這些指令多半很小，且專注於解決特定的問題，搭配Linux特有的管線命令，命令間能因此而有某種程度的交流，進而完成許多的動作 。 

但有的時後有些命令列帶的參數我們很常會重複使用，或是命令寫起來很複雜，亦或是純粹對命令的名稱很感冒，這時我們就可以使用alias來設定命令別名。 

像是在terminal下呼叫命令alias la='ls -la'設定別名la，這樣呼叫la就等同於呼叫ls -la。 

很好玩的是，alias設定別名也可以用來取代現有的命令。像是呼叫命令alias ls='ls --color=auto'，這樣設定別名之後在下ls就等同於呼叫命令ls --color=auto，查詢的結果會帶上色彩。此外我們也可以直接叫用alias命令來查閱目前已經設定的命令別名，或是叫用unalias將別名取消。 

不過這樣的設法只能在當次登入的session生效，換個Terminal或是重啟就會發現剛剛我們所加入的別名並無法使用。若要別名每次使用Terminal都能生效，我們可以修改.bashrc檔案，在裡面加入我們想要使用的別名設定。

## Link
     第十一章、認識與學習 BASH    30 Handy Bash Shell Aliases For Linux / Unix / Mac OS X