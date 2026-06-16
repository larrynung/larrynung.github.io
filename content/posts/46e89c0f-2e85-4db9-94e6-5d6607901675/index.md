---
title: "[Git]Stash Your Changes with git stash"
slug: "git-stash-your-changes-with-git-stash"
aliases: ["/posts/46e89c0f-2e85-4db9-94e6-5d6607901675/"]
date: "2013-11-06 12:00:00"
description: "我們在一個Branch開發著新的功能，開發到一半有時候會有中途插進來的事情要處理。像是要趕快修個Bug，或是要先建置一版給外面，抑或是要先做另一個feature之類的。但因為功能開發還沒告一段落，將做到一半的Commit進去也不太對勁，這時我們可以使用git stash將程式碼先暫存起來。"
tags: [Git]
---

我們在一個Branch開發著新的功能，開發到一半有時候會有中途插進來的事情要處理。像是要趕快修個Bug，或是要先建置一版給外面，抑或是要先做另一個feature之類的。但因為功能開發還沒告一段落，將做到一半的Commit進去也不太對勁，這時我們可以使用git stash將程式碼先暫存起來。

像是這邊筆者抽空在另外一個Branch試作一個小功能，開發到一半有工作要做了，必須要回到開發主線去做些事情，這時用git status可以看到一個檔案異動還未commit進去。

![2013-01-03_215339_thumb_1.png](/images/posts/46e89c0f-2e85-4db9-94e6-5d6607901675/2013-01-03_215339_thumb_1.png)

如同一開始所說的，因為功能尚在開發，還不到可以commit進去的程度，因此這邊筆者使用git stash將之暫存起來。

![2013-01-03_215456_thumb_1.png](/images/posts/46e89c0f-2e85-4db9-94e6-5d6607901675/2013-01-03_215456_thumb_1.png)

下完git stash暫存後，我們可以再次叫用git status查看，可以發現之前可以查看到有檔案異動，但是現在卻都沒了。

![2013-01-03_215523_thumb.png](/images/posts/46e89c0f-2e85-4db9-94e6-5d6607901675/2013-01-03_215523_thumb.png)

這邊可以再下git stash list查驗一下是否有把變動暫存，叫用後可以看到Git會吐回像下圖一樣的提示字樣，告知暫存的編號以及暫存的是哪個branch的變動。

![2013-01-03_215555_thumb.png](/images/posts/46e89c0f-2e85-4db9-94e6-5d6607901675/2013-01-03_215555_thumb.png)

確定有將變動暫存起來後，我們就可以用git checkout先切到別的branch去處理一些事情。當處理完畢要再繼續開發時，我們可以再下git stash pop將它取出。

![2013-01-03_215629_thumb.png](/images/posts/46e89c0f-2e85-4db9-94e6-5d6607901675/2013-01-03_215629_thumb.png)
