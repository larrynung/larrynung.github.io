---
title: "Share Your Terminal With No Fuss - ascii.io"
date: "2013-11-06 12:00:00"
description: "ASCII.IO是一個滿有趣的服務，我們只要在Terminal下呼叫一簡單的命令，就可以錄製並上傳我們在Terminal下的操作，而且錄製的動作可以直接被複製，跟一般的影片錄製有所不同，在做Terminal下的教學特別好用 。 使用上可參閱官方提供的Getting started這份文件。"
tags: [Mac, HomeBrew]
---

![screenshot(17)_thumb.png](/images/posts/2c3d60ed-91e1-478d-b403-e19fe058b498/screenshot%2817%29_thumb.png)

ASCII.IO是一個滿有趣的服務，我們只要在Terminal下呼叫一簡單的命令，就可以錄製並上傳我們在Terminal下的操作，而且錄製的動作可以直接被複製，跟一般的影片錄製有所不同，在做Terminal下的教學特別好用 。

使用上可參閱官方提供的Getting started這份文件。

![screenshot22_thumb.png](/images/posts/2c3d60ed-91e1-478d-b403-e19fe058b498/screenshot22_thumb.png)

簡單的說我們需先做個安裝的動作，只需要在Terminal下呼叫命令"`curl -sL get.ascii.io | bash`"將需要的套件安裝起來，若有安裝Homebrew的，可以改呼叫命令"`brew install https://raw.github.com/gist/3875486/asciiio.rb --HEAD`"，使用Homebrew套件管理程式下去安裝。

![screenshot(35)_thumb.png](/images/posts/2c3d60ed-91e1-478d-b403-e19fe058b498/screenshot%2835%29_thumb.png)

安裝好後若需要錄製，我們可以呼叫命令asciiio。

![screenshot(23)_thumb.png](/images/posts/2c3d60ed-91e1-478d-b403-e19fe058b498/screenshot%2823%29_thumb.png)

這時Terminal畫面會變成像下面這樣，上方會明確告知現在進入了錄製狀態，以及按下Ctrl+D或是輸入exit可離開錄製狀態。

![screenshot(24)_thumb.png](/images/posts/2c3d60ed-91e1-478d-b403-e19fe058b498/screenshot%2824%29_thumb.png)

在錄製狀態下我們可以進行我們想要被錄製的操作...

![screenshot25_thumb.png](/images/posts/2c3d60ed-91e1-478d-b403-e19fe058b498/screenshot25_thumb.png)

當要錄製的操作進行到一個段落，我們按下Ctrl+D或是輸入exit結束錄製，我們會看到像下面這樣的畫面，此時我們的錄製已經完成，按下y開始將錄製的影片上傳，上傳完畢asciiio會告知我們影片所在的位置。

![screenshot26_thumb.png](/images/posts/2c3d60ed-91e1-478d-b403-e19fe058b498/screenshot26_thumb.png)

我們可以將這邊顯示的影片的位置複製後貼在瀏覽器，實際看看錄製出來的效果。

![screenshot33_thumb.png](/images/posts/2c3d60ed-91e1-478d-b403-e19fe058b498/screenshot33_thumb.png)

注意到這邊，雖然錄製的動作完成，影片也上傳有了對應的影片位置。但此時這影片並未經過認證，沒有跟個人帳號Binding在一起，雖然可以在網站上瀏覽，但在個人檔案那邊我們會無法看到影片，也沒有辦法針對該影片下去編輯與刪除。

所以這邊我們可以再呼叫命令"asciiio auth"，將影片與個人帳號Binding在一起。

![screenshot(28)_thumb.png](/images/posts/2c3d60ed-91e1-478d-b403-e19fe058b498/screenshot%2828%29_thumb.png)

認證動作做完後可以看到個人檔案這邊已經可以瀏覽到錄製的影片。

![screenshot29_thumb.png](/images/posts/2c3d60ed-91e1-478d-b403-e19fe058b498/screenshot29_thumb.png)

影片這邊也已具備了編輯以及刪除的能力了。

![screenshot(30)_thumb.png](/images/posts/2c3d60ed-91e1-478d-b403-e19fe058b498/screenshot%2830%29_thumb.png)

## Link

* Share Your Terminal With No Fuss - ascii.io
