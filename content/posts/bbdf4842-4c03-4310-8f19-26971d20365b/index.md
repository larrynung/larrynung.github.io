---
title: "[C#]Notifyicon.Text 突破 64 字元的限制"
slug: "csharp-notifyicon-text-突破-64-字元的限制"
aliases: ["/posts/csharpnotifyicon.text-突破-64-字元的限制/"]
date: "2013-11-06 12:00:00"
description: "最近在寫程式時需要將一些資訊顯示在NotifyIcon上，才注意到NotifyIcon.Text有64個字元的限制。 在設定超過64個字元時，系統就會發出例外訊息。 經過一番的調整與精簡，仍是避免不了會超過64個字元。"
tags: [CSharp]
---

最近在寫程式時需要將一些資訊顯示在NotifyIcon上，才注意到NotifyIcon.Text有64個字元的限制。

![image_thumb.png](/images/posts/bbdf4842-4c03-4310-8f19-26971d20365b/image_thumb.png)

在設定超過64個字元時，系統就會發出例外訊息。

![image_thumb_1.png](/images/posts/bbdf4842-4c03-4310-8f19-26971d20365b/image_thumb_1.png)

經過一番的調整與精簡，仍是避免不了會超過64個字元。因此開始回思這64個字元是否是合理的限制，怎樣想都是怪怪的，為什麼是64？為什麼不是255？當然NotifyIcon的提示是不該太長，會影響使用者觀看，但是這個限制值也太Magic了，而且印象中也是有軟體顯示很多字元在上面。Google一下發現了How can I show a systray tooltip longer than 63 chars?這篇討論，裡面用了反射直接去設定未公開的NotifyIcon.text欄位，該問題就迎刃而解，所以這個值看起來是基於某些不為人知的原因而設的，底層並沒有這樣的限制。

```csharp
public static void SetNotifyIconText(NotifyIcon ni, string text)
{
	if (text.Length >= 128) throw new ArgumentOutOfRangeException("Text limited to 127 characters");
	Type t = typeof(NotifyIcon);
	BindingFlags hidden = BindingFlags.NonPublic | BindingFlags.Instance;
	t.GetField("text", hidden).SetValue(ni, text);
	if ((bool)t.GetField("added", hidden).GetValue(ni))
		t.GetMethod("UpdateIcon", hidden).Invoke(ni, new object[] { true });
}
```

使用時將NotifyICon的物件實體與要設定的字串帶入即可。

```csharp
private void button1_Click(object sender, EventArgs e)
{
	SetNotifyIconText(notifyIcon1, new string('*', 100));
}
```

帶入後一切正常，突破了64字元的限制了...

![image_thumb_2.png](/images/posts/bbdf4842-4c03-4310-8f19-26971d20365b/image_thumb_2.png)

## Link

* How can I show a systray tooltip longer than 63 chars?
* NotifyIcon.Text 屬性
