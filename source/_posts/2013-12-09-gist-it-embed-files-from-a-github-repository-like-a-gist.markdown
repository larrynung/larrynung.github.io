---
layout: post
title: "gist-it - Embed files from a github repository like a gist"
date: 2013-12-09 23:35
comments: true
categories: [GitHub]
keywords: "GitHub, Gist"
description: "gist-it - Embed files from a github repository like a gist"
---

筆者在寫部落格時，有時候會將範例程式碼整理放至 GitHub 上。而文章中又會針對程式做細部的拆解與解說，以往筆者會將程式碼片段複製在部落格的文章內，或是貼至 gist 然後將之內嵌。雖然都可以達到相同的結果，但這樣的作法總是會覺得有些不對勁，因為我的程式就在 GitHub 上，卻還是要將程式碼片段重複貼至部落格或是 gist 上。 

<!--More-->

也因如此順手找了一下相關的解決方案，發現了 gist-it 這個服務...  

gist-it 使用上十分的簡單，只要在文章中內嵌一段 JavaScript，像是:

    <script src="http://gist-it.appspot.com/github/robertkrimen/gist-it-example/blob/master/example.js"/>


Script 的位置前綴為 `http://gist-it.appspot.com/github/` ，也就是 gist-it 的服務位置，後面緊接著帶入要內嵌的檔案在 GitHub 上的位置。

像是下面這樣，筆者想要嵌入 `larrynung/RDPDemo` 這個 Repository 下的 `Source/RDPDemo/Form1.cs` 檔案，我們要帶到 gist-it 服務位置後的位置就是 `larrynung/blob/master/Source/RDPDemo/Form1.cs` 。 

{% img /images/posts/GistIt/1.png %}


所以內嵌的 JavaScript 會是

    <script src="http://gist-it.appspot.com/github/larrynung/blob/master/Source/RDPDemo/Form1.cs"/>


這樣放在部落格中就能將指定的檔案內容整個內嵌進去，很簡單吧？不過筆者不建議像這樣使用，因為以這個例子來說，內嵌到的會是最新的檔案，隨著 Commit 檔案的內容可能會有增減或是刪除，所以比較保險應該是由特定 Commit 的檔案去作內嵌。

像是下面這樣：

    <script src="http://gist-it.appspot.com/http://github.com/larrynung/RDPDemo/blob/bdc43c40e50305f2e12f29c5ff7e8b376b73d90b/Source/RDPDemo/Form1.cs">

此外， gist-it 服務也提供一些參數可接在 Script 位置後面供細部調整。  

像是 slice 參數可設定檔案所要內嵌的部份，可帶入指定的行數或是行數區間。（使用時可一邊開啟 GitHub 確定要做內嵌的部份，但要注意到這邊指定的行數是以 0 為基底）

所以要指定內嵌 Form1.cs 的第 31 行，可以像下面這樣撰寫

    <script src="http://gist-it.appspot.com/http://github.com/larrynung/RDPDemo/blob/bdc43c40e50305f2e12f29c5ff7e8b376b73d90b/Source/RDPDemo/Form1.cs?slice=31">

要指定內嵌 Form1.cs 的 33 行到 35 行，可以像下面這樣撰寫：

    <script src="http://gist-it.appspot.com/http://github.com/larrynung/RDPDemo/blob/bdc43c40e50305f2e12f29c5ff7e8b376b73d90b/Source/RDPDemo/Form1.cs?slice=33:35">

要指定從 Form1.cs 第 11 行開始內嵌，可以像下面這樣撰寫：

    <script src="http://gist-it.appspot.com/http://github.com/larrynung/RDPDemo/blob/bdc43c40e50305f2e12f29c5ff7e8b376b73d90b/Source/RDPDemo/Form1.cs?slice=11:">

另外可供設定的就是 footer 的參數，可帶入 no 或是 0 隱藏 footer，或是 minimal 移除 `This Gist brought to you by gist-it.` 字樣。

    <script src="http://gist-it.appspot.com/http://github.com/larrynung/RDPDemo/blob/bdc43c40e50305f2e12f29c5ff7e8b376b73d90b/Source/RDPDemo/Form1.cs?fotter=0">

    <script src="http://gist-it.appspot.com/http://github.com/larrynung/RDPDemo/blob/bdc43c40e50305f2e12f29c5ff7e8b376b73d90b/Source/RDPDemo/Form1.cs?fotter=no">

    <script src="http://gist-it.appspot.com/http://github.com/larrynung/RDPDemo/blob/bdc43c40e50305f2e12f29c5ff7e8b376b73d90b/Source/RDPDemo/Form1.cs?fotter=minimal">


最後一提， gist-it 服務也有提供測試的功能，可以線上測試會內嵌到什麼內容。若有需要可連至 [gist-it.appspot.com - Embed files from a github repository like a gist](http://gist-it.appspot.com/) 這邊，點選網站左上方的 Try It 連結，輸入網址後按下 Enter ，下方就會帶出會被內嵌的內容。


{% img /images/posts/GistIt/2.png %}


Link
----
* [gist-it.appspot.com - Embed files from a github repository like a gist](http://gist-it.appspot.com/)
