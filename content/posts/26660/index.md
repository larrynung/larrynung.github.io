---
title: "[IADP]C++ Intel AppUp Application Develop Process"
date: "2011-05-30 10:50:39"
description: "[IADP]C++ Intel AppUp Application Develop Process"
tags: [C++]
---

<p>
	在C++中開發IADP AppUp的應用程式，其程式的撰寫方式跟.NET程式很類似，使用的類別類似、認證程式碼類似、工具的使用上類似，所要特別注意的地方就是在C++中必須要設定一些lib、目錄、並加入一些標頭檔，並記得釋放掉資源。開發時，開發人員必須先行安裝Intel AppUp SDK 1.1.1 for Windows C/C++，為了加速開發，這邊可以順便安裝上Intel AppUp™ SDK Microsoft Visual Studio* IDE Plug-in。</p>
<p>
	 </p>
<p>
	安裝完Intel AppUp™ SDK Microsoft Visual Studio* IDE Plug-in後，在Visual Studio建立Win32 Windows Application，或是在建立MFC Application時，可看到精靈畫面會增加一個Use Intel AppUp(TM) SDK library的選項。</p>
<p>
	<img alt="image" border="0" height="524" src="\images\posts\26660\image_thumb_11.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="619" /></p>
<p>
	<img alt="image" border="0" height="524" src="\images\posts\26660\image_thumb.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="619" /></p>
<p>
	 </p>
<p>
	勾選Use Intel AppUp(TM) SDK library這個選項後，建立出來的應用程式專案即會滿足Intel AppUp開發的所有必要條件，像是在專案屬性設定Project&gt;Properties&gt;Configuration Properties&gt;Linker&gt;Input&gt;Additional Dependencies那邊</p>
<p>
	<img alt="image" border="0" height="351" src="\images\posts\26660\image18_thumb.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="597" /></p>
<p>
	<img alt="image" border="0" height="456" src="\images\posts\26660\image24_thumb.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="644" /></p>
<p>
	 </p>
<p>
	必須要加入下列lib檔：</p>
<p>
	<img alt="image" border="0" height="216" src="\images\posts\26660\image12_thumb.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="543" /></p>
<p>
	<img alt="image" border="0" height="216" src="\images\posts\26660\image15_thumb.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="543" /></p>
<p>
	 </p>
<p>
	Project&gt;Properties&gt;Configuration Properties&gt;Linker&gt;General&gt;Additional Library Directories必須設定、並將撰寫與編譯時所需要的Header檔的加入專案、與加入認證程式碼等，這些繁雜的設定Plug-In都幫我們完成了，開發人員只要專心建立自己的應用程式即可。</p>
<p>
	 </p>
<p>
	這樣的功能在我們新建Intel AppUp應用程式特別好用。但是若想把現有的專案發佈到Intel AppUp Center呢?其實Plug-In也有這方面功能的支援。</p>
<p>
	 </p>
<p>
	透過在程式碼編輯區中按下滑鼠右建，點選右鍵快顯選單中的[Add Header for Intel AppUp(TM) software]選單選項，Plug-In會幫我們自動帶入Include程式碼，會Include開發所需的adpcppf.h檔。</p>
<p>
	 <img alt="image" border="0" height="460" src="\images\posts\26660\image6_thumb.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="627" /></p>
<p>
	<img alt="image" border="0" height="272" src="\images\posts\26660\image9_thumb.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="462" /></p>
<p>
	 </p>
<p>
	再將滑鼠游標移至應用程式一開始建立的地方，按下滑鼠右鍵，點選右鍵快顯選單中的[Add Authorization Code for Intel AppUp(TM) software]選單選項，為應用程式加入Intel AppUp認證的功能。</p>
<p>
	<img alt="image" border="0" height="417" src="\images\posts\26660\image30_thumb.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="644" /></p>
<p>
	<img alt="image" border="0" height="449" src="\images\posts\26660\image42_thumb.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="621" /></p>
<p>
	 </p>
<p>
	此外，Intel AppUp C++應用程式開發所需要的必要條件都會在此時被加入，開發人員不需要手動再去處理。像是Project&gt;Properties&gt;Configuration Properties&gt;Linker&gt;Input&gt;Additional Dependencies的設定。</p>
<p>
	<img alt="image" border="0" height="436" src="\images\posts\26660\image_thumb_16.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="644" /></p>
<p>
	<img alt="image" border="0" height="394" src="\images\posts\26660\image_thumb_7.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="448" /></p>
<p>
	 </p>
<p>
	Project&gt;Properties&gt;Configuration Properties&gt;Linker&gt;General&gt;Additional Library Directories的設定。</p>
<p>
	<img alt="image" border="0" height="436" src="\images\posts\26660\image_thumb_15.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="644" /></p>
<p>
	 </p>
<p>
	與所需要的Header檔。</p>
<p>
	<img alt="image" border="0" height="271" src="\images\posts\26660\image1_thumb.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="274" /></p>
<p>
	 </p>
<p>
	最後在開發上還有個跟.NET程式不一樣但卻很重要的小步驟，那就是必須要記得在程式結束時，在程式碼編輯區按下滑鼠右建，點選右鍵快顯選單中的[Add Cleanup Code for Intel AppUp(TM) software]選單選項，加入刪除資源的程式碼，以避免資源洩漏。</p>
<p>
	<img alt="image" border="0" height="476" src="\images\posts\26660\image36_thumb.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="644" /></p>
<p>
	<img alt="image" border="0" height="390" src="\images\posts\26660\image39_thumb.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="638" /></p>
