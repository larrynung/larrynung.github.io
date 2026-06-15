---
title: "[C++]Simple nativated timer class"
date: "2011-11-05 11:26:53"
description: "[C++]Simple nativated timer class"
tags: [C++]
---
從.NET跨足到C++筆者還是不太習慣C++的寫作方式，比較習慣於用.NET的寫法來寫C++程式，既然C++也開始具備屬性跟事件，C++也能寫的跟.NET程式很像。這邊筆者試寫了一個簡單的C++ Nativated Timer，希望使用上會比較接近.NET的寫作習慣，這邊將之稍做整理。

程式的部分主要有EventArgs與Timer兩個類別，程式碼如下：

EventArgs.h

#pragma once
class EventArgs
{
#pragma region Constructor & DeConstructor
public:
EventArgs(void);
virtual ~EventArgs(void);
#pragma endregion

};

EventArgs.Cpp

#include "stdafx.h"
#include "EventArgs.h"

#pragma region Constructor & DeConstructor
EventArgs::EventArgs(void)
{
}

EventArgs::~EventArgs(void)
{
}
#pragma endregion

Timer.h

#pragma once
#include "EventArgs.h"
#include

[event_source]
[event_receiver]
class Timer
{
#pragma region Var
private:
int _nTimerID;
int _nInterval;
bool _bIsEnabled;
#pragma endregion

#pragma region Private Property
private:
__declspec(property(get=Get_nTimerID,put=Set_nTimerID))
int m_nTimerID;
#pragma endregion

#pragma region Public Property
public:
__declspec(property(get=Get_nInterval,put=Set_nInterval))
int m_nInterval;

__declspec(property(get=Get_bIsEnabled,put=Set_bIsEnabled))
bool m_bIsEnabled;
#pragma endregion

#pragma region Event
public:
__event void IntervalChanging(void* sender, EventArgs* e);
__event void IntervalChanged(void* sender, EventArgs* e);
__event void IsEnabledChanging(void* sender, EventArgs* e);
__event void IsEnabledChanged(void* sender, EventArgs* e);
__event void Tick(void* sender, EventArgs* e);
#pragma endregion

#pragma region Constructor & DeConstructor
public:
Timer(int nInterval = 0);
Timer(bool bIsEnabled, int nInterval = 0);
virtual ~Timer(void);
#pragma endregion

#pragma region Property Process Method
private:
inline int Get_nTimerID()
{
return _nTimerID;
}

inline void Set_nTimerID(int value)
{
if(_nTimer value)
return;

_nTimer
}

public:
inline int Get_nInterval()
{
return _nInterval;
}

inline void Set_nInterval(int value)
{
if(_nInterval == value)
return;

EventArgs e;
OnIntervalChanging(&e);

_nInterval = value;

OnIntervalChanged(&e);
}

inline bool Get_bIsEnabled()
{
return _bIsEnabled;
}

inline void Set_bIsEnabled(bool value)
{
if(_bIsEnabled == value)
return;

EventArgs e;
OnIsEnabledChanging(&e);

_bIsEnabled = value;

OnIsEnabledChanged(&e);
}
#pragma endregion

#pragma region Private Method
private:
void Init(bool bIsEnabled = false, int nInterval = 0);
void UnBindingEvent();
void BindingEvent();
void KillTimer();
void SetTimer();

static void CALLBACK TimerProc(HWND hwnd, UINT uMsg, UINT_PTR idEvent, DWORD dwTime);
#pragma endregion

#pragma region Protected Method
protected:
virtual void Reset(bool bIsInit = false);

void OnIntervalChanging(EventArgs* e)
{
__raise IntervalChanging(this, e);
}

void OnIntervalChanged(EventArgs* e)
{
__raise IntervalChanged(this, e);
}

void OnIsEnabledChanging(EventArgs* e)
{
__raise IsEnabledChanging(this, e);
}

void OnIsEnabledChanged(EventArgs* e)
{
__raise IsEnabledChanged(this, e);
}

void OnTick(EventArgs* e)
{
__raise Tick(this, e);
}
#pragma endregion

#pragma region Public Method
public:
void Start();
void Stop();
#pragma endregion

#pragma region Event Process
private:
void Timer_IsEnabledChanged(void* sender, EventArgs* e);
void Timer_IntervalChanged(void* sender, EventArgs* e);
#pragma endregion
};

Timer.Cpp

#include "stdafx.h"
#include "Timer.h"
#include

using namespace std;

map g_TimerPool;

#pragma region Constructor & DeConstructor
Timer::Timer(int nInterval)
{
Init(false, nInterval);
}

Timer::Timer(bool bIsEnabled, int nInterval)
{
Init(bIsEnabled, nInterval);
}

Timer::~Timer(void)
{
Reset();
}
#pragma endregion

#pragma region Private Method
void Timer::Init(bool bIsEnabled, int nInterval)
{
Reset(true);
m_bIsEnabled = bIsEnabled;
m_nInterval = nInterval;
BindingEvent();
}

void Timer::UnBindingEvent()
{
__unhook(&Timer::IsEnabledChanged, this, &Timer::Timer_IsEnabledChanged);
__unhook(&Timer::IntervalChanged, this, &Timer::Timer_IntervalChanged);
}

void Timer::BindingEvent()
{
UnBindingEvent();
__hook(&Timer::IsEnabledChanged, this, &Timer::Timer_IsEnabledChanged);
__hook(&Timer::IntervalChanged, this, &Timer::Timer_IntervalChanged);
}

void Timer::KillTimer()
{
if(!m_nTimerID)
return;
::KillTimer(NULL, m_nTimerID);
g_TimerPool[m_nTimerID] = NULL;
m_nTimer
}

void Timer::SetTimer()
{
KillTimer();

if(!m_bIsEnabled)
return;

if(m_nTimerID)
return;

m_nTimer NULL, m_nInterval, TimerProc);
g_TimerPool[m_nTimerID] = this;
}

void CALLBACK Timer::TimerProc(HWND hwnd, UINT uMsg, UINT_PTR idEvent, DWORD dwTime)
{
if(g_TimerPool.find(idEvent) == g_TimerPool.end())
return;

Timer* pTimer = g_TimerPool[idEvent];

if(!pTimer)
return;

EventArgs eventArgs;
pTimer->OnTick(&eventArgs);
}
#pragma endregion

#pragma region Protected Method
void Timer::Reset(bool bIsInit)
{
if(bIsInit)
{
_nTimer
}

__unhook(this);

UnBindingEvent();

_bIsEnabled = false;
_nInterval = 0;

if(_nTimerID)
{
KillTimer();
_nTimer
}
}
#pragma endregion

#pragma region Public Method
void Timer::Start()
{
m_bIsEnabled = true;
}

void Timer::Stop()
{
m_bIsEnabled = false;
}
#pragma endregion

#pragma region Event Process
void Timer::Timer_IsEnabledChanged(void* sender, EventArgs* e)
{
SetTimer();
}

void Timer::Timer_IntervalChanged(void* sender, EventArgs* e)
{
SetTimer();
}
#pragma endregion

使用上會像下面這樣，設定Timer的週期與是否啟用，並繫結事件處理常式做對應的處理。

// ConsoleApplication9.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"
#include
#include "Timer.h"

class TestClass
{
public:
Timer m_Timer;
int m_nTickCount;

TestClass()
{
m_nTickCount = 0;
__hook(&Timer::Tick, &m_Timer, &TestClass::Timer_Tick);
m_Timer.m_nInterval = 1000;
m_Timer.m_bIsEnabled = true;
}

void Timer_Tick(void* sender, EventArgs* e)
{
++m_nTickCount;
printf("Timer_Tick
");
}
};

int _tmain(int argc, _TCHAR* argv[])
{
MSG msg;
TestClass testObj;

while (testObj.m_nTickCount < 10)
{
GetMessage(&msg, NULL, 0, 0);
TranslateMessage(&msg);
DispatchMessage(&msg);
}
return 0;
}

運行後可每秒寫出一個Timer_Tick的字串，運行十秒後結束。