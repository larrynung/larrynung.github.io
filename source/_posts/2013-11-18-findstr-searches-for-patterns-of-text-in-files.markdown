---
layout: post
title: "Findstr - Searches for patterns of text in files"
date: 2013-11-18 21:49
comments: true
categories: 
---

Findstr是ㄧ命令列的內文搜尋工具，能同時針對多個檔案搜尋內文，類似Linux上的grep命令。

<!--More-->

他的使用方式可以呼叫下列命令查閱  

    findstr /?


叫用後會看到如下使用說明

    在檔案中搜尋字串。

    FINDSTR [/B] [/E] [/L] [/R] [/S] [/I] [/X] [/V] [/N] [/M] [/O] [/P] [/F:file]
        [/C:string] [/G:file] [/D:dir list] [/A:color attributes] [/OFF[LINE]]
        strings [[drive:][path]filename[ ...]]

      /B        如果是在行的開端，則符合類型。
      /E        如果是在行的尾端，則符合類型。
      /L        逐字使用搜尋字串。
      /R        使用搜尋字串為一般表示式。
      /S        在現存目錄及所有的子目錄中
                搜尋符合的檔案。
      /I        指定搜尋不區分大小寫。
      /X        列印完全符合的行數。
      /V        只列印不含相符字串的行數。
      /N        列印每一行符合的行數前的行編號。
      /M        只列印包含相符字串的檔案的檔案名稱。
      /O        列印每一個相符行之前的字元位移。
      /P        跳過沒有可列印字元的檔案。
      /OFF[LINE] 不要跳過有離線屬性設定的檔案。
      /A:attr    以兩個十六進位數字指定色彩屬性。請參閱 "color /?"。
      /F:file   從指定的檔案讀取檔案清單 (/ 代表主控台)。
      /C:string 使用特定的字串作為逐字搜尋的字串。
      /G:file   從指定的檔案取得搜尋字串 (/ 代表主控台)。
      /D:dir    搜尋以分號隔開的目錄清單。
      strings   要搜尋的文字。
      [drive:][path]filename
                指定要搜尋的一個或多個檔案。

    除非引數的字首有 /C，否則請以空格將多重搜尋字串分開。
    例如，'FINDSTR "hello there" x.y' 將會在檔案 x.y 中
    搜尋 "hello"，或 "there"。'FINDSTR /C:"hello there" x.y' 
    將會在檔案x.y 中搜尋 "hello there"。

    常見表示快速對照表:
      .        萬用字元: 任何字元
      *        重複: 零或之前字元或類別發生數次
      ^        行的位置: 行的開頭
      $        行的位置: 行的結尾
      [class]  字元類別: 組的任何一個字元
      [^class] 顛倒的類別: 不成組的任何一個字元
      [x-y]    範圍: 在特定範圍內的任何字元
      \x       跳開: metacharacter x 的字面使用方法
      \<xyz    字的位置: 字的開頭
      xyz\>    字的位置: 字的結尾

    有關 FINDSTR 一般表示式的資訊，請參閱線上
    命令參照。



簡單的來說，Findstr使用時要帶入搜尋的字串與要搜尋的檔案。搜尋的字串可以用雙引號包住直接帶在Findstr後，如果要同時搜尋多個字串，可以用空格將多個欲搜尋的字串分開:

    findstr "[SearchText1] [SearchText2]"  [SearchFile]


若要明確的搜尋特定字串，可帶入參數/c指定:

    findstr /c:"[SearchText]" [SearchFile]


比對時要忽略大小寫，可帶入參數/i：

    findstr /i /c:"[SearchText]" [SearchFile]


要搜尋當前目錄及子目錄，可帶入參數/s：

    findstr /s /c:"[SearchText]" [SearchFile]
   
{% img /images/posts/Findstr/1.png %}


要在搜尋結果加入行號顯示，可帶入參數/n：

    findstr /n /c:"[SearchText]" [SearchFile]

{% img /images/posts/Findstr/2.png %}


要在搜尋結果加入字元位移量顯示，可帶入參數/o：

    findstr /o /c:"[SearchText]" [SearchFile]

{% img /images/posts/Findstr/3.png %}


若搜尋結果顯示的顏色不夠明顯想要變更，可帶入參數/A指定：

    findstr /A:[Color] /c:"[SearchText]" [SearchFile]

{% img /images/posts/Findstr/4.png %}


若要從檔案讀出要比對的字串以及要比對的檔案：

    findstr /g:[SearchTextFile] /f:filelist.txt


若要比對當前目錄與子目錄，但只顯示有批配到的檔名，可帶入/m參數：

    findstr /s /m "[SearchText]" *.*

{% img /images/posts/Findstr/4.png %}


若比對時要用正規表示式去比對，Findstr也可以支援。  

最後一提，Findstr的參數也可以合併帶入，像是下面這樣：

    findstr /sim "[SearchText]" *.*


Link
----
* [Findstr - TechNet - Microsoft]( http://technet.microsoft.com/en-us/library/cc732459.aspx )
* [window中findstr命令的用法]( http://www.netingcn.com/window-findstr-command.html )
