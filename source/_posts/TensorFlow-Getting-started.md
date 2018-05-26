---
title: TensorFlow - Getting started
date: 2018-05-27 00:04:56
tags: [TensorFlow]
---

安裝完 TensorFlow 後，可以試著撰寫個簡單的 Hello World 程式。  

<!-- More -->

<br/>


首先我們需將 tensorflow 匯入。  

```python
import tensorflow as tf
...
```

<br/>


設定一個常數其內容為 "Hello World!"。  

```python
...
hello = tf.constant("Hello World!")
...
```

<br/>


再來要取得 TensorFlow 的 Session，可以把 Session 想成運行 TensorFlow 的環境。 

``` python
...
sess = tf.Session()
...
```

<br/>
 
最後將要運行的部分送至 Session 中運行即可。  

```python
...
print(sess.run(hello))
```

<br/>


完整的程式會像下面這樣：  

```python
import tensorflow as tf

hello = tf.constant("Hello World!")

sess = tf.Session()
print(sess.run(hello))
```

<br/>


運行結果如下：    

{% asset_img 1.png %}

