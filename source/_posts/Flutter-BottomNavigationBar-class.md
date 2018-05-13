---
title: Flutter - BottomNavigationBar class
date: 2018-05-09 23:33:10
tags: [Flutter]
---

Flutter 的 BottomNavigationBar widget 需搭配 Scaffold 使用，可用以設定 Scaffold 下方的巡覽列。  

<!-- More -->

<br/>


其建構子如下：

    BottomNavigationBar({Key key, @required List<BottomNavigationBarItem> items, ValueChanged<int> onTap, int currentIndex: 0, BottomNavigationBarType type, Color fixedColor, double iconSize: 24.0 })

<br/>


屬性如下：  

| Name | Type | Description |
|:-------------:|:-------------:|:-----:|
| currentIndex | int | The index into items of the current active item. |
| fixedColor | Color | The color of the selected item when bottom navigation bar is BottomNavigationBarType.fixed. |
| iconSize | double | The size of all of the BottomNavigationBarItem icons. |
| items | List<BottomNavigationBarItem> | The interactive items laid out within the bottom navigation bar. |
| onTap | ValueChanged<int> | The callback that is called when a item is tapped. |
| type | BottomNavigationBarType | Defines the layout and behavior of a BottomNavigationBar. |
| hashCode | int | The hash code for this object. |
| key | Key | Controls how one widget replaces another widget in the tree. |
| runtimeType | Type | A representation of the runtime type of the object. |

<br/>


方法如下：

| Name | Return Type | Description |
|:-------------:|:-------------:|:-----:|
| createState() | _BottomNavigationBarState | Creates the mutable state for this widget at a given location in the tree. |
| createElement() | StatefulElement | Creates a StatefulElement to manage this widget's location in the tree. |
| debugDescribeChildren() | List<DiagnosticsNode> | Returns a list of DiagnosticsNode objects describing this node's children. |
| debugFillProperties(DiagnosticPropertiesBuilder properties) | void | Add additional properties associated with the node. |
| noSuchMethod(Invocation invocation) | dynamic | Invoked when a non-existent method or property is accessed. |
| toDiagnosticsNode({String name, DiagnosticsTreeStyle style }) | DiagnosticsNode | Returns a debug representation of the object that is used by debugging tools and by toStringDeep. |
| toString({DiagnosticLevel minLevel: DiagnosticLevel.debug }) | String | Returns a string representation of this object. |
| toStringDeep({String prefixLineOne: '', String prefixOtherLines, DiagnosticLevel minLevel: DiagnosticLevel.debug }) | String | Returns a string representation of this node and its descendants. |
| toStringShallow({String joiner: ', ', DiagnosticLevel minLevel: DiagnosticLevel.debug }) | String | Returns a one-line detailed description of the object. |
| toStringShort() | String | A short, textual description of this widget. |

<br/>


比較重要的屬性有 fixedColor，可設定選取項目的顏色，iconSize 屬性可設定項目圖示的大小，currentIndex 屬性可設定作用中的項目，items 屬性可設定可使用的項目。  

<br/>


使用時只要建立出 BottomNavigationBar 實體，並指給 Scoffold 的 bottomNabigationBar 屬性即可。  

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(new MaterialApp(
      home: new Scaffold(
          bottomNavigationBar: new BottomNavigationBar(
    fixedColor: Colors.blue,
    iconSize: 64.0,
    currentIndex: 1,
    items: <BottomNavigationBarItem>[
      new BottomNavigationBarItem(
        icon: new Icon(Icons.arrow_left),
        title: new Text("Left"),
      ),
      new BottomNavigationBarItem(
        icon: new Icon(Icons.arrow_right),
        title: new Text("Right"),
      ),
    ],
  ))));
}
```


{% asset_img 1.png %}
 
<br/>

{% asset_img 2.png %}
 
<br/>


Link
----
* [BottomNavigationBar class - material library - Dart API](https://docs.flutter.io/flutter/material/BottomNavigationBar-class.html)
