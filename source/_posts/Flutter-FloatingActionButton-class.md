---
title: Flutter - FloatingActionButton class
date: 2018-04-08 23:32:03
tags: [Flutter]
---

Flutter 的 FloatingActionButton widget 可以用來做按鈕的呈現，一般會搭配 Scaffold一起使用。  

<!-- More -->

<br/>


其建構子如下：  

    FloatingActionButton({Key key, Widget child, String tooltip, Color backgroundColor, Object heroTag: const _DefaultHeroTag(), double elevation: 6.0, double highlightElevation: 12.0, @required VoidCallback onPressed, bool mini: false, double notchMargin: 4.0 })

<br/>


屬性如下：  

| Name | Type | Description |
|:-------------:|:-------------:|:-----:|
| backgroundColor | Color | The color to use when filling the button. |
| child | Widget | The widget below this widget in the tree. |
| elevation | double | The z-coordinate at which to place this button. This controls the size of the shadow below the floating action button. |
| heroTag | Object | The tag to apply to the button's Hero widget. |
| highlightElevation | dobule | The z-coordinate at which to place this button when the user is touching the button. This controls the size of the shadow below the floating action button. |
| mini | bool | Controls the size of this button. |
| notchMargin | double | The margin to keep around the floating action button when creating a notch for it. |
| onPressed | VoidCallback | The callback that is called when the button is tapped or otherwise activated. |
| tooltip | String | Text that describes the action that will occur when the button is pressed. |
| hashCode | int | The hash code for this object. |
| key | Key | Controls how one widget replaces another widget in the tree. |
| runtimeType | Type | A representation of the runtime type of the object. |

<br/>


方法如下：

| Name | Return Type | Description |
|:-------------:|:-------------:|:-----:|
| createState() | _FloatingActionButtonState | Creates the mutable state for this widget at a given location in the tree. |
| createElement() | StatefulElement | Creates a StatefulElement to manage this widget's location in the tree. |
| debugDescribeChildren() | List<DiagnosticsNode> | Returns a list of DiagnosticsNode objects describing this node's children. |
| debugFillProperties(DiagnosticPropertiesBuilder description) | void | Add additional properties associated with the node. |
| noSuchMethod(Invocation invocation) | dynamic | Invoked when a non-existent method or property is accessed. |
| toDiagnosticsNode({String name, DiagnosticsTreeStyle style }) | DiagnosticsNode | Returns a debug representation of the object that is used by debugging tools and by toStringDeep. |
| toString({DiagnosticLevel minLevel: DiagnosticLevel.debug }) | String | Returns a string representation of this object. |
| toStringDeep({String prefixLineOne: '', String prefixOtherLines, DiagnosticLevel minLevel: DiagnosticLevel.debug }) | String | Returns a string representation of this node and its descendants. |
| toStringShallow({String joiner: ', ', DiagnosticLevel minLevel: DiagnosticLevel.debug }) | String | Returns a one-line detailed description of the object. |
| toStringShort() | String | A short, textual description of this widget. |

<br/>


FloatingActionButton 元件需在 MaterialApp 下使用，使用上要設定 onPressed 屬性，指定按鈕按下後要觸發的動作，child 屬性可設定按鈕上要呈現的圖片或文字，tooltip 可設定按鈕的提示訊息。  

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(
    new MaterialApp(
      home: new FloatingActionButton(
        onPressed: () {},
        tooltip: 'Increment',
        child: new Icon(Icons.add),
      )
    )
  );
}
```

{% asset_img 1.png %}
 
<br/>

{% asset_img 2.png %}
 
<br/>

{% asset_img 3.png %}
 
<br/>


backgroundColor 屬性可設定按鈕的背景色。  

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(
    new MaterialApp(
      home: new FloatingActionButton(
        onPressed: () {},
        tooltip: 'Increment',
        child: new Icon(Icons.add),
        backgroundColor: Colors.green
      )
    )
  );
}
```

{% asset_img 4.png %}
 
<br/>

{% asset_img 5.png %}
 
<br/>


Link
----
* [FloatingActionButton class - material library - Dart API](https://docs.flutter.io/flutter/material/FloatingActionButton-class.html)
