---
title: Termux - Setup Jupyter Notebook
date: 2018-10-15 23:31:35
tags: [Termux]
---

要在 Termux 安裝 Jupyter Notebook，要先安裝一些依賴的套件。  

<!-- more -->

    apt install clang python python-dev fftw libzmq libzmq-dev freetype freetype-dev libpng libpng-dev pkg-config

{% asset_img 1.jpg %}

</br>


再用 pip 安裝 Jupyter。  

    pip install jupyter

</br>


安裝完後啟動 Jupyter。  

    jupyter notebook

{% asset_img 2.jpg %}

</br>


啟動訊息會帶出 Jupyter Notebook 的位置。  

{% asset_img 3.jpg %}

</br>


訪問該位置即可開始使用 Jupyter Notebook。  

{% asset_img 4.jpg %}
