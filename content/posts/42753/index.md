---
title: "[C++]C++ Nativated Property With Event Code Snippet"
date: "2011-10-14 12:47:10"
description: "[C++]C++ Nativated Property With Event Code Snippet"
tags: [C++]
---

筆者在[C++]C++ Nativated Property Code Snippet這篇整理過了Nativated Property的程式碼片斷，但只是便於建立很單純的屬性，若要在屬性中觸發事件就必須要自己下去處理。這邊筆者也稍微將這樣的需求整理一下，程式碼片段的XML內容如下：

```

<?xml version="1.0" encoding="utf-8"?>
<CodeSnippets>
<CodeSnippet Format="1.0.0">
<Header>
<Title>Nativated Property With Event</Title>
<Shortcut>npropwe</Shortcut>
<Description>Nativated Property with event trigger</Description>
<Author>Larry Nung</Author>
<SnippetTypes>
<SnippetType>Expansion</SnippetType>
</SnippetTypes>
</Header>
<Snippet>
<Declarations>
<Literal>
<ID>type</ID>
<ToolTip>Type of property</ToolTip>
<Default>int</Default>
</Literal>
<Literal Editable="true">
<ID>field</ID>
<Type></Type>
<ToolTip></ToolTip>
<Default>nValue</Default>
<Function></Function>
</Literal>
<Literal Editable="true">
<ID>eventArgs</ID>
<Type></Type>
<ToolTip></ToolTip>
<Default>EventArgs</Default>
<Function></Function>
</Literal>
</Declarations>
<Code Language="Cpp"><![CDATA[#pragma region Var
private:
$type$ _$field$;
#pragma endregion

#pragma region Public Property
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
On$field$Changing(&e);

_$field$ = value;

On$field$Changed(&e);
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

]]></Code>
</Snippet>
</CodeSnippet>
</CodeSnippets>
```

使用上在編譯視窗內輸入npropwe，連按兩次[Tab]按鍵就可以了。跑出的程式碼片段會像下面這樣，可以調整屬性的型態、名稱、與事件傳遞的參數型態。

```

#pragma region Var
private:
int _nValue;
#pragma endregion

#pragma region Public Property
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
OnnValueChanging(&e);

_nValue = value;

OnnValueChanged(&e);
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

```