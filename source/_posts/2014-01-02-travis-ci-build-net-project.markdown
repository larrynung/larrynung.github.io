---
layout: post
title: "Travis CI - Build .NET project"
date: 2014-01-02 23:59
comments: true
categories: [Travis, CI]
keywords: Travis,CI,.NET,Mono
description: "Travis CI - Build .NET project"
---

Travis CI 內建支援 C、C++、Clojure、Erlang、Go、Groovy、Haskell、Java、Python、Ruby 等語言，卻沒有支援 .Net 的，這表示官方並不特別的去做 .Net 語言的支援。然而 Travis CI 具備有相當程度的彈性，經由設定能在建置前先進行套件的安裝，因此我們還是能透過安裝 Mono 套件去建置 .Net 的專案。

<!-- More -->

在設定檔的撰寫上，Language 這邊指定語言為 C ，因為前面提到的 Travis CI 並不支援 C# 。

    language: c


install 這邊透過 apt-get 安裝 mono-devel 、 mono-gmcs 。

    install:
      - sudo apt-get install mono-devel mono-gmcs


script 這邊直接叫用 xbuild 去建置我們的專案或是方案就可以了。

    script:
      - xbuild Source/LevelUp.Extensions.Core/LevelUp.Extensions.Core.csproj
      - xbuild Source/LevelUp.Extensions.Control/LevelUp.Extensions.Control.csproj


整個設定檔撰寫起來會像下面這個樣子：

{% codeblock lang:yaml %}
 Travis CI Integration

language: c

install:
  - sudo apt-get install mono-devel mono-gmcs
script:
  - xbuild Source/LevelUp.Extensions.Core/LevelUp.Extensions.Core.csproj
  - xbuild Source/LevelUp.Extensions.Control/LevelUp.Extensions.Control.csproj
{% endcodeblock %}


若有單元測試的需求，這邊可改用 Nunit 去做測試。設定檔這邊只要在安裝 Mono 時順帶安裝 nunit-console ，然後在 script 那邊透過 nunit-console 進行測試即可。

{% codeblock lang:yaml %}
 Travis CI Integration

language: c

install:
  - sudo apt-get install mono-devel mono-gmcs nunit-console
script:
  - xbuild Source/LevelUp.Extensions.Core/LevelUp.Extensions.Core.csproj
  - xbuild Source/LevelUp.Extensions.Control/LevelUp.Extensions.Control.csproj
  - nunit-console Bin/LevelUp.Extensions.Test.dll -exclude Integration,NotWorkingOnMono
{% endcodeblock %}


Link
----
* [Finally Got Travis CI to Work With C#.NET](http://www.parttimelegend.co.uk/blog/2013/04/11/finally-got-travis-ci-to-work-with-c-number-net/)
* [Build Your Open Source .NET Project On Travis CI](http://danlimerick.wordpress.com/2013/02/03/build-your-open-source-net-project-on-travis-ci/)
