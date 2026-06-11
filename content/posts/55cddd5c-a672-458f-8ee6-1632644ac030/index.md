---
title: "How to use MetaWeblogSharp"
date: "2013-11-06 12:00:00"
description: "How to use MetaWeblogSharp"
tags: [CSharp]
---

簡單紀錄一下怎樣使用MetaWeblogSharp去操控支援MetaWeblog api的Blog。

首先使用NuGet將MetaWeblogSharp組件參考加入。

加入命名空間MetaWeblogSharp。

using MetaWeblogSharp;

就可以開始進行程式的撰寫。

因為對Blog的操作需要有權限，所以這邊先以Login來說。Login的動作我們需要先取得BlogConnectionInfo的物件，在第一次登入時BlogConnectionInfo物件實體是要自己建立的，建立時我們需要帶入MetaWeblog API的位置以及Blog的帳號密碼。建構子這邊雖然也可以帶入BlogID與BlogURL，但是像ID這樣的東西不太可能是開發時會知道的東西，筆者也不太了解開發者為何這樣設計，這邊筆者是直接將空字串帶入。建立完BlogConnectionInfo物件實體後，我們需要將剛建立好的BlogConnectionInfo物件實體帶入Client的建構子，以建立Client的物件實體，後續我們的操作都是針對這個Client物件實體。特別注意到這邊，建立Client的物件實體並不會實際的透過網路去做登入的動作，所以無法判別帳密是否是正確無誤，故這邊筆者在登入時會嘗試讀取Blog資訊，如果帳密錯誤這邊就會觸發例外並告知錯誤原因，若是帳密無誤，這邊可以取得Blog資訊，筆者藉由將這邊取得的資訊回填，補齊本來沒帶入的BlogID與BlogURL。

public static Client Login(string metaWeblogAPIUrl, string id, string password)
{
var connectionInfo = new BlogConnectionInfo(
string.Empty,
metaWeblogAPIUrl,
string.Empty,
id,
password
);

return Login(connectionInfo);
}

private static Client Login(BlogConnectionInfo connectionInfo)
{
var client = new Client(connectionInfo);

var blog = client.GetUsersBlogs().FirstOrDefault();

connectionInfo.Blog
connectionInfo.BlogURL = blog.URL;

return client;
}

登入成功後，若想讓程式下次可以直接登入，可以叫用BlogConnectionInfo的Save成員方法，將連線資訊儲存在本地。

client.BlogConnectionInfo.Save("connection.xml");

下次程式開啟時可透過BlogConnectionInfo的Load靜態方法，將儲存的連線資訊載回去做登入。

var client = Login(BlogConnectionInfo.Load("connection.xml"));

不過這邊筆者要提醒一下，MetaWeblogSharp的Save功能儲存的是未加密的資訊，所以不建議直接採用，比較好應該是自行處理掉這塊。

登入完成實際取得貼文看看，Client的GetRecentPosts成員方法可以讓我們取得最近n筆貼文。若是要取得所有的貼文，我們可以帶個極大的數值給它(MetaWeblog API在這塊感覺有點設計上的缺陷)。

var allPosts = client.GetRecentPosts(int.MaxValue);
allPosts.ForEach((post) =>
{
Console.WriteLine(post.Title);
Console.WriteLine(post.Link);
Console.WriteLine(new string('=', 78));
});

PostInfo內Title、Link、Description這些會是我們比較關注的，因為它是文章的標題、相對路徑、以及內文。

另外我們比較關注的可能就是文章的位置。不過因為MetaWeblogSharp在這塊的實作上有些問題，所以取得的PostInfo其PremaLink會永遠是Null。當然如果要從PostInfo.Link以及部落格位置去兜出PremaLink也是可以，但總是不夠方便。

好在它的RawData裡面確實是有東西的，所以這邊我們可以改從RawData那邊去撈出PremaLink。

像是下面這樣撰寫：

var permalink = ((post.RawData as MetaWeblogSharp.XmlRPC.Struct)["permalink"] as MetaWeblogSharp.XmlRPC.StringValue).String;

Permalink就可以確實的撈出。

除此之外文章的Category可能也是我們關注的重點，這邊一樣也是得從RawData內去撈。像是下面這樣：

var categories = ((post.RawData as MetaWeblogSharp.XmlRPC.Struct)["categories"] as MetaWeblogSharp.XmlRPC.Array).OfType().Select(item => item.String).ToArray();

其它比較簡單的操作應該看一下就會了。像是用Client.GetPost取得特定的文章。

var post = client.GetPost(postID);

用Client.DeletePost刪除特定的文章

client.DeletePost(post.PostID);

用Client.EditPost編輯特定的文章

client.EditPost(post.PostID, "NewTitle", "NewDescription", null, true);

用Client.NewMediaObject上傳檔案

var bytes = File.ReadAllBytes("test1.png");
var mo = client.NewMediaObject("foo.png", "image/png", bytes);

以及用Client.NewPost產生貼文

var categories1 = new List { "A", "B", "C" };
var new_post_ body, categories1, true);

## Link


MetaWeblogSharp - Home