---
title: "[C++]使用靜態函式庫(Static Library)開出類別給其他組件使用"
date: "2011-08-17 12:49:51"
description: "[C++]使用靜態函式庫(Static Library)開出類別給其他組件使用"
tags: [C++]
---

最近又開始要碰C++，雖然工作陸陸續續也寫了四年，但C++對我來說仍舊是個很陌生的東西。最近重拾C++的開發，碰到的第一個問題就是Dll組件中類別要如何才能開出給其他組件使用，經過同事的指導才知道原來使用靜態函式庫(Static Library)可以很快的將類別開出給其他組件使用，步驟也不困難，這邊老樣子隨筆做個記錄。

要建立靜態函式庫，在開發時我們可選用Win32 Project來做開發的動作。

![image_thumb.png](/images/posts/33350/image_thumb.png)

在Application Settings這頁將Application type設為Static library。

![image3_thumb.png](/images/posts/33350/image3_thumb.png)

當專案的設定精靈都設定完後，開啟專案屬性，切換至Configuration Properties\General頁面，會看到Configuration Type會是Static library (.lib)。若開發的專案是之前建立的，且是動態函式庫的話，可在這邊將其切換至Static library (.lib)。

![image6_thumb.png](/images/posts/33350/image6_thumb.png)

開發專案建立後，接著為其加入類別。

![image9_thumb.png](/images/posts/33350/image9_thumb.png)

![image12_thumb.png](/images/posts/33350/image12_thumb.png)

![image15_thumb.png](/images/posts/33350/image15_thumb.png)

類別加入後，為其加入類別的成員，這邊為了方便示範，僅加入個名為Test的成員方法，該方法被叫用時會彈出訊息框顯示Test的字樣。

![image21_thumb.png](/images/posts/33350/image21_thumb.png)

到此我們所需要的靜態函式庫就開發完畢了，簡單說起來他的重點只有要將專案屬性內Configuration Properties\General頁面中的Configuration Type設為Static library (.lib)，整個靜態函式庫就完成了。

靜態函式庫開發完畢接下來的重點就是要如何去使用開發出來的靜態函式庫，這邊我為開發方案加入個Win32 Console Application專案來示範一下。

![image18_thumb.png](/images/posts/33350/image18_thumb.png)

專案設定精靈設定完後，開啟專案屬性，切換至Configuration Properties\C/C++\General頁面，將Additional Include Directories加入剛剛靜態函式庫開發專案的目錄位置。

![image33_thumb.png](/images/posts/33350/image33_thumb.png)

接著再切換至Configuration Properties\Linker\Input頁面，設定Additional Dependencies，將靜態函式庫輸出檔的位置加入。

![image36_thumb.png](/images/posts/33350/image36_thumb.png)

到此前置準備動作就完成了，這時我們可以開啟需要引用靜態函式庫內類別的程式，加入類別標頭檔，這樣就可以建立靜態函式庫中的類別物件直接使用了。

![image39_thumb.png](/images/posts/33350/image39_thumb.png)

運行結果如下：

![image42_thumb.png](/images/posts/33350/image42_thumb.png)

這邊補充一下，當在程式中加入了靜態函式庫中的類別標頭檔，Visual Studio IDE會自動偵測用到的相依檔案，並更新開發專案下的External Dependencies目錄，可在External Dependencies目錄看到使用到的類別標頭檔。若開發上碰到不如預期的狀況，可以先從這邊檢查起，再向前檢查是否有少做的設定。

![image45_thumb.png](/images/posts/33350/image45_thumb.png)
