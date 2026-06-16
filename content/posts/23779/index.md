---
title: "[C#]OAuth認證開發"
slug: "[CSharp]OAuth認證開發"
date: "2011-04-28 01:22:31"
description: "OAuth為開放式的認證標準，提供一個簡單、標準、且較為安全的認證方法，相容於Http標準，可供較為私密的API使用。 這邊先試想一個情景，假設今天開發一個應用程式，需要存取其它服務的資訊加以應用處理，服務可能是Facebook、Youtube、Flickr等。"
tags: [CSharp]
---

OAuth為開放式的認證標準，提供一個簡單、標準、且較為安全的認證方法，相容於Http標準，可供較為私密的API使用。

這邊先試想一個情景，假設今天開發一個應用程式，需要存取其它服務的資訊加以應用處理，服務可能是Facebook、Youtube、Flickr等。

這樣的處理動作在OAuth認證標準出來之前，可能會直接向使用者要求所需要的帳密，應用程式才能透過使用者所給予的帳密向其它服務取得資訊，而使用者為了使用應用程式，就算不得已，也必需將帳密鍵入。雖然這樣的作法可以解決應用程式開發上的需求，但問題來了，使用者並不知道應用程式會拿使用者的帳密去做什麼，是否會做些惡意的行為?因此這樣的認證處理方式並不安全，開發出來的應用程式也不能令使用者放心的使用。

在OAuth認證標準出來之後，這問題獲得了改善，應用程式不需要向使用者所取帳號密碼，取而代之的是將認證的動作轉交給服務端去處理，使用者改經由服務端去處理驗證，且使用者可以從服務端所提供的資訊中看出該應用程式所要求的控制權限有哪些，可自行決定是否允許該應用程式存取。若是使用者允許應用程式存取，應用程式可取得存取該服務用的Access Token。透過這樣的處理機制，使用者可以清楚掌握應用程式可以存取的資源，可以很明確的將資源授權給應用程式，存取的權限也可在事後透過服務端的設定去取回，因此對使用者來說是比較安全的驗證方式。

除了安全性高外，OAuth認證在處理上也十分的簡單，只需要三個步驟就可以完成這樣的認證。可先參閱一下OAuth Authentication Flow V1.0a：

![image_thumb_2.png](/images/posts/23779/image_thumb_2.png)

流程圖的左半邊試驗證的流程圖，清楚點出每個步驟的流程與流程間的流向，右半邊則帶出每個流程所需要帶入或傳回的資料。而上面所提到的三個認證步驟，即為流程圖中間所描述的，分別為Obtain Unauthorized Request Token、User Authorizes Request Token、與Exchange Request Token for Access Token：

在Obtain Unauthorized Request Token步驟中，應用程式會向需要存取的服務提供商的Request Token URL發送訊息，向服務提供商請求一個未認證的Request Token。

在User Authorizes Request Token步驟，應用程式會向需要存取的服務提供商的User Authorization URL發送訊息，訊息中帶入至第一步驟取得的未認證Request Token，引導使用者到服務提供商的使用者授權頁面，讓使用者決定是否授予所要求的權限給應用程式。

最後在Exchange Request Token for Access Token步驟，應用程式會向需要存取的服務提供商的Access Token URL發送訊息，帶入至第二步驟取得的認證Request Token，向服務商索取存取服務所要用到的Access Token。

以上就是OAuth的認證三步驟，因OAuth認證脫離不了這三個主要的步驟，故應用程式可以在極少量程式碼的變更下，移植到不同的服務繼續使用。

在OAuth開發上面，現成的開發包也有很多，可參閱Google-OAuth項目提供各種語言的OAuth庫，選取自己所需要的使用。以C#來說裡面介紹的<OAuthBase>就是不錯的選擇，開發時可參閱[DoubanOAuthBasicSample的實作，可以發現裡面主要方法有getRequestToken、authorization、與getAccessToken，這三個方法分別對應至OAuth認證的三步驟。](http://douban-oauth-sample.googlecode.com/svn-history/r12/trunk/csharp/DoubanOAuthBasicSample/DoubanOAuthBasicSample/Program.cs)

![image_thumb.png](/images/posts/23779/image_thumb.png)

再深入至程式部份，這三個方法的實作上也都大同小異，以getRequestToken方法為例：

```
public void getRequestToken()
    {
        Uri uri = requestTokenUri;
        string nonce = oAuth.GenerateNonce();
        string timeStamp = oAuth.GenerateTimeStamp();
        string normalizeUrl, normalizedRequestParameters;
```

        // 签名
        string sig = oAuth.GenerateSignature(
            uri,
            apiKey,
            apiKeySecret,
            string.Empty,
            string.Empty,
            "GET",
            timeStamp,
            nonce,
            OAuthBase.SignatureTypes.HMACSHA1,
            out normalizeUrl,
            out normalizedRequestParameters);
        sig = HttpUtility.UrlEncode(sig);

```
        //构造请求Request Token的url
        StringBuilder sb = new StringBuilder(uri.ToString());
        sb.AppendFormat("?oauth_consumer_key={0}&", apiKey);
        sb.AppendFormat("oauth_nonce={0}&", nonce);
        sb.AppendFormat("oauth_timestamp={0}&", timeStamp);
        sb.AppendFormat("oauth_signature_method={0}&", "HMAC-SHA1");
        sb.AppendFormat("oauth_version={0}&", "1.0");
        sb.AppendFormat("oauth_signature={0}", sig);
```

        Console.WriteLine("请求Request Token的url: \n" + sb.ToString());

```
        //请求Request Token
        HttpWebRequest request = (HttpWebRequest)WebRequest.Create(sb.ToString());
        HttpWebResponse response = (HttpWebResponse)request.GetResponse();
        StreamReader stream = new StreamReader(response.GetResponseStream(), System.Text.Encoding.UTF8);
        string responseBody = stream.ReadToEnd();
        stream.Close();
        response.Close();
```

        Console.WriteLine("请求Request Token的返回值: \n" + responseBody);

```
        //解析返回的Request Token和Request Token Secret
        Dictionary<string, string> responseValues = parseResponse(responseBody);
        requestToken = responseValues["oauth_token"];
        requestTokenSecret = responseValues["oauth_token_secret"];
    }
```

應該不難看出程式中的oauth_consumer_key、oauth_nonce、oauth_timestamp...等參數就是上面OAuth流程圖上所要求的資料，而有些稍微要做些處理的資料像是簽章、時間戳...等多半也都已實作在OAuthBase裡，這部份開發人員並不需要自行處理，所以實作上十分的簡單。

這邊筆者也有發現些小Tool可以輔助開發，像是OAuth Signature Validation Tool、[OAuth Test Client](http://term.ie/oauth/example/client.php)、與[OAuth Test Server。只要填入要求的資料，送出後就可以直接透過工具看到回傳的Token之類的資訊。](http://term.ie/oauth/example/)

![image_thumb_1.png](/images/posts/23779/image_thumb_1.png)

## Link

* [OAuth Series] Introduction to OAuth: An open authorization protocol in the Internet
* [OAuth Series] OAuth 的各式參數說明
* OAUTH協議簡介
* Google-OAuth項目提供各種語言的OAuth庫
* OAuthBase
* DoubanOAuthBasicSample
* OAuth Signature Validation Tool
* OAuth Test Client
* OAuth Test Server
