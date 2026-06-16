---
title: "[C#][VB.NET]自定義.NET WindowForm表單介面(二)"
slug: "csharp-vbnet-自定義-dotnet-windowform表單介面-二"
aliases: ["/posts/csharpvb.net自定義.net-windowform表單介面二/"]
date: "2009-03-21 11:19:35"
description: "之前寫過一篇『自定義.NET WindowForm表單介面』，據網友反應才注意到其做出來的視窗無縮放的效果，因此這篇的重點將Focuse在自定義表單的縮放功能實作。 要實作具縮放功能的WindowForm表單目前得知的方法大概有三種，這邊就讓我們分別來探討。"
tags: [VB.NET,CSharp]
---

之前寫過一篇『自定義.NET WindowForm表單介面』，據網友反應才注意到其做出來的視窗無縮放的效果，因此這篇的重點將Focuse在自定義表單的縮放功能實作。

要實作具縮放功能的WindowForm表單目前得知的方法大概有三種，這邊就讓我們分別來探討。

### 方法一  用 FormBorderStyle = None 來做自定義表單並自行實作縮放

用 FormBorderStyle = None 來做自定義表單的方法請參考『[自定義.NET WindowForm表單介面』這篇，實做完後加入如下縮放代碼即可。](http://www.dotblogs.com.tw/larrynung/archive/2008/11/11/5959.aspx)

VB.NET

```
Enum Direction
     NONE
     TOP
     BOTTOM
     LEFT
     RIGHT
     LEFTTOP
     LEFTBOTTOM
     RIGHTTOP
     RIGHTBOTTOM
 End Enum

 Dim alreadyCaptured As Boolean
 Dim x As Integer
 Dim y As Integer
 Dim interval As Integer = 5
 Dim adjustDirection As Direction

 Private Sub Form_MouseMove(ByVal sender As Object, ByVal e As System.Windows.Forms.MouseEventArgs) Handles Me.MouseMove
     If Me.Capture Then
         If alreadyCaptured Then
             AdjustBounds(e)
         End If

         x = e.X
         y = e.Y
     Else
         SetAdjustDirection(e)
         SetCursor()
     End If
     alreadyCaptured = Me.Capture
 End Sub

 Private Function IsMatch(ByVal n As Integer, ByVal xy As Integer) As Boolean
     Return (xy - interval < n) AndAlso (n < xy + interval)
 End Function

 Private Sub SetCursor()
     Select Case adjustDirection
         Case Direction.LEFTTOP, Direction.RIGHTBOTTOM
             Me.Cursor = Cursors.SizeNWSE
         Case Direction.RIGHTTOP, Direction.LEFTBOTTOM
             Me.Cursor = Cursors.SizeNESW
         Case Direction.LEFT, Direction.RIGHT
             Me.Cursor = Cursors.SizeWE
         Case Direction.TOP, Direction.BOTTOM
             Me.Cursor = Cursors.SizeNS
         Case Direction.NONE
             Me.Cursor = Cursors.Default
     End Select
 End Sub

 Private Sub SetAdjustDirection(ByVal e As System.Windows.Forms.MouseEventArgs)
     If IsMatch(e.X, 0) AndAlso IsMatch(e.Y, 0) Then
         adjustDirection = Direction.LEFTTOP
     ElseIf IsMatch(e.X, 0) AndAlso IsMatch(e.Y, Me.Height - 1) Then
         adjustDirection = Direction.LEFTBOTTOM
     ElseIf IsMatch(e.X, Me.Width - 1) AndAlso IsMatch(e.Y, 0) Then
         adjustDirection = Direction.RIGHTTOP
     ElseIf IsMatch(e.X, Me.Width - 1) AndAlso IsMatch(e.Y, Me.Height - 1) Then
         adjustDirection = Direction.RIGHTBOTTOM
     ElseIf IsMatch(e.X, 0) Then
         adjustDirection = Direction.LEFT
     ElseIf IsMatch(e.X, Me.Width - 1) Then
         adjustDirection = Direction.RIGHT
     ElseIf IsMatch(e.Y, 0) Then
         adjustDirection = Direction.TOP
     ElseIf IsMatch(e.Y, Me.Height - 1) Then
         adjustDirection = Direction.BOTTOM
     Else
         adjustDirection = Direction.NONE
     End If
 End Sub

 Private Sub AdjustBounds(ByVal e As System.Windows.Forms.MouseEventArgs)
     Dim x As Integer = e.X - Me.x
     Dim y As Integer = e.Y - Me.y
     Select Case adjustDirection
         Case Direction.LEFTTOP
             Me.Left += e.X
             Me.Width -= e.X
             Me.Top += e.Y
             Me.Height -= e.Y
         Case Direction.LEFTBOTTOM
             Me.Left += e.X
             Me.Width -= e.X
             Me.Height += y
         Case Direction.RIGHTBOTTOM
             Me.Width += x
             Me.Height += y
         Case Direction.RIGHTTOP
             Me.Top += e.Y
             Me.Height -= e.Y
             Me.Width += x
         Case Direction.LEFT
             Me.Left += e.X
             Me.Width -= e.X
         Case Direction.RIGHT
             Me.Width += x
         Case Direction.TOP
             Me.Top += e.Y
             Me.Height -= e.Y
         Case Direction.BOTTOM
             Me.Height += y
     End Select
 End Sub
```

C#

```
enum Direction
     {
         NONE,
         TOP,
         BOTTOM,
         LEFT,
         RIGHT,
         LEFTTOP,
         LEFTBOTTOM,
         RIGHTTOP,
         RIGHTBOTTOM
     };
     Boolean alreadyCaptured;
     int x;
     int y;
     int interval = 5;
     Direction adjustDirection;
     private void Form1_MouseMove(object sender, MouseEventArgs e)
     {
         if (this.Capture)
         {
             if (alreadyCaptured)
                 AdjustBounds(e);
             x = e.X;
             y = e.Y;
         }
         else
         {
             SetAdjustDirection(e);
             SetCursor();
         }
         alreadyCaptured = this.Capture;

     }

     private Boolean IsMatch(int n, int xy)
     {
         return (xy - interval < n) && (n < xy + interval);
     }

     private void SetCursor()
     {
         switch (adjustDirection)
         {
             case Direction.LEFTTOP :
             case Direction .RIGHTBOTTOM :
                 this.Cursor = Cursors.SizeNWSE;
                 break;
             case Direction.RIGHTTOP:
             case Direction.LEFTBOTTOM:
                 this.Cursor = Cursors.SizeNESW;
                 break;
             case Direction.LEFT:
             case Direction.RIGHT:
                 this.Cursor = Cursors.SizeWE;
                 break;
             case Direction.TOP:
             case Direction.BOTTOM:
                 this.Cursor = Cursors.SizeNS;
                 break;
             default :
                 this.Cursor = Cursors.Default;
                 break;
         }
     }

     private void SetAdjustDirection(System.Windows.Forms.MouseEventArgs e)
     {
         if (IsMatch(e.X, 0) && IsMatch(e.Y, 0))
         {
             adjustDirection = Direction.LEFTTOP;
         }
         else if (IsMatch(e.X, 0) && IsMatch(e.Y, this.Height - 1))
         {
             adjustDirection = Direction.LEFTBOTTOM;
         }
         else if (IsMatch(e.X, this.Width - 1) && IsMatch(e.Y, 0))
         {
             adjustDirection = Direction.RIGHTTOP;
         }
         else if (IsMatch(e.X, this.Width - 1) && IsMatch(e.Y, this.Height - 1))
         {
             adjustDirection = Direction.RIGHTBOTTOM;
         }
         else if (IsMatch(e.X, 0))
         {
             adjustDirection = Direction.LEFT;
         }
         else if (IsMatch(e.X, this.Width - 1))
         {
             adjustDirection = Direction.RIGHT;
         }
         else if (IsMatch(e.Y, 0))
         {
             adjustDirection = Direction.TOP;
         }
         else if (IsMatch(e.Y, this.Height - 1))
         {
             adjustDirection = Direction.BOTTOM;
         }
         else
         {
             adjustDirection = Direction.NONE;
         }
     }
     private void AdjustBounds(System.Windows.Forms.MouseEventArgs e)
     {
         int x = e.X - this.x;
         int y = e.Y - this.y;
         switch (adjustDirection)
         {
             case Direction.LEFTTOP:
                 this.Left += e.X;
                 this.Width -= e.X;
                 this.Top += e.Y;
                 this.Height -= e.Y;
                 break;
             case Direction.LEFTBOTTOM:
                 this.Left += e.X;
                 this.Width -= e.X;
                 this.Height += y;
                 break;
             case Direction.RIGHTBOTTOM:
                 this.Width += x;
                 this.Height += y;
                 break;
             case Direction.RIGHTTOP:
                 this.Top += e.Y;
                 this.Height -= e.Y;
                 this.Width += x;
                 break;
             case Direction.LEFT:
                 this.Left += e.X;
                 this.Width -= e.X;
                 break;
             case Direction.RIGHT:
                 this.Width += x;
                 break;
             case Direction.TOP:
                 this.Top += e.Y;
                 this.Height -= e.Y;
                 break;
             case Direction.BOTTOM:
                 this.Height += y;
                 break;
         }
     }
```

用這方法的缺點就是比較麻煩，有點土法鍊鋼的感覺。而且有個問題存在，就是當滑鼠移到工作列上(如下圖)按右鍵，右鍵選單不會出來。

![image_thumb.png](/images/posts/7625/image_thumb.png)

### 方法二 用 ControlBox = False 來做自定義表單

用 ControlBox = False 來做自定義表單的方法很簡單，簡述如下：

**Step1.Form.ControlBox設為False**

![image_thumb_1.png](/images/posts/7625/image_thumb_1.png)

**Step2.清空Form.Text**

![image_thumb_2.png](/images/posts/7625/image_thumb_2.png)

如下圖所示，設完後會發現表單的標題列已經消失。

![image_thumb_3.png](/images/posts/7625/image_thumb_3.png)

**Step3.依照『**[**自定義.NET WindowForm表單介面**](http://www.dotblogs.com.tw/larrynung/archive/2008/11/11/5959.aspx)**』這篇的要領完成自定義表單。**

用這方法可以很簡單的做出自定義表單，且表單本來具有的縮放功能仍會存在，因此我們不需額外處理表單的縮放。但是這個方法仍有缺點存在，如下圖，使用該方法工作列上的標題會是空的，且按右鍵也是無選單彈出。

![image_thumb_4.png](/images/posts/7625/image_thumb_4.png)

### 方法三 利用Form.Region來做自定義表單

利用Form.Region來做自定義表單的方法簡述如下：

**Step1.加入程式碼用以去掉標題列**

VB.NET

```
Dim r As Rectangle = New Rectangle(0, 30, Me.Width, Me.Height)
Me.Region = New Region(r)
```

C#

```
Rectangle r = new Rectangle(0, 30, this.Width, this.Height);
this.Region = new Region(r);
```

**Step2.依照『****自定義.NET WindowForm表單介面****』這篇的要領完成自定義表單。**

**Step3.依照方法一的方法補上表單上方的縮放功能**

用這方法可以很簡單的做出自定義表單，基本上該有的功能也都有，只是需要額外補上表單上方的縮放功能而已。
