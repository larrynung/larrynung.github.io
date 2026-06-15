---
title: "Python's and_or operation"
date: "2013-11-06 12:00:00"
description: "Python's and_or operation"
tags: [Python]
---

在Python中除了Boolean的True以外，非空的值亦視為True，反之則視為False。所謂的空值指的就是0、空字串、空集合、空的Tuple...，所以除了False以外，0、''、()、[]、{}...在Python中也都代表著False。

因為有這樣的特性，Python中and/or運算變得非常的有趣。

以and操作來說，and運算是條件都成立就成立，當一個條件不成立即可判斷整個條件不成立。所以假設and運算式中看到了False的值就會停止繼續往下判斷，而若是看到了True的值則會繼續往下判斷。

所以像是下面這樣的例子：

```python
print "'a' and 'b': ", 'a' and 'b'
print "'' and 'b': ", '' and 'b'
print "'a' and '': ", 'a' and ''
print "'a' and 'b' and 'c': ", 'a' and 'b' and 'c'
```

運行起來就會像下面這樣：

![image_thumb_1.png](/images/posts/5e0b8fb2-ce84-43b7-b7d6-8b87a8bfb8da/image_thumb_1.png)

以'a' and 'b'來說，因為'a'為True，所以需要繼續往下判斷，而'b'亦為True，所以直接回傳'b'。

```python
print "'a' and 'b': ", 'a' and 'b'
```

以'' and 'b'來說，因為''為False，所以整個判斷式注定為不成立，不需要繼續往下判斷，故直接回傳''。

```python
print "'' and 'b': ", '' and 'b'
```

其它兩個以此類推。

以or操作來說，or運算是條件一個成立就成立，當一個條件成立即可判斷整個條件成立。所以假設or運算式中看到了True的值就會停止繼續往下判斷，而若是看到了False的值則會繼續往下判斷。

所以像是下面這樣的例子：

```python
print "'a' or 'b': ", 'a' or 'b'
print "'' or 'b': ", '' or 'b'
print "'a' or '': ", 'a' or ''
print "0 or '' or [] or {}: ", 0 or '' or [] or {}
```

運行起來就會像下面這樣：

![image_thumb_2.png](/images/posts/5e0b8fb2-ce84-43b7-b7d6-8b87a8bfb8da/image_thumb_2.png)

以'a' or 'b'來說，因為'a'為True，所以不需要繼續往下判斷，直接回傳'a'。

```python
print "'a' or 'b': ", 'a' or 'b'
```

以'' or 'b'來說，因為''為False，所以需要繼續往下判斷，而'b'亦為True，所以直接回傳'b'。

```python
print "'' or 'b': ", '' or 'b'
```

其它兩個一樣以此類推。

不過雖然Python and/or運算有著這樣的特性，但是仍舊不完全等價本來的Boolean型別，所以無法直接將之與Boolean型別的True/False去做比對，以下面這個例子來說：

```python
print "'a' == True: ", 'a' == True
print "'a' is True: ", 'a' is True
print "bool('a') == True: ", bool('a') == True
print "bool('a') is True: ", bool('a') is True
print "'a' == ('a' and 'b'): ", 'a' == ('a' and 'b')
print "'b' == ('a' and 'b'): ", 'b' == ('a' and 'b')
print "'a' == ('a' or 'b'): ", 'a' == ('a' or 'b')
print "'b' == ('a' or 'b'): ", 'b' == ('a' or 'b')
```

我們可以看到直接去用==運算子或是is關鍵字下去判斷是否為True是無效的，若需要類似這樣的判斷，我們會需要用內建的函式或是用特定的運算式去輔助處理。

![image_thumb_6.png](/images/posts/5e0b8fb2-ce84-43b7-b7d6-8b87a8bfb8da/image_thumb_6.png)

最後來看一下三元運算的部分，先來看一下程式碼的部分：

```python
print "True and 'TrueValue' or 'FalseValue': ", True and 'TrueValue' or 'FalseValue'
print "False and 'TrueValue' or 'FalseValue': ", False and 'TrueValue' or 'FalseValue'
print "True and '' or 'FalseValue': ", True and '' or 'FalseValue'
print "(True and [''] or ['FalseValue'])[0]: ", (True and [''] or ['FalseValue'])[0]
```

其運行結果為：

![image_thumb_4.png](/images/posts/5e0b8fb2-ce84-43b7-b7d6-8b87a8bfb8da/image_thumb_4.png)

可以看到若三元運算選取的兩個值都不為空的話，我們可以簡單的用[expression] and [value1] or [value2]這樣的方式下去撰寫。因為expression與value1之間為and運算，若expression為true則會去看value1的值，而與value2之間為or運算，value1的值又不為空值，所以會直接回傳value1；若expression為false，因為[expression] and [value1]運算出來為[expression]，所以運算式等同[expression] or [value2]，故回傳value2的值。等同於我們一般看到的三元運算效果。

但是這樣的寫法有個前提就是必須三元運算選取的兩個值都不為空，若是為空則整個效果就會不如預期，所以在使用時我們可以以陣列的方式下去封裝一下，以([expression] and [[value1]] or [[value2]])[0]這樣的方式下去撰寫。

## Link

* Built-in Types
