---
title: "C++_CLI Managed 與 Nativated 型態互轉"
date: "2013-11-06 12:00:00"
description: "C++_CLI Managed 與 Nativated 型態互轉"
---

CString -> System::String^    

CString strNativedMsg = _T("Test");
System::String^ strManagedMsg = %System::String(strNativedMsg);

System::String^ -> CString

System::String^ strManagedMsg = "Test";
CString strNativedMsg = (CString) strManagedMsg ;

System::String^ -> int

System::String^ strManagedNumber = "123";
int nNativatedNumber = System::Convert::ToInt32(strManagedNumber );