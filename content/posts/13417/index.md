---
title: "[Visual Studio]Visual Studio 2010 New Feature - Call Hierarchy"
date: "2010-01-31 11:26:59"
description: "[Visual Studio]Visual Studio 2010 New Feature - Call Hierarchy"
tags: [Visual Studio]
---

<h2>
	Introduction</h2>
<p>
	Call Hierarchy是Visual Studio 2010的新功能之一，能讓開發人員快速的找到類別成員被參考使用到的地方、其所使用到的其它類別成員、覆寫的地方、與實作的地方。以往這樣的動作我們可能要透過搜尋、[Go To Define]、與[Find All References]來完成。透過Visual Studio 2010 Call Hierarchy的新功能，我們可以更為輕鬆快速的達到這個目的。</p>
<p>
	 </p>
<h2>
	Call Hierarchy Window</h2>
<p>
	若要檢視Call Hierarchy視窗，我們可透過[View]→ [Call Hierarchy]，或是按下熱鍵Ctrl+W,K叫起。</p>
<p>
	<img alt="image" border="0" height="243" src="\images\posts\13417\image6_thumb.png" style="border-right-width: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" title="image" width="436" /></p>
<p>
	 </p>
<p>
	也可以滑鼠游標直接移到類別成員上，按下滑鼠右鍵，在快顯選單中選取[View Call Hierarchy]選項。Visual Studio會帶出Call Hierarchy視窗，並把其類別成員加入其中。<br />
	<img alt="image" border="0" height="312" src="\images\posts\13417\image_thumb.png" style="border-right-width: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" title="image" width="484" /></p>
<p>
	 </p>
<p>
	Call Hierarchy視窗顯示上會像下面這樣。</p>
<p>
	<img alt="image" border="0" height="250" src="\images\posts\13417\image9_thumb.png" style="border-right-width: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" title="image" width="474" /></p>
<p>
	 </p>
<p>
	上方的工具列具有過濾的功能，可選取所要監看的結果是整個方案、目前專案、或是目前文件。</p>
<p>
	<img alt="image" border="0" height="250" src="\images\posts\13417\image15_thumb.png" style="border-right-width: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" title="image" width="474" /></p>
<p>
	 </p>
<p>
	還可以切換是否要詳細到顯示程式碼的資訊。</p>
<p>
	<img alt="image" border="0" height="250" src="\images\posts\13417\image18_thumb.png" style="border-right-width: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" title="image" width="474" /></p>
<p>
	 </p>
<p>
	在Call Hierarchy功能的使用上，當我們把類別成員加入Call Hierarchy視窗後，資料會用Tree的型態來表示。根節點會顯示所要觀察的類別成員名稱，而其子節點則會顯示出叫用該類別成員的其它地方、或是該類別成員所叫用的其它類別成員，甚至是覆寫的地方(當觀看的是抽象或虛擬成員時)、與實作的地方(當觀看的是介面成員時)。</p>
<p>
	<img alt="image" border="0" height="250" src="\images\posts\13417\image21_thumb.png" style="border-right-width: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" title="image" width="474" /></p>
<p>
	 </p>
<p>
	可自行針對有興趣的部份去作展開。像這邊展開[Calls To 'Balance']，就可以發現到只有Main這邊有使用到Balance。</p>
<p>
	<img alt="image" border="0" height="250" src="\images\posts\13417\image24_thumb.png" style="border-right-width: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" title="image" width="474" /></p>
<p>
	 </p>
<p>
	若想移至程式碼部分，透過滑鼠左鍵點選兩下即可。</p>
<p>
	<img alt="image" border="0" height="408" src="\images\posts\13417\image_thumb_1.png" style="border-right-width: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" title="image" width="421" /></p>
<p>
	 </p>
<p>
	也可以在右半邊的詳細列表中連點想觀看的程式碼部分，Visual Studio會自動幫您帶到程式碼中對應的地方。</p>
<p>
	<img alt="image" border="0" height="454" src="\images\posts\13417\image_thumb_4.png" style="border-right-width: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" title="image" width="418" /></p>
<p>
	 </p>
<p>
	值得注意的是，Call Hierarchy視窗在顯示上是採用階層式的顯示方式，所以像下方的Main函式也可以再作展開，可以讓我們做一層層的監看。</p>
<p>
	<img alt="image" border="0" height="418" src="\images\posts\13417\image27_thumb.png" style="border-right-width: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" title="image" width="527" /></p>
<p>
	 </p>
<p>
	若覺得一層層看很難看，我們也可以透過滑鼠右鍵，再彈出的快顯選單中點選[Add As New Root]。</p>
<p>
	<img alt="image" border="0" height="191" src="\images\posts\13417\image_thumb_10.png" style="border-right-width: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" title="image" width="518" /></p>
<p>
	 </p>
<p>
	就可以把有興趣的部分再提出成為根節點。</p>
<p>
	<img alt="image" border="0" height="186" src="\images\posts\13417\image_thumb_12.png" style="border-right-width: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" title="image" width="515" /></p>
<p>
	 </p>
<p>
	另外快顯選單中還有整合舊有的[Go To Definition]、與[Find All References]，有興趣的可自行試驗。</p>
