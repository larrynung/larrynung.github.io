---
title: Flutter - Text widget
date: 2018-03-17 00:44:41
tags: [Flutter]
---

Flutter 的 Text widget 可以用來做簡易的文字顯示。  

<!-- More -->

<br/>


其建構子如下：  

    Text(String data, { Key key, TextStyle style, TextAlign textAlign, TextDirection textDirection, bool softWrap, TextOverflow overflow, double textScaleFactor, int maxLines })

<br/>


屬性如下：  

| Name | Type | Description |
|:-------------:|:-------------:|:-----:|
| data | String | The text to display.|
| maxLines | int | An optional maximum number of lines for the text to span, wrapping if necessary. If the text exceeds the given number of lines, it will be truncated according to overflow.  |
| overflow | TextOverflow | How visual overflow should be handled. |
| softWrap | bool | Whether the text should break at soft line breaks. |
| style | TextStyle | If non-null, the style to use for this text. |
| textAlign | TextAlign | How the text should be aligned horizontally. |
| textDirection | TextDirection | The directionality of the text. |
| textScaleFactor | double | The number of font pixels for each logical pixel. |
| hashCode | int | The hash code for this object. |
| key | Key | Controls how one widget replaces another widget in the tree. |
| runtimeType | Type | A representation of the runtime type of the object. |

<br/>


方法如下：

| Name | Return Type | Description |
|:-------------:|:-------------:|:-----:|
| build(BuildContext context) | Widget | Describes the part of the user interface represented by this widget. |
| debugFillProperties(DiagnosticPropertiesBuilder description) | void ||
| createElement() | StatelessElement | Creates a StatelessElement to manage this widget's location in the tree.  |
| debugDescribeChildren() | List<DiagnosticsNode> | Returns a list of DiagnosticsNode objects describing this node's children. |
| noSuchMethod(Invocation invocation) | dynamic | Invoked when a non-existent method or property is accessed. |
| toDiagnosticsNode({String name, DiagnosticsTreeStyle style }) | DiagnosticsNode | Returns a debug representation of the object that is used by debugging tools and by toStringDeep.  |
| toString({DiagnosticLevel minLevel: DiagnosticLevel.debug }) | String | Returns a string representation of this object. |
| toStringDeep({String prefixLineOne: '', String prefixOtherLines, DiagnosticLevel minLevel: DiagnosticLevel.debug }) | String | Returns a string representation of this node and its descendants. |
| toStringShallow({String joiner: ', ', DiagnosticLevel minLevel: DiagnosticLevel.debug }) | String | Returns a one-line detailed description of the object. |
| toStringShort() | String | A short, textual description of this widget. |

<br/>


使用時如果沒什麼特殊的需求，那麼只要在建置 Text widget 時透過建構子帶入要顯示的文字即可。  

<br/>


如果要控制文字的排列，可以設定 textAlign，若要設定文字顯示的比例，可以設定 textScaleFactor。  

```dart
import 'package:flutter/material.dart';
void main() {
  runApp(
    new Text(
      'Hello, world!',
      textDirection: TextDirection.ltr,
      textAlign: TextAlign.center,
      textScaleFactor: 2.0,
    )
  );
}
```

{% asset_img 1.png %}
 
<br/>

{% asset_img 2.png %}
 
<br/>


如果要對文字的樣式做調整，可以設定 style，像是設定字型的話可以設定 Style 的 fontFamily。  

```dart
import 'package:flutter/material.dart';
void main() {
  runApp(
    new Text(
      'Hello, world!',
      textDirection: TextDirection.ltr,
      textAlign: TextAlign.center,
      style: new TextStyle(fontFamily: 'Raleway')
    )
  );
}
```

{% asset_img 3.png %}
 
<br/>

{% asset_img 4.png %}
 
<br/>


要設定文字為粗體的話，可以設定 Style 的 fontWeight 為 FontWeight.bold。

```dart
import 'package:flutter/material.dart';
void main() {
  runApp(
    new Text(
      'Hello, world!',
      textDirection: TextDirection.ltr,
      textAlign: TextAlign.center,
      style: new TextStyle(fontWeight: FontWeight.bold)
    )
  );
}
```

{% asset_img 5.png %}
 
<br/>

{% asset_img 6.png %}
 
<br/>


要設定文字顏色的話，可設定 Style 的 color。  

```dart
import 'package:flutter/material.dart';
void main() {
  runApp(
    new Text(
      'Hello, world!',
      textDirection: TextDirection.ltr,
      textAlign: TextAlign.center,
      style: new TextStyle(color: Colors.yellow)
    )
  );
}
```

{% asset_img 7.png %}
 
<br/>


{% asset_img 8.png %}
 
<br/>


要設定文字底線的話，可以設定 Style 的 decoration，並用 decorationColor 設定其顏色，用 decorationStyle 設定樣式。  

```dart
import 'package:flutter/material.dart';
void main() {
  runApp(
    new Text(
      'Hello, world!',
      textDirection: TextDirection.ltr,
      textAlign: TextAlign.center,
      style: new TextStyle(
        decoration: TextDecoration.underline,
        decorationColor: Colors.red,
        decorationStyle: TextDecorationStyle.wavy)
    )
  );
}
```

{% asset_img 9.png %}
 
<br/>


{% asset_img 10.png %}
 
<br/>


Link
----
* [Text class - widgets library - Dart API](https://docs.flutter.io/flutter/widgets/Text-class.html)
