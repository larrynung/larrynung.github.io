---
title: TensorFlow - Installing TensorFlow on Ubuntu
date: 2018-05-23 00:23:11
tags: [TensorFlow]
---

要在 Ubuntu 下安裝 TensorFlow，可先用 apt-get 更新一下。  

<!-- More -->

<br/>

    sudo apt-get update

{% asset_img 1.png %}
 
<br/>


更新完後使用 apt-get 安裝 python 與 pip。  

    sudo apt-get install python-pip python-dev

{% asset_img 2.png %}
 
<br/>


最後透過 pip 將 TensorFlow 安裝起來即可。  

    sudo pip install --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.8.0-cp27-none-linux_x86_64.whl

{% asset_img 3.png %}
 
<br/>


安裝完後可以使用 python 測試一下 TensorFlow 是否已可正常使用，輸入 python 命令進入交互模式，引用 tensorflow 套件，調用 __version__ 查閱 TensorFlow 的版本。  

```python
import tensorflow as tf  
tf.__version__
```

{% asset_img 4.png %}
 
<br/>


如果可以正常看到 TensorFlow 版本的話代表 TensorFlow 已被正常安裝完成。  

<br/>


Link
----
* [真正從零開始，TensorFlow安裝入門教程！（圖文版） | 香港矽谷](https://www.hksilicon.com/articles/1106629)
