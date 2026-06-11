---
title: "[JavaScript]HTML5 New Feature - Web Storage"
date: "2013-11-06 12:00:00"
description: "[JavaScript]HTML5 New Feature - Web Storage"
---

Web storage是HTML5新功能之一，允許使用者透過瀏覽器將資料暫存在client端。以往使用cookie來做類似這樣的需求，每個頁面可容納的資料量，約只有 4 KB 左右，且會在HTTP Request時上傳資料至Server端，造成不必要的頻寬浪費，也對執行效能造成不好的影響。而若是透過 Web Storage來儲存，儲存容量依瀏覽器不同而有不同，約有 1-5MB，且能手動調整透過設定將空間放大，能存放更大的資料量，不耗費不必要的頻寬，使用起來也更為方便。

Web storage可依其儲存特性再被細分為sessionStorage與localStorage。以sessionStorage來說，所儲存的資料在瀏覽的分頁或是瀏覽器關閉時就會被清除，較適合用來儲存比較臨時性的資料。

至於localStorage所儲存的資料則是沒有像sessionStorage這樣的限制，其儲存的資料能一直存放在本地端，直至我們明確的呼叫釋放動作，儲存的資料才會自本地端移除。

Web Storage實作了Storage介面，這個介面資料的儲存與操作都是以key/value成對的方式下去做處理，類似一般我們所常見的字典檔的架構。

interface Storage {
readonly attribute unsigned long length;
getter DOMString key(in unsigned long index);
getter any getItem(in DOMString key);
setter creator void setItem(in DOMString key, in any data);
deleter void removeItem(in DOMString key);
void clear();
};

不論是sessionStorage還是localStorage皆遵循這樣的介面，因此使用起來十分的相似，並沒有太大的差異。像是設定資料時可透過setItem方法，將key與value成對帶入，即可將資料存放至Web Storage：

sessionStorage.setItem(key, value);
localStorage.setItem(key, value);

除此之外也可以直接將key值當作成員變數來存取：

sessionStorage.key = value;
localStorage.key = value;

要取得存放的資料時可透過getItem方法，帶入存放資料時所設定的key值，即可回傳所存放的資料值：

value = sessionStorage.getItem(key);
value = localStorage.getItem(key);

同樣的這也支援將key值當作成員變數來存取的操作方式：

value = sessionStorage.key;
value = localStorage.key;

當有移除某特定資料的需求時，可帶入要刪除的資料key值，像是下面這樣：

sessionStorage.removeItem(key);
localStorage.removeItem(key);

也可以透過叫用clear方法清除所有存放在Web Storage內的資料：

sessionStorage.clear();
localStorage.clear();

到這邊應該可以看出來因為是實作相同Interface的關係，sessionStorage跟localStorage的存取方式幾乎沒有差異，只是針對不同的類別下去存取。

這邊實際寫個示範用的範例，該範例可以將按鈕的點擊次數資料存放在Web Storage中

function clickCounter()
{
var key = "clickcount";
var value = localStorage.getItem(key);
if (value)
{
localStorage.setItem(key, Number(value)+1);
}
else
{
localStorage.setItem(key, 1);
}
document.getElementById("result").innerHTML="You have clicked the button " + localStorage.clickcount + " time(s).";
}

Click me!

Click the button to see the counter increase.

運行後結果會像下面這樣，點擊按鈕會累加點擊次數，而點擊次數會存放在localStorage中，因此下次再開啟相同的頁面仍能繼續累加。有興趣的可以將範例的localStorage字樣全部取代為sessionStorage，這樣運行起來點擊的次數就會在每次重開啟時重新計算。

最後這邊再補充一下，上面有提到Web Storage是實作自Storage介面，因此我們可以透過這個特性下去做瀏覽器支援與否的判斷，判斷Storage是否沒有被定義，若有定義則代表該瀏覽器支援Web Storage，若是undefined則代表該瀏覽器不支援Web Storage。

function checkWebStorageSupportable()
{
return (typeof(Storage)!=="undefined");
}

這邊一樣也提供個簡單的示範：

function OnLoad()
{
document.getElementById("result").innerHTML = checkWebStorageSupportable()?"Support":"UnSupport";
}

function checkWebStorageSupportable()
{
return (typeof(Storage)!=="undefined");
}

運行後會像下面這樣，會顯示出瀏覽器是否支援Web Storage。

## Link


Web Storage

Web storage

HTML5 Web Storage

JavaScript Web Storage (DOM Storage)

Web Storage 使用經驗

WebStorage API 簡介

[HTML5]簡述HTML5的Client端暫存-localStorage/sessionStorage