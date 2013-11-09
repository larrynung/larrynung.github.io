---
layout: post
title: "Octopress - A blogging feamework for hackers."
date: 2013-11-05 23:14
comments: true
categories: [Git,Octopress]
---

Octopress是ㄧ利用Jekll部落格引擎開發的部落格系統，能簡易的架設、擴充、客製、與套版，因其最後是生成靜態網頁，因此能很輕易的在許多服務上做部署，像是Github、Heroku、與Rsync等。

由於Github服務無流量與儲存空間之類的限制，部署到上面又能享有版本控制的好處，怎麼看都是首選的平臺。所以這篇會以Github來做個介紹與示範，看要怎樣透過Octopress架設一個Blog在上面。
  
Setup Octopress   
-----------------
首先進行Octopress的安裝。

因Octopress相依於Ruby 1.9.2以後的版本，這邊需先確保環境已安裝有正確的Ruby版本。

若是環境中無安裝正確的Ruby版本，可透過RVM進行安裝的動作。  

    rvm install 1.9.2    
    rvm use 1.9.2
  
  
Ruby環境準備妥當後，將Octopress從Github clone下來。 

    git clone git://github.com/imathis/octopress.git octopress

{% img /images/posts/Octopress/1.png %}

接著進到Octopress目錄下。 

    cd octopress


用Ruby gem安裝bundle。 

    gem bundle
    bundle install

{% img /images/posts/Octopress/2.png %}


bundle安裝完後，再將rake安裝上就可以了。 

    rake install
  
{% img /images/posts/Octopress/3.png %}  

Configure Octopress
---------------------
Octopress安裝完後有些設定動作要做，要針對_config.yml裡面的設定做些調整。像是部落格的網址、部落格的標題、部落格的副標題、是否啟用Facebook like...等。 
 
{% img /images/posts/Octopress/4.png %}
  
Init and deploy to Github page
-------------------------------
安裝與設置的動作都完成後，我們還需要先做個初始動作。 

因為這邊要將之Host在Github的Github page，所以要先至Github上建立Repository,Repository命名需像username/username.github.io這樣。 

{% img /images/posts/Octopress/5.png %}

{% img /images/posts/Octopress/6.png %}

建立完後呼叫命令: 

    rake setup_github_pages
  
  
該命令呼叫後會詢問Github page repository位置，帶入後Octopress會做些對應的設置動作。像是將Git的remote origin repository指向Github page repository、將branch從master切到source、設定_deploy目錄供存放要部署至master branch的內容...等。

到這邊初始的動作就已經完成了。 

接著嘗試將空的部落格部署到Github看看。 

呼叫下列命令產生部落格所需的靜態網頁(產生出來的靜態網頁會存放在_deploy目錄下等待部署)。

    rake generate


呼叫下列命令將產出的靜態網頁部署到Github上。 

    rake deploy

  
部署上去後，可以到Github page看部落格運行起來的樣子(Github page有時候會需要等一下)。

最後要注意到，因為剛部署的是產生出來的部落格靜態網頁，而用來產生靜態網頁的原始檔仍舊在本機上面，所以這邊通常還是會再將它上到Github上做版控。 

    git add .
    git commit -a -m "Init vcs"
    git push origin source

    
Write blog
-----------
要建立一篇新的部落格文章時，可呼叫命令： 

    rake new_post["title"]


然後開始撰寫，撰寫時需使用Markdown語法。

撰寫完可叫用命令產生對應的靜態網頁

    rake generate
   

這邊可呼叫命令查看產生的檔案

    rake watch
  
也可呼叫命令啟動預覽服務 

    rake preview

{% img /images/posts/Octopress/7.png %} 

預覽服務啟動後，可開啟瀏覽器訪問localhost:4000。沒意外的話會看到你部落格運行起來的樣子。

{% img /images/posts/Octopress/8.png %}

若在預覽時發現需要修改，可以不中斷預覽服務，預覽服務會偵測修改，自動產生對應的靜態網頁。


確定撰寫告ㄧ段落，可叫用命令將之部署至Github上  
    
    rake deploy


最後一樣記得原始檔仍舊在本機，要另行上到Github做版控。 

    git add .
    git commit -a -m "Post: Hello world"
    git push
