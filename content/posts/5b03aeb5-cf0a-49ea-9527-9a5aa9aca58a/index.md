---
title: "Using P4Merge with SVN"
date: "2013-11-06 12:00:00"
description: "前面在P4Merge - Visual Merge and Diff Tools這篇稍微介紹了一下P4Merge的使用，這邊進一步若是要將P4Merge與TortiseSVN整合，使用P4Merge去做版控的比對或是合併，我們可以開啟TortiseSVN的設定對話框。"
tags: [P4Merge]
---

前面在P4Merge - Visual Merge and Diff Tools這篇稍微介紹了一下P4Merge的使用，這邊進一步若是要將P4Merge與TortiseSVN整合，使用P4Merge去做版控的比對或是合併，我們可以開啟TortiseSVN的設定對話框。

![ScreenClip.2_thumb.jpg](/images/posts/5b03aeb5-cf0a-49ea-9527-9a5aa9aca58a/ScreenClip.2_thumb.jpg)

將左側節點切到 [External/Diff Viewer] 節點去設定比對的部分。因為要改用外部程式去取代預設的比對程式，所以這邊要將選取由TortiseMerge切換為External，並在下方的輸入框指定外部程式要如何叫用。

以P4Merge來說，它的命令列使用方式如下：

```xml
p4merge [options] left right
p4merge [options] [base] left right
p4merge [options] [base] left right [merge]
p4merge -h Print this message and exit
p4merge -V Print the version and exit
```

所以要進行比對時，我們可以直接在主檔後帶入要進行比對的兩個檔案。

因此SVN這邊的比對設定，我們將之帶入%base與%mine這兩個參數，指定比對目前SVN上的檔案以及本地修改的檔案就可以了。

設定上就像是下面這個樣子:

"C:\Program Files\Perforce\p4merge.exe" %base %mine
![ScreenClip_thumb.jpg](/images/posts/5b03aeb5-cf0a-49ea-9527-9a5aa9aca58a/ScreenClip_thumb.jpg)

接著將左側節點切到 [External/Merge Tool] 節點去設定合併的部分， 一樣將選取由TortiseMerge切換為External，輸入框帶入P4Merge主檔位置，以及%base、%theirs、%mine、%merged這幾個參數，用以指定當初修改的檔案、 SVN上目前的檔案、本地修改的檔案、以及合併後的檔案 。

設定上就像是下面這個樣子:

"C:\Program Files\Perforce\p4merge.exe" %base %theirs %mine %merged
![ScreenClip.3_thumb.jpg](/images/posts/5b03aeb5-cf0a-49ea-9527-9a5aa9aca58a/ScreenClip.3_thumb.jpg)

到這邊設定就完成了，實際在用SVN去比對或是合併，應該會由預設的TortiseMerge程式改為P4Merge 。
