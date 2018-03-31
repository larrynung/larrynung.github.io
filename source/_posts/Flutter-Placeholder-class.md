---
title: Flutter - Placeholder class
date: 2018-03-31 22:20:40
tags: [Flutter]
---

Flutter 的 Placeholder widget 主要用來標示後續會被其它 Widget 取代的地方。  

<!-- More -->

<br/>


其建構子如下：  

    Placeholder({Key key, Color color: const Color(0xFF455A64), double strokeWidth: 2.0, double fallbackWidth: 400.0, double fallbackHeight: 400.0 })

<br/>


屬性如下：  

| Name | Type | Description |
|:-------------:|:-------------:|:-----:|
| color | Color | The color to draw the placeholder box. |
| fallbackHeight | double | The height to use when the placeholder is in a situation with an unbounded height. |
| fallbackWidth | double | The width to use when the placeholder is in a situation with an unbounded width. |
| strokeWidth | double | The width of the lines in the placeholder box. |
| hashCode | int | The hash code for this object. |
| key | Key | Controls how one widget replaces another widget in the tree. |
| runtimeType | Type | A representation of the runtime type of the object. |

<br/>


方法如下：  

| Name | Return Type | Description |
|:-------------:|:-------------:|:-----:|
| build(BuildContext context) | Widget | Describes the part of the user interface represented by this widget. |
| createElement() | StatelessElement | Creates a StatelessElement to manage this widget's location in the tree. |
| debugDescribeChildren() | List<DiagnosticsNode> | Returns a list of DiagnosticsNode objects describing this node's children. |
| debugFillProperties(DiagnosticPropertiesBuilder description) | void | Add additional properties associated with the node. 
| noSuchMethod(Invocation invocation) | dynamic | Invoked when a non-existent method or property is accessed. |
| toDiagnosticsNode({String name, DiagnosticsTreeStyle style }) | DiagnosticsNode | Returns a debug representation of the object that is used by debugging tools and by toStringDeep. |
| toString({DiagnosticLevel minLevel: DiagnosticLevel.debug }) | String | Returns a string representation of this object. |
| toStringDeep({String prefixLineOne: '', String prefixOtherLines, DiagnosticLevel minLevel: DiagnosticLevel.debug }) | String | Returns a string representation of this node and its descendants. |
| toStringShallow({String joiner: ', ', DiagnosticLevel minLevel: DiagnosticLevel.debug }) | String | Returns a one-line detailed description of the object. |
| toStringShort() | String | A short, textual description of this widget. |

<br/>


該 Widget 可以不帶參數直接使用。  

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(new Placeholder());
}
```

{% asset_img 1.png %}
 
<br/>

{% asset_img 2.png %}
 
<br/>


若有需要也可以透過 color 屬性變更顏色。  

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(new Placeholder(
    color: Colors.green,
  ));
}
```

{% asset_img 3.png %}
 
<br/>

{% asset_img 4.png %}
 
<br/>


或是透過 strakeWidth 變更線條的寬度。  

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(new Placeholder(
    strokeWidth: 10.0,
  ));
}
```

{% asset_img 5.png %}
 
<br/>

{% asset_img 6.png %}
 
<br/>


Link
----
* [Placeholder class - widgets library - Dart API](https://docs.flutter.io/flutter/widgets/Placeholder-class.html)
