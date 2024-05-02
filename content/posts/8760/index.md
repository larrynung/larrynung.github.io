---
title: "[Software]快速清除SVN控管"
date: "2009-06-10 09:14:31"
description: "[Software]快速清除SVN控管"
tags: [Software]
---

<p>在使用SVN做檔案控管時，SVN會在專案目錄下新增個.svn目錄。</p><p><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" width="86" height="54" src="\images\posts\8760\image_thumb_2.png" /></p><p> </p><p>該目錄內記錄著SVN控管所需的資訊。</p><p>當我們需要把專案的SVN控管給取消時，最笨的作法是我們必需一層層瀏覽專案目錄，並把專案目錄下的.svn目錄全部給砍掉。</p><p>較好的作法是，我們可以撰寫個副檔名為reg的登錄檔。檔案內容如下：</p><div style="width: 561px; height: 165px; overflow: auto"><div class="csharpcode"><pre class="alt">
Windows Registry Editor Version 5.00 </pre><pre>
 </pre><pre class="alt">
[HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Folder\shell\DeleteSVN]</pre><pre>
@="Delete SVN Folders" </pre><pre class="alt">
 </pre><pre>
[HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Folder\shell\DeleteSVN