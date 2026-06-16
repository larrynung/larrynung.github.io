---
title: "How to Use Firebug Lite to Help Debug Web Pages"
slug: "how-to-use-firebug-lite-to-help-debug-web-pages"
aliases: ["/posts/7816fbce-e8e2-4b26-b557-54d9dd2c7c69/"]
date: "2013-11-06 12:00:00"
tags: [Web]
description: "有使用FireFox來開發網頁的，應該都有聽說過Firebug這個擴充套件，它能提供開發人員在開發網頁時所需要的偵錯功能。這篇所要介紹的Firebug Lite則是能讓你在各式各樣的平台上使用類似Firebug這樣的功能，不管是在IE、Chrome...都可以使用。"
---

有使用FireFox來開發網頁的，應該都有聽說過Firebug這個擴充套件，它能提供開發人員在開發網頁時所需要的偵錯功能。這篇所要介紹的Firebug Lite則是能讓你在各式各樣的平台上使用類似Firebug這樣的功能，不管是在IE、Chrome...都可以使用。

Firebug Lite有幾種使用方式，最簡單且最直接的就是透過網頁書籤下去啟用。這邊筆者以IE為例簡單的介紹一下，首先我們必須先到Firebug Lite : Firebug這邊找到給網頁書籤使用的連結位置，在上方按下滑鼠右鍵，在彈出的滑鼠右鍵快顯選單中，選取加到我的最愛的滑鼠右鍵選單選項。

![image_thumb_1.png](/images/posts/7816fbce-e8e2-4b26-b557-54d9dd2c7c69/image_thumb_1.png)

將之加入到我的最愛。

![image_thumb_2.png](/images/posts/7816fbce-e8e2-4b26-b557-54d9dd2c7c69/image_thumb_2.png)

加完到我的最愛後，當有網頁需要偵錯，我們可以透過我的最愛列表點選Firebug lite的網頁書籤。

![image_thumb_3.png](/images/posts/7816fbce-e8e2-4b26-b557-54d9dd2c7c69/image_thumb_3.png)

點選後我們可以看到網頁下方會出現類似Firebug的開發人員工具。

![image_thumb_4.png](/images/posts/7816fbce-e8e2-4b26-b557-54d9dd2c7c69/image_thumb_4.png)

另外一種做法是直接將Firebug lite嵌到網頁中，可以直接連接網路上的Firebug lite javascript，也可以將Firebug lite的Javascript抓下來本地連結。使用上都是類似的，只要在Header element中將Javascript加入，並在html element設定debug attribute為true就可以了。

```xml
<script type="text/javascript" src="\images\posts\7816fbce-e8e2-4b26-b557-54d9dd2c7c69\firebug-lite.js"></script>
```

使用起來會像下面這樣：

```xml
<html debug="true">
    <header>
        <script type="text/javascript" src="\images\posts\7816fbce-e8e2-4b26-b557-54d9dd2c7c69\firebug-lite.js"/>
    </header>
    <body>
        <h1>Test firebug lite page</h1>
    </body>
</html>
```

運行後我們可以看到跟使用書籤啟動一樣的效果：

![image_thumb.png](/images/posts/7816fbce-e8e2-4b26-b557-54d9dd2c7c69/image_thumb.png)

另外在這邊Firebug lite也提供了一些細項可供設定：

<table border="1" cellpadding="2" cellspacing="0" width="400"><tbody>
<tr>
<td valign="top" width="200">Option</td>
<td valign="top" width="200">Default</td>
</tr>
<tr>
<td valign="top" width="200"><code>saveCookies</code> </td>
<td valign="top" width="200">false</td>
</tr>
<tr>
<td valign="top" width="200"><code>startOpened</code> </td>
<td valign="top" width="200">false</td>
</tr>
<tr>
<td valign="top" width="200"><code>startInNewWindow</code> </td>
<td valign="top" width="200">false</td>
</tr>
<tr>
<td valign="top" width="200"><code>showIconWhenHidden</code> </td>
<td valign="top" width="200">true </td>
</tr>
<tr>
<td valign="top" width="200"><code>overrideConsole</code> </td>
<td valign="top" width="200">true </td>
</tr>
<tr>
<td valign="top" width="200"><code>ignoreFirebugElements</code> </td>
<td valign="top" width="200">true </td>
</tr>
<tr>
<td valign="top" width="200"><code>disableXHRListener</code> </td>
<td valign="top" width="200">false</td>
</tr>
<tr>
<td valign="top" width="200"><code>disableWhenFirebugActive</code> </td>
<td valign="top" width="200">true </td>
</tr>
<tr>
<td valign="top" width="200"><code>enableTrace</code> </td>
<td valign="top" width="200">false</td>
</tr>
<tr>
<td valign="top" width="200"><code>enablePersistent</code> </td>
<td valign="top" width="200">false</td>
</tr>
</tbody></table>

像是要在啟動時將Firebug lite以新視窗開啟，而不要置於網頁最下方的話，我們就可以使用類似下面這樣的撰寫方式：

```xml
<script type="text/javascript" src="\images\posts\7816fbce-e8e2-4b26-b557-54d9dd2c7c69\firebug-lite.js">
{
    startInNewWindow : true
}
</script>
```

## Link

* Firebug Lite : Firebug
* 網頁開發人員的秘密武器 – Firebug Lite
