---
title: "FlickrNet Development Series - Basic Feature Development (Part 2)"
slug: "flickrnet-development-series-basic-feature-development-part-2"
aliases: ["/posts/fa4d2166-577d-4ec8-90be-987aa4106b10/"]
date: "2013-11-06 12:00:00"
description: "前面介紹了FlickrNet基本的開發，細心的可能有注意到我並沒有提到怎樣去顯示圖片。雖然前面的文章例子中有圖片，但用的是縮圖的部份，解析度不適合拿來做播放顯示。這邊針對顯示圖片那邊在做些進一步的補充。 在Flickr中除了我們前面用到的縮圖外，還有各式各樣尺寸的圖片可供我們使用。"
tags: [CSharp]
---

前面介紹了FlickrNet基本的開發，細心的可能有注意到我並沒有提到怎樣去顯示圖片。雖然前面的文章例子中有圖片，但用的是縮圖的部份，解析度不適合拿來做播放顯示。這邊針對顯示圖片那邊在做些進一步的補充。

在Flickr中除了我們前面用到的縮圖外，還有各式各樣尺寸的圖片可供我們使用。有大圖、中圖、原圖、小圖、方圖...等。

![image_thumb_1.png](/images/posts/fa4d2166-577d-4ec8-90be-987aa4106b10/image_thumb_1.png)

因此我們只要找到適合尺寸的圖片去做圖片的播放顯示就可以了。但是真的有那麼簡單嗎?!當然是沒有，在Flick中圖片的位置有可能是空的，就連原圖位置也可能是空的，所以我們不能期望裡面所有大小的圖片都可以拿來用，必須繞點路去判斷，以找到最適合的圖片。在程式撰寫上可以透過FlickrNet.PhotosGetSizes方法，帶入photo的ID去找到支援的圖片大小有哪些，就像下面這樣：

```csharp
...
var sizes = m_Flickr.PhotosGetSizes(photo.PhotoId);
var hasLargePhoto = (from item in sizes
                      where string.Equals(item.Label, "Large", StringComparison.CurrentCultureIgnoreCase)
                      select item).Count() > 0;
...
 var photoBox = new PictureBox() { ImageLocation = hasLargePhoto ? photo.LargeUrl : photo.MediumUrl, Dock = DockStyle.Fill };
...
```

這邊也許有人會好奇為什麼筆者不直接用字串是否為空的下去判斷，這筆者也搞不清楚了，印象中筆者曾試圖這樣處理，但最後發生了些問題才轉回這樣的處理方式。可能是某些狀況下會網址不為空，但卻不能使用，有興趣的可以自己下去嘗試。最後筆者拿上一篇的範例下去修改，讓ShowPhotoCollection除了可以顯示出帶進去的圖片，點選後還能進一步顯示較大的圖片。

```csharp
private void ShowPhotoCollection(FlickrNet.PhotoCollection photos)
{
    var form = new Form();
    var container = new FlowLayoutPanel() { Dock = DockStyle.Fill };

    for (int i = 0; i < photos.Count; ++i)
    {
        var photo = photos[i];
        var pic = new PictureBox() { ImageLocation = photo.ThumbnailUrl, BorderStyle = BorderStyle.FixedSingle, SizeMode = PictureBoxSizeMode.AutoSize, Tag = photo };
        container.Controls.Add(pic);

        pic.Click += (sender, e) =>
        {
            photo = (sender as PictureBox).Tag as FlickrNet.Photo;
            var sizes = m_Flickr.PhotosGetSizes(photo.PhotoId);
            var hasLargePhoto = (from item in sizes
                                 where string.Equals(item.Label, "Large", StringComparison.CurrentCultureIgnoreCase)
                                 select item).Count() > 0;

            var dialog = new Form();
            var photoBox = new PictureBox() { ImageLocation = hasLargePhoto ? photo.LargeUrl : photo.MediumUrl, Dock = DockStyle.Fill };
            dialog.Controls.Add(photoBox);
            dialog.ShowDialog();
        };
    }

    form.Controls.Add(container);
    form.ShowDialog();
}
```

運行起來會像下面這樣，看到有興趣的圖片點選一下，就會帶出新視窗顯示大尺寸的圖片。

![image_thumb.png](/images/posts/fa4d2166-577d-4ec8-90be-987aa4106b10/image_thumb.png)
