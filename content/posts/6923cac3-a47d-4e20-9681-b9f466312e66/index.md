---
title: "Regionerate - Code Layouts in a Snap"
date: "2013-11-06 12:00:00"
description: "Regionerate 是一能將程式碼依照選取的排版樣式去自動排序，以及分類整理成 Region 的輔助工具。能自行擴充、定義排版樣式，及命令列的支援，使用上非常的彈性好用。對於個人自行用來整理程式，或是團隊用來統一程式的排版，該工具都非常的合用。"
---

Regionerate 是一能將程式碼依照選取的排版樣式去自動排序，以及分類整理成 Region 的輔助工具。能自行擴充、定義排版樣式，及命令列的支援，使用上非常的彈性好用。對於個人自行用來整理程式，或是團隊用來統一程式的排版，該工具都非常的合用。

Regionerate 官方這邊所提供的版本目前僅支援到Visual Studio 2010。若是想在Visual Studio 2012上使用，可以到這邊使用網友修改的版本。若是想在Visual Studio 2013上使用，我們一樣可以使用前面提到的網友修改版本，不過要額外的手動做些設定動作，像是要找到安裝目錄下的Regionerate.VS2012.AddIn將之開啟，將Version從11.0改為12.0，然後將它另存為Regionerate.VS2013.AddIn。

![image_thumb.png](/images/posts/6923cac3-a47d-4e20-9681-b9f466312e66/image_thumb.png)

還有就是要開啟登錄編輯程式，在[HKEY_CURRENT_USER\Software\Microsoft\VisualStudio\12.0_Config\AutomationOptions\LookInFolders]這位置加上 "C:\Program Files (x86)\Regionerate\" 這個字串值。

![image_thumb_1.png](/images/posts/6923cac3-a47d-4e20-9681-b9f466312e66/image_thumb_1.png)

安裝完成後，我們可以在程式編輯區中短按熱鍵 Ctrl + R觸發，讓 Regionerate 套用預設的排版樣式下去整理當前的程式。像是下面這樣的程式…

![image_thumb_5.png](/images/posts/6923cac3-a47d-4e20-9681-b9f466312e66/image_thumb_5.png)

經過套用預設的排版樣式就會變成下面這樣，程式碼會依照Fields、Constructors、Properties、Methods這樣的架構下去重新排版。

![image_thumb_4.png](/images/posts/6923cac3-a47d-4e20-9681-b9f466312e66/image_thumb_4.png)

除了預設的這種排版樣式外，Regionerate 也內建了其它的排版樣式，像是Primary Code Layout、Cluster By Name、Order Members (With Comments)、Order Members (Without Regions)、Remove All Regions 、Contract、Entity、Unit Test、以及Utility這幾種。

若要套用非預設排版樣式，我們可以點擊 Visual Studio 上方 Tool 主選單的 Regionerate this 選單選項。

![image_thumb_7.png](/images/posts/6923cac3-a47d-4e20-9681-b9f466312e66/image_thumb_7.png)

或是在程式碼編輯視窗中按下滑鼠右鍵，在彈出的滑鼠右鍵快顯選單中，選取 Regionerate this 選單選項 。

![image_thumb_6.png](/images/posts/6923cac3-a47d-4e20-9681-b9f466312e66/image_thumb_6.png)

選取後 Regionerate 會彈出像下面這樣的視窗詢問整理所要依循的排版樣式，

![image_thumb_2.png](/images/posts/6923cac3-a47d-4e20-9681-b9f466312e66/image_thumb_2.png)

接著依個人使用需求下去選取就可以了，選取完 Regionerate 會自動幫我們依照選取的排版樣式下去將程式碼做整理的動作。

如果想用熱鍵來做這樣的動作，我們可以長按 Ctrl + R 觸發，視窗出來後按住Ctrl鍵，並持續的交替按下/放開R鍵，或是輔以數字鍵，一樣可以選取到想要套用的排版樣式。

![image_thumb_8.png](/images/posts/6923cac3-a47d-4e20-9681-b9f466312e66/image_thumb_8.png)

除了對單檔整理外，Regionerate 也支援對多檔的整理，在方案總管內的專案或是方案節點上按下滑鼠右鍵， 按下滑鼠右鍵，都可以看到 Regionerate this 這個熟悉的選單選項。

![image_thumb_11.png](/images/posts/6923cac3-a47d-4e20-9681-b9f466312e66/image_thumb_11.png)

![image_thumb_10.png](/images/posts/6923cac3-a47d-4e20-9681-b9f466312e66/image_thumb_10.png)

若是需要整合建置事件，或是三不五時就想手動或自動戳它做些整理， Regionerate 也提供 Command Line 的運行方式。

先將安裝目錄開啟，開啟後會看到  Regionerate 程式主要的執行檔，到命令提示字元下運行該執行檔，就可看到命令列模式的使用方式。

![image_thumb_12.png](/images/posts/6923cac3-a47d-4e20-9681-b9f466312e66/image_thumb_12.png)

簡單的說，大至上支援的參數有六個。target可指定要套用排版樣式的檔案、方案、或專案；layout用來指定要套用的排版樣式，若不指定則套用預設的排版樣式；ignoreFiles可指定要忽略不處理的檔案；ignoreProjects用來指定要忽略不處理的專案；noinfo與nowarn則是指定要關閉顯示一些信息或是警告。

這邊實際來看幾個例子加深一下印象。

如果要將My Special Layout這個排版樣式套用至Calculator這個專案，可以像下面這樣輸入：

```xml
rgn -target:Calculator.csproj -layout:My Special Layout.xml
```

如果要將預設排版樣式套用至Calculator這個專案，並將AssemblyInfo.cs、MainForm.cs、以及MainWindow.cs這幾個檔案忽略不予處理，可以像下面這樣輸入：

```xml
rgn -target:Calculator.csproj -ignoreFiles:"AssemblyInfo.cs|MainForm.cs|MainWindow.cs"
```

如果要將預設排版樣式套用至MathLib這個方案，並將Calculator、以及Graphs這兩個專案忽略不予處理，可以像下面這樣輸入：

```xml
rgn -target:MathLib.sln -ignoreProjects:"Calculator.csproj|Graphs.csproj"
```

如果要將預設排版樣式套用至Calculator這個專案，並將信息與警告的輸出關閉，可以像下面這樣輸入：

```xml
rgn -target:Calculator.csproj -noinfo –nowarn
```

最後我們再回過頭來看一下排版樣式…

如果這邊內建的排版樣式都不符需求， Regionerate 也提供了很大的彈性讓我們來自行訂製。

要進行排版樣式的客制之前，我們可先開啟程式安裝目錄，開啟DefaultCodeLayout排版樣式或是 My Code Layouts下方的排版樣式來做些參考。也可以開啟My Code Layouts下的CodeLayoutSchema.xsd進行交叉比對，裡面針對可以使用的Tag Element有很詳盡的定義，像是Tag Element是什麼型態、有什麼Attribute、有什麼子Tag Element、以及相關的說明，在裡面都找的到。

像是下面這邊我們就可以清楚的看到ForEach Tag Element裡面可以放置CreateRegion Tag Element，也可以設定Type以及SeparatingLines這兩個Attribute。SeparatingLines這邊也很明確的告訴我們型態是int，以及是用來空行用的。

![image_thumb_14.png](/images/posts/6923cac3-a47d-4e20-9681-b9f466312e66/image_thumb_14.png)

簡單的來說，排版樣式檔最外圍的就是 ForEach 與  Configuration 這兩個節點。

利用ForEach節點，我們可以設定要處理的是Class、Struct、還是Interface型態。

```xml
...
<ForEach Type="Class">
	...
</ForEach>
<ForEach Type="Struct">
	...
</ForEach>
<ForEach Type="Interface">
	...
</ForEach>
...
```

ForEach內可以使用CreateRegion來做註解或是Region。Title attribute可指定該Region或是註解要顯示的字串，Style屬性可用來設定Region是Visible、Invisible、還是Comment，PadFirstChild、PadLastChild則是決定區塊前後要空幾行。

```xml
...
<ForEach Type="Class">
  ...
  <CreateRegion Title="Delegates and Events" Style="Comment" PadFirstChild="0" PadLastChild="0">
    ...
  </CreateRegion>
  <CreateRegion Title="Fields" Style="Invisible" PadFirstChild="0" PadLastChild="0">
    ...
  </CreateRegion>
  ...
</ForEach>
...
```

CreateRegion內可放置CreateRegion、PutDelegates、PutFields、PutEnums、PutEvents、PutProperties、PutMethods、與PutNestedClasses這幾個Tag Element，依需求決定要放置的Tag Element，像是要建立巢狀的Region，我們可以在CreateRegion內在放置CreateRegion Tag Element；要在Region內放置欄位，我們可以在CreateRegion內放置PutFields Tag Element；要在Region內放置屬性，我們可以在CreateRegion內放置PutPropertiesTag Element…其它以此類推。

```xml
...
<ForEach Type="Class">
    ...
    <CreateRegion Title="Fields" Style="Invisible">
      <PutFields>
        ...
      </PutFields>
    </CreateRegion>
    ...
</ForEach>
...
```

在PutDelegates、PutFields、PutEnums、PutEvents、PutProperties、PutMethods、與PutNestedClasses這幾個Tag Element裡面，我們可以下過濾與排序的條件，過濾的條件用Where Tag Element下去設定，排序用Order Tag Element下去設定。

```c
...
<ForEach Type="Class">
  ...
  <CreateRegion Title="Constructors" Style="Invisible">
    ...
    <PutMethods>
      <Where>
        <IsConstructor Equals="true" />
      </Where>
      <OrderBy>
        <ParametersCount Direction="Descending" />
      </OrderBy>
    </PutMethods>
    ...
  </CreateRegion>
  ...
</ForEach>
...
```

因為每個Type他能接受的參數與子Tag Element不盡相同，這邊在對於排版樣式的設定只是初略的帶過，實際在設定前還是請先看一下CodeLayoutSchema.xsd。

以筆者個人來說，會傾向依Field、Property、Event、Constructor、Method以及依照修飾詞Private、Protected、Public這樣的順序排放，所以稍稍的修改一下排版樣式，有需要的可以至這邊自取…

## Link

* Regionerate - Code Layouts in a Snap - rauchy.net
* Regionerate extension - Visual Studio Gallery – Microsoft
* [工具介紹]Regionerate for Visual Studio - In 91- 點部落
* Using Regionerate on VS2012, or alternative addin - Stack Overflow
