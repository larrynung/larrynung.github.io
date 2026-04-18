---
title: "MediaWiki - Unlock upload file size limitation"
date: "2014-06-15 00:07:00"
description: "MediaWiki - Unlock upload file size limitation"
tags: [MediaWiki ]
---

MediaWiki 在檔案上傳這邊預設是有 2MB 的限制在。

![/images/posts/MediaWikiUnlickFileLimit/1.png](/images/posts/MediaWikiUnlickFileLimit/1.png)

若要對此設定值做些調整，我們可以開啟 `Php.ini`。

![/images/posts/MediaWikiUnlickFileLimit/2.png](/images/posts/MediaWikiUnlickFileLimit/2.png)

調整 `upload_max_filesize` 設定值。

![/images/posts/MediaWikiUnlickFileLimit/3.png](/images/posts/MediaWikiUnlickFileLimit/3.png)

以及調整 `post_max_size` 設定值。

![/images/posts/MediaWikiUnlickFileLimit/4.png](/images/posts/MediaWikiUnlickFileLimit/4.png)

調整完存檔退出，檔案上傳這邊就會生效。

![/images/posts/MediaWikiUnlickFileLimit/5.png](/images/posts/MediaWikiUnlickFileLimit/5.png)