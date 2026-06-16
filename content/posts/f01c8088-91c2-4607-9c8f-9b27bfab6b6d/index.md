---
title: "[C#]使用Microsoft Translator Soap API實作翻譯功能"
slug: "[CSharp]使用Microsoft Translator Soap API實作翻譯功能"
date: "2013-11-06 12:00:00"
description: "要使用Microsoft Translator Soap API實作翻譯功能，首先我們必須要有Bing的開發者ID，可至Bing Developer網站申請。可點選『註冊以使用 Bing 搜尋 API 並建立 AppID』或是透過『建立您的 AppID』開始進行申請。"
tags: [CSharp]
---

要使用Microsoft Translator Soap API實作翻譯功能，首先我們必須要有Bing的開發者ID，可至Bing Developer網站申請。可點選『註冊以使用 Bing 搜尋 API 並建立 AppID』或是透過『建立您的 AppID』開始進行申請。

![image_thumb_1.png](/images/posts/f01c8088-91c2-4607-9c8f-9b27bfab6b6d/image_thumb_1.png)

接著按下『Add』按鈕新增一個應用程式。

![image_thumb_2.png](/images/posts/f01c8088-91c2-4607-9c8f-9b27bfab6b6d/image_thumb_2.png)

填寫要申請的應用程式相關資訊。

![image_thumb_3.png](/images/posts/f01c8088-91c2-4607-9c8f-9b27bfab6b6d/image_thumb_3.png)

都填好後系統會給予申請的應用程式一個Application ID，後續的開發會時常的需要帶入這個Application ID。

![image_thumb_4.png](/images/posts/f01c8088-91c2-4607-9c8f-9b27bfab6b6d/image_thumb_4.png)

有了Application ID後，在方案總管上按下右鍵，在彈出的滑鼠右鍵快顯選單中選取Add Service Reference， Visual Studio會帶出Add Service Reference對話方塊，在Address欄位中填入http://api.microsofttranslator.com/V2/Soap.svc後按下OK，這樣就完成了引用的動作，可以直接在程式中使用到Soap API現成的類別。

![image_thumb_8.png](/images/posts/f01c8088-91c2-4607-9c8f-9b27bfab6b6d/image_thumb_8.png)

接下來進入程式開發的階段，整個Microsoft Translator Soap API在使用上，最重要的類別就是LanguageServiceClient，必須建立一個LanguageServiceClient物件實體並對其操作，以完成我們想要的功能，像是偵測要翻譯的字串訊息是屬於哪種語言、如何取得可使用的語言清單、針對翻譯的內容發音、以及最重要的翻譯動作。

在偵測翻譯的字串訊息是屬於哪種語言上，我們可透過現成的API去偵測，將Application ID與要偵測的字串帶入。

```xml
http://api.microsofttranslator.com/V2/Http.svc/Detect?appId=[APP ID]&text=[字串訊息]
```

該API會回傳入下XML。

![image_thumb_10.png](/images/posts/f01c8088-91c2-4607-9c8f-9b27bfab6b6d/image_thumb_10.png)

因此在程式的撰寫上我們可以用WebRequest與WebResponse去取得網頁的內容，並擷取回傳的XML中我們感興趣的部分，就像是下面這樣：

```csharp
string GetDetectedLanguage(string text)
{
    const string DEFAULT_DETECTED_LANG = "en";

    if (String.IsNullOrEmpty(text))
        return DEFAULT_DETECTED_LANG;

    const string DETECT_API_URI_PATTERN = "http://api.microsofttranslator.com/V2/Http.svc/Detect?appId={0}&text={1}";
    const string MATCH_PATTERN = "<[^<>]*>([^<>]*)<[^<>]*>";

    WebRequest req = WebRequest.Create(String.Format(DETECT_API_URI_PATTERN, APP_ID, text));
    WebResponse resp = req.GetResponse();

    string local = DEFAULT_DETECTED_LANG;
    using (StreamReader reader = new StreamReader(resp.GetResponseStream()))
    {
        local = reader.ReadToEnd();
        local = Regex.Match(local, MATCH_PATTERN).Groups[1].Value;
    }
    return local;
}
```

在發音方面，可透過LanguageServiceClient.GetLanguagesForSpeak與LanguageServiceClient.Speak這兩個方法來實現。LanguageServiceClient.GetLanguagesForSpeak方法可以取得所有能支援發音的語言，可以用來列表發音的語系。LanguageServiceClient.Speak則是能取得發音檔的位置，帶入要發音的字串與期望的發音語系等資訊就可以了。抓出來的發音檔位置是一串網址，可直接透過MediaPlayer的Com元件下去撥放。

```csharp
string GetSpeakUri(LanguageServiceClient client, string text)
{
    string[] langs = client.GetLanguagesForSpeak(APP_ID);
    string lang = (cbTranslateTo.SelectedValue == null)? "en": cbTranslateTo.SelectedValue.ToString();

    if (!langs.Contains(lang))
        lang = "en";

    return client.Speak(APP_ID, tbxSource.Text, lang, "audio/wav", string.Empty);
}
```

而在取得能支援翻譯的語系方面，可使用LanguageServiceClient.GetLanguagesForTranslate與LanguageServiceClient.GetLanguageNames，LanguageServiceClient.GetLanguagesForTranslate可取得語系的代碼，LanguageServiceClient.GetLanguageNames則是可取得語系的名稱。若只是要以特定語系顯示能支援的語系名稱，只要像下面這樣就可以了：

```csharp
string   lang  = "en";
string[] langs = Client.GetLanguagesForTranslate(APP_ID);
string[] names = Client.GetLanguageNames(APP_ID, lang, langs);
```

這樣支援的語系名稱都會以英文的方式顯現，像是ja就會以Japan來顯示、en會以English。若是要以對應的語系來顯示支援的語系名稱，讓ja顯示日語、en顯示English，可以像下面這樣撰寫：

```csharp
void UpdateTranslationLanguages()
{
    string local = GetDetectedLanguage(tbxSource.Text);
    string[] langs = Client.GetLanguagesForTranslate(APP_ID);

    var langNames = (from lang in langs.AsParallel()
                     select new { Name = Client.GetLanguageNames(APP_ID, lang, new string[] { lang })[0], Value = lang }).ToList();

    cbTranslateTo.DisplayMember = "Name";
    cbTranslateTo.ValueMember = "Value";
    cbTranslateTo.DataSource = langNames;

    if (cbTranslateTo.Items.Count > 0)
        cbTranslateTo.Text = Client.GetLanguageNames(APP_ID, local, new string[] { local }).FirstOrDefault();
}
```

最後要提的是最重要的翻譯功能，直接叫用LanguageServiceClient.Translate就可以了，帶入的參數不外乎就是Application ID、要翻譯的訊息、要翻譯的訊息是何語系、要翻譯的語系...等。

```csharp
tbxTarget.Text = Client.Translate(APP_ID, tbxSource.Text, local, cbTranslateTo.SelectedValue.ToString(), "text/html", "general");
```

這邊筆者試做了個程式來展示API的功能，設計界面如下，期望該小程式能由使用者決定要翻譯的語系，能正常的翻譯到期望的語系，並具備發音的功能。

![image_thumb_9.png](/images/posts/f01c8088-91c2-4607-9c8f-9b27bfab6b6d/image_thumb_9.png)

完整的範例程式如下(Application ID部分請自行補上)：

```csharp
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Net;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using System.Windows.Forms;
using AxWMPLib;
using TranslateAPIDemo.TranslatorService;

namespace TranslateAPIDemo
{
    public partial class Form1 : Form
    {
        #region Const
        private const string APP_ID = "";
        #endregion

        #region Var
        private LanguageServiceClient _client;
        #endregion

        #region Property
        public LanguageServiceClient Client
        {
            get
            {
                if (_client == null)
                    _client = new LanguageServiceClient();
                return _client;
            }
        }
        #endregion

        public Form1()
        {
            InitializeComponent();
        }

        string GetDetectedLanguage(string text)
        {
            const string DEFAULT_DETECTED_LANG = "en";

            if (String.IsNullOrEmpty(text))
                return DEFAULT_DETECTED_LANG;

            const string DETECT_API_URI_PATTERN = "http://api.microsofttranslator.com/V2/Http.svc/Detect?appId={0}&text={1}";
            const string MATCH_PATTERN = "<[^<>]*>([^<>]*)<[^<>]*>";

            WebRequest req = WebRequest.Create(String.Format(DETECT_API_URI_PATTERN, APP_ID, text));
            WebResponse resp = req.GetResponse();

            string local = DEFAULT_DETECTED_LANG;
            using (StreamReader reader = new StreamReader(resp.GetResponseStream()))
            {
                local = reader.ReadToEnd();
                local = Regex.Match(local, MATCH_PATTERN).Groups[1].Value;
            }
            return local;
        }

        string GetSpeakUri(LanguageServiceClient client, string text)
        {
            string[] langs = client.GetLanguagesForSpeak(APP_ID);
            string lang = (cbTranslateTo.SelectedValue == null)? "en": cbTranslateTo.SelectedValue.ToString();

            if (!langs.Contains(lang))
                lang = "en";

            return client.Speak(APP_ID, tbxSource.Text, lang, "audio/wav", string.Empty);
        }

        void UpdateTranslationLanguages()
        {
            string local = GetDetectedLanguage(tbxSource.Text);
            string[] langs = Client.GetLanguagesForTranslate(APP_ID);

            var langNames = (from lang in langs.AsParallel()
                             select new { Name = Client.GetLanguageNames(APP_ID, lang, new string[] { lang })[0], Value = lang }).ToList();

            cbTranslateTo.DisplayMember = "Name";
            cbTranslateTo.ValueMember = "Value";
            cbTranslateTo.DataSource = langNames;

            if (cbTranslateTo.Items.Count > 0)
                cbTranslateTo.Text = Client.GetLanguageNames(APP_ID, local, new string[] { local }).FirstOrDefault();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string local = GetDetectedLanguage(tbxSource.Text);

            string speakUri = GetSpeakUri(Client, tbxSource.Text);
            if (speakUri.Length > 0)
            {
                axWindowsMediaPlayer1.URL = speakUri;
                axWindowsMediaPlayer1.Ctlcontrols.play();
            }

            if (cbTranslateTo.SelectedValue != null)
                tbxTarget.Text = Client.Translate(APP_ID, tbxSource.Text, local, cbTranslateTo.SelectedValue.ToString(), "text/html", "general");
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            UpdateTranslationLanguages();
        }
    }
}
```

## Link

* 使用 Bing 進行開發
* [C#] 運用微軟API 線上翻譯
* Using the SOAP API
* 微软在线翻译API试用
