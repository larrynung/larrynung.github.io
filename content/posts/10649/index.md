---
title: "VC.NET Natived Property"
date: "2009-09-16 09:04:35"
description: "VC.NET Natived Property"
tags: [C++]
---

在VC.NET Natived類別中，若需要撰寫屬性，我們可以透過__declspec關鍵字來達到我們的需求。

使用__declspec關鍵字來建立屬性跟一般的.NET的語言一樣，都需要get區塊與set區塊。因此我們必須撰寫get區塊與set區塊的方法，並用__declspec關鍵字把其與欲作為屬性的變數設上關聯。就像：
```
private:
bool _isRunning;
public:
__declspec(property(get=GetRunning,put=SetRunning))
bool m_bIsRunning;
public:
void SetRunning(bool value){
_isRunning=value;
}
bool GetRunning(){
return _isRunning;
}
```
以這個例子來說，當我們對m_bIsRunning做設定時，會呼叫SetRunning方法；而當我們對m_bIsRunning做讀取時，則會呼叫GetRunning方法。

## 完整範例
```
class TestObj
{
private:
bool _isRunning;
public:
__declspec(property(get=GetRunning,put=SetRunning))
bool m_bIsRunning;
public:
void SetRunning(bool value){
_isRunning=value;
}
bool GetRunning(){
return _isRunning;
}
};

int _tmain(int argc, _TCHAR* argv[])
{
TestObj obj;
obj.m_bIsRunning = true;
return 0;
}
```