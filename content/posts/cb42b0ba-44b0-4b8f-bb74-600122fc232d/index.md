---
title: "[Visual Studio]View JSON Strings with JSON Viewer"
slug: "visual-studio-view-json-strings-with-json-viewer"
aliases: ["/posts/cb42b0ba-44b0-4b8f-bb74-600122fc232d/"]
date: "2013-11-06 12:00:00"
tags: [Visual Studio]
description: "從JSON Viewer這邊下載壓縮包後解壓縮，可看到安裝包中有包含下列檔案： Fiddler目錄內是Fiddler用的外掛，JsonView目錄內是可單獨運行的JSON Viewer。 而Visualizer目錄下則放的是Visual Studio用的Visualizer，也是今天這篇要帶的重點。"
---

從JSON Viewer這邊下載壓縮包後解壓縮，可看到安裝包中有包含下列檔案：

![image16_thumb.png](/images/posts/cb42b0ba-44b0-4b8f-bb74-600122fc232d/image16_thumb.png)

Fiddler目錄內是Fiddler用的外掛，JsonView目錄內是可單獨運行的JSON Viewer。

![image19_thumb.png](/images/posts/cb42b0ba-44b0-4b8f-bb74-600122fc232d/image19_thumb.png)

而Visualizer目錄下則放的是Visual Studio用的Visualizer，也是今天這篇要帶的重點。因為壓縮包內Visualizer目錄下的檔案筆者在Visual Studio 2012下測試有點問題，這邊可能要下載原始碼後自行編譯。編譯後我們需將產生的組件放置VisualStudioInstallPath\Common7\Packages\Debugger\Visualizers或是My Documents\VisualStudioVersion\Visualizers位置下。

![image_thumb.png](/images/posts/cb42b0ba-44b0-4b8f-bb74-600122fc232d/image_thumb.png)

放置完畢在Visual Studio除錯時遇到JSON字串，點選前方的放大鏡。

![image4_thumb.png](/images/posts/cb42b0ba-44b0-4b8f-bb74-600122fc232d/image4_thumb.png)

JSON Viewer就會跑出來，整個除錯的畫面會像下面這樣，這樣除錯起來是不是方便了許多？

![image8_thumb.png](/images/posts/cb42b0ba-44b0-4b8f-bb74-600122fc232d/image8_thumb.png)

![image11_thumb.png](/images/posts/cb42b0ba-44b0-4b8f-bb74-600122fc232d/image11_thumb.png)

## Link

* [JSON Viewer](http://jsonviewer.codeplex.com/)
* [JSON Debugger visualizer in Visual Studio 2012](http://weblogs.asp.net/soever/archive/2013/03/03/json-debugger-visualizer-in-visual-studio-2012.aspx)
