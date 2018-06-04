---
title: TensorFlow - placeholder
date: 2018-06-04 23:52:52
tags: [TensorFlow]
---

TensonrFlow 的 placeholder 方法可用來指定後續運行才會帶入的值，其函式原型如下：  

<!-- More -->

    tf.placeholder(
        dtype,
        shape=None,
        name=None
    )

<br/>


其中 dtype 是值的型態，shape 是常數的維度。  

<br/>


可以直接調用 placeholder 方法並帶入指定的型態。  

```python
...
a = tf.placeholder(tf.float32)
...
```

<br/>


也可以帶入 shape 限定維度。  

```python
...
b = tf.placeholder(tf.float32, shape=(2, 3))
...
```

<br/>


然後使用 placeholder 構成運算。  

```python
...
a2 = a * a
...
bPlus = b + 1
...
```

<br/>


最後帶入 placeholder 的值丟到 session 運行即可。  

```python
...
print(sess.run(a2, feed_dict={a: 2}))
print(sess.run(a2, feed_dict={a: [[1, 2, 3], [4, 5, 6]]}))
print(sess.run(bPlus, feed_dict={b: [[1, 2, 3], [4, 5, 6]]}))
...
```  

<br/>


最後附上完整的範例程式：  

```python
import tensorflow as tf

a = tf.placeholder(tf.float32)
a2 = a * a
b = tf.placeholder(tf.float32, shape=(2, 3))
bPlus = b + 1

with tf.Session() as sess:
  print(sess.run(a2, feed_dict={a: 2}))
  print(sess.run(a2, feed_dict={a: [[1, 2, 3], [4, 5, 6]]}))
  print(sess.run(bPlus, feed_dict={b: [[1, 2, 3], [4, 5, 6]]}))
```

<br/>


其運行結果如下：  

{% asset_img 1.png %}
 
<br/>


Link
----
* [tf.placeholder  |  TensorFlow](https://www.tensorflow.org/api_docs/python/tf/placeholder)
