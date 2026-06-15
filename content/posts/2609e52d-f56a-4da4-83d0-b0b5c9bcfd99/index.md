---
title: "[IronPython]IronPython開發環境的安裝與設定"
date: "2013-11-06 12:00:00"
description: "[IronPython]IronPython開發環境的安裝與設定"
tags: [Python]
---

身為以程式開發為樂的程式開發人員，在蛇年玩蛇也是一件很合理的事。但是玩蛇也是要準備好工具的，而筆者的.NET背景又比其他語言濃厚，幾經思量最後還是選擇了IronPython，因為它可以同時使用.NET Framework與Python兩邊的類別庫，不論是用來慢慢熟悉Python語法，或是用來搭配.NET這邊的開發都會比較容易。

IronPython在官網下載後安裝，會看到程式集內會多兩個IronPython Console。

![image_thumb_3.png](/images/posts/2609e52d-f56a-4da4-83d0-b0b5c9bcfd99/image_thumb_3.png)

透過這兩個IronPython Console，我們可以在裡面撰寫並測試IronPython。

![image_thumb_2.png](/images/posts/2609e52d-f56a-4da4-83d0-b0b5c9bcfd99/image_thumb_2.png)

除此之外IronPython運行所需要的元件也都隨著安裝進去了，所以我們也可以將程式寫到附檔名為.py的檔案之中，再透過Ipy下去運行。

![image_thumb_4.png](/images/posts/2609e52d-f56a-4da4-83d0-b0b5c9bcfd99/image_thumb_4.png)

準備IronPython的開發環境就是那麼簡單。但這樣的開發環境對於熟悉.NET的開發人員還是不太夠，捨棄地表最強的編譯環境改用記事本總是有種自廢武功的感覺。因此這邊我們可以為Visual Studio加掛Python Tools for Visual Studio，讓我們可以透過Visual Studio來進行Python的開發與除錯。

Python Tools for Visual Studio安裝完後，開啟Visual Studio可以發現在Other Languages下多了Python，裡面有個Python Application的專案樣板可以使用。透過這個樣板建立一個專案，我們就可以進行Python的開發。

![image_thumb_1.png](/images/posts/2609e52d-f56a-4da4-83d0-b0b5c9bcfd99/image_thumb_1.png)

專案建立後，預設會有個Hello world的Python code，這邊我們就直接用這Code來做測試，按下F5運行。運行後可以發現開發環境的設定還不夠周全，會彈出像下面這樣的錯誤對話框。

![ScreenClip_thumb.png](/images/posts/2609e52d-f56a-4da4-83d0-b0b5c9bcfd99/ScreenClip_thumb.png)

這是因為Python Tools for Visual Studio不知道Python Interpreter在哪邊所致。這邊只要開啟Options對話框，切到Python Tools下的Interpreter Options，然後按下右側的Add Interpreter，設定Interpreter的名稱。

![ScreenClip(1)_thumb.png](/images/posts/2609e52d-f56a-4da4-83d0-b0b5c9bcfd99/ScreenClip%281%29_thumb.png)

以及Interpreter所在的位置就可以了。

![ScreenClip(2)_thumb.png](/images/posts/2609e52d-f56a-4da4-83d0-b0b5c9bcfd99/ScreenClip%282%29_thumb.png)

順帶一提，這邊可能需要切換到Python Tools下的Advanced，額外勾選"Wait for input when process exits normally"這個選項，不然運行Python時主控台視窗可能會一閃而過。

![ScreenClip(3)_thumb.png](/images/posts/2609e52d-f56a-4da4-83d0-b0b5c9bcfd99/ScreenClip%283%29_thumb.png)

都設定好後再次按下F5運行，就可以看到正常的將Python運行起來了。

![image_thumb.png](/images/posts/2609e52d-f56a-4da4-83d0-b0b5c9bcfd99/image_thumb.png)

## Link

* IronPython
* IronPython
* Python Tools for Visual Studio
