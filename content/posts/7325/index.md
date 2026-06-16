---
title: "[C#][VB.NET]使用AxWindowsMediaPlayer撥放多媒體"
slug: "[CSharp][VB.NET]使用AxWindowsMediaPlayer撥放多媒體"
date: "2009-03-01 02:09:40"
description: "加入工具箱 Step1.工具箱=>滑鼠右鍵=>選擇項目 Step2.切換至『COM 元件』頁籤=>勾選Windows Media Player=>確定 Step3.會發現工具箱多了個Windows Media Player的控制項 使用AxWindowsMediaPlayer撥放多媒體…"
tags: [VB.NET,CSharp]
---

## 加入工具箱

**Step1.**工具箱=>滑鼠右鍵=>選擇項目

![image_thumb_1.png](/images/posts/7325/image_thumb_1.png)

**Step2.**切換至『COM 元件』頁籤=>勾選Windows Media Player=>確定

![image_thumb.png](/images/posts/7325/image_thumb.png)

**Step3.**會發現工具箱多了個Windows Media Player的控制項

![image_thumb_1.png](/images/posts/7325/image_thumb_1.png)

## 使用AxWindowsMediaPlayer撥放多媒體

**Step1.**加入Windows Media Player控制項到設計表單，可看到如下的畫面。

![image_thumb_2.png](/images/posts/7325/image_thumb_2.png)

**Step2.**依序加入控制項使介面如下圖所示。

![image_thumb_3.png](/images/posts/7325/image_thumb_3.png)

**Step3.**撰寫控制項初始設定程式碼

此處是設定控制項的初始值，像是音量的最大值、最小值、目前的音量、與啟動Timer(用來偵測檔案總長度用)，值得注意的是AxWindowsMediaPlayer控制項的音量大小介於0~100之間，另外若不設定AutoStart = False則開啟檔案完程式就會自動撥放開啟的多媒體檔。

VB.NET

```
Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
Me.AxWindowsMediaPlayer1.settings.autoStart = False                     '設定不自動撥放
Me.tbarVolume.Minimum = 0                                               '設定音量調整Bar最小值為最小音量值(0)
Me.tbarVolume.Maximum = 100                                             '設定音量調整Bar最大值為最大音量值(100)
Me.tbarVolume.Value = Me.AxWindowsMediaPlayer1.settings.volume          '設定音量調整Bar目前值為目前音量值
Me.Timer1.Enabled = True
End Sub
```

C#

```
private void Form1_Load(object sender, EventArgs e)
{
this.axWindowsMediaPlayer1.settings.autoStart = false;                     //設定不自動撥放
this.tbarVolume.Minimum = 0;                                               //設定音量調整Bar最小值為最小音量值(0)
this.tbarVolume.Maximum = 100;                                             //設定音量調整Bar最大值為最大音量值(100)
this.tbarVolume.Value = this.axWindowsMediaPlayer1.settings.volume;        //設定音量調整Bar目前值為目前音量值
this.timer1.Enabled = true;
}
```

**Step4.**撰寫開啟程式碼

AxWindowsMediaPlayer控制項是去設定AxWindowsMediaPlayer.URL屬性值來達到多媒體檔案開啟的功能。

VB.NET

```
Private Sub btnOpen_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnOpen.Click
If OpenFileDialog1.ShowDialog = Windows.Forms.DialogResult.OK Then
Me.AxWindowsMediaPlayer1.URL = OpenFileDialog1.FileName                                     '開啟檔案
End If
End Sub
```

C#

```
private void btnOpen_Click(object sender, EventArgs e)
{
if (openFileDialog1.ShowDialog() == DialogResult.OK)
{
this.axWindowsMediaPlayer1.URL = openFileDialog1.FileName;             //開啟檔案
}
}
```

**Step5.**撰寫撥放程式碼

這部份功能程式碼只需呼叫AxWindowsMediaPlayer.Ctlcontrols.play()即可。

VB.NET

```
Private Sub btnPlay_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnPlay.Click
Me.AxWindowsMediaPlayer1.Ctlcontrols.play()
End Sub
```

C#

```
private void btnPlay_Click(object sender, EventArgs e)
{
this.axWindowsMediaPlayer1.Ctlcontrols.play();
}
```

**Step6.**撰寫停止程式碼

這部份功能程式碼只需呼叫AxWindowsMediaPlayer.Ctlcontrols.stop()即可。

VB.NET

```
Private Sub btnStop_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnStop.Click
Me.AxWindowsMediaPlayer1.Ctlcontrols.stop()         '停止播放
End Sub
```

C#

```
private void btnStop_Click(object sender, EventArgs e)
{
this.axWindowsMediaPlayer1.Ctlcontrols.stop();         //停止播放
}
```

**Step7.**撰寫暫停撥放程式碼

這部份功能程式碼只需呼叫AxWindowsMediaPlayer.Ctlcontrols.pause()即可。

VB.NET

```
Private Sub btnPause_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnPause.Click
Me.AxWindowsMediaPlayer1.Ctlcontrols.pause()        '暫停撥放
End Sub
```

C#

```
private void btnPause_Click(object sender, EventArgs e)
{
this.axWindowsMediaPlayer1.Ctlcontrols.pause();        //暫停撥放
}
```

**Step8.**撰寫音量控制程式碼

這部份功能程式碼只需對AxWindowsMediaPlayer.settings.volume做屬性值的變更即可。

VB.NET

```
Private Sub tbarVolume_Scroll(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles tbarVolume.Scroll
Me.AxWindowsMediaPlayer1.settings.volume = Me.tbarVolume.Value      '改變音量大小
End Sub

Private Sub btnIncreaseVolume_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnIncreaseVolume.Click
Me.AxWindowsMediaPlayer1.settings.volume += 1       '音量大小+1
End Sub

Private Sub btnDecreaseVolume_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnDecreaseVolume.Click
Me.AxWindowsMediaPlayer1.settings.volume -= 1       '音量大小-1
End Sub
```

C#

```
private void tbarVolume_Scroll(object sender, EventArgs e)
{
this.axWindowsMediaPlayer1.settings.volume = this.tbarVolume.Value;      //改變音量大小
}

private void btnIncreaseVolume_Click(object sender, EventArgs e)
{
this.axWindowsMediaPlayer1.settings.volume += 1;       //音量大小+1
}

private void btnDecreaseVolume_Click(object sender, EventArgs e)
{
this.axWindowsMediaPlayer1.settings.volume -= 1;       //音量大小-1
}
```

**Step9.**撰寫撥放位置控制程式碼

除需對AxWindowsMediaPlayer.Ctlcontrols.currentPosioion做屬性值的變更外，尚需利用AxWindowsMediaPlayer.currentMedia.duration去設定最大影片長度。

VB.NET

```
Private Sub tbarPlayLoaction_Scroll(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles tbarPlayLoaction.Scroll
Me.AxWindowsMediaPlayer1.Ctlcontrols.currentPosition = tbarPlayLoaction.Value          '改變撥放位置
End Sub

Private Sub Timer1_Tick(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Timer1.Tick
If Me.AxWindowsMediaPlayer1.currentMedia Is Nothing Then
Return
End If
Me.tbarPlayLoaction.Maximum = CInt(Me.AxWindowsMediaPlayer1.currentMedia.duration)          '設定撥放位置調整Bar最大值
End Sub
```

C#

```
private void tbarPlayLoaction_Scroll(object sender, EventArgs e)
{
this.axWindowsMediaPlayer1.Ctlcontrols.currentPosition = tbarPlayLoaction.Value;          //改變撥放位置
}

private void timer1_Tick(object sender, EventArgs e)
{
if (this.axWindowsMediaPlayer1.currentMedia == null)
return;
this.tbarPlayLoaction.Maximum = (int)this.axWindowsMediaPlayer1.currentMedia.duration;          //設定撥放位置調整Bar最大值
}
```

## Download

使用AxWindowsMediaPlayer撥放多媒體.zip

## 參考連結

1. MSDN Library - AxWindowsMediaPlayer Object (VB and C#)
2. 黑色幽默 - AxWindowsMediaPlayer媒体文件主要方法属性
