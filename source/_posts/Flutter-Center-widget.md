---
title: Flutter - Center widget
date: 2018-03-19 23:38:07
tags: [Flutter]
---

Flutter 的 Center widget 可用來做置中的呈現。  

<!-- More -->

其建構子如下：  

    Center({Key key, double widthFactor, double heightFactor, Widget child })

<br/>


屬性如下： 

| Name | Type | Description |
|:-------------:|:-------------:|:-----:|
| alignment | AlignmentGeometry | How to align the child. |
| child | Widget | The widget below this widget in the tree. |
| hashCode | int | The hash code for this object. |
| heightFactor | double | If non-null, sets its height to the child's height multiplied by this factor. |
| key | Key | Controls how one widget replaces another widget in the tree. |
| runtimeType | Type | A representation of the runtime type of the object. |
| widthFactor | doube | If non-null, sets its width to the child's width multiplied by this factor. |

<br/>


方法如下：  

| Name | Return Type | Description |
|:-------------:|:-------------:|:-----:|
| createElement() | SingleChildRenderObjectElement | RenderObjectWidgets always inflate to a RenderObjectElement subclass. |
| createRenderObject(BuildContext context) | RenderPositionedBox | Creates an instance of the RenderObject class that this RenderObjectWidget represents, using the configuration described by this RenderObjectWidget. |
| debugDescribeChildren() | List<DiagnosticsNode> | Returns a list of DiagnosticsNode objects describing this node's children. |
| debugFillProperties(DiagnosticPropertiesBuilder description)  | void | |
| didUnmountRenderObject(RenderObject renderObject) | void | A render object previously associated with this widget has been removed from the tree. The given RenderObject will be of the same type as returned by this object's createRenderObject. |
| noSuchMethod(Invocation invocation) | dynamic | Invoked when a non-existent method or property is accessed. |
| toDiagnosticsNode({String name, DiagnosticsTreeStyle style }) | DiagnosticsNode | Returns a debug representation of the object that is used by debugging tools and by toStringDeep. |
| toString({DiagnosticLevel minLevel: DiagnosticLevel.debug }) | String | Returns a string representation of this object. |
| toStringDeep({String prefixLineOne: '', String prefixOtherLines, DiagnosticLevel minLevel: DiagnosticLevel.debug }) | String | Returns a string representation of this node and its descendants. |
| toStringShallow({String joiner: ', ', DiagnosticLevel minLevel: DiagnosticLevel.debug }) | String | Returns a one-line detailed description of the object. |
| toStringShort() | String | A short, textual description of this widget. |
| updateRenderObject(BuildContext context, RenderPositionedBox renderObject) | void | Copies the configuration described by this RenderObjectWidget to the given RenderObject, which will be of the same type as returned by this object's createRenderObject. |

<br/>


使用上只要將元件放置於 Center widget 的 child 屬性。     

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

{% asset_img 1.png %}
 
<br/>


該元件即會被置中處理。  

{% asset_img 2.png %}
 
<br/>


Link
----
* [Center class - widgets library - Dart API](https://docs.flutter.io/flutter/widgets/Center-class.html)
