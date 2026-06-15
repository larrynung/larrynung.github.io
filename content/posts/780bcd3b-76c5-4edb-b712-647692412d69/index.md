---
title: "FlickrNet開發系列- FlickrNet基本功能開發(一)"
date: "2013-11-06 12:00:00"
description: "FlickrNet開發系列- FlickrNet基本功能開發(一)"
tags: [CSharp]
---

距上次介紹FlickrNET已經好一段日子了，稍微抽出了點空將這部分補一補。Flickr開發不外乎就是登入、查閱登入的帳號與朋友資訊、瀏覽相簿照片...等等，這邊針對基本的功能開發做些簡介，整理於此篇。

FlickrNet登入完後，想要知道現在登入的是誰？使用者ID是多少？我們可以透過FlickrNet.Auth.User去取得資訊，FlickrNet.Auth在登入的時候我們可以取得，忘記的可參閱筆者所撰寫的FlickrNet開發系列 - FlickrNet開發前準備與登入驗證機制的實現。使用上只要透過User的屬性就可以了， 可參閱下方的程式碼片段：

```csharp
        private void ShowProfile()
        {
            FlickrNet.FoundUser user = m_Auth.User;

            MessageBox.Show(string.Format(
@"FullName: {0}
UserId: {1}
UserName: {2}", user.FullName, user.UserId, user.UserName));
        }
```

![image_thumb.png](/images/posts/780bcd3b-76c5-4edb-b712-647692412d69/image_thumb.png)

取得了登入的帳號資訊後，多半隨之而來的我們會希望能知道該帳號有哪些朋友。這邊只要透過FlickrNet.Flickr的ContactsGetList方法取得ContactCollection，並依序取出Contact，從中擷取我們感興趣的資訊就可以了，以FlickrNet來說他是將每個朋友視為聯絡人，所以是以Contact來命名，這邊可以取得像是縮圖(BuddyIconUrl)、使用者名稱(UserName)...等資訊，詳細的部分這邊不多做介紹，看一下裡面有哪些屬性就知道了。另外若是覺得Contact的資訊不夠用，我們也可以利用FlickrNet.Flickr的PeopleGetInfo方法，帶入UserID以取得對應的Person物件，裡面也會有一些資訊可以取用。

```csharp
private void ShowFriends()
{
    var form = new Form();
    var tooltip = new ToolTip();
    var container = new FlowLayoutPanel() { Dock = DockStyle.Fill};
    foreach (var contact in m_Flickr.ContactsGetList())
    {
        var person = m_Flickr.PeopleGetInfo(contact.UserId);
        var pic = new PictureBox() { ImageLocation = contact.BuddyIconUrl, SizeMode = PictureBoxSizeMode.AutoSize };
        tooltip.SetToolTip(pic, contact.UserName);
        container.Controls.Add(pic);
    }
    form.Controls.Add(container);
    form.ShowDialog();
}
```

![image_thumb_1.png](/images/posts/780bcd3b-76c5-4edb-b712-647692412d69/image_thumb_1.png)

取得了帳號資訊與朋友資訊，接著就是要瀏覽相片了，不論是自己的相片還是朋友的相片，取用的方法都是一樣的。透過FlickrNet.Flickr的PhotosetsGetList方法，帶入想要瀏覽的使用者ID，可以取得PhotosetCollection，也就是使用者相簿的集合。

```csharp
...
var photoSets = m_Flickr.PhotosetsGetList(userID);
...
```

若想要觀看特定相簿裡面的圖片內容，可以FlickrNet.Flickr的PhotosetsGetPhotos方法，帶入相簿的ID，就可以取得PhotoCollection，也就是相片的集合。

```csharp
...
var photos = m_Flickr.PhotosetsGetPhotos(photoSet.PhotosetId)
...
```

另外撰寫瀏覽這邊還需要特別注意，相片不一定全部都會在相簿裡面，所以在撰寫時還必須透過FlickrNet.Flickr的PhotosGetNotInSet方法處理不在相簿裡的相片。

```csharp
...
var photos = m_Flickr.PhotosGetNotInSet();
...
```

整個瀏覽的程式部份撰寫起來會像下面這樣：

```csharp
private void ShowPhotos(string userID)
{
    var form = new Form();
    var container = new FlowLayoutPanel() { Dock = DockStyle.Fill };

    var photoSets = m_Flickr.PhotosetsGetList(userID);

    foreach (var photoSet in photoSets)
    {
        var pic = new PictureBox() { ImageLocation = photoSet.PhotosetThumbnailUrl, BorderStyle = BorderStyle.FixedSingle, SizeMode = PictureBoxSizeMode.AutoSize };
        container.Controls.Add(pic);
    }

    var photos = m_Flickr.PhotosGetNotInSet();
    foreach (var photo in photos)
    {
        var pic = new PictureBox() { ImageLocation = photo.ThumbnailUrl, SizeMode = PictureBoxSizeMode.AutoSize };
        container.Controls.Add(pic);
    }

    form.Controls.Add(container);
    form.ShowDialog();
}
```

這邊特別Highlight一下，FlickrNet在開發上很多地方都是相簿與相片這樣的架構，因此叫用的方法可能不同，但通常都是以PhotosetCollection與PhotoCollection這兩種型態回傳，所以我們可以將重複的部份提取出來，後續的開發會比較方便，像下面這個範例就可以用來做PhotoCollection的顯示。

```csharp
private void ShowPhotoCollection(FlickrNet.PhotoCollection photos)
{
    var form = new Form();
    var container = new FlowLayoutPanel() { Dock = DockStyle.Fill };

    foreach (var photo in photos)
    {
        var pic = new PictureBox() { ImageLocation = photo.ThumbnailUrl, BorderStyle = BorderStyle.FixedSingle, SizeMode = PictureBoxSizeMode.AutoSize };
        container.Controls.Add(pic);
    }

    form.Controls.Add(container);
    form.ShowDialog();
}
```

如果我們要將Interesting的圖片顯示出來，就可以利用FlickrNet.Flickr的InterestingnessGetList方法取得對應的相片集合，帶入上面提取出來的方法去顯示。

```csharp
private void ShowInterestingPhotos()
{
    ShowPhotoCollection(m_Flickr.InterestingnessGetList());
}
```

![image_thumb_2.png](/images/posts/780bcd3b-76c5-4edb-b712-647692412d69/image_thumb_2.png)

最後這邊附上完整的程式範例：

![image_thumb_3.png](/images/posts/780bcd3b-76c5-4edb-b712-647692412d69/image_thumb_3.png)

```csharp
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace Flickr.NET_Demo
{
    public partial class Form1 : Form
    {
        #region Property
        public FlickrNet.Flickr m_Flickr { get; set; }
        public FlickrNet.Auth m_Auth { get; set; }
        #endregion

        #region Constructor
        public Form1()
        {
            InitializeComponent();
        }
        #endregion

        #region Private Method
        private void Login()
        {
            m_Flickr = new FlickrNet.Flickr(tbxAPIKey.Text, tbxSecret.Text);
            var frob = m_Flickr.AuthGetFrob();
            string url = m_Flickr.AuthCalcUrl(frob, FlickrNet.AuthLevel.Read | FlickrNet.AuthLevel.Write);

            Form loginDlg = new Form();
            loginDlg.Text = "Login";
            loginDlg.Width = 500;
            loginDlg.Height = 600;
            loginDlg.StartPosition = FormStartPosition.CenterScreen;
            WebBrowser browser = new WebBrowser();
            browser.Navigate(url);
            browser.Dock = DockStyle.Fill;
            loginDlg.Controls.Add(browser);
            loginDlg.ShowDialog();

            m_Auth = m_Flickr.AuthGetToken(frob);
            m_Flickr.AuthToken = m_Auth.Token;
        }

        private void ShowProfile()
        {
            FlickrNet.FoundUser user = m_Auth.User;

            MessageBox.Show(string.Format(
@"FullName: {0}
UserId: {1}
UserName: {2}", user.FullName, user.UserId, user.UserName));
        }

        private void ShowFriends()
        {
            var form = new Form();
            var tooltip = new ToolTip();
            var container = new FlowLayoutPanel() { Dock = DockStyle.Fill};
            foreach (var contact in m_Flickr.ContactsGetList())
            {
                var person = m_Flickr.PeopleGetInfo(contact.UserId);
                var pic = new PictureBox() { ImageLocation = contact.BuddyIconUrl, SizeMode = PictureBoxSizeMode.AutoSize };
                tooltip.SetToolTip(pic, contact.UserName);
                container.Controls.Add(pic);
            }
            form.Controls.Add(container);
            form.ShowDialog();
        }

        private void ShowPhotos(string userID)
        {
            var form = new Form();
            var container = new FlowLayoutPanel() { Dock = DockStyle.Fill };

            var photoSets = m_Flickr.PhotosetsGetList(userID);

            foreach (var photoSet in photoSets)
            {
                var pic = new PictureBox() { ImageLocation = photoSet.PhotosetThumbnailUrl, BorderStyle = BorderStyle.FixedSingle, SizeMode = PictureBoxSizeMode.AutoSize };
                container.Controls.Add(pic);
            }

            var photos = m_Flickr.PhotosGetNotInSet();
            foreach (var photo in photos)
            {
                var pic = new PictureBox() { ImageLocation = photo.ThumbnailUrl, SizeMode = PictureBoxSizeMode.AutoSize };
                container.Controls.Add(pic);
            }

            form.Controls.Add(container);
            form.ShowDialog();
        }

        private void ShowInterestingPhotos()
        {
            ShowPhotoCollection(m_Flickr.InterestingnessGetList());
        }

        private void ShowPhotoCollection(FlickrNet.PhotoCollection photos)
        {
            var form = new Form();
            var container = new FlowLayoutPanel() { Dock = DockStyle.Fill };

            foreach (var photo in photos)
            {
                var pic = new PictureBox() { ImageLocation = photo.ThumbnailUrl, BorderStyle = BorderStyle.FixedSingle, SizeMode = PictureBoxSizeMode.AutoSize };
                container.Controls.Add(pic);
            }

            form.Controls.Add(container);
            form.ShowDialog();
        }

        #endregion

        #region Event Process
        private void btnLogin_Click(object sender, EventArgs e)
        {
            Login();
        }

        private void btnProfile_Click(object sender, EventArgs e)
        {
            ShowProfile();
        }

        private void btnFriends_Click(object sender, EventArgs e)
        {
            ShowFriends();
        }

        private void btnMyPhotos_Click(object sender, EventArgs e)
        {
            ShowPhotos(m_Auth.User.UserId);
        }
        #endregion

        private void btnInteresting_Click(object sender, EventArgs e)
        {
            ShowInterestingPhotos();
        }

    }
}
```

## Download

FlickrNet.Demo.zip

## Link

* 用 Flickr.NET 來上傳照片的開發步驟
* 用 Flickr.NET 搜尋下載照片的開發步驟
* Implementing Flickr.Net
