---
title: "[C#][VB.NET]Play Media with AxMediaPlayer"
slug: "csharp-vbnet-play-media-with-axmediaplayer"
aliases: ["/posts/csharpvb.net使用axmediaplayer撥放多媒體/"]
date: "2009-02-28 03:41:58"
description: "加入工具箱 Step1.工具箱=>滑鼠右鍵=>選擇項目 Step2.切換至『COM 元件』頁籤並按下瀏覽鍵。 Step3.找到Windows\\System32下的msdxm.ocx檔後按下開啟鍵。 Step4.會看到多了一個Windows Media Player的Com元件，此時勾選並按下確定鍵。"
tags: [CSharp,VB.NET]
---

## 加入工具箱

**Step1.**工具箱=>滑鼠右鍵=>選擇項目

![image_thumb_1.png](/images/posts/7319/image_thumb_1.png)

**Step2.**切換至『COM 元件』頁籤並按下瀏覽鍵。

![image_thumb.png](/images/posts/7319/image_thumb.png)

**Step3.**找到Windows\System32下的msdxm.ocx檔後按下開啟鍵。

![image_thumb_2.png](/images/posts/7319/image_thumb_2.png)

**Step4.**會看到多了一個Windows Media Player的Com元件，此時勾選並按下確定鍵。

![image_thumb_3.png](/images/posts/7319/image_thumb_3.png)

**Step5.**會發現工具箱多了個Windows Media Player的控制項

![image_thumb_5.png](/images/posts/7319/image_thumb_5.png)

## 使用AxMediaPlayer撥放多媒體

**Step1.**加入Windows Media Player控制項到設計表單，可看到如下的畫面。

![image_thumb_6.png](/images/posts/7319/image_thumb_6.png)

**Step2.**依序加入控制項使介面如下圖所示。

![image_thumb_8.png](/images/posts/7319/image_thumb_8.png)

**Step3.**撰寫控制項初始設定程式碼

此處是設定控制項的初始值，像是音量的最大值、最小值與目前的音量，值得注意的是AxMediaPlayer控制項的音量大小好像介於-10000~0之間，另外若不設定AutoStart = False則開啟檔案完程式就會自動撥放開啟的多媒體檔。

VB.NET

```
Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
    Me.AxMediaPlayer1.AutoStart = False              '設定不自動撥放
    Me.tbarVolume.Minimum = -10000                    '設定音量調整Bar最小值為最小音量值
    Me.tbarVolume.Maximum = 0                         '設定音量調整Bar最大值為最大音量值
    Me.tbarVolume.Value = Me.AxMediaPlayer1.Volume    '設定音量調整Bar目前值為目前音量值
End Sub
```

C#

```
private void Form1_Load(object sender, EventArgs e)
{
    this.axMediaPlayer1.AutoStart = false;              //設定不自動撥放
    this.tbarVolume.Minimum = -10000;                   //設定音量調整Bar最小值為最小音量值(-10000)
    this.tbarVolume.Maximum = 0;                        //設定音量調整Bar最大值為最大音量值(0)
    this.tbarVolume.Value = this.axMediaPlayer1.Volume; //設定音量調整Bar目前值為目前音量值
}
```

**Step4.**撰寫開啟程式碼

AxMediaPlayer控制項的開啟可以直接設定FileName，亦可以使用Open函式。這邊除了開啟檔案外也需順道設定撥放位置的最大值與最小值。

VB.NET

```
Private Sub btnOpen_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnOpen.Click
    If OpenFileDialog1.ShowDialog = Windows.Forms.DialogResult.OK Then
        'Me.AxMediaPlayer1.Open(OpenFileDialog1.FileName)
        Me.AxMediaPlayer1.FileName = OpenFileDialog1.FileName               '開啟檔案
        Me.tbarPlayLoaction.Minimum = CInt(Me.AxMediaPlayer1.SelectionStart)       '設定撥放位置調整Bar最小值
        Me.tbarPlayLoaction.Maximum = CInt(Me.AxMediaPlayer1.SelectionEnd)         '設定撥放位置調整Bar最大值
    End If
End Sub
```

C#

```
private void btnOpen_Click(object sender, EventArgs e)
{
    if (openFileDialog1.ShowDialog() == DialogResult.OK) {
        //this.axMediaPlayer1.Open(openFileDialog1.FileName);
        this.axMediaPlayer1.FileName = openFileDialog1.FileName;                    //開啟檔案
        this.tbarPlayLoaction.Minimum = (int)this.axMediaPlayer1.SelectionStart;    //設定撥放位置調整Bar最小值
        this.tbarPlayLoaction.Maximum = (int)this.axMediaPlayer1.SelectionEnd;      //設定撥放位置調整Bar最大值
    }
}
```

**Step5.**撰寫撥放程式碼

撰寫這部份功能程式碼只需呼叫AxMediaPlayer.Play()即可。

VB.NET

```
Private Sub btnPlay_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnPlay.Click
    Me.AxMediaPlayer1.Play()        '撥放
End Sub
```

C#

```
private void btnPlay_Click(object sender, EventArgs e)
{
    this.axMediaPlayer1.Play();        //撥放
}
```

**Step6.**撰寫停止程式碼

這邊需注意的是，AxMediaPlayer控制項的Stop函式雖然會停止撥放，但是停止後撥放位置仍維持在原位，因此當又按下撥放時，該控制項會從上次位置繼續撥放，有點類似暫停的功能(跟暫停的差異在於它會按下控制項上的Stop按鈕)，因此這邊須自行把撥放位置設回起始點。

VB.NET

```
Private Sub btnStop_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnStop.Click
    Me.AxMediaPlayer1.Stop()                '停止
    AxMediaPlayer1.CurrentPosition = 0      '把撥放位置設回起點
End Sub
```

C#

```
private void btnStop_Click(object sender, EventArgs e)
{
    this.axMediaPlayer1.Stop();                     //停止
    this.axMediaPlayer1.CurrentPosition = 0;        //把撥放位置設回起點
}
```

**Step7.**撰寫暫停撥放程式碼

撰寫這部份功能程式碼只需呼叫AxMediaPlayer.Pause()即可。

VB.NET

```
Private Sub btnPause_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnPause.Click
    Me.AxMediaPlayer1.Pause()       '暫停撥放
End Sub
```

C#

```
private void btnPause_Click(object sender, EventArgs e)
{
    this.axMediaPlayer1.Pause();       //暫停撥放
}
```

**Step8.**撰寫音量控制程式碼

這部份功能程式碼只需對AxMediaPlayer.Volume做屬性值的變更即可。

VB.NET

```
Private Sub tbarVolume_Scroll(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles tbarVolume.Scroll
    Me.AxMediaPlayer1.Volume = tbarVolume.Value                     '改變音量大小
End Sub

Private Sub btnIncreaseVolume_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnIncreaseVolume.Click
    Me.AxMediaPlayer1.Volume += 1       '音量大小+1
End Sub

Private Sub btnDecreaseVolume_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnDecreaseVolume.Click
    Me.AxMediaPlayer1.Volume -= 1       '音量大小-1
End Sub
```

C#

```
private void tbarVolume_Scroll(object sender, EventArgs e)
{
    this.axMediaPlayer1.Volume = tbarVolume.Value;                     //改變音量大小
}

private void btnIncreaseVolume_Click(object sender, EventArgs e)
{
    this.axMediaPlayer1.Volume += 1;       //音量大小+1
}

private void btnDecreaseVolume_Click(object sender, EventArgs e)
{
    this.axMediaPlayer1.Volume -= 1;       //音量大小-1
}
```

**Step9.**撰寫撥放位置控制程式碼

這部份功能程式碼只需對AxMediaPlayer.CurrentPosition做屬性值的變更即可。

VB.NET

```
Private Sub tbarPlayLoaction_Scroll(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles tbarPlayLoaction.Scroll
    Me.AxMediaPlayer1.CurrentPosition = tbarPlayLoaction.Value          '改變撥放位置
End Sub
```

C#

```
private void tbarPlayLoaction_Scroll(object sender, EventArgs e)
{
    this.axMediaPlayer1.CurrentPosition = tbarPlayLoaction.Value;          //改變撥放位置
}
```

## Download

使用AxMediaPlayer撥放多媒體.zip

## 參考連結

1. 藍色小鋪 - media 播放設定問題
2. [如何使用 Visual Basic.NET 或 Visual Basic 2005 中播放音訊檔案](http://support.microsoft.com/kb/821767/zh-tw)
