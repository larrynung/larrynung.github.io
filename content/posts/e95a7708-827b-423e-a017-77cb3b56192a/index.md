---
title: "[CodePlex]如何使用CodePlex website發佈自己的開源專案"
date: "2013-11-06 12:00:00"
description: "[CodePlex]如何使用CodePlex website發佈自己的開源專案"
---

筆者因為最近在整理了一個序列化的函式庫，對微軟的開源程式碼網站CodePlex稍稍玩了一下，這邊隨手做個紀錄。

	要將自己的開源專案程式放在CodePlex上其實很簡單，先將瀏覽器連到CodePlex - Open Source Project Hosting網站，登入自己的帳號，這邊有提供兩種登入方式，可以用Windows Live ID登入，也可以用CodePlex去做登入。

	登入帳號後我們可以看到下面這樣的畫面，按下Create Project，開始建立自己的CodePlex開源專案。

	在建立一個新的CodePlex Project，我們需要為這個Project起個名字，並告訴它專案的網址要用怎樣的開頭，以及要選擇用什麼來做我們Project的版本控制。

	輸入完按下CREATE按鈕建立CodePlex Project，你的CodePlex Project就建立出來了，這時Project還是尚未發布的狀態，記得30天內必需要將專案該設定的設完並發佈出去。

	這邊就先讓我們把建立的專案它的細部資料給補齊，注意頁面右上方會有個Edit Project Summary & Details的連結，按下去進入設定頁面。這頁面主要要補齊的是SUMMARY的部份，可以在這邊概略的介紹一下專案。另外下面的FUND設定也可以看一下，這是廣告的設置設定，可以為專案頁面右側放置廣告，為專案放置個廣告去做公益也是不錯的。

	設定完專案的細部資料後，我們可以開始著手編輯使用者第一眼會看到的HOME這頁，先用滑鼠點選Edit連結進入編輯狀態。

	剛進入CodePlex編輯的功能，有用過Wiki的可能會很熟悉。編輯時若需要些加些效果，像是要將描述變成黑體、斜體、或是要放程式碼進去，必需要善用右邊所提示的MARKUP GUIDE，套用對應的MARKUP GUIDE來達到我們想要的效果。

	若對Wiki這種編輯方是很感冒的，CodePlex也提供Html Markup這種編輯方式，可在上方的FORMAT區域切換，編輯上就會像一般的網站一樣會有些編輯Html的小工具讓我們直接套用。

	HOME頁面除了內容可以編輯外，注意右邊還會有些資訊，像是瀏覽人數之類的，比較要注意的是右下角有個Tag的設定，這能幫助專案被搜尋與曝光，可以為專案標註上一些關鍵字。以筆者的序列化函式庫來說，就標注了序列化與解序列化這些關鍵字。

	HOME頁面這邊的編輯若是都能上手，那麼後續的動作相信都不是問題了，因為這樣的編輯方式在很多頁面都是類似的，像是Document頁面的編輯也一樣，這邊就不多做介紹，你可以試著在Document頁面幫專案加上一些相關的教學文章，讓他人在使用您的專案時更為上手。

	Home與Document頁面都依序設置完成，我們還必須要注意到要切換到LICENSE頁面，為專案設定它的授權。

	到此專案大致該有的設定都設定完了，接著要進入上Code的階段，上Code的部份這邊會依照當初選擇的版本控制方式而有不同，因為筆者選擇的是Git上Code，故這邊以Git的方式來做個簡單的介紹(不足的地方請自行參閱CodePlex Information and Discussion這篇教學)，沒裝Git的請先自行安裝妥當。

	首先我們必需要切至SOURCE CODE頁面，按下右下角的Git連結，CodePlex會彈出個小對話框，上面會顯示這個專案的Git位置、帳密提示、與教學說明的連結。

	有了Git位置後我們要先將這個專案給它Clone下來，開啟Git Bash用git clone指令就可以了，像是下面這樣：

git clone https://YourCodePlexUsername@CloneUrl NameOfFolder

	以CodePlex教學頁面上所提的例子來說，就是先將Git Bash切至桌面，並將CodePlex專案Clone下來放在MyAwesomeGitProject目錄下。下Git指令時Git Bash會詢問帳號密碼，這邊帶入自己的帳密就可以了。

	Clone下來自己的專案後，我們可以直接用抓下來的專案進行編程，編程一個段落可以將Code加入索引，並將Code Commit後Push到CodePlex。

	上完的Code我們可以在SOURCE CODE頁面直接查閱，是修改什麼、有改動哪些檔案、其差異是什麼，每版的紀錄都是清清楚楚。

	專案程式開發告一段落，功能達到預期且穩定的話，我們可以將專案Release。只要切至DOWNLOADS頁面，按下Create New Release。

	填入這次Release是幾版，有什麼重大的功能與修正，並附上Release的檔案，以及是否是穩定版本。

	CodePlex上專案的流程到這邊大概簡單的介紹完畢了，整體來說CodePlex算是個還不錯也還滿完整的開放源碼網站服務，該有的功能大致上都內建了，也還滿好用的，不過Release時要自己編譯後壓縮上傳這點還是有點麻煩。

## 
	Link

		CodePlex Information and Discussion