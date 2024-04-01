---
title: "Visual Studio Code - Launch files in browser"
date: "2017-05-01 23:11:36"
tags: [Visual Studio Code]
---


要設定 Visual Studio Code 用瀏覽器開啟運行檔案，可開啟 Command palette (MAC 下使用 'CMD + Shift + P'，Windows 下使用 'Ctrl + Shift + P') 選取 'Configure Task Runner' 為專案加入 task.json。  

<!-- More -->

![1.png](1.png)

<br/>


![2.png](2.png)

<br/>


MAC 下 task.json 可設定如下：  

```json
{
    "version": "0.1.0",
    "command": "Chrome",
    "osx": {
        "command": "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    },
    "args": ["${file}"]
}
```

<br/>


![3.png](3.png)

<br/>


Windows 下設定如下：  

```json
{
    "version": "0.1.0",
    "command": "Chrome",
    "windows": {
        "command": "C:\Program Files (x86)\Google\Chrome\Application
