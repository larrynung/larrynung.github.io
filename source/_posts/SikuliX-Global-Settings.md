---
title: SikuliX - Global Settings
date: 2016-11-03 12:59:29
tags: SikuliX
---

SikuliX 有提供一些設定值可供設定，像是 ActionLogs、InfoLogs、DebugLogs、MinSimilarity、MoveMouseDelay、DelayAfterDrag、DelayBeforeDrop、SlowMotionDelay、WaitScanRate、ObserveScanRate、ObserveMinChangedPixels 等，若有需要可以透過程式修改設定，詳細的說明可參閱[這篇](http://doc.sikuli.org/globals.html)。  

<!-- More -->

<br/>


像是我們可以修改滑鼠移動的延遲、修改點擊的延遲、修改滑鼠按下前的延遲、修改鍵盤輸入的延遲、修改等待逾時的時間。  

```python
Settings.MoveMouseDelay = 0
Settings.ClickDelay = 0
Settings.DelayBeforeMouseDown = 0
Settings.TypeDelay = 0
Settings.AutoWaitTimeout = 30 * 1000
```

<br/>


用程式設定起來就像是下面這樣：

{% asset_img 1.png %}

<br/>


Link
----
* [Global Functions and Features — Sikuli X 1.0 documentation](http://doc.sikuli.org/globals.html)