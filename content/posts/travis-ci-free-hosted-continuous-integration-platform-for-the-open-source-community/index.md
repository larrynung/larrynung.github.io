---
title: "Travis CI - Free Hosted Continuous Integration Platform for the Open Source Community"
date: "2014-01-01 23:34:00"
description: "Travis CI - Free Hosted Continuous Integration Platform for the Open Source Community"
tags: [Travis, CI]
---


Travis CI 是免費的 CI 服務，支援 C、C++、Clojure、Erlang、Go、Groovy、Haskell、Java、Python、Ruby等語言。能用來建置 GitHub 上的 Repository， 為 GitHub 加上 CI 的能力，不需另行為此架設 CI Server。只要在 Repository 放置個 Travis CI 的設定檔，並授權給 Travis CI，最後再將 Service Hook 啟用就可以了。 

<!-- More -->

此外，Travis CI 也提供狀態貼紙的功能，能將建置的狀態內嵌在想放置的位置，讓建置狀態一目了然。 

使用時需先至 Travis CI 做 GitHub 的登入

{% img /images/posts/TravisCI/1.png %}


登入後會 Travis CI 會向我們要求授權

{% img /images/posts/TravisCI/2.png %}


若對要求的權限沒什麼意見，可以進一步按下 `Allow access` 按鈕授予權限。

{% img /images/posts/TravisCI/3.png %}


授予權限時，為了安全起見，GitHub 會再次請求輸入密碼。

{% img /images/posts/TravisCI/4.png %}


密碼確認無誤，Travis CI 即會開始將我們的 Repository 給拉回來。

{% img /images/posts/TravisCI/5.png %}


拉完後會看到像下面這樣的畫面，會將我們所屬的 Repository 給列出。

{% img /images/posts/TravisCI/6.png %}


這邊將欲啟用 CI 功能的 Repository 開關開啟

{% img /images/posts/TravisCI/7.png %}


接著在 Repository 中放置 Travis CI 的設定檔 .travis.yml。設定檔依語言的不同會有不同的設置，像是 C++ 的設定就會像下面這樣：  

```yaml
language: cpp
compiler:
  - gcc
  - clang
# Change this to your needs
script: ./configure && make
```


詳細的設定請參閱 [Travis CI Documentation](http://about.travis-ci.org/docs/) 。  

設定檔設定完，將它 Commit 並 Push 回 Remote Repository 設定就完成了。以後上 Code 到 Remote Repository ，或是有人發 Pull Request 過來，Travis CI 就會自動觸發建置的動作。如想手動觸發建置，又不想為此 Push 一些不必要的 Commit，可至 GitHub test Service Hook。

建置的過程與資訊在 Travis CI 這邊都有詳細的記載...  

{% img /images/posts/TravisCI/8.png %}


Link
-----
* [ Travis CI - Free Hosted Continuous Integration Platform for the Open Source Community ]( https://travis-ci.org )
