---
title: "RubyGems"
date: "2013-11-06 12:00:00"
description: "RubyGems是Ruby上的套件管理工具，透過RubyGems我們可以很容易的呼叫命令去搜尋、安裝、與管理Ruby上的套件。若是安裝Ruby 1.9以後的版本，或是電腦中有安裝RVM的就會內建RubyGems可供使用，不然就要自行另外安裝。"
tags: [Ruby]
---

RubyGems是Ruby上的套件管理工具，透過RubyGems我們可以很容易的呼叫命令去搜尋、安裝、與管理Ruby上的套件。若是安裝Ruby 1.9以後的版本，或是電腦中有安裝RVM的就會內建RubyGems可供使用，不然就要自行另外安裝。

安裝這邊若有需要可參閱Installing RubyGems或是[函式庫 - Ruby](http://www.ruby-lang.org/zh_TW/libraries/)。

安裝完後，我們就可以開始使用RubyGems來做些動作。像是呼叫命令gem list，可以查閱在本地中安裝了那些Ruby的套件。

![screenshot(95)_thumb.png](/images/posts/d2f8c8d8-474d-4356-afe1-83740866086f/screenshot%2895%29_thumb.png)

gem list -r命令可查閱RubyGems有提供那些套件可供安裝。

gem list -r [package name] (e.x. gem list -r vagrant)命令可查閱RubyGems是否有提供指定的套件可供安裝。

![screenshot(99)_thumb.png](/images/posts/d2f8c8d8-474d-4356-afe1-83740866086f/screenshot%2899%29_thumb.png)

gem list -ra [package name] (e.x. gem list -ra vagrant)命令可進一步查閱RubyGems提供的指定套件有哪些版本可供安裝，而不是像gem list -r [package name]命令這樣只秀出最新的版本，當有需要找尋是否提供舊版套件時可以叫用。

![screenshot(100)_thumb.png](/images/posts/d2f8c8d8-474d-4356-afe1-83740866086f/screenshot%28100%29_thumb.png)

gem install [package name] (e.x. gem install vagrant)命令可安裝指定的套件至本機系統中。

![screenshot(94)_thumb.png](/images/posts/d2f8c8d8-474d-4356-afe1-83740866086f/screenshot%2894%29_thumb.png)

gem install -v [version] [package name] (e.x. gem install -v 1.0.6 vagrant)命令可安裝特定版本的指定套件至本機系統中。

![screenshot(101)_thumb.png](/images/posts/d2f8c8d8-474d-4356-afe1-83740866086f/screenshot%28101%29_thumb.png)

gem uninstall [package name] (e.x. gem uninstall vagrant)命令可將指定套件至本機系統中移除。

![screenshot(93)_thumb.png](/images/posts/d2f8c8d8-474d-4356-afe1-83740866086f/screenshot%2893%29_thumb.png)

gem update --system命令可更新本機所安裝的RubyGems版本。

![screenshot(103)_thumb.png](/images/posts/d2f8c8d8-474d-4356-afe1-83740866086f/screenshot%28103%29_thumb.png)

gem cleanup命令可移除舊的或是重複安裝的RubyGems版本。

![screenshot(102)_thumb.png](/images/posts/d2f8c8d8-474d-4356-afe1-83740866086f/screenshot%28102%29_thumb.png)

## Link

* [函式庫 - Ruby](http://www.ruby-lang.org/zh_TW/libraries/)
* [RubyGems─管理你的紅寶石](http://www.openfoundry.org/tw/tech-column/8534-rubygems-manage-your-gems)
* [Rubygems 套件管理工具| ihower { blogging }](http://ihower.tw/blog/archives/4496)
* [gem cleanup 幫你清除重複安裝的 rubygem](http://wildjcrt.pixnet.net/blog/post/28146099-gem-cleanup-helps-you-cleaning-older-versions-gems)
