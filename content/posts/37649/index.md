---
title: "[Visual Studio]Visual Studio 2011 Preview New Feature - C++ IDE improvements"
date: "2011-09-25 11:02:04"
description: "[Visual Studio]Visual Studio 2011 Preview New Feature - C++ IDE improvements"
tags: [Visual Studio,C++]
---

<p>
	Visual Studio 2011 Preview對C++的開發做了些改進，有些改進的是從VC6開始就存在的問題，像是Intellisense彈不太出來，或是Intellisense不夠聰明，在Visual Studio 2011 Preview都做了改善，為C++開發人員提供了更友善的開發環境。這邊筆者在此篇做些簡單的整理與介紹：</p>
<p>
	 </p>
<h3>
	Semantic colorization</h3>
<p>
	Visual Studio 2011 Preview 在『Options\Environment\Fonts and Colors』中，新增了許多C++的可設定項目，開發人員可依需求將C++的編輯環境顏色與字型做些調整。</p>
<p>
	<img alt="image" border="0" height="376" src="\images\posts\37649\image_thumb.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="644" /></p>
<p>
	 </p>
<h3>
	Highlighting reference</h3>
<p>
	Highlighting reference功能筆者在[Visual Studio]Visual Studio 2010 New Feature – Highlight Reference已有做過了介紹，此功能第一次是在Visual Studio 2010被釋出，但是當時只支援C#與VB.NET，而在Visual Studio 2011 Preview時將C++也給補齊。</p>
<p>
	 </p>
<p>
	該功能能依選取的變數下去處理，將其他用到的地方給標記起來。</p>
<p>
	<img alt="image" border="0" height="534" src="\images\posts\37649\image_thumb_3.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="511" /></p>
<p>
	 </p>
<p>
	並能快速的透過『Ctrl + Shift + Up』向下，或是透過『Ctrl + Shift + Down』向下巡覽。</p>
<p>
	<img alt="image" border="0" height="534" src="\images\posts\37649\image_thumb_5.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="511" /></p>
<p>
	<img alt="image" border="0" height="534" src="\images\posts\37649\image_thumb_4.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="511" /></p>
<p>
	 </p>
<p>
	當不希望啟用該功能時，也能將其關閉，只要透過『Tools\Options...』將設定選項對話框開啟，切換至『Text Editor\C/C++\Advanced』設定頁面，再將『Disable Reference Highlighting』設為True就可以了。</p>
<p>
	<img alt="image" border="0" height="376" src="\images\posts\37649\image_thumb_2.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="644" /></p>
<p>
	 </p>
<h3>
	List Member enhancements</h3>
<p>
	Visual Studio 2011 Preview針對C++的List Member功能也做了些調整，列出的清單可以依自己的需求選用不同的過濾策略。透過透過『Tools\Options...』將設定選項對話框開啟，切換至『Text Editor\C/C++\Advanced』設定頁面，可看到『Member List Filter Mode』的下拉清單內有None、Prefix、Smart、與Fuzzy這幾個過濾策略可以選取。</p>
<p>
	<img alt="image" border="0" height="376" src="\images\posts\37649\image_thumb_1.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="644" /></p>
<p>
	 </p>
<p>
	Prefix策略就是一般以往我們在用的，也就是列出的成員必須要以我們在編輯區輸入的字串為開頭才會顯示。</p>
<p>
	<img alt="image" border="0" height="162" src="\images\posts\37649\image_thumb_6.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="644" /></p>
<p>
	 </p>
<p>
	而Fuzzy就是像是Visual Studio 2010在其他語言做的改進，過濾的比對上會比較聰明點。</p>
<p>
	<img alt="image" border="0" height="134" src="\images\posts\37649\image_thumb_8.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="644" /></p>
<p>
	<img alt="image" border="0" height="160" src="\images\posts\37649\image_thumb_17.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="644" /></p>
<p>
	 </p>
<h3>
	C++/CLI IntelliSense</h3>
<p>
	C++/CLI在Visual Studio 2010基於某些考量暫時拿掉了IntelliSense功能，開發實非常的痛苦，Visual Studio 2011 Preview又將該功能放回去了，因此在Visual Studio 2011 Preview中像是Quick Info,、Parameter Help、 List Members、與Auto Completion現在都能夠正常的運作。</p>
<p>
	 </p>
<h3>
	C++ code snippets</h3>
<p>
	Visual Studio 2011 Preview開始支援C++的Code Snippet，在C++上的開發便利了許多。</p>
<p>
	<img alt="image" border="0" height="463" src="\images\posts\37649\image_thumb_9.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="514" /></p>
<p>
	<img alt="image" border="0" height="259" src="\images\posts\37649\image_thumb_10.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="458" /></p>
<p>
	 </p>
<h3>
	Surround With</h3>
<p>
	Visual Studio 2011 Preview開始C++也支援了Sorround With功能，用過C#的對此功能就不陌生，該功能能透過選取一段程式碼片段，透過Sorroud With將程式碼片段套到指定的樣板。</p>
<p>
	<img alt="image" border="0" height="423" src="\images\posts\37649\image_thumb_7.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="545" /></p>
<p>
	<img alt="image" border="0" height="224" src="\images\posts\37649\image_thumb_18.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="432" /></p>
<p>
	 </p>
<h3>
	Upgrading project</h3>
<p>
	在C++專案的屬性設定內有兩個跟編譯環境有關的設定，一個是TargetFramework，一個是Plateform Toolset，當偵測到設定是舊的編譯器時，Visual Studio 2011 Preview方案總管上的右鍵選單會多出個『Upgrade...』選單選項，能快速的讓開發人員將設定改為新的編譯環境設定。</p>
<p>
	<img alt="image" border="0" height="667" src="\images\posts\37649\image_thumb_11.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="554" /></p>
<p>
	 </p>
<p>
	升級的過程會在輸出視窗顯示細部資訊。</p>
<p>
	<img alt="image" border="0" height="152" src="\images\posts\37649\image_thumb_12.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="644" /></p>
<p>
	 </p>
<h3>
	Templates</h3>
<p>
	在Visual Studio 2011 Preview以前，Visual Studio是不支援C++客製化樣板的，從Visual Studio放樣版的目錄就可以知道，以往只支援C#、VB.NET、與Web。</p>
<p>
	<img alt="image" border="0" height="412" src="\images\posts\37649\image_thumb_15.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="617" /></p>
<p>
	 </p>
<p>
	在Visual Studio內的『File\Export Template...』功能也是被Disable的。</p>
<p>
	<img alt="image" border="0" height="458" src="\images\posts\37649\image_thumb_16.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="393" /></p>
<p>
	 </p>
<p>
	Visual Studio 2011 Preview開始支援C++的客製化樣板功能，一樣來看一下Visual Studio放樣版的目錄，相較於以往的目錄，我們可以很清楚的知道C++、與JavaScript也開始支援了。</p>
<p>
	<img alt="image" border="0" height="412" src="\images\posts\37649\image_thumb_13.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="617" /></p>
<p>
	 </p>
<p>
	在Visual Studio中『File\Export Template...』也Enable了。</p>
<p>
	<img alt="image" border="0" height="414" src="\images\posts\37649\image_thumb_14.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="367" /></p>
<p>
	 </p>
<h3>
	Code Analysis</h3>
<p>
	Code Analysis功能在Visual Studio 2011 Preview也做了一點改善，以往要跑程式碼分析我們只能在『Project\Properties...』做設定，也只能在建置時自動運行。但也不是每個人都真的想在每次建置時去跑這樣的分析，不僅增加等待的時間，分析出來的結果也不一定都會去看。</p>
<p>
	<img alt="image" border="0" height="458" src="\images\posts\37649\image_thumb_24.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="644" /></p>
<p>
	 </p>
<p>
	在Visual Studio 2011 Preview對此做了些調整，程式碼分析能在想做的時候再做，透過滑鼠右鍵在方案總管上叫出右鍵快顯選單，點選『Run Code Analysis On Solution』選單選項，或是透過點選『Build\Run Code Analysis On Solution』選單選項，我們可以隨時運行程式碼分析。</p>
<p>
	<img alt="image" border="0" height="388" src="\images\posts\37649\image_thumb_23.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="644" /></p>
<p>
	<img alt="image" border="0" height="439" src="\images\posts\37649\image_thumb_28.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="644" /></p>
<p>
	 </p>
<p>
	分析出來的資料會顯示在『Code Analysis』工具視窗。 </p>
<p>
	<img alt="image" border="0" height="534" src="\images\posts\37649\image_thumb_20.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="511" /></p>
<p>
	 </p>
<p>
	可以直接用滑鼠點選查看 ，點選後除了會顯是詳細的資訊外，編輯區會自動帶至對應的位置。</p>
<p>
	<img alt="image" border="0" height="437" src="\images\posts\37649\image_thumb_21.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="644" /></p>
<p>
	 </p>
<p>
	若要切換分析規則，可點選『Code Analysis』工具視窗上方工具列的設定按鈕，在彈出的設定視窗進行調整。</p>
<p>
	<img alt="image" border="0" height="371" src="\images\posts\37649\image_thumb_22.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="644" /></p>
<p>
	 </p>
<h3>
	Call Hierarchy</h3>
<p>
	Call Hierarchy功能也是自Visual Studio 2010開始有的功能，當初也是只支援C#開發環境，在Visual Studio 2011 Preview中C++開發人員也可以享受該功能帶來的便利了。Call Hierarchy簡單說來就是能讓開發人員了解方法被誰呼叫、與呼叫了哪些方法，有點類似於設計階段的呼叫堆疊。</p>
<p>
	 </p>
<p>
	使用時只要在想查看的方法上點選滑鼠右鍵，在彈出的滑鼠右鍵快顯選單中選取『View Call Hierarchy』選單選項。</p>
<p>
	<img alt="image" border="0" height="484" src="\images\posts\37649\image_thumb_29.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="639" /></p>
<p>
	 </p>
<p>
	Visual Studio會帶出『Call Hierarchy』工具視窗，詳細的使用步驟筆者在[Visual Studio]Visual Studio 2010 New Feature – Call Hierarchy已有詳細的介紹，這邊不做贅述。</p>
<p>
	<img alt="image" border="0" height="484" src="\images\posts\37649\image_thumb_30.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="638" /></p>
<p>
	 </p>
<h3>
	Dependency Graphic</h3>
<p>
	Dependency Graphic一樣是Visual Studio 2010就有的功能，C++自Visual Studio 2011 Preview開始支援，能讓開發人員了解程式中的相依關係。使用時可在編輯區中按下滑鼠右鍵，在彈出的滑鼠右鍵快顯選單中，點選『Generate Graph of Include Files』快顯選單選項。</p>
<p>
	<img alt="image" border="0" height="480" src="\images\posts\37649\image_thumb_25.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="536" /></p>
<p>
	 </p>
<p>
	或是透過主視窗上方選單『Archicteure\Generate Dependenct Graph』產生相依圖形。</p>
<p>
	<img alt="image" border="0" height="392" src="\images\posts\37649\image_thumb_27.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="644" /></p>
<p>
	 </p>
<p>
	產生的相依圖形會像下面這樣，可以看到彼此間的關係。</p>
<p>
	<img alt="image" border="0" height="437" src="\images\posts\37649\image_thumb_26.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="644" /></p>
<p>
	 </p>
<h2>
	Link</h2>
<ul>
	<li>
		[Visual Studio]Visual Studio 2010 New Feature – Highlight Reference</li>
</ul>
