---
title: "vscode-hexo - VSCode extension to manage hexo commands"
date: "2017-08-13 16:31:10"
tags: [Hexo, Visual Studio Code]
---


vscode-hexo 是 VSCode 的擴充套件，能讓我們在 VSCode 內簡易的調用 Hexo 命令。  

<!-- More -->

<br/>


按下熱鍵 Ctrl-Shift-P / Cmd-Shift-P 開啟 command palette，輸入 Extensions:Install Extensions，輸入 hexo 找到 vscode-hexo 擴充套件進行安裝。   

![1.png](1.png)

<br/>


安裝完後重啟 VSCode。  

![2.png](2.png)

<br/>


![3.png](3.png)

<br/>


點選 [File | Open...] 將 Hexo 部落格目錄開啟。  

![4.png](4.png)

<br/>


![5.png](5.png)

<br/>


按下熱鍵 Ctrl-Shift-P / Cmd-Shift-P，輸入 Hexo 即可看到可用的 Hexo 命令。  

    - hexo init         # Initializes a website
    - hexo new          # Creates a new article
    - hexo generate     # Generates static files
    - hexo publish      # Publishes a draft
    - hexo server       # Starts a local server
    - hexo stop         # stop a local server(Ctrl-C)
    - hexo deploy       # Deploys your website
    - hexo clean        # Cleans the cache file (db.json) and generated files (public)

<br/>


像是 hexo:hexo new 可以用來建立文章。  

![6.png](6.png)

<br/>


選擇要建立的是文章、頁面、或是草稿。  

![7.png](7.png)

<br/>


要建立文章的話輸入 post 後按下 Enter。  

![8.png](8.png)

<br/>


接著輸入文章的標題後按下 Enter，記住文章的標題要用雙引號包著。  

![9.png](9.png)

<br/>


文章就會被建立起來。  

![10.png](10.png)

<br/>
 

要起 Hexo Server 查看部落格文章的話，可按下 Ctrl-Shift-P / Cmd-Shift-P，輸入 Hexo 後選取 hexo: hexo server。  

![11.png](11.png)

<br/>


按下 Enter。  

![12.png](12.png)

<br/>


Hexo Server 即會啟動。  

![13.png](13.png)

<br/>


![14.png](14.png)

<br/>


若要停止 Hexo Server，可按下 Ctrl-Shift-P / Cmd-Shift-P，輸入 Hexo 後選取 hexo:stop hexo server。  

![15.png](15.png)

<br/>


選取要停止的 Hexo Server。  

![16.png](16.png)

<br/>


Hexo Server 即會停止。   

![17.png](17.png)

<br/>


Link
----
* [vscode-hexo - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=codeyu.vscode-hexo)
