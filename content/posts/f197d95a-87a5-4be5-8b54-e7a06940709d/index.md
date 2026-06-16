---
title: "C++_CLI Managed 與 Nativated 型態互轉"
date: "2013-11-06 12:00:00"
tags: [C++]
description: "CString -> System::String^ System::String^ -> CString System::String^ -> int"
---

1. CString -> System::String^

   ```c
CString strNativedMsg = _T("Test");
System::String^ strManagedMsg = %System::String(strNativedMsg);
```
2. System::String^ -> CString

   ```c
System::String^ strManagedMsg = "Test";
CString strNativedMsg = (CString) strManagedMsg ;
```
3. System::String^ -> int

   ```c
System::String^ strManagedNumber = "123";
int nNativatedNumber = System::Convert::ToInt32(strManagedNumber );
```
