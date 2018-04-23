---
title: Flutter - ListView class
date: 2018-04-20 23:27:17
tags: [Flutter]
---

Flutter 的 ListView 元件是一具備捲軸的元件且能用來顯示多筆內容的元件。  

<!-- More -->

<br/>


其建構子如下：  

    ListView({Key key, Axis scrollDirection: Axis.vertical, bool reverse: false, ScrollController controller, bool primary, ScrollPhysics physics, bool shrinkWrap: false, EdgeInsetsGeometry padding, double itemExtent, bool addAutomaticKeepAlives: true, bool addRepaintBoundaries: true, List<Widget> children: const [] })
    ListView.builder({Key key, Axis scrollDirection: Axis.vertical, bool reverse: false, ScrollController controller, bool primary, ScrollPhysics physics, bool shrinkWrap: false, EdgeInsetsGeometry padding, double itemExtent, @required IndexedWidgetBuilder itemBuilder, int itemCount, bool addAutomaticKeepAlives: true, bool addRepaintBoundaries: true })
    ListView.custom({Key key, Axis scrollDirection: Axis.vertical, bool reverse: false, ScrollController controller, bool primary, ScrollPhysics physics, bool shrinkWrap: false, EdgeInsetsGeometry padding, double itemExtent, @required SliverChildDelegate childrenDelegate })

<br/>


屬性如下：  

| Name | Type | Description |
|:-------------:|:-------------:|:-----:|
| childrenDelegate | SliverChildDelegate | A delegate that provides the children for the ListView. |
| itemExtent | double | If non-null, forces the children to have the given extent in the scroll direction. |
| controller | ScrollController | An object that can be used to control the position to which this scroll view is scrolled. |
| hashCode | int | The hash code for this object. |
| key | Key | Controls how one widget replaces another widget in the tree. |
| padding | EdgeInsetsGeometry | The amount of space by which to inset the children. |
| physics | ScrollPhysics | How the scroll view should respond to user input. |
| primary | bool | Whether this is the primary scroll view associated with the parent PrimaryScrollController. |
| reverse | bool | Whether the scroll view scrolls in the reading direction. |
| runtimeType | Type | A representation of the runtime type of the object. |
| scrollDirection | Axis | The axis along which the scroll view scrolls. |
| shrinkWrap | bool | Whether the extent of the scroll view in the scrollDirection should be determined by the contents being viewed. |

<br/>


方法如下：

| Name | Return Type | Description |
|:-------------:|:-------------:|:-----:|
| buildChildLayout(BuildContext context) | Widget | Subclasses should override this method to build the layout model. |
| debugFillProperties(DiagnosticPropertiesBuilder properties) | void ||
| build(BuildContext context) | Widget | Describes the part of the user interface represented by this widget. |
| buildSlivers(BuildContext context) | List<Widget> | Build the list of widgets to place inside the viewport. |
| buildViewport(BuildContext context, ViewportOffset offset, AxisDirection axisDirection, List<Widget> slivers) | Widget | Build the viewport. |
| createElement() | StatelessElement | Creates a StatelessElement to manage this widget's location in the tree. |
| debugDescribeChildren() | List<DiagnosticsNode> | Returns a list of DiagnosticsNode objects describing this node's children. |
| getDirection(BuildContext context)  | AxisDirection | Returns the AxisDirection in which the scroll view scrolls. |
| noSuchMethod(Invocation invocation) | dynamic | Invoked when a non-existent method or property is accessed. |
| toDiagnosticsNode({String name, DiagnosticsTreeStyle style }) | DiagnosticsNode | Returns a debug representation of the object that is used by debugging tools and by toStringDeep. |
| toString({DiagnosticLevel minLevel: DiagnosticLevel.debug }) | String | Returns a string representation of this object. |
| toStringDeep({String prefixLineOne: '', String prefixOtherLines, DiagnosticLevel minLevel: DiagnosticLevel.debug }) | String | Returns a string representation of this node and its descendants. |
| toStringShallow({String joiner: ', ', DiagnosticLevel minLevel: DiagnosticLevel.debug }) | String | Returns a one-line detailed description of the object. |
| toStringShort() | String | A short, textual description of this widget. |

<br/>


使用上可以直接建立 ListView 元件，並透過 children 屬性直接帶入 ListView 內要呈現的內容，用 padding 屬性設定內容與內容間的間隔。  

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(new MaterialApp(
      home: new ListView(
    padding: const EdgeInsets.all(20.0),
    children: <Widget>[
      new Card(
        child: const Text('1. one')
      ),
      new Card(
        child: const Text('2. two')
      ),
      new Card(
        child: const Text('3. three')
      )
    ],
  )));
}
```

{% asset_img 1.png %}
 
<br/>

{% asset_img 2.png %}
 
<br/>


也可以建立 ListView.builder，設定 itemCount 屬性指定 ListView 內的內容數，並設定 itemBuilder 屬性指定 ListView 內的內容要怎樣呈現。  

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(new MaterialApp(
      home: new ListView.builder(
        shrinkWrap: true,
    padding: new EdgeInsets.all(20.0),
    itemCount: 3.toInt(),
    itemBuilder: (BuildContext context, int index) {
      return new Card
      (
        child: new Text(index.toString() + '. Element' + index.toString())
      );
    },
  )));
}

```

{% asset_img 3.png %}
 
<br/>


Link
----
* [ListView class - widgets library - Dart API](https://docs.flutter.io/flutter/widgets/ListView-class.html)
