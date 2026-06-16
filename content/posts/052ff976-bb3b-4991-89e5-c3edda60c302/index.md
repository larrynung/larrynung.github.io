---
title: "Connect to Team Fundation Service"
date: "2013-11-06 12:00:00"
tags: [TFS]
description: "之前筆者就一直很想抽空玩一下Team Fundation Server，但總是卡在環境這邊。因為要玩TFS首先就必需要生出一個Server版的Windows才能安裝，而筆者就是沒有多餘的電腦可以安裝Server版本的Windows，工作中又是用SVN或是用Git來做版控，所以遲遲沒能碰觸這塊。"
---

之前筆者就一直很想抽空玩一下Team Fundation Server，但總是卡在環境這邊。因為要玩TFS首先就必需要生出一個Server版的Windows才能安裝，而筆者就是沒有多餘的電腦可以安裝Server版本的Windows，工作中又是用SVN或是用Git來做版控，所以遲遲沒能碰觸這塊。

聽到微軟推出名為Team Fundation Service的雲端版本TFS也已經一陣子了，但筆者以為跟Azure一樣需要刷個卡才能玩，最近才輾轉得知可以免費使用，又不用刷入信用卡號，就小小的試玩了一下。

免費版本的Team Fundation Service的Plan如下，提供5個使用者、無限的專案...等等，基本上個人、小團隊、或是小公司在使用上應該都是夠用的。

![image_thumb_6.png](/images/posts/052ff976-bb3b-4991-89e5-c3edda60c302/image_thumb_6.png)

使用前不免俗地必須要先進行註冊。

![image_thumb.png](/images/posts/052ff976-bb3b-4991-89e5-c3edda60c302/image_thumb.png)

註冊這邊我們必須要建立一個我們要使用的Team Fundation Service帳戶位置。

![image_thumb_1.png](/images/posts/052ff976-bb3b-4991-89e5-c3edda60c302/image_thumb_1.png)

帳戶建立完畢，會導到像下面這樣的畫面。左邊可以讓我們建立Team Project，右邊則是一些說明的文件。這邊我們直接按下New Team Project按鈕開始建立Team Project (New Team Project + Git按鈕只是幫我們預設選取用Git版控，兩個按鈕沒太大的差異)。

![image_thumb_11.png](/images/posts/052ff976-bb3b-4991-89e5-c3edda60c302/image_thumb_11.png)

按下New Team Project按鈕後，會帶出CREATE NEW TEAM PROJECT對話框，畫面如下。依序填入專案的名稱、專案的描述、要用哪種範本、以及版控要用TFVC還是Git，然後按下Create Project按鈕進行Team Project的建立。

![image_thumb_3.png](/images/posts/052ff976-bb3b-4991-89e5-c3edda60c302/image_thumb_3.png)

![image_thumb_5.png](/images/posts/052ff976-bb3b-4991-89e5-c3edda60c302/image_thumb_5.png)

Team Project建立完後點選Navigate to Project按鈕，將畫面導到建立出的Team Project首頁。

![image_thumb_4.png](/images/posts/052ff976-bb3b-4991-89e5-c3edda60c302/image_thumb_4.png)

Team Project的首頁會長的像下面這樣，上方提供簡易的按鈕列可供加入Product Backlog Item、Task、Bug、與Test Case，下方還有個簡單的Burndown chart，另外在右側這邊有Backlog、Work ITem、Board等連結，可以點選過去查閱。

![image_thumb_7.png](/images/posts/052ff976-bb3b-4991-89e5-c3edda60c302/image_thumb_7.png)

但那些都不是這篇的重點，剛開始使用我們只要能連到Team Fundation Service就好，先不要Assign Task或是Bug把事情複雜化。這邊要用到只有Open new instance of Visual Studio這個連結，直接點選該連結就好...

![image_thumb_8.png](/images/posts/052ff976-bb3b-4991-89e5-c3edda60c302/image_thumb_8.png)

點選後會跳出個視窗要求執行外部程式，直接按下Lauch Application按鈕。

![image_thumb_9.png](/images/posts/052ff976-bb3b-4991-89e5-c3edda60c302/image_thumb_9.png)

Visual Studio就會被運行起來，並幫我們自動設定連結Team Foundation Service。

![image_thumb_10.png](/images/posts/052ff976-bb3b-4991-89e5-c3edda60c302/image_thumb_10.png)

若不想透過點選Open new instance of Visual Studio連結自動設定，這邊我們也可以透過Visual Studio的Team Explorer自行新增Server進行連接。

![image_thumb_13.png](/images/posts/052ff976-bb3b-4991-89e5-c3edda60c302/image_thumb_13.png)

## Link

* [Team Foundation Service](http://tfs.visualstudio.com/)
* [Get started with Team Foundation Service](http://tfs.visualstudio.com/en-us/learn/start/get-started/)
* [使用 Team Foundation Service](http://kevintsengtw.blogspot.tw/2012/11/team-foundation-service.html#.UZDwCbXYKGs)
