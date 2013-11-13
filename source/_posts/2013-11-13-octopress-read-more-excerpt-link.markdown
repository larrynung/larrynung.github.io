---
layout: post
title: "Octopress - Read more excerpt link"
date: 2013-11-13 20:57
comments: true
categories: [Octopress]
---

在Octopress上撰寫文章時，若不特別做些處理，在Blog分頁那邊會將所有文章的全文依序列出。  

這樣的呈現方式很難被訪客所閱讀，通常我們會期望只顯示部分的文章內容，若有興趣在進ㄧ步的去閱讀全文，這樣文章也比較好找。 

若您也有這樣的需求，可以開啟_config.yaml這個設定檔，在excerpt_link這邊設定進ㄧ步閱讀的按鈕所要呈現的字樣。 

{% img /images/posts/OctopressReadMore/1.png %}


設定好後存檔，並在撰寫文章的同時，加入特定的註解:

    <!--More-->


像是這樣  

{% img /images/posts/OctopressReadMore/2.png %}



該註解可以用以指定文章的摘要要顯示到哪。

實際將部落格跑起來就會像下面這樣: 

{% img /images/posts/OctopressReadMore/3.png %}
