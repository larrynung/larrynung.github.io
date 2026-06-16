---
title: "[C#]如何修正MDI父視窗受子視窗影響而無法正常關閉的問題"
date: "2013-11-06 12:00:00"
description: "昨天有讀者在筆者[VB.NET]MDI子視窗清單的實作這篇反應用筆者的程式讓MDI的父視窗無法正常關閉，筆者覺得很不可思議，因為筆者的程式只有替換掉內建的MDI子視窗清單，並在點選時將對應的子視窗帶上來，不怎麼可能造成視窗無法關閉的情況，就算影響也應該只影響子視窗才是，因為筆者並未動到父視窗的部分。"
---

昨天有讀者在筆者[VB.NET]MDI子視窗清單的實作這篇反應用筆者的程式讓MDI的父視窗無法正常關閉，筆者覺得很不可思議，因為筆者的程式只有替換掉內建的MDI子視窗清單，並在點選時將對應的子視窗帶上來，不怎麼可能造成視窗無法關閉的情況，就算影響也應該只影響子視窗才是，因為筆者並未動到父視窗的部分。因此用Visual Studio內建的MDI樣板來做試驗。

實際照著步驟測試，先點開兩個子視窗。

![image_thumb.png](/images/posts/c4f374c8-a102-41a5-8da0-d429f48ea73b/image_thumb.png)

將最上面的子視窗縮小。

![image_thumb_1.png](/images/posts/c4f374c8-a102-41a5-8da0-d429f48ea73b/image_thumb_1.png)

然後把未縮小的子視窗給關閉。

![image_thumb_2.png](/images/posts/c4f374c8-a102-41a5-8da0-d429f48ea73b/image_thumb_2.png)

這時候按下MDI父視窗右上角的關閉按鈕，發現的確是無法正常退出，按下去完全沒有反應。追了一下發現MDI父視窗不知道怎麼回事在FormClosing觸發時就已經將cancel設為true了。

![image_thumb_4.png](/images/posts/c4f374c8-a102-41a5-8da0-d429f48ea73b/image_thumb_4.png)

若碰到這個問題，開發人員可自行將cancel設回false來避開。

```csharp
private void MDIParent1_FormClosing(object sender, FormClosingEventArgs e)
{
    e.Cancel = false;
}
```
