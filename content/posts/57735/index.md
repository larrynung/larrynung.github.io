---
title: "[C++]Monitor File System Changes with the ReadDirectoryChangesW API"
slug: "cpp-monitor-file-system-changes-with-the-readdirectorychangesw-api"
aliases: ["/posts/57735/"]
date: "2011-11-13 10:53:52"
description: "在C++中若想要監控檔案系統改變有很多方法，可以用FindFirstChangeNotification取得檔案變更、或是Hook底層的API等方法來實現，這邊使用ReadDirectoryChangesW API來實現，該API使用前必須先加入Kernel32.lib。"
tags: [C++]
---

在C++中若想要監控檔案系統改變有很多方法，可以用FindFirstChangeNotification取得檔案變更、或是Hook底層的API等方法來實現，這邊使用ReadDirectoryChangesW API來實現，該API使用前必須先加入Kernel32.lib。

![image_thumb.png](/images/posts/57735/image_thumb.png)

並加入Windows.h的標頭檔

```c
#include "Windows.h"
```

這些步驟做完後在程式中就可以看到ReadDirectoryChangesW API了，其函式原型如下：

```c
BOOL WINAPI ReadDirectoryChangesW(
  __in         HANDLE hDirectory,
  __out        LPVOID lpBuffer,
  __in         DWORD nBufferLength,
  __in         BOOL bWatchSubtree,
  __in         DWORD dwNotifyFilter,
  __out_opt    LPDWORD lpBytesReturned,
  __inout_opt  LPOVERLAPPED lpOverlapped,
  __in_opt     LPOVERLAPPED_COMPLETION_ROUTINE lpCompletionRoutine
);
```

該API必須帶入八個參數，hDirectory帶入的是要監控的目錄Handle、lpBuffer帶入的是用來回傳變動資料的空間、nBufferLength是lpBuffer空間的大小、bWatchSubtree是指定是否偵測子目錄、dwNotifyFilter是指定監控的目錄有哪些動作時需要通知、lpBytesReturned是用來回傳變動資料內含的長度、lpOverlapped可用來在非同步環境下使用重疊IO用、lpCompletionRoutine則是當監控完成或取消時所呼叫的回調函式。

其中dwNotifyFilter的值可設定的有FILE_NOTIFY_CHANGE_FILE_NAME、FILE_NOTIFY_CHANGE_DIR_NAME、FILE_NOTIFY_CHANGE_ATTRIBUTES、FILE_NOTIFY_CHANGE_SIZE、FILE_NOTIFY_CHANGE_LAST_WRITE、FILE_NOTIFY_CHANGE_LAST_ACCESS、FILE_NOTIFY_CHANGE_CREATION、與FILE_NOTIFY_CHANGE_SECURITY，詳細所代表的意義可參閱ReadDirectoryChangesW function。

了解了函式原型後，就可以開始進入實際的使用。剛有提到說在ReadDirectoryChangesW API函式必須要帶入的第一個參數是要監控的目錄Handle，所以我們必須透過CreateFile API取得要監控的目錄Handle，像是下面這樣：

```c
HANDLE  hDirectoryHandle	= NULL;

hDirectoryHandle = ::CreateFileA(
	file,
	FILE_LIST_DIRECTORY,
	FILE_SHARE_READ
	| FILE_SHARE_WRITE
	| FILE_SHARE_DELETE,
	NULL,
	OPEN_EXISTING,
	FILE_FLAG_BACKUP_SEMANTICS
	| FILE_FLAG_OVERLAPPED,
	NULL);

if(hDirectoryHandle == INVALID_HANDLE_VALUE)
	return;
```

取得監控的目錄Handle後，將其帶入ReadDirectoryChangesw API，順帶帶入像是回傳變動資料的Buffer空間、與要監控的變動類型等必要參數。像是下面這樣：

```c
int		nBufferSize			= 1024;
char*	buffer				= new char[nBufferSize];
DWORD dwBytes = 0;

memset(buffer, 0, nBufferSize);

if(!::ReadDirectoryChangesW(
	hDirectoryHandle,
	buffer,
	nBufferSize,
	bIncludeSubdirectories,
	FILE_NOTIFY_CHANGE_LAST_WRITE | FILE_NOTIFY_CHANGE_CREATION | FILE_NOTIFY_CHANGE_FILE_NAME,
	&dwBytes,
	NULL,
	NULL) || GetLastError() == ERROR_INVALID_HANDLE)
{
	break;
}

if(!dwBytes)
{
	printf("Buffer overflow~~\r\n");
}
```

這邊需注意到的是，若是變動的資料太多，提供的存儲空間不足以存放時，回傳的變動資料長度會是0，此時所有變動資料都會丟失。這樣的情況多半只會出在一瞬間大量的變動，可以增大存儲空間或是減少監控的變動類型，以減少回傳的資料量，避免溢位的發生。

若是運行沒發生問題，變動的資料會存放在當初塞進去的存儲空間，該空間的資料其實是FILE_NOTIFY_INFORMATION structure的型態存在，因此我們可將存儲空間的資料轉換成PFILE_NOTIFY_INFORMATION。裡面的Action是我們所關注的變動類型，FileName是變動的檔案名稱，檔案名稱的部分是沒有結尾符號的，必須要搭配FileNameLength去截取。另外變動的資料有時候不止一筆，因此我們必須在這邊用迴圈搭配NextEntryOffset去重覆運行處理流程，處理所有變動的資料。

```c
PFILE_NOTIFY_INFORMATION record = (PFILE_NOTIFY_INFORMATION)buffer;
DWORD cbOffset = 0;

do
{
	switch (record->Action)
	{
	case FILE_ACTION_ADDED:
		printf("FILE_ACTION_ADDED:");
		break;
	case FILE_ACTION_REMOVED:
		printf("FILE_ACTION_REMOVED:");
		break;
	case FILE_ACTION_MODIFIED:
		printf("FILE_ACTION_MODIFIED:");
		break;
	case FILE_ACTION_RENAMED_OLD_NAME:
		printf("FILE_ACTION_RENAMED_OLD_NAME:");
		break;

	case FILE_ACTION_RENAMED_NEW_NAME:
		printf("FILE_ACTION_RENAMED_NEW_NAME:");
		break;

	default:
		break;
	}

	char fileBuffer[512];

	WideCharToMultiByte(CP_ACP, 0, record->FileName, record->FileNameLength, fileBuffer, record->FileNameLength, NULL, NULL);
	printf(fileBuffer);
	printf("\r\n");

	cbOffset = record->NextEntryOffset;
	record = (PFILE_NOTIFY_INFORMATION)((LPBYTE) record + cbOffset);
}while(cbOffset);
```

這邊示範一個簡易的使用範例，實際使用時最好還是搭配執行緒處理：

```c
// ConsoleApplication10.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "Windows.h"

void MonitorDir(char* file, bool bIncludeSubdirectories = false)
{
	int		nBufferSize			= 1024;
	char*	buffer				= new char[nBufferSize];
	HANDLE  hDirectoryHandle	= NULL;

	hDirectoryHandle = ::CreateFileA(
		file,
		FILE_LIST_DIRECTORY,
		FILE_SHARE_READ
		| FILE_SHARE_WRITE
		| FILE_SHARE_DELETE,
		NULL,
		OPEN_EXISTING,
		FILE_FLAG_BACKUP_SEMANTICS
		| FILE_FLAG_OVERLAPPED,
		NULL);

	if(hDirectoryHandle == INVALID_HANDLE_VALUE)
		return;

	while(1)
	{
		DWORD dwBytes = 0;

		memset(buffer, 0, nBufferSize);

		if(!::ReadDirectoryChangesW(
			hDirectoryHandle,
			buffer,
			nBufferSize,
			bIncludeSubdirectories,
			FILE_NOTIFY_CHANGE_LAST_WRITE | FILE_NOTIFY_CHANGE_CREATION | FILE_NOTIFY_CHANGE_FILE_NAME,
			&dwBytes,
			NULL,
			NULL) || GetLastError() == ERROR_INVALID_HANDLE)
		{
			break;
		}

		if(!dwBytes)
		{
			printf("Buffer overflow~~\r\n");
		}

		PFILE_NOTIFY_INFORMATION record = (PFILE_NOTIFY_INFORMATION)buffer;
		DWORD cbOffset = 0;

		do
		{
			switch (record->Action)
			{
			case FILE_ACTION_ADDED:
				printf("FILE_ACTION_ADDED:");
				break;
			case FILE_ACTION_REMOVED:
				printf("FILE_ACTION_REMOVED:");
				break;
			case FILE_ACTION_MODIFIED:
				printf("FILE_ACTION_MODIFIED:");
				break;
			case FILE_ACTION_RENAMED_OLD_NAME:
				printf("FILE_ACTION_RENAMED_OLD_NAME:");
				break;

			case FILE_ACTION_RENAMED_NEW_NAME:
				printf("FILE_ACTION_RENAMED_NEW_NAME:");
				break;

			default:
				break;
			}

			char fileBuffer[512];

			WideCharToMultiByte(CP_ACP, 0, record->FileName, record->FileNameLength, fileBuffer, record->FileNameLength, NULL, NULL);
			printf(fileBuffer);
			printf("\r\n");

			cbOffset = record->NextEntryOffset;
			record = (PFILE_NOTIFY_INFORMATION)((LPBYTE) record + cbOffset);
		}while(cbOffset);
	}

	delete buffer;

	if(hDirectoryHandle)
		CloseHandle(hDirectoryHandle);
}

int _tmain(int argc, _TCHAR* argv[])
{
	MonitorDir("C:\\Users\\larry\\Desktop\\新增資料夾");
	return 0;
}
```

運行後去對監控的目錄操作~可得到類似如下的結果：

![image3_thumb.png](/images/posts/57735/image3_thumb.png)

## Link

* ReadDirectoryChangesW function
* Obtaining Directory Change Notifications
