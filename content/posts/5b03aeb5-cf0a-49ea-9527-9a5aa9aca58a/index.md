---
title: "Using P4Merge with SVN"
date: "2013-11-06 12:00:00"
description: "Using P4Merge with SVN"
tags: [P4Merge]
---

<p>
	前面在P4Merge - Visual Merge and Diff Tools這篇稍微介紹了一下P4Merge的使用，這邊進一步若是要將P4Merge與TortiseSVN整合，使用P4Merge去做版控的比對或是合併，我們可以開啟TortiseSVN的設定對話框。</p>
<p>
	<img alt="ScreenClip.2" border="0" height="260" src="\images\posts\5b03aeb5-cf0a-49ea-9527-9a5aa9aca58a\ScreenClip.2_thumb.jpg" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="460" /></p>
<p>
	 </p>
<p>
	將左側節點切到 [External/Diff Viewer] 節點去設定比對的部分。因為要改用外部程式去取代預設的比對程式，所以這邊要將選取由TortiseMerge切換為External，並在下方的輸入框指定外部程式要如何叫用。</p>
<p>
	 </p>
<p>
	以P4Merge來說，它的命令列使用方式如下：</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:1fc06df0-01fc-4513-b42b-046557cf537e" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="xml" name="code">
p4merge [options] left right
p4merge [options] [base] left right
p4merge [options] [base] left right [merge]
p4merge -h Print this message and exit
p4merge -V Print the version and exit </pre>
</div>
<p>
	 </p>
<p>
	所以要進行比對時，我們可以直接在主檔後帶入要進行比對的兩個檔案。</p>
<p>
	 </p>
<p>
	因此SVN這邊的比對設定，我們將之帶入%base與%mine這兩個參數，指定比對目前SVN上的檔案以及本地修改的檔案就可以了。</p>
<p>
	 </p>
<p>
	設定上就像是下面這個樣子:</p>
    "C:\Program Files\Perforce\p4merge.exe" %base %mine 
	<img alt="ScreenClip" border="0" height="432" src="\images\posts\5b03aeb5-cf0a-49ea-9527-9a5aa9aca58a\ScreenClip_thumb.jpg" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="644" /></p>
<p>
	 </p>
<p>
	接著將左側節點切到 [External/Merge Tool] 節點去設定合併的部分， 一樣將選取由TortiseMerge切換為External，輸入框帶入P4Merge主檔位置，以及%base、%theirs、%mine、%merged這幾個參數，用以指定當初修改的檔案、 SVN上目前的檔案、本地修改的檔案、以及合併後的檔案 。</p>
<p>
	 </p>
<p>
	設定上就像是下面這個樣子:</p>
    "C:\Program Files\Perforce\p4merge.exe" %base %theirs %mine %merged
	<img alt="ScreenClip.3" border="0" height="432" src="\images\posts\5b03aeb5-cf0a-49ea-9527-9a5aa9aca58a\ScreenClip.3_thumb.jpg" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="644" /></p>
<p>
	 </p>
<p>
	到這邊設定就完成了，實際在用SVN去比對或是合併，應該會由預設的TortiseMerge程式改為P4Merge 。</p>
