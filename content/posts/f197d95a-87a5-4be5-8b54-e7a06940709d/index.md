---
title: "C++/CLI Converting Between Managed and Native Types"
slug: "cpp-cli-converting-between-managed-and-native-types"
aliases: ["/posts/f197d95a-87a5-4be5-8b54-e7a06940709d/"]
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
