---
title: ".NET 4.0 New Feature - Corrupted State Exceptions(CSEs)"
date: "2011-01-25 12:45:08"
description: "在.NET 4.0 以前的例外處理機制，開發人員能透過Try...Catch將所有例外攔截，也許是用來做一致性的例外處理、也許是將例外吞掉。不論是哪種狀況我們都可以藉由例外處理機制攔截到所有的例外。"
tags: [CSharp]
---

在.NET 4.0 以前的例外處理機制，開發人員能透過Try...Catch將所有例外攔截，也許是用來做一致性的例外處理、也許是將例外吞掉。不論是哪種狀況我們都可以藉由例外處理機制攔截到所有的例外。

```csharp
try
{
	...
}catch (Exception e)
{
	...
}
```

而.NET 4.0以後，可能有人會發現程式會截取不到某些的例外， 那是因為在.NET 4.0以後微軟對於例外機制有做了些許的調整，會將native code的例外，像是EXCEPTION_ACCESS_VIOLATION、EXCEPTION_STACK_OVERFLOW、EXCEPTION_ILLEGAL_INSTRUCTION、EXCEPTION_IN_PAGE_ERROR、EXCEPTION_INVALID_DISPOSITION、EXCEPTION_NONCONTINUABLE_EXCEPTION、EXCEPTION_PRIV_INSTRUCTION、STATUS_UNWIND_CONSOLIDATE...等，又或是由CLR發出的較為嚴重的例外，在.NET 4.0都會將其標示為Corrupted State Exceptions，這種例外在.NET 4.0以後會由CLR自行處理，而不會再像以往一般交由程式人員去處理。

當然微軟還是有保留彈性讓開發人員採用以前的處理方式，一種是透過在App.Config設定legacyCorruptedState­­ExceptionsPolicy元素來指定整個專案要遵尋以往的運行模式，像是下面這樣：

```xml
<configuration>
    <runtime>
        <legacyCorruptedStateExceptionsPolicy enabled="true"/>
    </runtime>
</configuration>
```

另一種則是透過.NET 4.0新的System.Runtime.ExceptionServices命名空間內的HandleProcessCorruptedStateExceptionsAttribute屬性來處理，可指定特定方法使用先前運作模式。

```csharp
[HandledProcessCorruptedStateExceptions]
public static int Main()
{
	try
	{
		...
	}catch (Exception e)
	{
		...
	}
}
```

## Link

* All about Corrupted State Exceptions in .NET4
* Handling Corrupted State Exceptions
* CLR 4.0: Corrupted State Exceptions
* .NET 4.0新特性-- Corrupted State Exceptions
* CLR 4.0: Corrupted State Exceptions
* <legacyCorruptedStateExceptionsPolicy> Element
* HandleProcessCorruptedStateExceptionsAttribute Class
