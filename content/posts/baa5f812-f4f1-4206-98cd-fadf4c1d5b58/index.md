---
title: "Visual Studio 2013 Preview New Feature - Peek Definition"
date: "2013-11-06 12:00:00"
description: "Visual Studio 2013 Preview New Feature - Peek Definition"
---

<p>
	Peek Definition是Visual Studio 2013 Preview的新功能，支援<span style="color: rgb(42, 42, 42); font-family: 'Segoe UI', 'Lucida Grande', Verdana, Arial, Helvetica, sans-serif; font-size: 13px; line-height: 18px;">C#,、Visual Basic,、與C++</span>。以往我們在查閱定義時必須使用內建的移至定義功能跳至定義的地方，如果是定義在同一份文件，Visual Studio會將編輯區移至定義處，若是定義在別的文件中，則Visual Studio會開啟定義所在的文件，並將編輯區帶至定義處。這樣的作法很容易就造成程式編輯的動作被中斷，有時候可能只是要稍微看一下定義是放在哪邊，正在編輯的位置就被帶走，看完後可能又要找尋一下剛剛編到了哪邊。Peek Definition功能的出現改善了這個問題，定義的內容改以類似內嵌的方式呈現，可以以較不受打擾的方式同時查看目前所在編輯的程式以及定義的部分。</p>
<p>
	 </p>
<p>
	Peek Definition在使用上非常的簡單，只要在要查看的地方按下熱鍵Alt + F12，或是透過滑鼠右鍵快顯選單選取查看定義的滑鼠右鍵選單選項。</p>
<p>
	<img alt="image" border="0" height="315" src="\images\postsaa5f812-f4f1-4206-98cd-fadf4c1d5b58\image_thumb_6.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="644" /></p>
<p>
	 </p>
<p>
	編輯區的程式碼就會被推開，並在其中內嵌一個Peek Definition Window查看的定義內容。該Peek Definition Window只供查看定義，以及複製拖曳部分程式碼到編輯區，無法進行任何的編輯動作。(若要在編輯區與Peek Definition Window間進行切換，可用熱鍵Shift+Esc)</p>
<p>
	<img alt="image" border="0" height="207" src="\images\postsaa5f812-f4f1-4206-98cd-fadf4c1d5b58\image_thumb_7.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="644" /></p>
<p>
	 </p>
<p>
	要關閉Peek Definition Window的話，按下Peek Definition Window右上方的頁籤關閉按鈕，或是按下熱鍵ESC即可。</p>
<p>
	 </p>
<p>
	在Peek Definition Window中若有需要，這邊也允許再次查看定義。</p>
<p>
	<img alt="image" border="0" height="227" src="\images\postsaa5f812-f4f1-4206-98cd-fadf4c1d5b58\image_thumb_8.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="644" /></p>
<p>
	 </p>
<p>
	這樣會讓Peek Definition Window產生分頁，使用上可透過上方的巡覽列或是熱鍵 Ctrl+Alt+- 與 Ctrl+Alt+= 進行切換查閱。</p>
<p>
	<img alt="image" border="0" height="188" src="\images\postsaa5f812-f4f1-4206-98cd-fadf4c1d5b58\image_thumb_11.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="644" /></p>
<p>
	 </p>
<p>
	其它還有些細部的操作，大概就跟Visual Studio的分頁頁籤一樣，沒甚麼要特別留意的，這邊稍稍的帶一下。</p>
<p>
	 </p>
<p>
	像是滑鼠移至Peek Definition Window右上方的頁籤，可以看到檔案詳細的位置。</p>
<p>
	<img alt="image" border="0" height="90" src="\images\postsaa5f812-f4f1-4206-98cd-fadf4c1d5b58\image_thumb_9.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="644" /></p>
<p>
	 </p>
<p>
	若有需要將定義的部分變成一般的編輯文件頁籤，可以按下Peek Definition Window關閉按鈕旁的小圖示，或是按下熱鍵Shift+Alt+Home，這邊跟以前的File Preview功能是類似的。</p>
<p>
	<img alt="image" border="0" height="159" src="\images\postsaa5f812-f4f1-4206-98cd-fadf4c1d5b58\image_thumb_10.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="370" /></p>
<p>
	<img alt="image" border="0" height="180" src="\images\postsaa5f812-f4f1-4206-98cd-fadf4c1d5b58\image_thumb_3.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="659" /></p>
<p>
	 </p>
<p>
	最後附上相關的熱鍵表。</p>
<p>
	<img alt="image" border="0" height="327" src="\images\postsaa5f812-f4f1-4206-98cd-fadf4c1d5b58\image_thumb_12.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="601" /></p>
<p>
	 </p>
<h2>
	Link</h2>
<ul>
	<li>
		How to: Use Peek Definition</li>
</ul>
