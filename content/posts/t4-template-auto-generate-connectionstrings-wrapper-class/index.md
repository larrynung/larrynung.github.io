---
title: "T4 template - Auto generate ConnectionString's wrapper class"
date: "2014-03-27 23:28:00"
description: "T4 template - Auto generate ConnectionString's wrapper class"
tags: [T4, CSharp]
---

在 .Net 程式中要使用資料庫的連線字串，多半我們會將資料庫的連線字串設定在 Config 檔中，然後透過 ConfigurationManager.ConnectionStrings 帶入對應的 Key 去將之取出來使用。

用這樣的撰寫方式，連線字串名稱打錯無法立即的被意識到，連線字串名稱調動時也很容易漏改，造成系統運行時的錯誤。因此有的人會將連線字串這邊再包一層，透過這層物件的屬性去取得連線字串，將連線字串的修改都在這層處理，減少人為造成的錯誤。

然而這樣的做法並無法完全解決問題，因為多包的那層還是人工下去做的，仍舊是無法避免連線名稱鍵錯的問題，連線字串變動時仍是會有改錯的可能。故這邊筆者嘗試使用 T4 template，讀取專案的 config 檔，動態產生強型別物件，提供連線字串給系統使用。

首先我們要為專案加入一個 t4 template 檔。

然後將其程式碼替換成下面這樣。
```c#

using System.Configuration;

namespace
{
public class ConnectionStrings
{

public static string
{
get
{
return ConfigurationManager.ConnectionStrings["  "].ConnectionString;
}
}

}
}
```
存檔運行，沒意外的話應該可以看到對應的強型別物件被產生了出來。

在系統中我們就可直接透過該強型別物件去取得連線字串，像是假設有個名為 Oracle 的 ConnectionString，就可像下面這樣取用。
```c#
var connectionString = ConnectionStrings.Oracle;
...
```
如果後續 config 內的連線字串有所增減，或是連線字串的名稱有所更動，可直接在該 t4 template 上按下滑鼠右鍵，在彈出的滑鼠右鍵快顯選單中點選 Run custom tool 這個滑鼠右鍵選單選項，讓 t4 template 重新產生對應的強型別物件就可以了。