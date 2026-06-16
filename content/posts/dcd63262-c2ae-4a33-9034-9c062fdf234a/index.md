---
title: "[C#][VB.NET]A Custom Exception Dialog"
slug: "csharp-vbnet-a-custom-exception-dialog"
aliases: ["/posts/csharpvb.net自定義例外對話框/"]
date: "2013-11-06 12:00:00"
description: "之前在『例外處理使用時機』這篇有提到我目前很少會寫例外處理。除了在那篇提到的原因之外，還有個因素就是我會弄個自定義的例外處理視窗，讓使用者在例外發生時，可以匯出例外訊息並提供給開發人員。有了匯出的例外訊息，我們就可以很快的把未處理完的例外(指給程式員看的例外)給修正。"
tags: [CSharp]
---

之前在『例外處理使用時機』這篇有提到我目前很少會寫例外處理。除了在那篇提到的原因之外，還有個因素就是我會弄個自定義的例外處理視窗，讓使用者在例外發生時，可以匯出例外訊息並提供給開發人員。有了匯出的例外訊息，我們就可以很快的把未處理完的例外(指給程式員看的例外)給修正。

要做到自定義的例外對話框，我們需要利用Application.ThreadException事件。

先讓我們看一下MSDN的說明：

![image_thumb.png](/images/posts/dcd63262-c2ae-4a33-9034-9c062fdf234a/image_thumb.png)

從MSDN的說明可以很清楚的看到，當執行緒發生例外，且該例外未被處理，則該事件即會觸發。

接著就讓我們來看看如何才能利用該事件做出自定義的例外對話框。首先，我們需要設計自定義的例外對話框。

![image_thumb_1.png](/images/posts/dcd63262-c2ae-4a33-9034-9c062fdf234a/image_thumb_1.png)

接著撰寫繫上事件用的副程式。

VB.NET

```
Public Shared Sub ShowBugWindowOnError()
    AddHandler Application.ThreadException, AddressOf OnErrorOccur
End Sub
```

C#

```
public static void ShowBugWindowOnError()
{
    Application.ThreadException += new System.Threading.ThreadExceptionEventHandler(OnErrorOccur);
}
```

最後寫上事件觸發時要執行的事件處理函式。

VB.NET

```
Protected Shared Sub OnErrorOccur(ByVal sender As Object, ByVal e As ThreadExceptionEventArgs)
    Dim errorDlg As New ExceptionDialog
    errorDlg.DetailErrorMsg_TextBox.Text = GetDetailErrorMsg(e.Exception)
    errorDlg.ShowDialog()
End Sub
```

C#

```
protected static void OnErrorOccur(object sender, System.Threading.ThreadExceptionEventArgs e)
{
    ExceptionDlg errorDlg = new ExceptionDlg();
    errorDlg.DetailErrorMsg_TextBox.Text = GetDetailErrorMsg(e.Exception);
    errorDlg.ShowDialog();
}
```

到此一個簡單的自定義例外對話框就完成了。使用上，我們只需呼叫剛寫的繫上事件用副程式即可。

VB.NET

```
Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
     ExceptionDialog.ShowBugWindowOnError()
 End Sub
```

C#

```
private void Form1_Load(object sender, EventArgs e)
{
    ExceptionDlg.ShowBugWindowOnError();
}
```

完整程式碼：

VB.NET

```
Imports System.Windows.Forms
Imports System.Threading
Imports System.Text

Public Class ExceptionDialog

#Region "Const"
    Const OpenDetailButtonText As String = "v 詳細資料"
    Const CloseDetailButtonText As String = "^ 詳細資料"
#End Region

#Region "Var"
    Private _isDetailOpened As Boolean
#End Region

#Region "Public Shared Method"

    '***************************************************************************
    'Author: Larry Nung
    'Date: 2009/4/9
    'Purpose:
    'Memo:
    '***************************************************************************
    ''' <summary>
    ''' Shows the bug window on error.
    ''' </summary>
    ''' <remarks></remarks>
    Public Shared Sub ShowBugWindowOnError()
        AddHandler Application.ThreadException, AddressOf OnErrorOccur
    End Sub
#End Region

#Region "Protected Shared Method"

    '***************************************************************************
    'Author: Larry Nung
    'Date: 2009/4/9
    'Purpose:
    'Memo:
    '***************************************************************************
    ''' <summary>
    ''' Called when [error occur].
    ''' </summary>
    ''' <param name="sender">The sender.</param>
    ''' <param name="e">The <see cref="System.Threading.ThreadExceptionEventArgs" /> instance containing the event data.</param>
    ''' <remarks></remarks>
    Protected Shared Sub OnErrorOccur(ByVal sender As Object, ByVal e As ThreadExceptionEventArgs)
        Dim errorDlg As New ExceptionDialog
        errorDlg.DetailErrorMsg_TextBox.Text = GetDetailErrorMsg(e.Exception)
        errorDlg.ShowDialog()
    End Sub
#End Region

#Region "Private Shared Method"

    '***************************************************************************
    'Author: Larry Nung
    'Date: 2009/4/9
    'Purpose:
    'Memo:
    '***************************************************************************
    ''' <summary>
    ''' Gets the detail error MSG.
    ''' </summary>
    ''' <returns></returns>
    ''' <remarks></remarks>
    Private Shared Function GetDetailErrorMsg(ByVal e As Exception) As String
        Dim str As New StringBuilder
        str.AppendLine(String.Format("Source: {0}", e.Source))
        str.AppendLine(String.Format("Message: {0}", e.Message))
        str.AppendLine(String.Format("TargetSite: {0}", e.TargetSite))
        str.AppendLine("")
        str.AppendLine("StackTrace: ")
        str.AppendLine(e.StackTrace)
        Return str.ToString
    End Function
#End Region

#Region "Event Process"
    Private Sub OK_Button_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles OK_Button.Click
        Me.DialogResult = System.Windows.Forms.DialogResult.OK
        Me.Close()
    End Sub

    Private Sub Cancel_Button_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Cancel_Button.Click
        Me.DialogResult = System.Windows.Forms.DialogResult.Cancel
        Application.Exit()
    End Sub

    Private Sub Detail_Button_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Detail_Button.Click
        _isDetailOpened = Not _isDetailOpened
        Detail_Button.Text = If(_isDetailOpened, CloseDetailButtonText, OpenDetailButtonText)
        Me.Height = If(_isDetailOpened, Me.DetailErrorMsg_TextBox.Bottom, Me.DetailErrorMsg_TextBox.Top) + 32
    End Sub

    Private Sub ExceptionDialog_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        Me.Height = Me.DetailErrorMsg_TextBox.Top + 32
        Me.ErrorIcon_Label.Image = SystemIcons.Error.ToBitmap
    End Sub
#End Region

End Class
```

C#

```
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace ExceptionDlgTest
{
    public partial class ExceptionDlg : Form
    {

        #region Const
        const string OpenDetailButtonText = "v 詳細資料";
        const string CloseDetailButtonText = "^ 詳細資料";
        #endregion

        #region Var
        private Boolean _isDetailOpened;
        #endregion

        #region Construction
        public ExceptionDlg()
        {
            InitializeComponent();
        }
        #endregion

        #region Public Shared Method

        //***************************************************************************
        //Author: Larry Nung
        //Date: 2009/4/9
        //Purpose:
        //Memo:
        //***************************************************************************
        /// <summary>
        ///
        /// </summary>
        public static void ShowBugWindowOnError()
        {
            Application.ThreadException += new System.Threading.ThreadExceptionEventHandler(OnErrorOccur);
        }
        #endregion

        #region Protected Shared Method
        protected static void OnErrorOccur(object sender, System.Threading.ThreadExceptionEventArgs e)
        {
            ExceptionDlg errorDlg = new ExceptionDlg();
            errorDlg.DetailErrorMsg_TextBox.Text = GetDetailErrorMsg(e.Exception);
            errorDlg.ShowDialog();
        }
        #endregion

        #region Private Shared Method
        private static string GetDetailErrorMsg(Exception e)
        {
            StringBuilder str = new StringBuilder();
            str.AppendLine(String.Format("Source: {0}", e.Source));
            str.AppendLine(String.Format("Message: {0}", e.Message));
            str.AppendLine(String.Format("TargetSite: {0}", e.TargetSite));
            str.AppendLine("");
            str.AppendLine("StackTrace: ");
            str.AppendLine(e.StackTrace);
            return str.ToString();
        }
        #endregion

        #region Event Process
        private void Cancel_Button_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void OK_Button_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void Detail_Button_Click(object sender, EventArgs e)
        {
            _isDetailOpened = !_isDetailOpened;
            Detail_Button.Text = _isDetailOpened ? CloseDetailButtonText : OpenDetailButtonText;
            this.Height = _isDetailOpened ? this.DetailErrorMsg_TextBox.Bottom : this.DetailErrorMsg_TextBox.Top + 32;
        }

        private void ExceptionDlg_Load(object sender, EventArgs e)
        {
            this.Height = this.DetailErrorMsg_TextBox.Top + 32;
            this.ErrorIcon_Label.Image = SystemIcons.Error.ToBitmap();
        }
        #endregion

    }
}
```

執行畫面如下：

![image_thumb_2.png](/images/posts/dcd63262-c2ae-4a33-9034-9c062fdf234a/image_thumb_2.png)

![image_thumb_3.png](/images/posts/dcd63262-c2ae-4a33-9034-9c062fdf234a/image_thumb_3.png)

## Conclusion

透過Application.ThreadException事件，我們可以很容易達到該篇的效果。但需注意這樣的作法只對繫上的執行緒有效，非繫上的執行緒若發生例外，將無法截取到。在實際應用上，也可依自己需求加入記錄到事件記錄簿等功能，甚至可以使用.NET預設的例外視窗來顯示，只是多加了一些自己的處理，讓使用者感覺不出差異。

```vb
Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
    AddHandler Application.ThreadException, AddressOf Application_ThreadException
    ...
End Sub

Private Sub Application_ThreadException(ByVal sender As Object, ByVal e As ThreadExceptionEventArgs)
    ...
    Dim exceptionDlg As New ThreadExceptionDialog(e.Exception)
    exceptionDlg.ShowDialog()
End Sub
```

![image_thumb.png](/images/posts/dcd63262-c2ae-4a33-9034-9c062fdf234a/image_thumb.png)

另外，若有興趣的也可以改繫上AppDomain.UnhandledException試看看。

![image_thumb_4.png](/images/posts/dcd63262-c2ae-4a33-9034-9c062fdf234a/image_thumb_4.png)

## Download

ExceptionDlg.zip
