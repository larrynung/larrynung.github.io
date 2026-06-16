---
title: "Octopress - Add Linkedin profile link with Octoflat theme"
date: "2013-12-21 21:59:00"
description: "Octoflat Theme 預設就有支援 Linkedin Profile 的連結，只要在 _config.yml 設定檔中設定 linkedin_user，將 Linkedin User ID 設上去就可以了。"
tags: [Octopress]
---

Octoflat Theme 預設就有支援 Linkedin Profile 的連結，只要在 _config.yml 設定檔中設定 `linkedin_user`，將 Linkedin User ID 設上去就可以了。

![1.png](/images/posts/OctopressOctoflatLinkedinProfile/1.png)

呼叫命令產生靜態網頁並啟用預覽：

rake generate
rake preview

我們可以看到在部落格的右上方會多出 Linkedin 的 Icon。

![2.png](/images/posts/OctopressOctoflatLinkedinProfile/2.png)

點擊該 Icon，沒意外的話應該可以看到 Linkedin 的 Profile 頁面。

但是筆者看到的畫面卻是...

![3.png](/images/posts/OctopressOctoflatLinkedinProfile/3.png)

因為 Octoflat 他的 Linkedin Profile 位置是設成 `http://www.linkedin.com/in/[UserID]`，而 Linkedin Profile 的位置看起來是有很多不同的可能，像是筆者的 Profile 位置就不是 Octoflat 預期的那樣。

![4.png](/images/posts/OctopressOctoflatLinkedinProfile/4.png)

因此筆者修改 `source/_includes/navigation.html` 檔案，為其加入 linkedin_url。

{% if site.linkedin_url %}
- []({{ site.linkedin_url }})

{% endif %}

像是下面這樣：

![5.png](/images/posts/OctopressOctoflatLinkedinProfile/5.png)

再開啟 _config.yml 設定檔設定 linkedin_url，將其指到 Linkedin Profile 的位置就可以了。

![6.png](/images/posts/OctopressOctoflatLinkedinProfile/6.png)