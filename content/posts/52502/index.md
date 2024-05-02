---
title: "[C++]Simple nativated timer class"
date: "2011-11-05 11:26:53"
description: "[C++]Simple nativated timer class"
tags: [C++]
---

<p>
	從.NET跨足到C++筆者還是不太習慣C++的寫作方式，比較習慣於用.NET的寫法來寫C++程式，既然C++也開始具備屬性跟事件，C++也能寫的跟.NET程式很像。這邊筆者試寫了一個簡單的C++ Nativated Timer，希望使用上會比較接近.NET的寫作習慣，這邊將之稍做整理。</p>
<p>
	 </p>
<p>
	程式的部分主要有EventArgs與Timer兩個類別，程式碼如下：</p>
<p>
	 </p>
<p>
	EventArgs.h</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:6ae96aae-fac0-4024-a491-b31f1e4f7b95" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c" name="code">
#pragma once
class EventArgs
{
#pragma region Constructor &amp; DeConstructor
public:
	EventArgs(void);
	virtual ~EventArgs(void);  
#pragma endregion

};</pre>
</div>
<p>
	 </p>
<p>
	EventArgs.Cpp</p>
<p>
	 </p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:432276ab-16ea-49e5-8a60-04bd8b24f425" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c" name="code">
#include "stdafx.h"
#include "EventArgs.h"


#pragma region Constructor &amp; DeConstructor
EventArgs::EventArgs(void)
{
}


EventArgs::~EventArgs(void)
{
}  
#pragma endregion</pre>
</div>
<p>
	 </p>
<p>
	 </p>
<p>
	Timer.h</p>
<p>
	 </p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:22b00d3e-a9a4-4749-b94f-55fbdeaae854" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c" name="code">
#pragma once
#include "EventArgs.h"
#include &lt;Windows.h&gt;

[event_source]
[event_receiver]
class Timer
{
#pragma region Var
private:
	int		_nTimerID;
	int		_nInterval;
	bool	_bIsEnabled;
#pragma endregion


#pragma region Private Property
private:
	__declspec(property(get=Get_nTimerID,put=Set_nTimerID))
		int m_nTimerID;
#pragma endregion


#pragma region Public  Property
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
	

#pragma region Constructor &amp; DeConstructor
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
		if(_nTimerID == value)
			return;

		_nTimerID = value;
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
		OnIntervalChanging(&amp;e);

		_nInterval = value;

		OnIntervalChanged(&amp;e);
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
		OnIsEnabledChanging(&amp;e);

		_bIsEnabled = value;

		OnIsEnabledChanged(&amp;e);
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
};</pre>
</div>
<p>
	 </p>
<p>
	 </p>
<p>
	Timer.Cpp</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:79101e44-89c1-43d0-9349-8e8cf6340e37" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c" name="code">
#include "stdafx.h"
#include "Timer.h"
#include &lt;map&gt;

using namespace std;

map&lt;int, Timer*&gt;		g_TimerPool;

#pragma region Constructor &amp; DeConstructor
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
	m_bIsEnabled	= bIsEnabled;
	m_nInterval		= nInterval;
	BindingEvent();
}

void Timer::UnBindingEvent()
{
	__unhook(&amp;Timer::IsEnabledChanged, this, &amp;Timer::Timer_IsEnabledChanged);
	__unhook(&amp;Timer::IntervalChanged, this, &amp;Timer::Timer_IntervalChanged);
}

void Timer::BindingEvent()
{	
	UnBindingEvent();
	__hook(&amp;Timer::IsEnabledChanged, this, &amp;Timer::Timer_IsEnabledChanged);
	__hook(&amp;Timer::IntervalChanged, this, &amp;Timer::Timer_IntervalChanged);
}

void Timer::KillTimer()
{
	if(!m_nTimerID)
		return;
	::KillTimer(NULL, m_nTimerID);			
	g_TimerPool[m_nTimerID] = NULL;
	m_nTimerID = 0;
}

void Timer::SetTimer()
{
	KillTimer();
	
	if(!m_bIsEnabled)
		return;

	if(m_nTimerID)
		return;

	m_nTimerID = ::SetTimer(NULL, NULL, m_nInterval, TimerProc);
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
	pTimer-&gt;OnTick(&amp;eventArgs);
}
#pragma endregion


#pragma region Protected Method
void Timer::Reset(bool bIsInit)
{
	if(bIsInit)
	{
		_nTimerID	= 0;
	}

	__unhook(this);
	
	UnBindingEvent();
	
	_bIsEnabled	= false;
	_nInterval	= 0;

	if(_nTimerID)
	{
		KillTimer();
		_nTimerID = 0;
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
#pragma endregion</pre>
</div>
<p>
	 </p>
<p>
	使用上會像下面這樣，設定Timer的週期與是否啟用，並繫結事件處理常式做對應的處理。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:5a5c2a57-6b9e-4b70-9607-1e3348874358" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c" name="code">
// ConsoleApplication9.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"
#include &lt;Windows.h&gt;
#include "Timer.h"

class TestClass
{
public:
	Timer	m_Timer;
	int		m_nTickCount;

	TestClass()
	{
		m_nTickCount = 0;
		__hook(&amp;Timer::Tick, &amp;m_Timer, &amp;TestClass::Timer_Tick);
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

	while (testObj.m_nTickCount &lt; 10)
	{ 
		GetMessage(&amp;msg, NULL, 0, 0);
		TranslateMessage(&amp;msg); 
		DispatchMessage(&amp;msg);  
	} 
	return 0;
}</pre>
</div>
<p>
	 </p>
<p>
	運行後可每秒寫出一個Timer_Tick的字串，運行十秒後結束。</p>
<p>
	<img alt="image" border="0" height="303" src="\images\posts\52502\image_thumb.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="321" /></p>
