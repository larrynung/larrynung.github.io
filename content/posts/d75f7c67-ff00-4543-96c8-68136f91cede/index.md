---
title: "VC.NET Natived Event"
date: "2013-11-06 12:00:00"
tags: [C++]
description: "事件宣告 事件繫結 hook(&事件來源類別::EventName,事件來源物件指標,&處理事件的類別::HandleMethod); 移除繫結 unhook(&事件來源類別::EventName,事件來源物件指標,&處理事件的類別::HandleMethod); 事件觸發 範例 注意事項…"
---

## 事件宣告

```
__event void EventName();
```

## 事件繫結

__hook(&事件來源類別::EventName,事件來源物件指標,&處理事件的類別::HandleMethod);

## 移除繫結

__unhook(&事件來源類別::EventName,事件來源物件指標,&處理事件的類別::HandleMethod);

## 事件觸發

```
__raise EventName();
```

## 範例

```c
// TestNativedEvent.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

class TestObj
{
public:
	__event void Executed();

protected:
	void OnExecuted()
	{
		printf("Executed\n");
	}

public:
	void Execute()
	{
		__raise Executed();
	}

	void BindingEvent(){
		__hook(&TestObj::Executed,this,&TestObj::OnExecuted);
	}

	void UnBindingEvent(){
		__unhook(&TestObj::Executed,this,&TestObj::OnExecuted);
	}

};

int _tmain(int argc, _TCHAR* argv[])
{
	TestObj obj;
	obj.BindingEvent();
	obj.Execute ();
	return 0;
}
```

## 注意事項

若在使用上出現AccessViolationException例外，可參閱 KB811193 - 注意： 您會收到 「 0xC0000005 「 原生的事件引發或 unhooked 時的錯誤代碼。

## Link

* Event Handling
* Event Handling in Native C++
* event_source
* event_receiver
* __event
* __raise
* __hook
* __unhook
* KB811193 - 注意： 您會收到 「 0xC0000005 「 原生的事件引發或 unhooked 時的錯誤代碼
