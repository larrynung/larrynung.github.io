---
title: "[C++/CLI]Nativated物件處理Managed物件的事件"
date: "2010-07-01 01:01:43"
description: "[C++/CLI]Nativated物件處理Managed物件的事件"
tags: [C++]
---

在C++/CLI中Nativated物件與Managed物件允許混合使用，像是Nativated物件裡面就可以拿Managed物件來直接使用，只要透過gcroot關鍵字來宣告Managed物件就可以了，使用上不會太難。但若希望Nativated物件能去處理Managed物件所觸發的事件，由於無法將Nativated事件處理函式直接繫上Managed物件的事件，我們就必須自行做些特殊的處理。

舉個例子來看，假設今天我有個CNativatedClass，想要在裡面直接使用Managed的Timer(這邊命名為m_pAutoRunTimer)，我們要去處理Timer.Tick事件時，就必須要再造個Managed的殼來輔助我們，像是下面這樣：
```
ref class AutoRunTimerThunk
{
private:
CNativedClass*_handler;
public:
AutoRunTimerThunk( CNativedClass* handler)
{
_handler = handler;
}

void OnAutoRunTimerTick(System::Object^ sender, System::EventArgs^ e)
{
_handler->AutoRunTimer_Tick(sender, e);
}
};
```
這邊的寫法只是造個Managed的殼，把Nativated物件的指標透過建構子給傳入，並造個事件處理函式來觸發Nativated物件的事件處理函式。

最後在Nativated物件中使用上面造的殼，把自身的參考傳入並繫上Timer.Tick事件就可以了。
```
m_pAutoRunTimer->Tick += gcnew System::EventHandler(gcnew AutoRunTimerThunk(this), &AutoRunTimerThunk::OnAutoRunTimerTick);
```