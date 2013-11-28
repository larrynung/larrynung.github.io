---
layout: post
title: "RAML - RESTful API Modeling Language"
date: 2013-11-28 22:24
comments: true
categories: [RAML]
keywords: "RAML"
description: "RAML - RESTful API Modeling Language"
---

RAML (RESTful API Modeling Language) 是ㄧ以YAML為基礎、專門用來描述 RESTful API、且人與機器都看得懂的標記語言。 

<!--More-->

{% img /images/posts/RAML/1.png %}


因為透過RAML去描述的API，機器也能夠看得懂，所以可以衍生出一些附加的功能服務，像是解析並自動產生對應的 API Console、API Client、API Server、API User Document…等。


Root Section
------------

RAML文檔最開始是Root Section，是用來做 API 基本的描述用，像是 API 的標題、API 版本、API 基底位置、相關文檔、與 schema 及其參考...等。

就像下面這樣：

    #%RAML 0.8
    ---
    title: GitHub API
    baseUri: http://api.github.com/{version}
    version: v1

一開始要描述RAML的版本，接著就是帶入 API 的標題等。以這例子來說，這邊是在描述 GitHub 的 API ，API 的基底位置是 `http://api.github.com/{version}` ，基底位置內寫的 {version} 會被實際的版本取代，而目前的版本是 v1 。  

除了上面範例提到的設定外，還有其它可用的設定，這邊不深究，請直接參閱下表整理： 

<table>
<tr><td> Property </td> <td> Required</td> <td> Description</td> </tr>
<tr><td> title </td> <td> Yes </td> <td> API 文件標題</td> </tr>
<tr><td> version </td> <td> No </td> <td> API 版本</td> </tr>
<tr><td> baseUri </td> <td> No </td> <td> API 基底位置</td> </tr>
<tr><td> baseUriParameters </td> <td> No </td> <td> API 基底位置的參數</td> </tr>
<tr><td> Protocols </td> <td> No </td> <td> API 支援的通訊協定</td> </tr>
<tr><td> mediaType </td> <td> No </td> <td> API 預設的MediaType</td> </tr>
<tr><td> schemas </td> <td> No </td> <td> </td> schema</tr>
<tr><td> uriParameters </td> <td> No </td> <td> API 相關參數</td> </tr>
<tr><td> documentation </td> <td> No </td> <td> API 相關文件</td> </tr>
</table>


Resource
--------

Root Section設定好我們已經有 API 的基底位置了，所有的 API 都是以這基底下去延伸，我們可能為了讓 API 更為清楚，而在 API 基底位置下再加上幾層 Resource 進去，像是 GitHub API 的 API 基底位置是 `https://api.github.com/`，Gist 相關的功能就被放在 `/gists` Resource 下， 所以對應的 API 位置就變成 `https://api.github.com/gists/`這樣。

所以 Resource 在 RAML 這邊的設定就是以 `/` 開頭，像是下面這樣：

    /gists:


要做巢狀的 Resource 也是可以的：

    /gists:
    	/{gistId}:

      

Methods
-------

Resource 定義完，我們可以決定 Resource 對應下列哪些Method：

- get	
- put
- post
- delete

像是 GitHub 的 Gist API 支援get，所以我們可以像下面這樣定義：

    /gists:
        /{gistId}:
    		get:


Query parameters
----------------

Resource 跟 Method 都設定好，有的簡單的 API 到這邊就可以動了，但是有的比較複雜的會要帶 QueryString 當參數，這時我們就需要在對應的 Method 後設定 queryParameters ，像是下面這樣： 

    /gw:
      get:
        queryParameters:
          method:
            type: string
            enum: ["album.channel.get"]
            default: "album.channel.get"
          channel:
            type: string
            enum: ["z"]
          appKey:
            type: string
            default: "myKey"
          format:
            type: string
            enum: ["xml", "json"]
          pageNo:
            type: integer
          pageSize:
            type: integer      


queryParameters 後面帶上 QueryString 內所含的參數設定，每個參數設定都可套用需要的 Named Parameters，Named Parameters 這邊可參考下表：

<table>
<tr><td> displayName </td> <td> Required</td> <td> 顯示名稱 </td> </tr>
<tr><td> title </td> <td> Yes </td> <td> 標題</td> </tr>
<tr><td> type </td> <td> No </td> <td> 型態</td> </tr>
<tr><td> enum </td> <td> No </td> <td> 列舉值</td> </tr>
<tr><td> pattern </td> <td> No </td> <td> </td> </tr>
<tr><td> minLength </td> <td> No </td> <td>最小長度</td> </tr>
<tr><td> maxLength </td> <td> No </td> <td>最大長度</td> </tr>
<tr><td> minimum </td> <td> No </td> <td> 最小值</td> </tr>
<tr><td> maximum </td> <td> No </td> <td> 最大值</td> </tr>
<tr><td> example </td> <td> No </td> <td> 範例</td> </tr>
<tr><td> repeat </td> <td> No </td> <td> </td> </tr>
<tr><td> required </td> <td> No </td> <td>必要值</td> </tr>
<tr><td> default </td> <td> No </td> <td> 預設值</td> </tr>
</table>


Response
--------

Response 這塊是定義 API 的回傳值，一樣是接在 Method 後面，帶上 responses 設定，後面接著 HTTP Status Code ，接著是 body、對應的MediaType、以及example，像是下面這樣：

    /gists: 
      /{gistId}:
        get:
          responses:
            404:
              body:
                application/json:
                  example: |
                    {
                      "message": "Not Found",
                      "documentation_url": "http://developer.github.com/v3"
                    }


Conclusion
----------

RAML 的文檔基礎來說就是這樣而已，當然還有些細部的設定參數這邊沒有介紹到，若有需要請自行查閱 Spec 文檔。 

最後這邊要提一下，一開始筆者就有提到了 RAML 文檔機器也能看得懂，因此有延伸出來很多服務。  

比較重要的像是 [API Designer](http://www.apihub.com/raml/api-designer#/api-designer) 就能輔助我們編輯 RAML 文檔

{% img /images/posts/RAML/2.png %}


編輯的同時右側這邊會即時呈現對應的 API Console 

{% img /images/posts/RAML/3.png %}


藉由比對我們可以更清楚了解 RAML 文檔的欄位會用在哪邊，也可以即時叫用 API。


另外就是 [API Console](http://www.apihub.com/raml-tools)，是跟 API Designer 右側一樣的東西，可解析 RAML 檔產生對應的互動式文檔。

{% img /images/posts/RAML/4.png %}


這些 Tool 都有開源在 GitHub 上，有需要都可以自行架設。

Link
----
* [ RESTful API Modeling Language ]( http://raml.org/index.html )
* [ RAML 100 TUTORIAL ]( http://raml.org/docs.html )
