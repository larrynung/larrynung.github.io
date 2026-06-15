---
title: "[.NET Resource]PowerCommands"
date: "2010-06-27 01:21:11"
description: "[.NET Resource]PowerCommands"
tags: [.NET Resource]
---

PowerCommands是Visual Studio輔助外掛，提供許多方便好用的小功能，像是複製參考、貼上參考、開啟Folder、複製類別等等。

在安裝PowerCommands時，可透過Visual Studio 2010內建的Extension Manager搜尋後安裝，也可連至PowerCommands for Visual Studio 2010 網站下載後透過點擊安裝。(Visual Studio 2008的使用者可到[PowerCommands for Visual Studio 2008](http://code.msdn.microsoft.com/PowerCommands)下載使用)

![image_thumb.png](/images/posts/16212/image_thumb.png)

安裝完畢後，重新啟動Visual Studio，就可以享受PowerCommands所帶來的便利了。

**Enable/Disable PowerCommands in Options dialog**
這功能能讓我們設定PowerCommands要啟用的功能，只要透過滑鼠點選[Tools]→[Options]選單選項，滑鼠左鍵點選PowerCommands下方的點選Commands節點，接著在右側頁面依個人需求選取即可。(預設所有PowerCommands功能在安裝完後皆會啟用)

![image_thumb_2.png](/images/posts/16212/image_thumb_2.png)

**Format document on save / Remove and Sort Usings on save**
[Tools]→[Options]開啟Options對話盒後，滑鼠左鍵點選PowerCommands下方的General節點，在右側頁面可看到兩個可選取的功能，[Format document on save]功能是在儲存時自動整理程式碼格式，相當於在存檔時去執行[Edit]→[Advanced]→[Format Document]。而[Remove and sort Usings on save]功能是只支援C#專案的功能，可在存檔時自動移除多餘的Using陳述式，並把Using陳述式做排序。(這兩個功能在安裝後預設是關閉的狀態)

![image_thumb_1.png](/images/posts/16212/image_thumb_1.png)

**Clear All Panes**
開啟輸出對話框可發現工具列上多出一個[Clear All Panes]工具列按鈕，該按鈕功能為清除所有窗格內的文字(可用前方Show output from切換至不同窗格)，而本來的[Clear All]則是清除當前窗格內的文字。

![image_thumb_3.png](/images/posts/16212/image_thumb_3.png)

**Copy Path**
該功能可以複製所選取的項目的完整路徑，只要在方案總管視窗上的方案節點、專案節點、專案項目節點、或是目錄節點上按下滑鼠右鍵，在右鍵快顯選單中點選[Copy Path]選單選項，即會將該項目的完整路徑給複製到剪貼簿中。

![image_thumb_4.png](/images/posts/16212/image_thumb_4.png)

**Email CodeSnippet**
該功能可把程式碼片段用Email傳至他人，只要用滑鼠左鍵選取要傳的程式碼片段，在選取的程式碼片段上按下滑鼠右鍵，點選滑鼠右建清單中的[Email CodeSnippet]選單選項，系統會帶出預設的郵件軟體，並把所選取的程式碼片段自動帶至信件，填寫完畢就可以寄送了。

![image_thumb_6.png](/images/posts/16212/image_thumb_6.png)

![image_thumb_7.png](/images/posts/16212/image_thumb_7.png)

**Insert Guid Attribute**
該功能可以為類別加上Guid屬性，只要在類別定義中按下滑鼠右鍵，滑鼠點選右鍵快顯清單中的[Insert Guid Attribute]選單選項，該類別前面就會被加上Guid屬性。

![image_thumb_8.png](/images/posts/16212/image_thumb_8.png)

![image_thumb_9.png](/images/posts/16212/image_thumb_9.png)

**Show All Files**
該功能可以在方案總管中顯示所有被隱藏的檔案，只要透過滑鼠點選方案總管上方工具列的[Show All Files]工具按鈕即可，它加強了本來舊有的[Show All Files]功能，除了在專案節點上使用外，也能在方案節點上直接使用。

![image_thumb_10.png](/images/posts/16212/image_thumb_10.png)

**Undo Close**
該功能可顯示最近關閉的文件，使用時須先透過[Visw]→[Other Windows]→[Undo Close Window]選單選項把Undo Close視窗開啟，當文件關閉時該視窗會自動顯示關閉的視窗，可直接在Undo Close視窗中的項目上面點選，也可以透過[Edit]→[Undo Close]選單選項，或是使用熱鍵Ctrl + Shift +Z開啟最近關閉的文件。

![image_thumb_5.png](/images/posts/16212/image_thumb_5.png)

![image_thumb_11.png](/images/posts/16212/image_thumb_11.png)

**Collapse Projects**
該功能可以折疊專案節點，只要在方案總管上的專案節點、方案節點、或是方案目錄節點上，按下滑鼠右鍵，點選右鍵快顯選單的[Collapse Projects]選單選項，其下方的專案節點就可快速的折疊起來。![image_thumb_12.png](/images/posts/16212/image_thumb_12.png)

**Copy Class**
該功能可複製所選取的類別，需搭配Past Class功能一起使用，使用時可透過滑鼠在方案總管中的文件上按下滑鼠右鍵，點選右鍵選單中的[Copy Class]選單選項，所選取的類別資訊就會被複製至剪貼簿中，供後續貼上使用。

![image_thumb_13.png](/images/posts/16212/image_thumb_13.png)

**Paste Class**
該功能可貼上之前所複製的類別，需搭配Copy Class功能一起使用，使用時可透過滑鼠在方案總管中的專案節點或是目錄節點上按下滑鼠右鍵，點選右鍵選單中的[Past Class]選單選項，之前複製的類別就會貼至指定的專案或是目錄下，該功能在貼上時會自動替換類別檔名，避免編譯錯誤。

![image_thumb_14.png](/images/posts/16212/image_thumb_14.png)

**Copy References**
該功能可複製專案的參考，需搭配Past Reference功能一起使用，使用時在方案總管中的References節點、個別的參考結點、或是自行選取多個參考結點後按下滑鼠右鍵，點選右鍵選單中的[Copy Reference]選單選項，參考的資訊就會被複製至剪貼簿中，供後續貼上使用。

![image_thumb_15.png](/images/posts/16212/image_thumb_15.png)

![image_thumb_16.png](/images/posts/16212/image_thumb_16.png)

**Paste References**
該功能可貼上所複製的專案參考，需搭配Copy Reference功能一起使用，使用時在方案總管中的References節點按下滑鼠右鍵(VB.NET與WebSite可在專案節點上使用)，點選右鍵選單中的[Past Reference]選單選項，就可以把之前複製的專案參考給貼至目前專案。

![image_thumb_17.png](/images/posts/16212/image_thumb_17.png)

**Copy As Project Reference**
該功能在使用上可透過在方案總管中的專案節點上按下滑鼠右鍵，點選右鍵選單中的[Copy As Project Reference]選單選項。

![image_thumb_18.png](/images/posts/16212/image_thumb_18.png)

**Edit Project File**
該功能可以讓我們編輯專案檔的內容，只要在方案總管中的專案節點上按下滑鼠右鍵，點選右鍵選單中的[Edit Project File]選單選項，專案會立即卸載，並在程式碼編輯區會自動帶出專案檔的內容供編輯。

![image_thumb_26.png](/images/posts/16212/image_thumb_26.png)

![image_thumb_27.png](/images/posts/16212/image_thumb_27.png)

**Open Containing Folder**
該功能可開啟文件所在的目錄，透過方案總管選取文件，在文件上方按下滑鼠右鍵，點選滑鼠右鍵清單中的[Open Containing Folder]選單選項，系統就會幫我們用檔案總管開啟文件所在的目錄。

![image_thumb_19.png](/images/posts/16212/image_thumb_19.png)

**Open Command Prompt**
該功能能為我們把命令提示字元的目錄設為指定的目錄位置並帶出，使用上可透過在方案總管上的方案節點、專案節點、目錄節點、或是在文件節點按下滑鼠右鍵，點選滑鼠右鍵選單中的[Open Command Prompt]選單選項。

![image_thumb_20.png](/images/posts/16212/image_thumb_20.png)

**Unload Projects**
該功能可卸載方案中所有的專案，可在方案總管視窗上的方案節點按下滑鼠右鍵，在滑鼠右鍵選單中的[Unload Projects]選單選項，該方案中所有的專案就會被卸載。

![image_thumb_29.png](/images/posts/16212/image_thumb_29.png)

**Unload Project**
該功能可卸載方案指定的專案，可在方案總管視窗上的專案節點按下滑鼠右鍵，在滑鼠右鍵選單中的[Unload Project]選單選項，指定的專案就會自方案中卸載。

![image_thumb_21.png](/images/posts/16212/image_thumb_21.png)

**Reload Projects**
該功能可重新載入所有卸載的專案，可在方案總管視窗上的方案節點按下滑鼠右鍵，在滑鼠右鍵選單中的[Reload Projects]選單選項，可為方案重新載入所有卸載的專案。

![image_thumb_22.png](/images/posts/16212/image_thumb_22.png)

**Reload Project**
該功能可重新載入指定的已卸載專案，可在方案總管視窗上的專案節點按下滑鼠右鍵，在滑鼠右鍵選單中的[Reload Project]選單選項，可為方案重新載入指定的已卸載專案。

![image_thumb_30.png](/images/posts/16212/image_thumb_30.png)

**Remove and Sort Usings**
該功能可移除C#專案中多餘的Using陳述式並作排序，可在方案總管上的方案節點或是專案節點上，按下滑鼠右鍵，點選滑鼠右鍵選單中的[Remove and Sort Usings]選單選項，專案或方案下的檔案其內含的Using陳述式就會被做整理的動作。

![image_thumb_28.png](/images/posts/16212/image_thumb_28.png)

**Extract Constant**
該功能能為我們所選取的數值建立常數替換，使用上先選取程式碼中要轉為常數的數值，按下滑鼠右鍵，點選滑鼠右鍵選單中的[Refactor]→[Extract Constant…]選單選項，在彈出的Extract Constant對話盒中，選取常數範圍與設定常數名，按下確定就可以了。

![image_thumb_31.png](/images/posts/16212/image_thumb_31.png)

![image_thumb_32.png](/images/posts/16212/image_thumb_32.png)

![image_thumb_33.png](/images/posts/16212/image_thumb_33.png)

**Clear Recent File List**
該功能能清除最近開啟檔案的清單，在主選單的[File]→[Recent Files]選單選項中，可看到最下面會多一個[Clear Recent File List]選單選項，點選後會帶出Clear List對話盒，選取要刪除的清單後確定即可。

![image_thumb_23.png](/images/posts/16212/image_thumb_23.png)

![image_thumb_24.png](/images/posts/16212/image_thumb_24.png)

**Clear Recent Project List**
該功能能清除最近開啟專案與方案的清單，在主選單的[File]→[Recent Projects and Solutions]選單選項中，可看到最下面會多一個[Clear Recent Project List]選單選項，點選後會帶出Clear List對話盒，選取要刪除的清單後確定即可。

![image_thumb_25.png](/images/posts/16212/image_thumb_25.png)

## Link

* [PowerCommands for Visual Studio 2010](http://visualstudiogallery.msdn.microsoft.com/en-us/e5f41ad9-4edc-4912-bca3-91147db95b99)
* [PowerCommands for Visual Studio 2008](http://code.msdn.microsoft.com/PowerCommands)
