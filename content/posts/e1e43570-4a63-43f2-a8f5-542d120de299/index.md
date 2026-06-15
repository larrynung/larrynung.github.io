---
title: "[HTML]HTML5 New Feature - progress tag"
date: "2013-11-06 12:00:00"
description: "[HTML]HTML5 New Feature - progress tag"
---

HTML新增了progress標籤，可在網頁中加入進度列，用以表示目前處理的進度，目前該標籤僅支援Firefox, Opera, 與 Chrome

![compatible_firefox.gif](/images/posts/e1e43570-4a63-43f2-a8f5-542d120de299/compatible_firefox.gif) ![compatible_opera.gif](/images/posts/e1e43570-4a63-43f2-a8f5-542d120de299/compatible_opera.gif) ![compatible_chrome.gif](/images/posts/e1e43570-4a63-43f2-a8f5-542d120de299/compatible_chrome.gif)

該標籤主要有兩個可設定的attribute，一個是max，用以指定進度列最大的值，一個是value，用以指定進度列當前的進度值。

<table border="1" cellpadding="2" cellspacing="0" width="440"><tbody> <tr> <td valign="top" width="113">Attribute</td> <td valign="top" width="325">Description</td> </tr> <tr> <td valign="top" width="117">max</td> <td valign="top" width="325">進度列最大值</td> </tr> <tr> <td valign="top" width="120">value</td> <td valign="top" width="325">進度列的值</td> </tr> </tbody></table>

有興趣的可用w3school提供的Editor去體驗看看

![image_thumb.png](/images/posts/e1e43570-4a63-43f2-a8f5-542d120de299/image_thumb.png)

若有需要也可以透過JavaScript去跟progress互動，像是下面這個例子：

```xml
<!DOCTYPE html>
<html>
<body>

Downloading progress:
<progress value="0" max="100"></progress>
<span id="show">0%</span>
</br>
<input type="button" value="-" onclick="subProgress();">
<input type="button" value="+" onclick="addProgress();">
<input type="button" value="Start" onclick="Btn_Click();">

<script>
var progress = document.getElementsByTagName("progress")[0];
var percentage = document.getElementById("show");
var timerID;

function subProgress()
{
    progress.value -= 10;
    percentage.innerHTML = progress.value + "%";
}

function addProgress()
{
    progress.value += 10;
    percentage.innerHTML = progress.value + "%";
}

function Btn_Click()
{
    progress.value = 0;
    timerID = setInterval(Interval_handker, 100);
}

function Interval_handker()
{
    if(progress.value >= progress.max)
    {
        clearInterval(timerID);
        timerID = 0;
        return;
    }
    progress.value += 10;
    percentage.innerHTML = progress.value + "%";
}
</script>

</body>
</html>
```

運行後可透過按鈕去控制進度列當前的進度值

![image_thumb_2.png](/images/posts/e1e43570-4a63-43f2-a8f5-542d120de299/image_thumb_2.png)

## Link

* HTML5 <progress> Tag
* HTML 5 <progress> 标签
* Progress Bar in HTML 5
* HTML DOM 快速導覽 - 元素物件 <progress> (HTMLProgressElement)
