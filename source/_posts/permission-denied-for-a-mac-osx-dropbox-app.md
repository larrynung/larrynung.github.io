---
layout: post
title: "Permission denied for a Mac OSX Dropbox app"
date: 2015-09-12 00:00:00
comments: true
tags: [Mac, Dropbox]
keywords: "Mac, Dropbox"
description: "Permission denied for a Mac OSX Dropbox app"
---

最近 Mac 的 Dropbox 突然出問題，可能是前陣子搬動家目錄所導致，想將他進行重裝還原，但過程中總是會跟我要求提升權限：

<!-- More -->

<br/>


{% img /images/posts/DropboxPermissionDenied/1.png %}


輸入密碼後權限好像都沒取道，怎樣都出現權限錯誤的問題。  

{% img /images/posts/DropboxPermissionDenied/2.png %}

<br/>


查了一下要在 Terminal 下下列指令：  

{% codeblock lang:bash %}
mv ~/.dropbox ~/.Trash
sudo mv /Library/DropboxHelperTools ~/.Trash
```

<br/>

指令下完後重新安裝就可以了。  

<br/>

Link
----
* [Dropbox asking for permissions to wrong folder after changing account name - Ask Different](http://apple.stackexchange.com/questions/128551/dropbox-asking-for-permissions-to-wrong-folder-after-changing-account-name)
* [IPG EMEA Deployment Knowledge Base: After migrating a Mac user's profile, Dropbox fails to open: keeps asking for permissions](http://emeadeployment.blogspot.tw/2015/03/after-migrating-mac-users-profile.html)
