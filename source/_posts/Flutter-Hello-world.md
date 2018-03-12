---
title: Flutter - Hello world
date: 2018-03-13 00:03:15
tags: [Flutter]
---

Flutter 專案建立後可以先撰寫個簡單的 Hello world 程式，lib/main.dart 為 Flutter 程式的主要進入點，將之開啟後撰寫如下程式。  

<!-- More -->

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(
    new Center(
      child: new Text(
        'Hello, world!',
        textDirection: TextDirection.ltr,
      ),
    ),
  );
}
```

<br/>


可以看到 Flutter 程式撰寫上主要有幾個要注意的部分，首先需引用 flutter/material.dart 套件，再來就是要在 main 這個處函式內調用 runApp 方法，runApp 方法調用時要帶入構成畫面的 widget。  

<br/>


像是這邊就帶入一個 Center 的 Widget，Center 的 Widget 內又放置了一個 Text Widget，所以 Text Widget 設定的字串會在程式的正中央顯示。  

{% asset_img 1.png %}
 
<br/>


{% asset_img 2.png %}
 
<br/>
