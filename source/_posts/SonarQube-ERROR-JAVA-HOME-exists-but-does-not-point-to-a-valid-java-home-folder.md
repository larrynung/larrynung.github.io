---
title: >-
  SonarQube - ERROR: JAVA_HOME exists but does not point to a valid java home
  folder
date: 2018-01-23 00:34:31
tags: [SonarQube]
---

運行 SonarQubeAnalyze 後如果看到 ERROR: JAVA_HOME exists but does not point to a valid java home folder 這樣的錯誤訊息。  


<!-- More -->

{% asset_img 1.png %}
 
<br/>


我們可能會查閱系統中的 JAVA_HOME 環境變數，且查驗該環境變量所指定的位置是否存在，及是否指到正確的目錄。。。等。  

<br/> 


查驗過後你可能會發現一切都是正常的卻運行不起來。這是因為在 SonarQubeAnalyze 檔中有去設定 JAVA_HOME 的位置，該位置並非環境變量所指定的位置，而是指到 sonar-scanner 下的 jre 目錄。  

{% asset_img 2.png %}
 
<br/>


所以問題發生的話，可以檢查一下 sonar-scanner 下的 jre 目錄看看。像是筆者碰到的狀況就是因為沒將檔案加入並上傳到 git，從 git 拉下來的 jre 目錄在有少檔的狀況下就無法正常的運作。  

{% asset_img 3.png %}
 
<br/>
