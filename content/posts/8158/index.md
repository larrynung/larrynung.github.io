---
title: "[VB.NET].NET多語系程式(一)"
date: "2009-04-24 12:32:11"
description: "範例說明 本篇將介紹.NET多語系程式的寫法 ，下面會利用最簡單方便且正統的方法也就是資源檔來達到多語系的功能。 學習目標 .NET多語程式撰寫 資源檔的使用與操作 CultureInfo類別的使用 語系的切換 操作步驟 介面上的多語 Step1.將表單的Localizable屬性設為True…"
tags: [VB.NET]
---

## ![image_thumb_16.png](/images/posts/8158/image_thumb_16.png)

## 範例說明

本篇將介紹.NET多語系程式的寫法 ，下面會利用最簡單方便且正統的方法也就是資源檔來達到多語系的功能。

## 學習目標

* .NET多語程式撰寫
* 資源檔的使用與操作
* CultureInfo類別的使用
* 語系的切換

## 操作步驟

### 介面上的多語

**Step1.將表單的Localizable屬性設為True**

![image_thumb.png](/images/posts/8158/image_thumb.png)

**Step2.切換表單的Language屬性為欲使用的語系**

![image_thumb_1.png](/images/posts/8158/image_thumb_1.png)

設完後會在分頁標籤上看到目前設定的語系

![image_thumb_4.png](/images/posts/8158/image_thumb_4.png)

**Step3.設定介面上欲顯示的字樣並適當的調整版面**

![image_thumb_2.png](/images/posts/8158/image_thumb_2.png)

![image_thumb_3.png](/images/posts/8158/image_thumb_3.png)

到此，用資源檔做的多語系程式就完成了。

我們可以到檔案總管看一下，可看到Visual Studio自己幫我們產生了對應的資源檔。

![image_thumb_5.png](/images/posts/8158/image_thumb_5.png)

因此，在實作介面上的多語時，我們並不需自己手動加入資源檔。

![image_thumb_9.png](/images/posts/8158/image_thumb_9.png)

### 訊息的多語

上面的範例帶出了介面上支援多語的寫法，但卻不適用於訊息上，若要在訊息上也支援多語。請依下列步驟：

**Step1.加入資源檔**

資源檔依照 "資源檔名.文化特性.resx" 格式命名，如 "Resources.zh-tw.resx"。

![image_thumb_9.png](/images/posts/8158/image_thumb_9.png)

**Step2.設定資源檔內的訊息內容**

在資源檔上連點兩下

![image_thumb_12.png](/images/posts/8158/image_thumb_12.png)

設定對應的語系字串

![image_thumb_11.png](/images/posts/8158/image_thumb_11.png)

![image_thumb_13.png](/images/posts/8158/image_thumb_13.png)

**Step3.使用資源檔內的訊息內容**

這邊只要透過My.Resources去取出資源檔內的值即可，內部OR Mapping轉換都幫你做好好，可以用強型別的方式直接取用，能避免掉許多不必要的低級錯誤。

```
MsgBox(My.Resources.Resource1.String1)
```

其實個人習慣是命名為 "Resources.文化特性.resx"，因為專案裡已偷放了一個Resources.resx資源檔，因此只需加入非預設語系的資源檔即可。

![image_thumb_14.png](/images/posts/8158/image_thumb_14.png)

在使用上也會變得較為簡短

```
MsgBox(My.Resources.String1)
```

## 切換語系

依上面步驟操作完後，其實已具多語支援能力。當程式開啟時，會自動依照當前語系去顯示介面畫面。因此我們開啟時應該是顯示中文而不是本來的英文。若要自己切換語系可利用Threading.Thread.CurrentThread.CurrentUICulture。

```
Threading.Thread.CurrentThread.CurrentUICulture = New CultureInfo("en")
```

值得注意的是，這樣的寫法是不會影響已開啟的視窗的。只有後來開啟的視窗會被切換語系。

那是否已開啟的視窗就無法切換了呢？那倒也不是。可以透過使用ResourceManager.GetString去取得對應的字串，把取出的字串再設到介面上即可。但是這也不是很好的方法，個人傾向使用ComponentResourceManager配合遞迴去把介面上的字串換成對應語系的字串。有興趣的可以參考Form.Designer.vb檔的程式碼。

![image_thumb_7.png](/images/posts/8158/image_thumb_7.png)

![image_thumb_8.png](/images/posts/8158/image_thumb_8.png)

## 注意事項

在用多國語言資源檔時，建議最後在弄其它語系的設定。因為當我們設定多語系時，Visual Studio會自動幫我們產生資源檔，且內含預設的設定值。若太早讓Visual Studi產生資源檔，則預設的設定值將只有少少的幾個，後面的設定值都需手動的設定，且每個語系的資源檔都要設定。

![image_thumb_17.png](/images/posts/8158/image_thumb_17.png)
