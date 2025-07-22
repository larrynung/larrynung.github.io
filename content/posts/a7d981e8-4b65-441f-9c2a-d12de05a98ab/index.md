---
title: "[Visual Studio][.NET Resource]使用ConnectionString Manager extension擴充元件管理方案中用到的連線字串"
date: "2013-11-06 12:00:00"
description: "[Visual Studio][.NET Resource]使用ConnectionString Manager extension擴充元件管理方案中用到的連線字串"
---

ConnectionString Manager extension是一套用來管理連線字串的Visual Studio擴充套件，他能夠讓開發人員用一個統一的管理介面控管整個方案中有用到的連線字串，透過這個統一的管理介面我們能很容易的新增、編輯、與刪除連線字串，也可以很快速的查驗連線字串是否還能夠正確的連到資料庫。

ConnectionString Manager extension主要具有以下幾個特點：
     Quickly View all connection strings in a solution    Test one or all connection strings     Quick open    Add, Edit, Remove connection strings    Save connections for later    Swap connection strings    Add multiple connection strings to multiple configs at once        
   
簡單的說就是它能夠提供一個單一的連線字串控管介面，能夠新增、編輯、刪除連線字串，並允許測試連線字串實際對資料庫的連線狀況，且能在有需求時快速的幫我們開啟連線字串所在的Config檔，也可以將常用的連線字串儲存起來供下次直接套用。

介紹了這麼多，這邊讓我們來實際操作看看ConnectionString Manager extension。首先我們可透過Extension Manager搜尋ConnectionString，將ConnectionString Manager擴充套件安裝起來。

安裝完後，透過Tools\ConnectionString Manager將ConnectionString Manager開啟。

開啟後我們可以看到ConnectionString Manager將我們把方案中所有用到的連線字串給列出來了(這邊是用Petshop方案來做範例)。我們可以從中看到連線字串在哪個專案中、它所在的Config檔是什麼、連線字串的名稱、以及連線字串本身的內容。所有用到的連線字串全都清楚可見。

看到不該存在的連線字串，我們可以很快速的透過ConnectionString Manager將之刪除。

看到以後可以重用的連線字串，我們可以透過Add Connection To Saved按鈕將之儲存在ConnectionString Manager中，後續有需要時就可以直接拿來套用。

儲存的連線字串若有需要都可以透過Manage Saved Connections去管理。

此外，以ConnectionString Manager來說，最搶眼的功能莫過於測試連線的功能。透過ConnectionString Manager我們可以測試連線字串對資料庫的連線狀況，只要點選上方工具列最左邊的按鈕，再選取要測試選取到的連線字串還是所有的連線字串就可以了。這邊因為筆者並未裝有SQL Server，所以所有的連線字串都會測試失敗，在連線字串前面會被打上叉叉。

除了測試連線之外，ConnectionString Manager也可以直接在上面修改連線字串。只要選取連線字串再點選上方工具列畫有鉛筆的按鈕，ConnecionString Manager就會彈出ConnectionString Editor對話框供開發人員編輯。

開發人員可透過ConnectionString Editor對話框編輯連線字串的名稱與連線字串，也可以直接測試連線字串的連線狀況。

若有加入新的連線字串需求，透過ConnectionString Manager也十分的簡單。點選Add New Connection按鈕後，ConnectionString Manager會開啟New Connection編輯對話框供開發人員設定新的連線字串。

在New Connection編輯對話框中我們可以選取該連線字串要放置在哪個設定檔，以及新的連線字串內容。連線字串除了可以自行手動輸入外。

也可以直接套用先前儲存在ConnectionString Manager內的連線字串。

除此之外，若有需要想要切換到連線字串所在的設定檔中去做些細部的調整，ConnectionString Manager也提供了Open config file按鈕，按下後ConnectionString Manager會幫我們在Visual Studio開啟對應的設定檔。

ConnectionString Manger算是一個不錯的擴充套件，針對連線字串的管理有其強大之處，若上述這些針對連線字串的操作已經困擾您許久，或是總是覺得不夠便利，那麼您可以下載這套擴充套件試試。

## Link
     ConnectionString Manager     Introducing ConnectionString Manager