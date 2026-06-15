---
title: "FlickrNet開發系列 - FlickrNet開發前準備與登入驗證機制的實現"
date: "2011-04-23 11:50:39"
description: "FlickrNet開發系列 - FlickrNet開發前準備與登入驗證機制的實現"
tags: [CSharp]
---

使用FlickrNet開發Flickr服務程式，需先至Flickr.Net API Library網站下載開發用的組件包。

![image_thumb_1.png](/images/posts/23404/image_thumb_1.png)

下載玩開發用組件包後，解壓縮會看到許多組件，從組件的檔名可以很清楚的知道所支援的平台，有一般Windows Form開發用的、行動裝置開發用的、Silverlight開發用的、與Windows Phone 7開發用的，這邊請依自己的開發需求將對應的組件加入參考。

![image_thumb_2.png](/images/posts/23404/image_thumb_2.png)

![image_thumb_3.png](/images/posts/23404/image_thumb_3.png)

加入參考後需加入FlickrNet命名空間

```
using FlickrNet;
```

在開發時，最主要要使用的類別就是Flickr，其建構函式有四個多載版本：

```
public Flickr()
public Flickr(string apiKey)
public Flickr(string apiKey, string sharedSecret)
public Flickr(string apiKey, string sharedSecret, string token)
```

可以看到建構Flickr時要帶入的不外乎就是apiKey、secret、與token。apiKey與secret可參閱[Flickr開發系列 - 應用程式與API Key的申請](http://www.dotblogs.com.tw/larrynung/archive/2011/04/09/22384.aspx)這篇取得，多半的動作我們只需要戴入apiKey與secret，當有進階的處理動作才須帶入token。

以開發的流程來看，首先我們必須將flickr物件建立起來

```
var flickr = new Flickr(apiKey, secret);
```

建立起來後透過Flickr.AuthGetFrob取得Frob

```
var frob = flickr.AuthGetFrob();
```

透過Flickr.AuthCalcUrl函式，帶入剛產生的Frob與所要跟使用者要求的權限，產出登入所需要用到的網址。這邊要求的權限是透過FlickrNet.AuthLevel列舉指定，可依自己程式的需求決定所需的權限。

```
string url = flickr.AuthCalcUrl(frob, FlickrNet.AuthLevel.Read | FlickrNet.AuthLevel.Write);
```

將產出的登入網址帶入瀏覽器，讓使用者做登入與授權動作

```
Form loginDlg = new Form();
loginDlg.Text = "Login";
loginDlg.Width = 500;
loginDlg.Height = 600;
loginDlg.StartPosition = FormStartPosition.CenterScreen;
```

```
WebBrowser browser = new WebBrowser();
browser.Navigate(url);
browser.Dock = DockStyle.Fill;
```

```
loginDlg.Controls.Add(browser);
loginDlg.ShowDialog();
```

![image_thumb.png](/images/posts/23404/image_thumb.png)

![image_thumb_4.png](/images/posts/23404/image_thumb_4.png)

登入與授權動作完成後，透過Flickr.AuthGetToken函式帶入Frob取得Auth。

```
Auth auth = flickr.AuthGetToken(frob);
```

取得的Auth內會含一開始所提到的Token資訊，要將其塞回Flickr.AuthToken，如此才能操作一些進階的動作。

```
flickr.AuthToken = auth.Token;
```

要注意的是，若開發的服務程式需要做到登入驗證後，下次開啟會自動登入驗證的話，須將上面認證的Token記錄下來，將紀錄的Token透過Flickr.AuthCheckToken將認證資訊取回，取回後再塞回Flickr.AuthToken。

```
auth = flickr.AuthCheckToken(token);
```

```
flickr.AuthToken = auth.Token;
```

## Link

* [Flickr.Net API Library](http://flickrnet.codeplex.com/)
* [[Windows Mobile .NET CF] 拍照上傳 Flickr – Day2](http://www.dotblogs.com.tw/laneser/archive/2009/07/19/9579.aspx)
* [用 Flickr.NET 來上傳照片的開發步驟](http://programer.blog.richiestyle.org/2006/12/flickrnet_05.html)
