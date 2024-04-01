---
title: "SpecFlow - Getting Started"
date: "2015-09-13 16:14:00"
description: "SpecFlow - Getting Started"
---


Specflow 使用前 Visual Studio 需先透過 Extension Manager 搜尋並安裝 SpecFlow Extension。  

<!-- More -->

{% img /images/posts/SpecFlowGettingStarted/1.png %}

<br/>


{% img /images/posts/SpecFlowGettingStarted/2.png %}

<br/>


{% img /images/posts/SpecFlowGettingStarted/3.png %}

<br/>


然後建立一個測試專案，並透過 NuGet 為其加入 SpecFlow Package。  

{% img /images/posts/SpecFlowGettingStarted/4.png %}

<br/>


{% img /images/posts/SpecFlowGettingStarted/5.png %}

<br/>


{% img /images/posts/SpecFlowGettingStarted/6.png %}

<br/>


套件加入後在專案中會多個 App.config 檔，若非使用 NUnut 去撰寫測試，這邊需加指定 unitTestProvider。  

{% img /images/posts/SpecFlowGettingStarted/7.png %}

<br/>


接著用 SpecFlow Extension 裝進去的 SpecFlow Feature File 範本建立一個 Feature 檔 。  

{% img /images/posts/SpecFlowGettingStarted/8.png %}

<br/>


Feature 檔建立後會長的像下面這樣：  

{% img /images/posts/SpecFlowGettingStarted/9.png %}

<br/>


Feature 其實就是用 User Story 下去撰寫功能描述。Feature 由一或多個 Scenario 所組成(可想成測試案例中的測試情境)，而 Scenario 又是由 Given、 When、 Then 三個 Step (可想成測試案例中的測試步驟)所組成，這三個 Step 分別對應到單元測試的 3A 原則。  

<br/>


這邊筆者用序列化套件來做個示範，其 Feature 檔寫起來會像這樣：
 
{% img /images/posts/SpecFlowGettingStarted/10.png %}

<br/>


Scenario 撰寫完後，我們可以在 Feature 檔的上面按下滑鼠右鍵，在彈出的滑鼠右鍵快顯選單中選取 `Generate Step Definitions` 選單選項。  

{% img /images/posts/SpecFlowGettingStarted/11.png %}

<br/>


Visual Studio 會彈出 `Generate Step Definition Skeleton` 視窗，該視窗會列出我們尚未建立的 Step，通常是直接保持全選，但若有需要也可依需求選取欲建立的 Step。

<br/>


接著要選取要使用的 Style (若有需要可按下 Preview 按鈕查看會產生的結果)，即可進行 Step 的建立。

{% img /images/posts/SpecFlowGettingStarted/12.png %}

<br/>


這邊的 Style 有三種，通常是用第一種 Style，也就是 `Regular expressions in attributes`，該 Style 是在方法上用 Attribute 帶入正規表示式的 Pattern 去做 Match，用以決定 Feature 檔內的 Scenario Step 要如何對應到 Step 檔的方法。使用該 Style 方法因為主要是看 Attribute 帶入的正規表示式 Pattern，所以方法的名稱可以視需要修改。

{% img /images/posts/SpecFlowGettingStarted/13.png %}

<br/>


第二種 Style 是 `Method name - underscores`，該 Style 是在方法上加上 Given、 When、 Then 三個 Attribute 識別是 Step 的方法，然後用底線串接的方法名稱去決定 Feature 檔內的 Scenario Step 要如何對應到 Step 檔的方法。因為方法名稱是決定如何對應的依據，所以不可任意變更。

{% img /images/posts/SpecFlowGettingStarted/14.png %}

<br/>


第三種 Style 是 `Method name - pascal case`，該 Style 一樣是在方法上加上 Given、 When、 Then 三個 Attribute 去識別是 Step 的方法，然後用 pascal 方法名稱去決定 Feature 檔內的 Scenario Step 要如何對應到 Step 檔的方法。 方法名稱一樣不可任意變更。

{% img /images/posts/SpecFlowGettingStarted/15.png %}

<br/>


要產生的 Step 與要使用的 Style 選取完後，因為我們是尚未有對應的 Step 檔，所以要按下 Generate 按鈕建立對應的 Step 檔。    

{% img /images/posts/SpecFlowGettingStarted/16.png %}

<br/>


{% img /images/posts/SpecFlowGettingStarted/17.png %}

<br/>


Step 檔建立後會像下面這樣，預設 Step 的方法裡面放的都是 ScenarioContext.Current.Pending()，也就是待處理的意思。  

{% img /images/posts/SpecFlowGettingStarted/18.png %}

<br/>


以這 Scenario 來說，在 Given 這邊我將要序列化的物件存放至 ScenarioContext.Current 內，然後在 When 這邊將要序列化的物件自 ScenarioContext.Current 取出，取出後將其序列化放回 ScenarioContext.Current，最後在 Then 這邊將序列化後的結果自 ScenarioContext.Current 取出後驗證。  

{% img /images/posts/SpecFlowGettingStarted/19.png %}

<br/>


寫完後準備開始運行測試，需先確定 Test runner tool 設定正確，不然會無法正常運行測試。  

{% img /images/posts/SpecFlowGettingStarted/20.png %}

<br/>


接著設定斷點並在 Feature 檔上按下滑鼠右鍵，在彈出的滑鼠右鍵快顯選單中點選 `Run SpecFlow Scenarios` 選單選項，即會針對 Feature 內的所有 Scenario 運行測試。若點選的是 `Debug SpecFlow Scenarios` 選單選項，則會進行除錯。  

{% img /images/posts/SpecFlowGettingStarted/21.png %}

<br/>


{% img /images/posts/SpecFlowGettingStarted/22.png %}

<br/>


{% img /images/posts/SpecFlowGettingStarted/23.png %}

<br/>


這邊筆者在進一步加個 Scenario，這邊測試序列化 10 次，平均序列化的時間應該小於 1 秒內。Scenario 如下，物件與驗證 Xml 的 Step 描述撰寫的跟 Scenario1 的一樣，共用相同的 Step，寫完一樣在 Feature 檔的上面按下滑鼠右鍵，在彈出的滑鼠右鍵快顯選單中選取 `Generate Step Definitions` 選單選項。    

{% img /images/posts/SpecFlowGettingStarted/24.png %}

<br/>


因為對應的 Step 檔案已經建立，所以 `Generate Step Definition Skeleton` 視窗這邊要改選 `Copy methods to clipboard`。

{% img /images/posts/SpecFlowGettingStarted/25.png %}

<br/>


接著開啟對應的 Step 檔將剛複製的內容貼上，多出來的 Step 就進去了。注意到這邊，SpecFlow 已經將我們在 Scenario Step 中用數值描述的部分改用參數帶入，我們可以直接在後面實作中使用。

{% img /images/posts/SpecFlowGettingStarted/26.png %}

<br/>
 


{% img /images/posts/SpecFlowGettingStarted/27.png %}

<br/>


參數部分除了數值外，也支援字串與表的形式。字串部分跟數值大同小異，只要描述 Scenario Step 時用雙引號包住字串去描述即可，產生 Step 時 SpecFlow 就會偵測到。  

<br/>


如果參數是表的形式，我們可以像下面這樣撰寫，用 `|` 將資料描述成表。  

{% img /images/posts/SpecFlowGettingStarted/28.png %}

<br/>



建立的 Step 就會將資料表示用 Table 帶入。需注意到這邊的 Table 非我們常用的 ADO.NET 的 Table，但操作上大同小異。  

{% img /images/posts/SpecFlowGettingStarted/29.png %}

<br/>


最後一提，上面描述的作法 SpecFlow 會自行去依 Style 的不同，用對應的方式去將 Scenario Step 與 Step 的實作對應。但有時候不同的 Feature Scenario 可能是做不同的事但有著相同的 Step 描述，這時我們可以用 ScopeAttribute 自行決定要怎樣對應。  

{% img /images/posts/SpecFlowGettingStarted/30.png %}

<br/>


{% img /images/posts/SpecFlowGettingStarted/31.png %}

<br/>
