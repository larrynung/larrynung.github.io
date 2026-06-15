---
title: "P4Merge - Visual Merge and Diff Tools"
date: "2013-11-06 12:00:00"
description: "P4Merge - Visual Merge and Diff Tools"
tags: [P4Merge]
---

P4Merge是PERFORCE底下用來比對與合併檔案的工具程式,跟Winmerge的功能與用途類似,但更為方便好用,且對於像筆者這樣的色弱來說,呈現的方式也更為友善 。

P4Merge是免費的軟體,安裝包可至PERFORCE官網下載。

![1_thumb_1.jpg](/images/posts/57047a0a-0800-4ea3-ac4a-8142f36eda42/1_thumb_1.jpg)

![image_thumb.png](/images/posts/57047a0a-0800-4ea3-ac4a-8142f36eda42/image_thumb.png)

下載後將之點擊安裝

![image_thumb_1.png](/images/posts/57047a0a-0800-4ea3-ac4a-8142f36eda42/image_thumb_1.png)

因為P4Merge是免費的,但其它元件不是,所以安裝這邊要將其它的元件取消選取,讓其只安裝P4Merge元件

![ScreenClip_thumb.jpg](/images/posts/57047a0a-0800-4ea3-ac4a-8142f36eda42/ScreenClip_thumb.jpg)

![image_thumb_16.png](/images/posts/57047a0a-0800-4ea3-ac4a-8142f36eda42/image_thumb_16.png)

![image_thumb_17.png](/images/posts/57047a0a-0800-4ea3-ac4a-8142f36eda42/image_thumb_17.png)

![Untitled%20Note%20Image_thumb.jpg](/images/posts/57047a0a-0800-4ea3-ac4a-8142f36eda42/Untitled%20Note%20Image_thumb.jpg)

安裝完後將之點擊開啟

![ScreenClip.6_thumb.png](/images/posts/57047a0a-0800-4ea3-ac4a-8142f36eda42/ScreenClip.6_thumb.png)

開啟後會看到Choose Files對話框，透過這個對話框我們可以指定是要比對還是合併，也可以指定對應處理所需要的檔案。

![ScreenClip.2_thumb.png](/images/posts/57047a0a-0800-4ea3-ac4a-8142f36eda42/ScreenClip.2_thumb.png)

設定完後會進到像下面這樣的主畫面，以檔案的比對來說， 它會切隔為左右兩個窗格，分別顯示我們要做比對的兩個檔案，左右兩邊如有差異會有高亮標記，且兩個窗格間會有輔助線輔輔助，可以清楚看到左側這塊內容對應到右側哪一塊，在比對上會比較容易。

![ScreenClip.9_thumb.jpg](/images/posts/57047a0a-0800-4ea3-ac4a-8142f36eda42/ScreenClip.9_thumb.jpg)

上方工具列有工具可供比對時快速的巡覽至衝突的位置。

若要針對檔案內容進行修正，以修改左側開啟的檔案為例，我們可以點擊工具列上的 [Edit file in left panel] 按鈕。

![ScreenClip.7_thumb.jpg](/images/posts/57047a0a-0800-4ea3-ac4a-8142f36eda42/ScreenClip.7_thumb.jpg)

按下後下方會多出一個窗格，用以做內容的修改，預設的內容就是我們選取要編輯的檔案，比對時發現衝突的地方在這個窗格一樣會高亮顯示，在高亮的後方會有按鈕列，可供我們在編輯時快速的套用左右兩邊的內容。像是如果今天衝突的這行應該用右側窗格所對應的內容的話，可以直接點擊該行後方工具列上代表右側窗格的那個按鈕，該行內容既會被替換。

![ScreenClip.11_thumb.jpg](/images/posts/57047a0a-0800-4ea3-ac4a-8142f36eda42/ScreenClip.11_thumb.jpg)

合併的處理跟比對類似，這邊就不多做介紹。

最後要提醒一下，在進行比對動作前，需先注意到檔案一開始這邊是否有出現亂碼。

如果有發現亂碼，代表編碼這邊設定不正確，此時若去比對儲存，可能會讓檔案內容連帶變得不正確。此時需透過 [File/Character Encoding] 主選單選項去設定正確的編碼，通常是設為Unicode (UTF-8, no BOM)，設定完檔案內容應該就會恢復正常，不再有亂碼。

![ScreenClip.4_thumb.jpg](/images/posts/57047a0a-0800-4ea3-ac4a-8142f36eda42/ScreenClip.4_thumb.jpg)

另外若是比對時找出過多的衝突，可試著勾選 [File/Comparison Method/Ignore Line Ending and All White Space Differences] 主選單選項，可以忽略掉因換行與空格所造成的衝突，有助於減少要解決的衝突。

![ScreenClip.5_thumb.jpg](/images/posts/57047a0a-0800-4ea3-ac4a-8142f36eda42/ScreenClip.5_thumb.jpg)

若要修改預設就套用編碼或是忽略換行與空白，也可以透過 Preferences 對話框去做對應的設定。

![ScreenClip.8_thumb.jpg](/images/posts/57047a0a-0800-4ea3-ac4a-8142f36eda42/ScreenClip.8_thumb.jpg) ![ScreenClip.3_thumb.jpg](/images/posts/57047a0a-0800-4ea3-ac4a-8142f36eda42/ScreenClip.3_thumb.jpg)

#### Link

* [Visual Merge and Diff Tools](http://www.perforce.com/product/components/perforce-visual-merge-and-diff-tools)
