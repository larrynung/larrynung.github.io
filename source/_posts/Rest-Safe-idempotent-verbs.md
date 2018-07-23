---
title: Rest - Safe/idempotent verbs
date: 2018-07-23 19:23:41
tags: [Rest]
---

Rest API 的方法依其性質可以被劃分為 Safe method 或是 Idempotent method。 

<!-- More -->

<br/>

Safe method 也就是安全的方法，表示該方法不會對資源進行任何的修改，且其結果可以被快取。GET 與 HEAD 屬於這類方法。  

<br/>


Idempotent method 也就是冪等方法，表示該方法重複調用的結果都是相同的， GET、PUT、DELETE、HEAD、OPTIONS 屬於這類方法。  

<br/>


POST、PATCH 則兩類方法都不是。  

<br/>


最後附上對應總表：  

| Verb | Safe | Indempotent |
|:-------------:|:-------------:|:-----:|
| GET | Y | Y |
| POST | N | N |
| PUT | N | Y |
| DELETE | N | Y |
| PATCH | N | N |
| HEAD | Y | Y |
| OPTIONS | Y | Y |


Link
----
* [程式設計 - 簡明RESTful API設計要點 - Twincl](https://tw.twincl.com/programming/*641y)
* [哪些是冪等或/且安全的方法？ - RESTful 手冊](https://sofish.github.io/restcookbook/http%20methods/idempotency/)
* [RFC 7231 - Hypertext Transfer Protocol (HTTP/1.1): Semantics and Content](https://tools.ietf.org/html/rfc7231#section-4.2)
* [HTTP Verbs: 談 POST, PUT 和 PATCH 的應用 | ihower { blogging }](https://ihower.tw/blog/archives/6483)
* [What are idempotent and/or safe methods? - The RESTful cookbook](http://restcookbook.com/HTTP%20Methods/idempotency/)
* [HTTP Methods [ RESTful APIs Verbs ] – REST API Tutorial](https://restfulapi.net/http-methods/)
* [Idempotent REST APIs – REST API Tutorial](https://restfulapi.net/idempotent-rest-apis/)
