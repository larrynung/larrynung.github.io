---
title: "[C++]C++ Simple Lazy class"
date: "2011-09-28 09:41:37"
description: "[C++]C++ Simple Lazy class"
tags: [C++]
---

<p>
	延遲載入是程式寫作時很重要的一個概念，能讓物件要用在建立，避免不必要的運算。這篇簡單示範一下如何使用VC++ 2010以後的Lambda表示式撰寫C++版本的Lazy類別，透過std::function與template搭配使用，可以將lambda或是Callback Function儲存，當物件要建立時再透過剛儲存的初始動作執行。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:22b9071d-fefe-4ce7-a070-89a83deffb4d" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c" name="code">
#include &lt;functional&gt;

template&lt;class T&gt;
class Lazy
{
#pragma region Var
private:
	std::function&lt;T (void)&gt;		_func;
	T							_result;
	bool						_bIsValueCreated;
#pragma endregion


	
#pragma region Private Property
private:
	__declspec(property(get=Get_func,put=Set_func))
		std::function&lt;T (void)&gt; m_func;
#pragma endregion

	
	
#pragma region Public Property
public:
	__declspec(property(get=Get_result))
		T m_result;

	__declspec(property(get=Get_bIsValueCreated,put=Set_bIsValueCreated))
		bool m_bIsValueCreated;
#pragma endregion
	
	

#pragma region Constructor &amp; DeConstructor
public:		
	Lazy(std::function&lt;T (void)&gt; func)
	{
		Reset();
		m_func = func;
	}

	~Lazy(void)
	{
		Reset();
	}
#pragma endregion


	
#pragma region Property Process Method
private:
	inline std::function&lt;T (void)&gt; Get_func()
	{
		return _func;
	}

	inline void Set_func(std::function&lt;T (void)&gt; value)
	{
		_func = value;
	}

	inline void Set_bIsValueCreated(bool value)
	{
		_bIsValueCreated = value;
	}

public:
	inline T Get_result()
	{
		if(!m_bIsValueCreated)
		{
			Init();
		}
		return _result;
	}

	inline bool Get_bIsValueCreated()
	{
		return _result;
	}
#pragma endregion


#pragma region Protected Method
protected:
	void Reset()
	{
		_func				=	NULL;
		_result				=	NULL;
		_bIsValueCreated	=	false;
	}
#pragma endregion


#pragma region Public Method
public:
	void Init()
	{
		if(m_bIsValueCreated)
			return;
		_result = m_func();
		m_bIsValueCreated=true;
	}

	void ClearValue()
	{
		std::function&lt;T (void)&gt; func = m_func;
		Reset();
		m_func = func;
	}
#pragma endregion
};</pre>
</div>
<p>
	 </p>
<p>
	使用上像是下面這般，這邊示範的是將一個簡單的Lambda設給Lazy物件，Lambda裡面會做初始動作，這邊我以簡單的運算示意，透過Lazy.m_bIsValueCreated可以判斷是否已初始完成，而透過Lazy.m_result則是會做初始動作並將初始完的值回傳。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:a5713547-82d0-4d87-ad30-dcc783627cb1" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c" name="code">
int _tmain(int argc, _TCHAR* argv[])
{
	auto lazyObj = Lazy&lt;int&gt;([]()
	{
		return 1 + 2;
	});
	printf("IsValueCreated: %d
",lazyObj.m_bIsValueCreated);
	printf("Value: %d
",lazyObj.m_result);
	printf("IsValueCreated: %d
",lazyObj.m_bIsValueCreated);
	return 0;
}</pre>
</div>
<p>
	 </p>
<p>
	運行結果如下，可以看到一開始是未初始化的，當使用了Lazy.m_result才會做初始的動作，也才可以取到我們想要的值。</p>
<p>
	<img alt="image" border="0" height="191" src="\images\posts\38161\image_thumb.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="417" /></p>
