---
title: "Visual Studio 2013 RC New Feature - Method return value inspection"
date: "2013-11-06 12:00:00"
description: "Visual Studio 2013 RC新加入了Method return value inspection功能，能讓開發人員很容易的查閱方法運行後傳回的回傳值，讓除錯更加的便利。 像是下面這個例子，方法中帶入的值是其它方法的回傳值。"
---

Visual Studio 2013 RC新加入了Method return value inspection功能，能讓開發人員很容易的查閱方法運行後傳回的回傳值，讓除錯更加的便利。

像是下面這個例子，方法中帶入的值是其它方法的回傳值。

![image_thumb.png](/images/posts/1df380c3-5586-47f8-bb7f-5d78f19b0f00/image_thumb.png)

以往這樣的情況我們要查驗哪個環節出了問題，要馬是改程式碼，將方法回傳值改用變數去接，修改完後再次運行除錯。要馬就是用滑鼠選取後監看。

![image_thumb_6.png](/images/posts/1df380c3-5586-47f8-bb7f-5d78f19b0f00/image_thumb_6.png)

在Visual Studio 2013 RC後，我們可以直接中斷在該行程式碼，然後Step over，方法的回傳值就會在自動變數監看視窗中出現。

![image_thumb_2.png](/images/posts/1df380c3-5586-47f8-bb7f-5d78f19b0f00/image_thumb_2.png)

若是像下面這樣直接在方法中將其它方法的值回傳，Method return value inspection一樣可以支援。

![image_thumb_4.png](/images/posts/1df380c3-5586-47f8-bb7f-5d78f19b0f00/image_thumb_4.png)

這邊要注意到，Method return value inspection功能需藉助Step over trigger，如果是直接將斷點斷在下一行程式碼，這樣是完全沒有效用的。

![image_thumb_3.png](/images/posts/1df380c3-5586-47f8-bb7f-5d78f19b0f00/image_thumb_3.png)

最後一提，即時運算視窗這邊也新增了$ReturnValue命令，可以直接取得最後一次的方法回傳值。

![image_thumb_5.png](/images/posts/1df380c3-5586-47f8-bb7f-5d78f19b0f00/image_thumb_5.png)

## Link

* Examine return values of method calls
