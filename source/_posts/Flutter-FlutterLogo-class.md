---
title: Flutter - FlutterLogo class
date: 2018-04-01 21:50:14
tags: [Flutter]
---

Flutter 的 FlutterLogo widget 可用來顯示 Flutter 的 Logo。  

<!-- More -->

<br/>


其建構子如下：  

    FlutterLogo({Key key, double size, MaterialColor colors, Color textColor: const Color(0xFF616161), FlutterLogoStyle style: FlutterLogoStyle.markOnly, Duration duration: const Duration(milliseconds: 750), Curve curve: Curves.fastOutSlowIn })

<br/>


屬性如下：  

| Name | Type | Description |
|:-------------:|:-------------:|:-----:|
| colors | MaterialColor | The color swatch to use to paint the logo, Colors.blue by default. |
| curve | Curve | The curve for the logo animation if the style, colors, or textColor change. |
| duration | Duration | The length of time for the animation if the style, colors, or textColor properties are changed. |
| size | double | The size of the logo in logical pixels. |
| style | FlutterLogoStyle | Whether and where to draw the "Flutter" text. By default, only the logo itself is drawn. |
| textColor | Color | The color used to paint the "Flutter" text on the logo, if style is FlutterLogoStyle.horizontal or FlutterLogoStyle.stacked. The appropriate color is const Color(0xFF616161) (a medium gray), against a white background. |
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
| debugFillProperties(DiagnosticPropertiesBuilder description) | void | 
Add additional properties associated with the node. |
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
  runApp(new FlutterLogo());
}
```

{% asset_img 1.png %}
 
<br/>

{% asset_img 2.png %}
 
<br/>


若有需要可以透過 colors 屬性變更 Logo 的顏色。  

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(new FlutterLogo(colors: Colors.green));
}
```


{% asset_img 3.png %}
 
<br/>

{% asset_img 4.png %}
 
<br/>


或是變更 style 屬性為 FlutterLogoStyle.horizontal，將 Logo 與 Flutter 字樣水平呈現。  

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(new FlutterLogo(style: FlutterLogoStyle.horizontal));
}
```


{% asset_img 5.png %}
 
<br/>

{% asset_img 6.png %}
 
<br/>


變更為 FlutterLogoStyle.stacked 的話就會將 Flutter 字樣放置 Logo 下方。  

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(new FlutterLogo(style: FlutterLogoStyle.stacked));
}
```


{% asset_img 7.png %}
 
<br/>

{% asset_img 8.png %}
 
<br/>


若要調動 Flutter 字樣的顏色，可以透過 textColor 屬性設定。  

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(new FlutterLogo(
    style: FlutterLogoStyle.stacked,
    textColor: Colors.green,
  ));
}
```


{% asset_img 9.png %}
 
<br/>

{% asset_img 10.png %}
 
<br/>
