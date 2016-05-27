---
layout: post
title: "Octopress - Notify search engine"
date: 2013-12-13 23:00:00
comments: true
categories: [Octopress]
keywords: "Octopress"
description: "Octopress - Notify search engine"
---

sitemap.xml 是 Google 提出來的標準，以 XML 為格式，紀錄著網頁的連結與最後修改的時間。  

<!--More-->

{% img /images/posts/OctopressNotifySearchEngine/1.png %}


如果要即時通知搜尋引擎更新，而不等待搜尋引擎自行檢測，我們可以主動將 sitmap.xml 上傳給搜尋引擎。  

若是想要在 Octopress 中做這動作的話，我們可以編輯 Octopress 的 Rakefile 檔案，將下面腳本加入。  

{% codeblock lang:ruby %}
desc 'Ping pingomatic'
task :pingomatic do
  begin
    require 'xmlrpc/client'
    puts '* Pinging ping-o-matic'
    XMLRPC::Client.new('rpc.pingomatic.com', '/').call('weblogUpdates.extendedPing', 'Level Up' , 'http://larrynung.github.io', 'http://larrynung.github.io/atom.xml')
  rescue LoadError
    puts '! Could not ping ping-o-matic, because XMLRPC::Client could not be found.'
  end
end

desc 'Notify Google of the new sitemap'
task :sitemapgoogle do
  begin
    require 'net/http'
    require 'uri'
    puts '* Pinging Google about our sitemap'
    Net::HTTP.get('www.google.com', '/webmasters/tools/ping?sitemap=' + URI.escape('http://larrynung.github.io/sitemap.xml'))
  rescue LoadError
    puts '! Could not ping Google about our sitemap, because Net::HTTP or URI could not be found.'
  end
end

desc 'Notify Bing of the new sitemap'
task :sitemapbing do
  begin
    require 'net/http'
    require 'uri'
    puts '* Pinging Bing about our sitemap'
    Net::HTTP.get('www.bing.com', '/webmaster/ping.aspx?siteMap=' + URI.escape('http://larrynung.github.io/sitemap.xml'))
  rescue LoadError
    puts '! Could not ping Bing about our sitemap, because Net::HTTP or URI could not be found.'
  end
end

desc "Notify various services about new content"
task :notify => [:pingomatic, :sitemapgoogle, :sitemapbing] do
end
{% endcodeblock %}

腳本中發送給搜尋引擎那邊的站名、網站位置、RSS位置、以及 sitemap 位置都要替換成自己的。  

腳本加入後，我們可以透過 Rake 命令下去通知搜尋引擎

像是通知 ping-o-matic ，可以這樣下：

    rake pingomatic


要通知 Google 更新的話：

    rake sitemapgoogle


通知 Bing 更新:

    rake sitemapbing


一次要通知上面所有的話：

    rake notify


若想要在發佈的同時去通知搜尋引擎，這邊也可以開啟 Rakefile 檔案進行編輯，將本來的 deploy 任務更名，再造個新的 deploy 任務，該任務叫用時會依序叫用本來的 deploy 任務以及 notify 任務。  

像是下面這樣：  

{% codeblock lang:ruby %}
desc "Default deploy task"
task :deploy => [:deploy1, :notify] do
end

desc "Default deploy task"
task :deploy1 do
  # Check if preview posts exist, which should not be published
  if File.exists?(".preview-mode")
    puts "## Found posts in preview mode, regenerating files ..."
    File.delete(".preview-mode")
    Rake::Task[:generate].execute
  end

  Rake::Task[:copydot].invoke(source_dir, public_dir)
  Rake::Task["#{deploy_default}"].execute
end
{% endcodeblock %}


這樣修改後以後叫用 `rake deploy` 就會自動在部屬後通知搜尋引擎。


Link
----
* [Octopress Customizations - Ewal.net](http://www.ewal.net/2012/09/08/octopress-customizations/)
* [Octopress 通知搜尋引擎新文章發佈](http://blog.eavatar.com/post/2013/06/octopress-ping-search-engines/)
* [Octopress 的 sitemap.xml](http://blog.ianwu.tw/blog/2012/07/26/intro-octopress-seo/)
* [SEO 搜尋引擎最佳化](http://blog.ianwu.tw/blog/2008/11/23/SEO-Optimization/)
* [Sitemaps - Wiki](http://en.wikipedia.org/wiki/Sitemaps)
