---
title: PhantomJS - Support ES6/ES2015 Features
date: 2018-11-30 23:47:56
tags: [PhantomJS]
---

PhantomJS 目前版本為 2.1 版，是不支援 ES6/ES2015 的，所以在某些情境下使用 PhantomJS 會被受限，像是網站使用到 let 之類的語法就會無法使用 PhantomJS。  

<!-- More -->

<br/>


PhantomJS 的預計在 2.5 版對 ES6/ES2015 進行支援，但從 [用Python做爬蟲的各位，不要再用PhantomJS了- 知乎](https://zhuanlan.zhihu.com/p/34293235) 這邊看起來 PhantomJS 已經停止了開發，一度在 [Support ES6/ES2015 Features · Issue #14506 · ariya/phantomjs](https://github.com/ariya/phantomjs/issues/14506#issuecomment-251611067) 這邊釋出的 2.5 版也被拿掉。  

<br/>


目前要用 PhantomJS 支援 ES6/ES2015 只能從 [phantomjs25-beta - npm](https://www.npmjs.com/package/phantomjs25-beta) 這邊取得使用，除了透過 npm 套件安裝，若有需要也可以從這裡面提供的位置下載下來使用，位置是 https://bitbucket.org/takuhii/phantomjs25-beta/downloads/。  

<br/>


Link
---
* [Support ES6/ES2015 Features · Issue #14506 · ariya/phantomjs](https://github.com/ariya/phantomjs/issues/14506#issuecomment-251611067)
* [phantomjs25-beta - npm](https://www.npmjs.com/package/phantomjs25-beta)
