---
layout: post
title: "Octopress - SEO for Octopress website"
date: 2013-11-21 23:13:00
comments: true
categories: [Octopress, SEO] 
keywords: "Octopress, SEO"
description: "SEO for Octopress website"
---

Octopress在SEO這塊預設就處理的滿好的了，但仍舊是有可以優化的地方，像是發佈文章後Octopress會為該文章頁面添加meta description，內容為文章內文的前150個字，而首頁則是以最上面的文章，也就是最後一篇文章的前150個字符來做為meta description。這跟我們的預期有些出入，這邊介紹怎樣將之作些調整，並加入meta keyword來改善SEO。  

<!--More-->

Meta data for every blog
------------------------------------

在文章的開頭這邊我們加入keywords與description這兩個參數，文章撰寫時就同時決定該文章適合的ketwords與description。

    ---
    layout: post
    title: "Octopress - SEO for Octopress website"
    date: 2013-11-21 23:13:00
    categories: [Octopress, SEO]

    keywords: "Octopress, SEO"
    description: "SEO for Octopress website"
    ---


這邊也可以將Rakefile開啟，修改new_post時所產生的文章範本，讓產生文章的同時就幫我們預留好keywords與description這兩個參數。

{% codeblock lang:rb %}
# usage rake new_post[my-new-post] or rake new_post['my new post'] or rake new_post (defaults to "new-post")
desc "Begin a new post in #{source_dir}/#{posts_dir}"
task :new_post, :title do |t, args|
  if args.title
    title = args.title
  else
    title = get_stdin("Enter a title for your post: ")
  end
  raise "### You haven't set anything up yet. First run `rake install` to set up an Octopress theme." unless File.directory?(source_dir)
  mkdir_p "#{source_dir}/#{posts_dir}"
  filename = "#{source_dir}/#{posts_dir}/#{Time.now.strftime('%Y-%m-%d')}-#{title.to_url}.#{new_post_ext}"
  if File.exist?(filename)
    abort("rake aborted!") if ask("#{filename} already exists. Do you want to overwrite?", ['y', 'n']) == 'n'
  end
  puts "Creating new post: #{filename}"
  open(filename, 'w') do |post|
    post.puts "---"
    post.puts "layout: post"
    post.puts "title: \"#{title.gsub(/&/,'&amp;')}\""
    post.puts "date: #{Time.now.strftime('%Y-%m-%d %H:%M')}"
    post.puts "comments: true"
    post.puts "categories: "
    post.puts "keywords: "
    post.puts "description: "
    post.puts "---"
  end
end
{% endcodeblock %}


Meta data for home page
-----------------------

首頁這邊一樣需要加入keywords與description參數，開啟_config.yaml檔將keywords與description設定好。

{% codeblock lang:yaml %}
# ----------------------- #
#      Main Configs       #
# ----------------------- #

url: http://larrynung.github.io
title: Level Up
subtitle: 謙卑學習，持之以恆，才能不斷的Level Up
author: Larry Nung
simple_search: http://google.com/search
description: "Level Up Blog (http://larrynung.github.io)"
keywords: "C#, VB.Net, .NET, Python, WPF, C++/CLI, C++/0x, UML, LINQ, 網樂通"
{% endcodeblock %}


Dynamic inject meta data
------------------------

文章與首頁的 Meta data 都設定好了，這邊我們要將 source/_includes/head.html 開啟作些修改，將本來的meta description與meta keyword的處理用下面這段程式替換：

{% codeblock lang:rb %}
{% capture description %}{% if page.description %}{{ page.description }}{% elsif site.description %}{{ site.description }}{% else %}{{ content | raw_content }}{% endif %}{% endcapture %}
<meta name="description" content="{{ description | strip_html | condense_spaces | truncate:150 }}" />

{% capture keywords %}{% if page.keywords %}{{ page.keywords }}{% elsif site.keywords %}{{ site.keywords }}{% endif %}{% endcapture %}
<meta name="keywords" content="{{ keywords | strip_html | condense_spaces }}" />
{% endcodeblock %}


像是下面這樣

{% img /images/posts/OctopressSEO/1.png %}


Generate & Preview & Deploy
---------------------------

都完成後產生頁面並啟用預覽服務

    rake generate
    rake preview


接著開啟瀏覽器連至 127.0.0.1:4000 檢視網頁原始碼，我們會發現在首頁這邊，meta description 與 meta keywords 已經變成我們設在 _config.yaml 內的 description 與 keywords

{% img /images/posts/OctopressSEO/2.png %}


在文章這邊也變成我們在撰寫文章時所設定的

{% img /images/posts/OctopressSEO/3.png %}


最後老樣子呼叫命令發佈

    rake deploy


一樣要將 Source Commit 回 Github

    git add .
    git commit -a -m "SEO Adjust"
    git push


Link
----
* [Octopress 的 SEO 优化](http://havee.me/internet/2013-01/octopress-seo.html)
* [SEO for Octopress Websites](http://xit0.org/2013/05/seo-for-octopress-websites/)
* [Octopress中的SEO](http://codemacro.com/2012/09/06/octopress-seo/)
* [SEO for Octopress,Heroku](http://www.yatishmehta.in/seo-for-octopress)
* [[轉載][翻譯]Octopress中的搜索引擎優化](http://dinever.com/blog/2013/01/23/zhuan-zai-fan-yi-octopresszhong-de-seo-youhua/)
