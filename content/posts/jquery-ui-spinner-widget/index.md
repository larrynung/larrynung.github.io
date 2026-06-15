---
title: "JQuery UI - Spinner Widget"
date: "2015-12-24 05:44:00"
description: "JQuery UI - Spinner Widget"
---

要使用 JQuery UI 的 Spinner Widget，首先必須引用 JQuery、JQueryUI。
```html
```
接著在畫面上放入一個 input element。
```html
```
在 Javascript 中用 JQuery 找到該 input element，並叫用 spinner 方法即可將該 input element 設為 spinner。
```js
$(function() {
$("#spinner").spinner();
});
```
![1.png](/images/posts/JQueryUISpinner/1.png)

若要做些細部設定，spinner 有提供些 options 可供我們使用，像是 min 可以設定  spinner 的最小值，max 可以設定 spinner 的最大值，step 可以設定 spinner 按一次要增加多少值。
```js
$(function() {
$("#spinner").spinner(
{
min:0,
max:100,
step:10
});
});
```
若要主動觸發 spinner，也提供了些 methods 讓我們使用，像是 value。
```js
$(function() {
$("#spinner").spinner();
$("#spinner").spinner("value", 0);
});
```
最後這邊附上測試用的範例：
```html

$(function() {
$("#spinner").spinner(
{
min:0,
max:100,
step:10
});
$("#spinner").spinner("value", 0);
});
```
Link
----
* [Spinner Widget | jQuery UI API Documentation](http://api.jqueryui.com/spinner/#event-change)