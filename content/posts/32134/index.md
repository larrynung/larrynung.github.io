---
title: "[C#]DictService"
slug: "[CSharp]DictService"
date: "2011-07-26 01:18:26"
description: "DictService是一個免費的Web Service，可用來做單字與單字的定義查詢，允許非商業與商業使用。 有興趣的可先至Definition Lookup網站上使用看看，輸入關鍵字並選取想要查詢的字典，按下[Search]按鈕搜尋的結果就會顯示在下方。"
tags: [CSharp]
---

DictService是一個免費的Web Service，可用來做單字與單字的定義查詢，允許非商業與商業使用。

![image_thumb.png](/images/posts/32134/image_thumb.png)

有興趣的可先至[Definition Lookup](http://services.aonaware.com/DictService/)網站上使用看看，輸入關鍵字並選取想要查詢的字典，按下[Search]按鈕搜尋的結果就會顯示在下方。這個Web Service所能提供給我們開發人員的就是這些資訊，像是字典有哪些、搜尋的內容、單字的定義...等。

![image_thumb_6.png](/images/posts/32134/image_thumb_6.png)

使用時，我們需先將Web Service加入。可在方案總管上面點選滑鼠右鍵，在滑鼠右鍵選單中選取[Add Service Reference...]。

![image_thumb_1.png](/images/posts/32134/image_thumb_1.png)

在[Add Service Reference]對話框中點擊左下方的[Advanced...]按鈕。

![image_thumb_2.png](/images/posts/32134/image_thumb_2.png)

在[Service Reference Settings]對話框中點擊左下方的[Add Web Reference...]按鈕。

![image_thumb_3.png](/images/posts/32134/image_thumb_3.png)

在[Add Web Reference]對話框中輸入Web Service的網址(<http://services.aonaware.com/DictService/DictService.asmx>)，再點擊[Add Reference]按鈕將Web Service加入專案參考。

![image_thumb_4.png](/images/posts/32134/image_thumb_4.png)

專案參考加入後，在程式中加入DictServceDemo.com.aonaware.services命名空間。

```csharp
using DictServceDemo.com.aonaware.services;
```

再建立DictService物件就可以使用了。像是DictService.DictionaryList()可以取得字典的列表、DictService.DictionaryInfo()可以取得字典的描述、DictService.Match()與DictService.MatchInDict()可以查詢符合的單字、DictService.Define()與DictService.DefineInDict()可以查詢單字的定義。

這邊示範一個較為完整的使用範例，運行畫面如下：

![image_thumb_5.png](/images/posts/32134/image_thumb_5.png)

完整的程式碼如下：

```csharp
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using DictServceDemo.com.aonaware.services;

namespace DictServceDemo
{
    public partial class Form1 : Form
    {

        #region Var
        private DictService _dictService;
        #endregion

        #region Private Property
        public DictService m_DictService
        {
            get
            {
                if (_dictService == null)
                    _dictService = new DictService();
                return _dictService;
            }
        }
        #endregion

        #region Constructor
        public Form1()
        {
            InitializeComponent();
        }
        #endregion

        #region Event Process
        private void Form1_Load(object sender, EventArgs e)
        {
            cbxDict.DisplayMember = "Name";
            cbxDict.DataSource = m_DictService.DictionaryList();

            cbxStrategy.DisplayMember = "Id";
            cbxStrategy.DataSource = m_DictService.StrategyList();
        }

        private void lbxResult_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (cbxDict.SelectedItem == null)
                return;

            if (lbxResult.SelectedItem == null)
                return;

            var dict = cbxDict.SelectedItem as Dictionary;
            var dictWord = lbxResult.SelectedItem as DictionaryWord;

            lbxDefine.DisplayMember = "WordDefinition";
            lbxDefine.DataSource = m_DictService.DefineInDict(dict.Id, dictWord.Word).Definitions;
        }

        private void tbxKeyword_KeyUp(object sender, KeyEventArgs e)
        {
            if (cbxDict.SelectedItem == null)
                return;

            if (cbxStrategy.SelectedItem == null)
                return;

            lbxDefine.DataSource = null;

            if (tbxKeyword.Text.Length == 0)
            {
                lbxResult.DataSource = null;
                return;
            }

            var dict = cbxDict.SelectedItem as Dictionary;
            var strategy = cbxStrategy.SelectedItem as Strategy;

            lbxResult.DisplayMember = "Word";
            lbxResult.DataSource = m_DictService.MatchInDict(dict.Id, tbxKeyword.Text, strategy.Id);
        }
        #endregion
    }
}
```

看到這邊可能有人會覺得這不會用到，因為字典內的定義資料並不會是我所想要的呈現方式，但是其實他的單字匹配功能倒是滿實用的，像是如果想要檢查單字或是在輸入時給些提示時，這服務就能派上用場，像是下面簡陋的範例一樣。

![image_thumb_7.png](/images/posts/32134/image_thumb_7.png)

```csharp
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using WindowsFormsApplication6.com.aonaware.services;

namespace WindowsFormsApplication6
{
    public partial class Form1 : Form
    {

        #region Var
        private AutoCompleteStringCollection _autoCompleteSource;
        private DictService _dictService;
        #endregion

        #region Private Property
        private AutoCompleteStringCollection m_AutoCompleteSource
        {
            get
            {
                if (_autoCompleteSource == null)
                    _autoCompleteSource = new AutoCompleteStringCollection();
                return _autoCompleteSource;
            }
            set
            {
                _autoCompleteSource = value;
            }
        }

        private DictService m_DictService
        {
            get
            {
                if (_dictService == null)
                {
                    _dictService = new DictService();
                    _dictService.MatchInDictCompleted += new MatchInDictCompletedEventHandler(m_DictService_MatchInDictCompleted);
                }
                return _dictService;
            }
        }
        #endregion

        public Form1()
        {
            InitializeComponent();
            textBox1.AutoCompleteMode = AutoCompleteMode.Append;
            textBox1.AutoCompleteSource = AutoCompleteSource.CustomSource;
        }

        #region Event Process
        private void textBox1_KeyUp(object sender, KeyEventArgs e)
        {
            if (textBox1.Text.Length == 0)
                return;

            textBox1.AutoCompleteCustomSource = m_AutoCompleteSource;

            var userState = new object();
            m_DictService.CancelAsync(userState);
            m_DictService.MatchInDictAsync("wn", textBox1.Text, "prefix", userState);
        }

        void m_DictService_MatchInDictCompleted(object sender, MatchInDictCompletedEventArgs e)
        {
            if (e.Cancelled)
                return;

           m_AutoCompleteSource = new AutoCompleteStringCollection();
            m_AutoCompleteSource.AddRange(e.Result.Select((item) => item.Word).ToArray());
        }
        #endregion

    }
}
```

## Download

DictServceDemo.zip

## Link

* DictService
* Sample Dictionary Service Client Application
* Definition Lookup
