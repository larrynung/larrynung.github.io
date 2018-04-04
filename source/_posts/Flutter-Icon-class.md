---
title: Flutter - Icon class
date: 2018-04-04 23:24:37
tags: [Flutter]
---

Flutter 的 Icon widget 可用來顯示 icon。  

<!-- More -->

<br/>


其建構子如下：  

    Icon(IconData icon, { Key key, double size, Color color, String semanticLabel, TextDirection textDirection })

<br/>


屬性如下：  

| Name | Type | Description |
|:-------------:|:-------------:|:-----:|
| color | Color | The color to use when drawing the icon. |
| icon | IconData | The icon to display. The available icons are described in Icons. |
| semanticLabel | String | Semantic label for the icon. |
| size | double | The size of the icon in logical pixels. |
| textDirection | TextDirection | The text direction to use for rendering the icon. |
| hashCode | int | The hash code for this object. |
| key | Key | Controls how one widget replaces another widget in the tree. |
| runtimeType | Type | A representation of the runtime type of the object. |

<br/>


方法如下：

| Name | Return Type | Description |
|:-------------:|:-------------:|:-----:|
| build(BuildContext context) | Widget | Describes the part of the user interface represented by this widget. |
| debugFillProperties(DiagnosticPropertiesBuilder description) | void ||
| createElement() | StatelessElement | Creates a StatelessElement to manage this widget's location in the tree. |
| debugDescribeChildren() | List<DiagnosticsNode> | Returns a list of DiagnosticsNode objects describing this node's children. |
| noSuchMethod(Invocation invocation) | dynamic | Invoked when a non-existent method or property is accessed. |
| toDiagnosticsNode({String name, DiagnosticsTreeStyle style }) | DiagnosticsNode | Returns a debug representation of the object that is used by debugging tools and by toStringDeep. |
| toString({DiagnosticLevel minLevel: DiagnosticLevel.debug }) | String | Returns a string representation of this object. |
| toStringDeep({String prefixLineOne: '', String prefixOtherLines, DiagnosticLevel minLevel: DiagnosticLevel.debug }) | String | Returns a string representation of this node and its descendants. |
| toStringShallow({String joiner: ', ', DiagnosticLevel minLevel: DiagnosticLevel.debug }) | String | Returns a one-line detailed description of the object. |
| toStringShort() | String | A short, textual description of this widget. |

<br/>


Icon 元件需在 MaterialApp 下使用，所以會要建立 MaterialApp，然後將 Icon 元件塞給 MaterialApp 的 home 屬性。  

<br/>


Icon 元件建立時需要指定要顯示的 Icon，可直接用 Icons 指定內建的 Icon。  

<br/>


其它屬性像是 color 屬性可設定 Icon 的顏色。  

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(
    new MaterialApp
    (
      home: new Icon
      (
        Icons.flag, 
        color: Colors.white,
      )
    )
  );
}
```

{% asset_img 1.png %}
 
<br/>

{% asset_img 2.png %}
 
<br/>


或是 size 屬性可設定 Icon 的大小。  

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(
    new MaterialApp
    (
      home: new Icon
      (
        Icons.flag, 
        color: Colors.white,
        size: 100.0,
      )
    )
  );
}
```

{% asset_img 3.png %}
 
<br/>

{% asset_img 4.png %}
 
<br/>


Link
----
* [Icon class - widgets library - Dart API](https://docs.flutter.io/flutter/widgets/Icon-class.html)
* [Icons class - material library - Dart API](https://docs.flutter.io/flutter/material/Icons-class.html)
