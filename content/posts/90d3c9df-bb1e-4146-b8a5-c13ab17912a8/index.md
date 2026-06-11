---
title: "[C#]使用ControlPaint.DrawBorder調整控制項外框的顏色"
slug: "[CSharp]使用ControlPaint.DrawBorder調整控制項外框的顏色"
date: "2013-11-06 12:00:00"
description: "[C#]使用ControlPaint.DrawBorder調整控制項外框的顏色"
tags: [CSharp]
---

最近跟UX Team合作體驗到能將設計好的UI完美呈現真是考驗程式人員的能力，UX Team的設計人員考量的細節都跟程式開發人員不同，在某些細節上比程式人員都還講究，就像是控制項的邊框顏色不對都不行。但是幾乎所有的控制項都不具備設定邊框顏色的能力，這該怎麼辦呢？想來想去都只能自己下去繪製控制項的邊框。

這邊的繪製控制項邊框並不是要我們將整個控制項重繪，而是用ControlPaint.DrawBorder在控制項上面再蓋上個新的邊框，下面是ControlPaint.DrawBorder的函式原型：
  public static void DrawBorder(
Graphics graphics,
Rectangle bounds,
Color color,
ButtonBorderStyle style
)

簡單的說它需要帶入畫布、邊框的範圍、邊框的顏色、以及邊框的風格，這邊實際用個簡單的例子來示範一下，筆者在表單上放了一個DataGridView元件，試圖將其元件的邊框改為黃色。

我們可以在DataGridView的繪製事件中填入像下面這樣的程式碼片段：

...
private void dataGridView1_Paint(object sender, PaintEventArgs e)
{
ControlPaint.DrawBorder(e.Graphics, (sender as Control).DisplayRectangle, Color.Yellow, ButtonBorderStyle.Solid);
}
...

運行後我們可以看到控制項元件的邊框變成我們所指定的顏色了，若有需要改變邊框的Style，像是想要虛線的邊框或是有3D的效果，可以調整最後一個參數。

## Link

  ControlPaint.DrawBorder Method (Graphics, Rectangle, Color, ButtonBorderStyle)