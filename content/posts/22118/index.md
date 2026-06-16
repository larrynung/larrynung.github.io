---
title: "土豆視頻開發系列-依影集分類查詢"
date: "2011-03-27 10:53:19"
description: "要從土豆往上截取影集資料，我們可先參閱頻道劇集查詢，該API的URL位置會像下面這樣： http://api.tudou.com/v3/gw?method=album.channel.get&appKey=&format=&channel=&pageNo=&pageSize=…"
tags: [CSharp]
---

要從土豆往上截取影集資料，我們可先參閱頻道劇集查詢，該API的URL位置會像下面這樣：

http://api.tudou.com/v3/gw?method=album.channel.get&appKey=&format=&channel=&pageNo=&pageSize=

除了appKey與format這兩個API所通用的參數外，另外又含有channel、pagegNo、pageSize這三個參數，channel部份可帶入的有m、t、z三個，分別代表的是電影、電視、與綜藝，而pageNo與pageSize用以指定想要截取的頁數與資料量。

使用上就像是下面這樣：

http://api.tudou.com/v3/gw?method=album.channel.get&appKey=myKey&format=xml&channel=z&pageNo=1&pageSize=10

API會依照指定的指定的格釋回傳所查詢的資料，因這邊示範的是XML所以會以XML的形式呈現。

![image_thumb_5.png](/images/posts/22118/image_thumb_5.png)

其資料所對應的欄位可查閱劇集字段定義。

![image_thumb_1.png](/images/posts/22118/image_thumb_1.png)

範例程式如下：

```
private void SetTudouAlbumContent()
{
    UnBindingEvent();
    var channels=new string[]{"m","t","z"};
    var url = string.Format(ALBUM_URL_PATTERN, textBox1.Text, channels[cbxChannel.SelectedIndex], (cbxPage.SelectedIndex < 0) ? 1 : cbxPage.SelectedIndex + 1, 10);
    string xml = GetHTMLSourceCode(url);
    XmlDocument xmlDom = new XmlDocument();
    xmlDom.LoadXml (xml);

    XmlNodeList nodes = xmlDom.SelectNodes(@"/result/results/AlbumInfo");
    foreach (XmlNode node in nodes)
    {
        // Name = node.ChildNodes[1].InnerText
        // picUrl = node.ChildNodes[2].InnerText
        // ...
        ...
    }
    ...
}
```

透過上面的程式已經可以取得影集的資料，若要進一步取得影集中的節目資訊，需參閱劇集節目查詢，該API的URL位置會像下面這樣：

http://api.tudou.com/v3/gw?method=album.item.get&appKey=&format=&albumId=&pageNo=&pageSize=

該道API的參數跟上面大同小異，這邊不作重複的敘述，不同的是albumId這個參數，我們可將上面取得的albumid帶入，像是下面這樣：

http://api.tudou.com/v3/gw?method=album.item.get&appKey=myKey&format=xml&albumId=50815&pageNo=1&pageSize=10

叫用後會取得如下XML資料：

![image_thumb_6.png](/images/posts/22118/image_thumb_6.png)

其資料所對應的欄位可查閱視頻字段定義。

![image_thumb_3.png](/images/posts/22118/image_thumb_3.png)

這邊做了ㄧ個範例程式，將上面的API做了較為完整的示範，可查閱電視、電影、綜藝這三種不同類型的影片，可指定查閱的頁數，以及透過網頁做簡易的播放。

![image_thumb_7.png](/images/posts/22118/image_thumb_7.png)

![image_thumb_8.png](/images/posts/22118/image_thumb_8.png)

![image_thumb_9.png](/images/posts/22118/image_thumb_9.png)

## Download

TudouDemo.rar

## Link

* 頻道劇集查詢
* 劇集字段定義
* 劇集節目查詢
* 視頻字段定義
