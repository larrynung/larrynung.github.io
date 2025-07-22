---
title: "[VB.NET]HatchBrush"
date: "2009-06-17 09:03:57"
description: "[VB.NET]HatchBrush"
tags: [VB.NET]
---

## Introduction

HatchBrush為.NET所提供的Brush類別，提供使用者 54 種系統筆刷樣式。

## Constructer

HatchBrush基本上用法跟一般的Brush一樣，多半我們只需了解建構子即可。HatchBrush內建兩個多載建構子，只要傳入HatchStyle、前景色、背景色，HatchBrush筆刷物件即可完成建置。

## HatchStyle 列舉型別

指定 HatchBrush 物件可用的不同花紋。
成員名稱說明圖示Horizontal水平線花紋。Vertical垂直線花紋。ForwardDiagonal從左上到右下的斜線線條花紋。BackwardDiagonal從右上到左下的斜線線條花紋。Cross指定交叉的水平和垂直線條。 DiagonalCross十字形對角線的模式。Percent05指定百分之 5 的規劃。前景色彩與背景色彩的比例為 5:100。Percent10指定百分之 10 的規劃。前景色彩與背景色彩的比例為 10:100。Percent20指定百分之 20 的規劃。前景色彩與背景色彩的比例為 20:100。Percent25指定百分之 25 的規劃。前景色彩與背景色彩的比例為 25:100。Percent30指定百分之 30 的規劃。前景色彩與背景色彩的比例為 30:100。Percent40指定百分之 40 的規劃。前景色彩與背景色彩的比例為 40:100。Percent50指定百分之 50 的規劃。前景色彩與背景色彩的比例為 50:100。Percent60指定百分之 60 的規劃。前景色彩與背景色彩的比例為 60:100。Percent70指定百分之 70 的規劃。前景色彩與背景色彩的比例為 70:100。Percent75指定百分之 75 的規劃。前景色彩與背景色彩的比例為 75:100。Percent80指定百分之 80 的規劃。前景色彩與背景色彩的比例為 80:100。Percent90指定百分之 90 的規劃。前景色彩與背景色彩的比例為 90:100。LightDownwardDiagonal指定從頂點到底點往右斜的對角線，其間距比 ForwardDiagonal 接近百分之 50，但是沒有反鋸齒。LightUpwardDiagonal指定從頂點到底點往左斜的斜線，間距比 BackwardDiagonal 相互接近百分之 50，但是沒有反鋸齒補償。DarkDownwardDiagonal指定從頂點到底點往右斜的斜線，間距比 ForwardDiagonal 相互接近百分之 50，並且寬度為其兩倍。這個規劃花紋沒有反鋸齒補償。DarkUpwardDiagonal指定從頂點到底點往左斜的斜線，間距比 BackwardDiagonal 相互接近百分之 50，並且寬度為其兩倍，但是線條沒有反鋸齒補償。WideDownwardDiagonal指定從頂點到底點往右斜的斜線，間距與 ForwardDiagonal 規劃樣式相同，並且寬度為其三倍，但是沒有反鋸齒補償。WideUpwardDiagonal指定從頂點到底點往左斜的斜線，間距與 BackwardDiagonal 規劃樣式相同，並且寬度為其三倍，但是沒有反鋸齒補償。LightVertical指定間距比 Vertical 相互接近百分之 50 的垂直線。LightHorizontal指定間距比 Horizontal 相互接近百分之 50 的水平線。NarrowVertical指定間距比 Vertical 規劃樣式相互接近百分之 75 (或比 LightVertical 相互接近百分之 25) 的垂直線。NarrowHorizontal指定間距比 Horizontal 規劃樣式相互接近百分之 75 (或比 LightHorizontal 相互接近百分之 25) 的水平線。DarkVertical指定間距比 Vertical 相互接近百分之 50 並且寬度為其兩倍的垂直線。DarkHorizontal指定水平線，其間距比 Horizontal 接近百分之 50，且寬度為 Horizontal 的兩倍。DashedDownwardDiagonal指定從頂點到底點向右斜的短折斜線。DashedUpwardDiagonal指定從頂點到底點向左斜的短折斜線。DashedHorizontal指定短折水平線。DashedVertical指定短折垂直線。SmallConfetti指定具有五彩碎紙外觀的規劃。LargeConfetti指定具有五彩碎紙外觀並且由比 SmallConfetti 更大的碎紙組成的規劃。ZigZag指定由 Z 字形組成的水平線。Wave指定由波狀符號 (~) 組成的水平線。DiagonalBrick指定具有從頂點到底點向左斜的層次磚形外觀之規劃。HorizontalBrick指定具有水平層次磚形外觀的規劃。Weave指定具有編織材質外觀的規劃。Plaid指定具有格子圖案材質外觀的規劃。Divot指定具有草皮外觀的規劃。DottedGrid指定交叉的水平虛線和垂直虛線。DottedDiamond指定交叉的正斜虛線和反斜虛線。Shingle指定規劃之圖樣，其外觀為從頂點到底點向右斜的對角層次木瓦。Trellis指定具有格子外觀的規劃。Sphere指定具有相鄰置放的球體外觀之規劃。SmallGrid指定間距比 Cross 規劃樣式相互接近百分之 50 的交叉水平線和垂直線。SmallCheckerBoard指定具有棋盤外觀的規劃。LargeCheckerBoard指定具有方格大小為 SmallCheckerBoard 兩倍的棋盤外觀之規劃。OutlinedDiamond指定交叉但是沒有反鋸齒補償的正斜線和反斜線。SolidDiamond指定具有斜對置放的棋盤外觀之規劃。LargeGrid指定 Cross 規劃樣式。 Min指定 Horizontal 規劃樣式。 Max指定 SolidDiamond 規劃樣式。 

## 程式範例

VB.NET

執行結果