---
title: "[Visual Studio][C#]Visual Studio Achievements API"
date: "2013-11-06 12:00:00"
description: "[Visual Studio][C#]Visual Studio Achievements API"
tags: [CSharp]
---

筆者在[Visual Studio]Introduce Visual Studio Achievements這篇簡單的介紹了一下Visual Studio的成就系統，但對於API的使用並未著墨，這篇將針對API的部分做個介紹，若有自製些小程式需要成就系統的資料，就可以使用它所提供的API來實現。

	Visual Studio Achievements目前大概提供的API有二個，為REST API，資料則以JSON格式呈現，使用上都不會太難。像是若要取得所有的成就勳章資訊，我們可以透過下面網址取得JSON資料，從取得的JSON資料擷取出我們感興趣的部分。

	http://channel9.msdn.com/achievements/visualstudio?json=true

	以這API來說其JSON資料會像下面這般，所有的勳章資訊皆在Achievements下，可以取得像是勳章的名稱、勳章的類型、勳章的點數、及勳章圖示等。

	這邊利用JSON C# Class Generator為JSON資料產生對應的C#類別，實際示範如何撰寫個簡易的範例程式。

	程式範例如下：

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace AchievementsAPIDemo
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private string GetHTMLSourceCode(string url)
        {
            HttpWebRequest request = (WebRequest.Create(url)) as HttpWebRequest;
            HttpWebResponse response = request.GetResponse() as HttpWebResponse;
            using (StreamReader sr = new StreamReader(response.GetResponseStream()))
            {
                return sr.ReadToEnd();
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            var obj = new VSAchievements.Achievement(GetHTMLSourceCode("http://channel9.msdn.com/achievements/visualstudio?json=true"));
            foreach (var achievement in obj.Achievements)
            {
                flowLayoutPanel1.Controls.Add(new PictureBox() 
                {
                    ImageLocation = achievement.IconSmall
                });

                flowLayoutPanel1.Controls.Add(new Label()
                {
                    Text = achievement.FriendlyName
                });
            }
        }
    }
}

	程式運行後會像下面這樣，雖然範例示範的是指有勳章的圖示跟名稱，但如上面JSON所給的資料所示，所有的勳章資訊都可以透過這道API取得。

	另外一道API則是用來取得特定人員的勳章資訊，API位置如下，使用時必須將使用者的名稱帶入。

	http://channel9.msdn.com/niners/[user name]/achievements/visualstudio?json=true

	它的JSON資料跟第一道API類似，不同的是多了UserFriendName，而在勳章的資料部分，若是是已取得的勳章會多個DateEarned，用以表示勳章取得的時間。

	這邊一樣做個簡單的程式示範，程式碼如下：

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace AchievementsAPIDemo
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private string GetHTMLSourceCode(string url)
        {
            HttpWebRequest request = (WebRequest.Create(url)) as HttpWebRequest;
            HttpWebResponse response = request.GetResponse() as HttpWebResponse;
            using (StreamReader sr = new StreamReader(response.GetResponseStream()))
            {
                return sr.ReadToEnd();
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            var obj = new VSAchievements.Achievement(GetHTMLSourceCode("http://channel9.msdn.com/niners/larrynung/achievements/visualstudio?json=true"));
            
            this.Text = obj.UserFriendlyName;

            FlowLayoutPanel fp;

            foreach (var achievement in obj.Achievements)
            {
                fp = string.IsNullOrEmpty(achievement.DateEarned) ? flowLayoutPanel2 : flowLayoutPanel1;
                fp.Controls.Add(new PictureBox() 
                {
                    ImageLocation = achievement.IconSmall
                });

                fp.Controls.Add(new Label()
                {
                    Text = achievement.FriendlyName
                });
            }
        }
    }
}

	運行後可以看到我們可以透過這道API取得特定使用者得到了哪些勳章以及尚缺少的勳章。

	另外第二道API也可以外加raw=true的參數，可以只取得得到的勳章名稱與取得的時間。

	http://channel9.msdn.com/niners/[user name]/achievements/visualstudio?json=true&raw=true

## 
	Link

		Visual Studio Achievements API