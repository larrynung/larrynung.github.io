---
title: Flutter - Container class
date: 2018-03-23 00:38:51
tags: [Flutter]
---

Flutter 的 Container widget 是能用來繪製、設定位置/尺寸的容器 widget。  

<!-- More -->

其建構子如下：  

    Container({Key key, AlignmentGeometry alignment, EdgeInsetsGeometry padding, Color color, Decoration decoration, Decoration foregroundDecoration, double width, double height, BoxConstraints constraints, EdgeInsetsGeometry margin, Matrix4 transform, Widget child })


<br/>


屬性如下： 

| Name | Type | Description |
|:-------------:|:-------------:|:-----:|
| alignment | AlignmentGeometry | Align the child within the container. |
| child | Widget | The child contained by the container. |
| constraints | BoxConstraints | Additional constraints to apply to the child. |
| decoration | Decoration | The decoration to paint behind the child. |
| foregroundDecoration | Decoration | The decoration to paint in front of the child. |
| margin | EdgeInsetsGeometry | Empty space to surround the decoration and child. |
| padding | EdgeInsetsGeometry | Empty space to inscribe inside the decoration. The child, if any, is placed inside this padding. |
| transform | Matrix4 | The transformation matrix to apply before painting the container. |
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


使用上可以設定 color 屬性變更顏色。  

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(
    new Container(
      color: Colors.blue,
    ),
  );
}
```

{% asset_img 1.png %}
 
<br/>

{% asset_img 2.png %}
 
<br/>


可以設定 width 屬性變更寬度，設定 height 屬性變更高度。  

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(
    new Center(
      child: new Container(
        color: Colors.blue,
        width: 48.0,
        height: 48.0,
      ),
    ),
  );
}
```

{% asset_img 3.png %}
 
<br/>

{% asset_img 4.png %}
 
<br/>


可以設定 child 屬性指定容器內的元件，設定 alignment 指定容器內的元件要怎麼排放，設定 transform 屬性指定容器要怎樣變形。  

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(
    new Container(
        color: Colors.blue,
        child: new Container(
          color: Colors.yellow,
          margin: const EdgeInsets.all(10.0),
          alignment: Alignment.center,
          child: new Container(
            color: Colors.white,
            width: 48.0,
            height: 48.0,
            transform: new Matrix4.rotationZ(0.1),
          )
        )
      ),
  );
}
```

{% asset_img 5.png %}
 
<br/>

{% asset_img 6.png %}
 
<br/>


Link
----
* [Container class - widgets library - Dart API](https://docs.flutter.io/flutter/widgets/Container-class.html)
