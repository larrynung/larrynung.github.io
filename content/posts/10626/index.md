---
title: "C++/CLI索引子"
date: "2009-09-15 09:02:41"
description: "C++/CLI在撰寫索引子時，寫法跟屬性大同小異。不同的是，索引子須使用default關鍵字取代屬性名稱。就像： 完整範例"
tags: [C++]
---

C++/CLI在撰寫索引子時，寫法跟屬性大同小異。不同的是，索引子須使用default關鍵字取代屬性名稱。就像：

```c
property int default[int]
{
	int get(int idx)
	{
		return _ary[idx];
	}
	void set(int idx,int value)
	{
		_ary[idx]=value;
	}
}
```

## 完整範例

```c
ref class ArrayClass
{
private:
	int* _ary;
public:
	property int default[int]
	{
		int get(int idx)
		{
			return _ary[idx];
		}
		void set(int idx,int value)
		{
			_ary[idx]=value;
		}
	}
public:
	ArrayClass()
	{
		_ary = new int[1024];
	}
};

int _tmain(int argc, _TCHAR* argv[])
{
	ArrayClass a;
	for (int i=0;i<1024;++i){
		a[i]=i;
	}
	return 0;
}
```
