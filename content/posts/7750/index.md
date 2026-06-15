---
title: "[Control][C#]WebCamPictureBox Control"
date: "2009-03-29 11:08:51"
description: "[Control][C#]WebCamPictureBox Control"
tags: [Control,CSharp]
---

WebCamPictureBox 是我很久以前拿在討論區看到的範例所改的控制項，不過範例我找不到了，有找到的麻煩通知我一下。主要功能是結合WebCam與PictureBox，透過該控制項能輕鬆的控制WebCam (附檔含控制項程式碼與使用範例)。

主要功能如下：

![image_thumb.png](/images/posts/7750/image_thumb.png)

**測試WebCam連線狀態**

```
if (this.webCamPictureBox1.TestConnect())
{
    MessageBox.Show("WebCam connect state is ok");
}
else
{
    MessageBox.Show("WebCam connect state is error");
}
```

**啟動WebCam**

```
this.webCamPictureBox1.Start();
```

**停止WebCam**

```
this.webCamPictureBox1.Stop();
```

**判斷WebCam是否啟動**

```
this.toolStripStatusLabel2.Text = this.webCamPictureBox1 .IsStarted?"Start":"Stop";
```

##

## CodePlex

WebCamPictureBox
