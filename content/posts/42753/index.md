---
title: "[C++]C++ Nativated Property With Event Code Snippet"
date: "2011-10-14 12:47:10"
description: "[C++]C++ Nativated Property With Event Code Snippet"
tags: [C++]
---

<p>
	筆者在[C++]C++ Nativated Property Code Snippet這篇整理過了Nativated Property的程式碼片斷，但只是便於建立很單純的屬性，若要在屬性中觸發事件就必須要自己下去處理。這邊筆者也稍微將這樣的需求整理一下，程式碼片段的XML內容如下：</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:559e2dac-7cdb-4e3b-b702-d8e770e691a5" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="xml" name="code">
&lt;?xml version="1.0" encoding="utf-8"?&gt;
&lt;CodeSnippets xmlns="http://schemas.microsoft.com/VisualStudio/2005/CodeSnippet"&gt;
  &lt;CodeSnippet Format="1.0.0"&gt;
    &lt;Header&gt;
      &lt;Title&gt;Nativated Property With Event&lt;/Title&gt;
      &lt;Shortcut&gt;npropwe&lt;/Shortcut&gt;      
      &lt;Description&gt;Nativated Property with event trigger&lt;/Description&gt;
      &lt;Author&gt;Larry Nung&lt;/Author&gt;
      &lt;SnippetTypes&gt;
	&lt;SnippetType&gt;Expansion&lt;/SnippetType&gt;
      &lt;/SnippetTypes&gt;      
    &lt;/Header&gt;
    &lt;Snippet&gt;     
      &lt;Declarations&gt;
	&lt;Literal&gt;
	  &lt;ID&gt;type&lt;/ID&gt;
	  &lt;ToolTip&gt;Type of property&lt;/ToolTip&gt;
	  &lt;Default&gt;int&lt;/Default&gt;
	&lt;/Literal&gt;
        &lt;Literal Editable="true"&gt;
          &lt;ID&gt;field&lt;/ID&gt;
          &lt;Type&gt;&lt;/Type&gt;
          &lt;ToolTip&gt;&lt;/ToolTip&gt;
          &lt;Default&gt;nValue&lt;/Default&gt;
          &lt;Function&gt;&lt;/Function&gt;
        &lt;/Literal&gt;
        &lt;Literal Editable="true"&gt;
          &lt;ID&gt;eventArgs&lt;/ID&gt;
          &lt;Type&gt;&lt;/Type&gt;
          &lt;ToolTip&gt;&lt;/ToolTip&gt;
          &lt;Default&gt;EventArgs&lt;/Default&gt;
          &lt;Function&gt;&lt;/Function&gt;
        &lt;/Literal&gt;
      &lt;/Declarations&gt;
      &lt;Code Language="Cpp"&gt;&lt;![CDATA[#pragma region Var
private:
	$type$ _$field$;
#pragma endregion


#pragma region Public  Property
public:
	__declspec(property(get=Get_$field$,put=Set_$field$))
		$type$ m_$field$;
#pragma endregion



#pragma region Event
public:	
	__event void $field$Changing(void* sender, $eventArgs$* e);
	__event void $field$Changed(void* sender, $eventArgs$* e);
#pragma endregion



#pragma region Property Process Method
public:
	inline $type$ Get_$field$()
	{
		return _$field$;
	}

	inline void Set_$field$($type$ value)
	{
		if(_$field$ == value)
			return;

		$eventArgs$ e;
		On$field$Changing(&amp;e);

		_$field$ = value;

		On$field$Changed(&amp;e);
	}
#pragma endregion


#pragma region Protected Method
protected:
	void On$field$Changing($eventArgs$* e)
	{
		__raise $field$Changing(this, e);
	}

	void On$field$Changed($eventArgs$* e)
	{
		__raise $field$Changed(this, e);
	}
#pragma endregion

]]&gt;&lt;/Code&gt;
    &lt;/Snippet&gt;
  &lt;/CodeSnippet&gt;
&lt;/CodeSnippets&gt;</pre>
</div>
<p>
	 </p>
<p>
	使用上在編譯視窗內輸入npropwe，連按兩次[Tab]按鍵就可以了。跑出的程式碼片段會像下面這樣，可以調整屬性的型態、名稱、與事件傳遞的參數型態。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:05248321-d39d-4628-9497-54f30f03e411" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c" name="code">
#pragma region Var
private:
	int _nValue;
#pragma endregion


#pragma region Public  Property
public:
	__declspec(property(get=Get_nValue,put=Set_nValue))
		int m_nValue;
#pragma endregion



#pragma region Event
public:	
	__event void nValueChanging(void* sender, EventArgs* e);
	__event void nValueChanged(void* sender, EventArgs* e);
#pragma endregion



#pragma region Property Process Method
public:
	inline int Get_nValue()
	{
		return _nValue;
	}

	inline void Set_nValue(int value)
	{
		if(_nValue == value)
			return;

		EventArgs e;
		OnnValueChanging(&amp;e);

		_nValue = value;

		OnnValueChanged(&amp;e);
	}
#pragma endregion


#pragma region Protected Method
protected:
	void OnnValueChanging(EventArgs* e)
	{
		__raise nValueChanging(this, e);
	}

	void OnnValueChanged(EventArgs* e)
	{
		__raise nValueChanged(this, e);
	}
#pragma endregion
</pre>
</div>
