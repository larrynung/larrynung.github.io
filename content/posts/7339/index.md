---
title: "[.NET Concept]善用AutoScroll達到用捲軸捲動顯示內容的效果"
date: "2009-03-02 06:52:50"
description: "時常會在討論區碰到有人提問內容過長想要增加捲軸效果這類的問題，通常多半這類的提問者都會陷入如何使用VScrollBar或是HScrollBar的迷思。事實上要達到這效果其實可以不需要使用這兩個控制項，只需善用容器類別的AutoScroll屬性，經過設定屬性的動作，不須撰寫半行程式即可達成。"
tags: [.NET Concept]
---

時常會在討論區碰到有人提問內容過長想要增加捲軸效果這類的問題，通常多半這類的提問者都會陷入如何使用VScrollBar或是HScrollBar的迷思。事實上要達到這效果其實可以不需要使用這兩個控制項，只需善用容器類別的AutoScroll屬性，經過設定屬性的動作，不須撰寫半行程式即可達成。

舉個例子來說，假設今天我要顯示一張很大的圖片在表單上，我們可以依下列步驟設定：

**Step1.**設定表單的AutoScroll屬性為True

![image_thumb7_thumb.png](/images/posts/7339/image_thumb7_thumb.png)

**Step2.**加入PictureBox控制項到設計表單

![image_thumb1_thumb.png](/images/posts/7339/image_thumb1_thumb.png)

**Step3.**設定PictureBox顯示的圖片

![image_thumb5_thumb.png](/images/posts/7339/image_thumb5_thumb.png)

**Step4.**把PictureBox的SizeMode設為AutoSize，讓PictureBox控制項可以隨著圖片自行調整大小。

![image_thumb6_thumb.png](/images/posts/7339/image_thumb6_thumb.png)

設完後設計介面會變成如下圖所示，捲軸效果已出現。

![image_thumb9_thumb.png](/images/posts/7339/image_thumb9_thumb.png)

如此簡單的捲軸顯示效果就完成了，執行後效果如下。

![image_thumb16_thumb.png](/images/posts/7339/image_thumb16_thumb.png)

再來看個例子，假設今天我只想在某區域放個需有捲軸顯示效果的內容的話又該怎麼做呢？其實步驟也差不多，我們可以依下列步驟設定：

**Step1.**放入Panel控制項至設計介面

![image_thumb20_thumb.png](/images/posts/7339/image_thumb20_thumb.png)

**Step2.**設定Panel的AutoScroll屬性為True

![image_thumb22_thumb.png](/images/posts/7339/image_thumb22_thumb.png)

**Step3.**放入PictureBox控制項至Panel

![image_thumb23_thumb.png](/images/posts/7339/image_thumb23_thumb.png)

**Step4.**設定PictureBox顯示的圖片

![image_thumb5%5B3%5D_thumb.png](/images/posts/7339/image_thumb5%5B3%5D_thumb.png)

**Step5.**把PictureBox的SizeMode設為AutoSize ，讓PictureBox控制項可以隨著圖片自行調整大小。

![image_thumb24_thumb.png](/images/posts/7339/image_thumb24_thumb.png)

設完後設計介面會變成如下圖所示，捲軸效果已出現。

![image_thumb26_thumb.png](/images/posts/7339/image_thumb26_thumb.png)

執行後效果如下

![image_thumb28_thumb.png](/images/posts/7339/image_thumb28_thumb.png)

P.S.

1. 以上範例雖都示範顯示圖片，但實際應用上不限於此，只要有設定AutoScroll屬性，則當內部的控制項超過容器時，自動會有捲軸效果出現。
2. 上面範例的Panel也可換成其它容器控制項

## Conclusion

善用.NET元件很多功能其實很容易達成，並沒有想像中那麼難。當然要用VScrollBar與HScrollBar應該也是可以做到一樣的效果，不過要耗多少功就不得而知了。

## 相關連結

1. [程式設計俱樂部 - 如何模擬Word表格編輯模式](http://www.programmer-club.com/pc2020v5/forum/ShowSameTitleN.asp?URL=N&board_pc2020=csharp&index=11&id=10849&mode=&type_pc2020=sametitleLevel-2)
