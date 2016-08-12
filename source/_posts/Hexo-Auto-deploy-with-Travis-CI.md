---
title: Hexo - Auto deploy with Travis CI
date: 2016-08-12 07:37:24
tags: Hexo
---

要使用 Travis CI 自動幫我們發佈 Hexo 部落格 (Travis CI 入門可參閱筆者 [Travis CI - Free Hosted Continuous Integration Platform for the Open Source Community | Level Up](http://larrynung.github.io/2014/01/01/travis-ci-free-hosted-continuous-integration-platform-for-the-open-source-community/) 這篇)，首先我們需先準備一組 Personal access token 給 Travis CI。  

<!-- More -->

<br/>


開啟 GitHub 的 Settings。  

{% asset_img 1.png %}

<br/>


切到 Personal access tokens 頁面。  

{% asset_img 2.png %}

<br/>


按下 `Generate new token` 按鈕建立一組 token。  

{% asset_img 3.png %}

<br/>


為這組 Token 設定一個名稱，並給予它 repo 的權限。  

{% asset_img 4.png %}

<br/>


Token 產生後複製留存以供後續使用。  

{% asset_img 5.png %}

<br/>


接著準備 Travis CI 的設定檔 .travis.yml，放置於 Repository 的根目錄，內容大概像這樣 (使用者名稱與電子郵件位置請自行替換)：    

{% codeblock lang:yml %}
language: node_js
node_js:
- '0.12'
branches:
  only:
  - hexo
before_install:
- npm install -g hexo-cli
install:
- npm install
script:
- hexo clean
- hexo generate
after_success:
- git config --global user.name "[Name]"
- git config --global user.email "[Email]"
- sed -i'' "/^ *repo/s~github\.com~${GH_TOKEN}@github.com~" _config.yml
- hexo deploy
{% endcodeblock %}

<br/>


再來要安裝 travis 命令列工具。  

    gem install travis

{% asset_img 6.png %}

<br/>


安裝完後查閱命令列工具版本以確定安裝無誤。  

    travis version

{% asset_img 7.png %}

<br/>


使用命令列工具登入 GitHub 帳號。  

    travis login

{% asset_img 8.png %}

<br/>


使用命令列工具將剛產生出來的 Token 加密並寫入 Travis CI 設定檔。  

    travis encrypt 'GH_TOKEN=<TOKEN>' --add

{% asset_img 9.png %}

<br/>


寫入後的設定檔會變得像下面這樣：  

{% asset_img 10.png %}

<br/>


將設定檔 Commit 回 Repository。  

<br/>

接著回到 Travis CI 將部落格的 Repository 啟用建置。  

{% asset_img 11.png %}

<br/>


這樣每當我們將部落格文章 Commit 回 Repository 時，Travis CI 就會自動開始進行發佈的動作。  

{% asset_img 12.png %}

<br/>


Link
----
* [Travis CI - Free Hosted Continuous Integration Platform for the Open Source Community | Level Up](http://larrynung.github.io/2014/01/01/travis-ci-free-hosted-continuous-integration-platform-for-the-open-source-community/)
* [Hexo 自动部署到 Github | 三点水](http://lotabout.me/2016/Hexo-Auto-Deploy-to-Github/)
