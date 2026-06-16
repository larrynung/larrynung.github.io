---
title: "[C++]C++ Create GUID"
date: "2011-10-13 01:24:27"
description: "在C++中若有建立GUID的需求，可先建立GUID的物件實體，透過CoCreateGuid API填寫GUID到GUID的物件實體，再透過UuidToString API將GUID轉為字元陣列，像是下面這樣： 完整的範例如下： 運行起來會像下面這樣： 若建置時Link不過，"
tags: [C++]
---

在C++中若有建立GUID的需求，可先建立GUID的物件實體，透過CoCreateGuid API填寫GUID到GUID的物件實體，再透過UuidToString API將GUID轉為字元陣列，像是下面這樣：

```c
wstring GetGUID()
{
	_TUCHAR *guidStr = NULL;

	GUID *pguid = new GUID;

	CoCreateGuid(pguid);

	// Convert the GUID to a string
	UuidToString(pguid, (RPC_WSTR*)&guidStr);
	delete pguid;
	return wstring(guidStr);
}
```

完整的範例如下：

```c
// ConsoleApplication5.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <objbase.h>
#include <string>

using namespace std;

wstring GetGUID()
{
	_TUCHAR *guidStr = NULL;

	GUID *pguid = new GUID;

	CoCreateGuid(pguid);

	// Convert the GUID to a string
	UuidToString(pguid, (RPC_WSTR*)&guidStr);
	delete pguid;
	return wstring(guidStr);
}

int _tmain(int argc, _TCHAR* argv[])
{
	wstring guid = GetGUID();
	wprintf(guid.c_str());
	return 0;
}
```

運行起來會像下面這樣：

![image_thumb.png](/images/posts/42376/image_thumb.png)

若建置時Link不過，可以檢查一下Additional Dependencies設定，需確保Rpcrt4.lib與Ole32.lib有設定在裡面，詳細的可參閱MSDN說明。

![image_thumb_1.png](/images/posts/42376/image_thumb_1.png)

## Link

* CoCreateGuid function
* UuidToString function
