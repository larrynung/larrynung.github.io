---
title: "C++/CLI Managed Natived語法對應"
date: "2009-09-18 09:00:15"
description: "C++/CLI Managed Natived語法對應"
tags: [C++]
---

Natived
 			
Managed
Pointer
```cpp
NativedClass* obj = new NativedClass();
```

```cpp
ManagedClass^ obj = gcnew ManagedClass();
```
Call By Reference
```cpp
void Method(int& value)
{
}
```

```cpp
void Method(int% value)
{
}
```
Enum
```cpp
enum
{	
    Element1,
    Element2
};
```

```cpp
enum class EnumName
{	
    Element1,
    Element2
};
```
Class
```cpp
class ClassName
{
};
```

```cpp
ref class ClassName
{
};
```
Struct
```cpp
struct StructName
{
    int m_nElement1;
}
```

```cpp
ref struct StructName
{
    int m_nElement1;
}
```
Property
```cpp
private:
	bool _propertyValue;
public:
	__declspec(property(get=GetPropertyValue,put=SetPropertyValue))
		bool m_propertyValue;
public:
	void SetPropertyValue(bool value)
	{
		_propertyValue = value;
	}
	bool GetPropertyValue()
	{
		return _propertyValue;
	}
```

```cpp
private:
	System::Boolean _propertyValue;
public:
	property System::Boolean PropertyValue
	{
		System::Boolean get()
		{
			return _propertyValue;
		}
		void set(System::Boolean value)
		{
			_propertyValue = value;
		}
	}
```

void Method(int% value)
{
}

Enum

enum
{	
    Element1,
    Element2
};

enum class EnumName
{	
    Element1,
    Element2
};

Class

class ClassName
{
};

ref class ClassName
{
};

Struct

struct StructName
{
    int m_nElement1;
}

ref struct StructName
{
    int m_nElement1;
}

Property

private:
bool _propertyValue;
public:
__declspec(property(get=GetPropertyValue,put=SetPropertyValue))
bool m_propertyValue;
public:
void SetPropertyValue(bool value)
{
_propertyValue = value;
}
bool GetPropertyValue()
{
return _propertyValue;
}

private:
System::Boolean _propertyValue;
public:
property System::Boolean PropertyValue
{
System::Boolean get()
{
return _propertyValue;
}
void set(System::Boolean value)
{
_propertyValue = value;
}
}