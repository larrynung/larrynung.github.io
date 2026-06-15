---
title: "[VC.NET] 如何修復 quot;C2039: lsquo;GetCurrentDirectoryA()rsquo; : is Not a Member of lsquo;System::IO::Directoryrsquo;quot;問題"
date: "2009-10-03 12:57:56"
description: "[VC.NET] 如何修復 \"C2039: ‘GetCurrentDirectoryA()’ : is Not a Member of ‘System::IO::Directory’\"問題"
tags: [C++]
---

看到論壇上有人問到如何處理這樣的問題。看了一下前輩的回應後才發現，原來這樣的問題是由於Windows.h檔案內，已定義了GetCurrentDirectory這個巨集所導致。該巨集會在編譯時把GetCurrentDirectory給改為GetCurrentDirectoryA或是GetCurrentDirectoryW。

```c
#if UNICODE
#define GetCurrentDirectory GetCurrentDirectorryW
#else
#define GetCurrentDirectory GetCurrentDirectorryA
#endif
```

因此使用類似下面的程式，在編譯時就會發生錯誤。

```c
#include "stdafx.h"
#include <windows.h>
using namespace System;
using namespace System::IO;

int main(array<System::String ^> ^args)
{
	Console::WriteLine(L"Dir: "+System::IO::Directory::GetCurrentDirectory()); // Error!
    return 0;
}
```

錯誤訊息
![image_thumb.png](/images/posts/10899/image_thumb.png)

解決辦法可利用#undef去把該巨集給取消。

```c
#undef GetCurrentDirectory
```

像是

```c
#include "stdafx.h"
#include <windows.h>
using namespace System;
using namespace System::IO;

#undef GetCurrentDirectory

int main(array<System::String ^> ^args)
{
	Console::WriteLine(L"Dir: "+System::IO::Directory::GetCurrentDirectory());
    return 0;
}
```

## Link

* How to Fix – "C2039: ‘GetCurrentDirectoryA()’ : is Not a Member of ‘System::IO::Directory’"
