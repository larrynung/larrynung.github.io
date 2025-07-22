---
title: "[IE8白皮書]自動損毀修復(ACR)"
date: "2013-11-06 12:00:00"
description: "[IE8白皮書]自動損毀修復(ACR)"
---

## 概述
  
自動損毀修復(ACR) 是IE8的特色之一，該功能可以防止因瀏覽器當機所造成的工作流失與生產力的降低 。 自動損毀修復為IE提供了新的復原機制, 像是分頁修復(tab recovery),可有效降低使用者瀏覽網頁被中斷的機率。
  
使用者透過瀏覽器可以做很多的工作。像是: 
  創作類工作  
創作類工作涉及寫作或是創作。 創作是很難的工作;且是時間密集的工作，若是不幸資料流失，將令人非常的頭痛。 創作類的工作有: 
     電子郵件訊息     部落格文章     學術課件（留言板，書面轉讓，等等。 ）    
 
  具前後關聯性的工作  
雖然這類工作當發生工作流失時並不會令人非常的頭痛，但仍是令人相當沮喪的。 這類工作有: 
     資訊搜尋與取得     購物車     登入Session （銀行，電子郵件，等等。 ）     分頁設定與載入的網址     瀏覽紀錄    
自動損毀修復能防止在做具前後關聯與創作類工作時，因當機或非預期的應用程式關閉所造成的資料流失。

## 自動損毀修復(ACR)功能詳述
  
下面將分別對於自動損毀修復的架構與使用者介面做一些探討。
  架構  
如下圖所示，自動損毀修復在架構上使用獨立的處理序，與介面框架獨立開來。
     
IE超過70%的當機通常是由擴充元件所造成，像是ActiveX® controls, Browser Helper Objects (BHOs), 與工具列。因此藉由把擴充的程式碼獨立到分頁處理序，我們可以保護整個瀏覽器，並把很多的錯誤給限制在分頁處理序中。
  
自動損毀修復扮演著資料記錄器的角色，可以備份分頁處理序內存在的必要資訊，包括：
     瀏覽記錄     分頁設定(分頁網址與分頁順序)    
下圖為自動損毀修復的高階架構示意圖：
     
當整個瀏覽器損毀，或是非預期的系統關閉，persistent backing store可使瀏覽器回復到先前的瀏覽狀態。

## 使用者介面
  
自動損毀修復具有下列功能：
  分頁修復  如下圖所示，當損毀被成功的修復，IE會在分頁上顯示氣泡對話框來通知使用者。   框架修復  
當非預期的關閉發生，像是突發性的斷電，如下圖所示，IE可修復這類的問題。

## 程式範例 
  
許多網頁並不需要修改程式就能夠正確的修復。
  
然而，當分頁修復與框架修復發生，IE將重新瀏覽目前頁面。AJAX網站動態注入的形式應當使用IE書籤頁面狀態功能，以確保當前頁面狀態能正確的恢復。
  
AJAX Navigation for Bookmarking Page State in the Browser 
  
In IE8 Standards Mode, Internet Explorer treats changes in window.location.hash like navigations and saves the previous document URL. The following actions occur as a result:   
              
The previous URL, which might be from the previous hash fragment, is updated in the address bar, the back button, and other browser components. 
            
A click sound is played just as in a traditional navigation scenario. 
            
新的hashChanged事件被觸發. 
      
Internet Explorer also saves the hash URL fragment before navigating away from the page. 
  
下面程式碼片段介紹如何設定事件處理程序與雜湊物件去觸發瀏覽器更新它的元件：
  
// 1. 附加事件處理程序到新的onhashchange事件. 
  
onhashchange = hashchange;  
  
// 2. 設定雜湊物件.  
  
window.location.hash = "Fragment_added_to_URL";