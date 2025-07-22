---
title: "[Git]使用git tag為commit加入標籤"
date: "2013-11-06 12:00:00"
description: "[Git]使用git tag為commit加入標籤"
tags: [Git]
---

最近用CodePlex在控管Process Pro Extension的Source Code，比較有自己可以惡搞的git repositories，稍稍試玩了一下git tag的指令，用來為每次的版本變更打上標籤，後續比較好查閱各版本的變動，這邊隨手紀錄一下git tag指令的用法。

git tag指令它的使用方式如下：

這邊先不用一下子紀錄所有的命令列參數，實際來看例子比較好懂。假設今天我們要為當前這個commit新增一個標籤，可以直接下git tag並帶入要新增的標籤名稱，像是git tag v1.2，指定的標籤名稱就會被加在當前的commit上。

若要確認標籤是否加入成功，可以用git tag或是用git tag -l。要找尋特定的標籤的話，可以用git tag -l並帶入要搜尋的標籤關鍵字，像是git tag -l "v1.0*"。

要是之前忘了標註標籤就繼續向下開發也沒關係，git tag也可以標註之前的commit，呼叫git tag -a並帶入標籤名稱以及commit的編號，就可為指定的commit標註上指定的標籤。

若是標籤標註錯誤或已過時，可呼叫git tag -d並帶上指定的標籤名稱進行標籤的刪除動作。

這邊要特別注意到的是，像上面介紹的這樣標註在當前commit上的標籤是屬於本地的標籤，若要上到遠端我們還需要下git push origin並帶上標籤名稱，如此遠端的repositories才會有新增的標籤。

以筆者在用的CodePlex為例，若標籤有上到遠端，就可在SourceCode\History頁面看到所標註的標籤。像是剛剛筆者打上的v1.2就可在下圖中清楚地看到，這樣到時需要回憶版本間的差異與變動，或是要找回特定的版本都很容易。

若是某特定版本有出現甚麼重大Bug，平時若有標註標籤也可以讓我們很容易地找回並分支修正，再出給使用者Hotfix安裝。以筆者的例子來說，假設Process Pro Extension v1.1出現了重大Bug，而筆者因為持續的開發，所以開發支線已經跟v1.1版有很大的差距，這時就可以用git branch指令帶入新的分支名稱以及指定的標籤名稱(e.x. git branch fix/fixSomething v1.1)，用v1.1標籤那版開一個新的分支去修正。這樣聽起來git tag是不是很方便呢?!

## Link
     [Git] 版本控制: 如何使用標籤(Tag)     Git 初學筆記 - 指令操作教學    Git标签