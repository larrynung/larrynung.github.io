---
title: "[C++]C++ Nativated Property Code Snippet"
date: "2011-10-13 12:39:34"
description: "[C++]C++ Nativated Property Code Snippet"
tags: [C++]
---Visual Studio 2011 Preview開始支援C++的Code Snippet，開發人員可以將自己常用的功能寫成Code Snippet加速專案的開發。由於筆者在開發Nativated C++時，常會需要撰寫Nativated Property，故將其整理為Code Snippet，Code Snippet內容如下：

```

<?xml version="1.0" encoding="utf-8"?>
<CodeSnippets>
<CodeSnippet Format="1.0.0">
<Header>
<Title>Nativated Property</Title>
<Shortcut>nprop</Shortcut>
<Description>Nativated Property</Description>
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

_$field$ = value;
}
#pragma endregion]]></Code>
</Snippet>
</CodeSnippet>
</CodeSnippets>
```

將其複製下來存至 [My Documents]\Visual Studio 11\Code Snippets\Visual C++\My Code Snippets 下，副檔名為snippet。

![](/images/posts/42366/)

放置好後可叫出Code Snippets Manager查看。

![](/images/posts/42366/)

剛剛手動加入的Code Snippet應該可在Code Snippets Manager看到。

![](/images/posts/42366/)

使用上在編譯視窗內輸入nprop，連按兩次[Tab]按鍵。

![](/images/posts/42366/)

Nativated Property的程式碼片斷就會輸入到編輯區中，再針對屬性的型態、屬性的名稱做些調整就可以了。

![](/images/posts/42366/)