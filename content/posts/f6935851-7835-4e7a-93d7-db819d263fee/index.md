---
title: "[C++]使用GetAdaptersAddresses API取得本地IP"
date: "2013-11-06 12:00:00"
description: "[C++]使用GetAdaptersAddresses API取得本地IP"
---

最近有個需求必須在C++中取得本地的IP，包括IPv6與IPv4兩種的IP，查來查去就只有GetAdaptersAddresses API比較合用，但是使用上卻不是很容易，這篇將之稍做整理。

GetAdaptersAddresses API在使用時必須先將相關的函式庫與標頭擋設定好，必須設定靜態函式庫Iphlpapi.lib與Iphlpapi.h標頭擋，像是下面這樣，靜態函式庫若有需要也可以透過專案屬性設定。

...
#include
...
#pragma comment(lib, "IPHLPAPI.lib")

準備動作設定完成就可以使用GetAdaptersAddresses API了，但在使用前我們必須對GetAdaptersAddresses API的參數做些深入的了解，才會知道我們必須帶入哪些參數，這可以直接查閱API的函式原型：

ULONG WINAPI GetAdaptersAddresses(
__in ULONG Family,
__in ULONG Flags,
__in PVOID Reserved,
__inout PIP_ADAPTER_ADDRESSES AdapterAddresses,
__inout PULONG SizePointer
);

從函式原型中我們可以看出，GetAdaptersAddresses API必須帶入五個參數，前兩個參數是我們要設定的Flag，是要IPv4還是IPv6?是不是某些裝置要被忽略?或是提供一些相關的設定，第三個參數是系統保留的參數，固定帶NULL就可以了，第四個參數是問回來的網卡資訊，是我們主要要看的部分，而最後一個參數是空間大小，會回傳告知我們必須提供多少的記憶體空間。

第一個參數是用來決定感興趣的是IPv4還是IPv6的資訊，它能接受的Flag有下表列的這些，若帶入的是AF_UNSPEC代表IPv4跟IPv6都想要知道，帶入AF_INET代表只對IPv4感興趣，而帶入AF_INET6則是想查閱的只有IPv6。

Value

Meaning

AF_UNSPEC

0

Return both IPv4 and IPv6 addresses associated with adapters with IPv4 or IPv6 enabled.

AF_INET

2

Return only IPv4 addresses associated with adapters with IPv4 enabled.

AF_INET6

23

Return only IPv6 addresses associated with adapters with IPv6 enabled.

第二個參數可設定某些裝置要被忽略，或是提供一些相關的設定，像是可以設定忽略DNS Server的資訊等等，這邊不多做介紹，可直接參閱下表：

Value

Meaning

GAA_FLAG_SKIP_UNICAST

0x0001

Do not return unicast addresses.

GAA_FLAG_SKIP_ANYCAST

0x0002

Do not return IPv6 anycast addresses.

GAA_FLAG_SKIP_MULTICAST

0x0004

Do not return multicast addresses.

GAA_FLAG_SKIP_DNS_SERVER

0x0008

Do not return addresses of DNS servers.

GAA_FLAG_INCLUDE_PREFIX

0x0010

Return a list of IP address prefixes on this adapter. When this flag is set, IP address prefixes are returned for both IPv6 and IPv4 addresses.

This flag is supported on Windows XP with SP1 and later.

GAA_FLAG_SKIP_FRIENDLY_NAME

0x0020

Do not return the adapter friendly name.

GAA_FLAG_INCLUDE_WINS_INFO

0x0040

Return addresses of Windows Internet Name Service (WINS) servers.

This flag is supported on Windows Vista and later.

GAA_FLAG_INCLUDE_GATEWAYS

0x0080

Return the addresses of default gateways.

This flag is supported on Windows Vista and later.

GAA_FLAG_INCLUDE_ALL_INTERFACES

0x0100

Return addresses for all NDIS interfaces.

This flag is supported on Windows Vista and later.

GAA_FLAG_INCLUDE_ALL_COMPARTMENTS

0x0200

Return addresses in all routing compartments.

This flag is not currently supported and reserved for future use.

GAA_FLAG_INCLUDE_TUNNEL_BINDINGORDER

0x0400

Return the adapter addresses sorted in tunnel binding order. This flag is supported on Windows Vista and later.

在使用上通常習慣會呼叫兩次GetAdaptersAddresses API，第一次呼叫時會先將第四個參數帶NULL值，因為這次的叫用主要是要取得要多少的空間才夠存放網卡資訊，像下面這樣叫用需要的記憶體空間大小就會寫到最後一個參數。

ULONG outBufLen = 0;

GetAdaptersAddresses(AF_UNSPEC, 0, NULL, NULL, &outBufLen);

取得了所需的空間大小後，透過malloc指派足夠的記憶體，再次叫用GetAdaptersAddresses API取得網卡資訊：

PIP_ADAPTER_ADDRESSES pAddresses = (IP_ADAPTER_ADDRESSES*) malloc(outBufLen);

GetAdaptersAddresses(AF_UNSPEC, GAA_FLAG_SKIP_ANYCAST, NULL, pAddresses, &outBufLen);

取得了網卡資訊後，網卡資訊會是IP_ADAPTER_ADDRESSES structure的型態，以Linked List的方式存放，因此在取用時必須遍尋Linked List每個元素，取出我們需要的IP位置，其中比較麻煩的就是IP位置是以SOCKET_ADDRESS structure型態存放，要透過inet_ntop function轉換為字串，程式寫起來就像下面這樣：

...
char buff[100];
DWORD bufflen=100;
PIP_ADAPTER_ADDRESSES pCurrAddresses = NULL;
PIP_ADAPTER_UNICAST_ADDRESS pUnicast = NULL;
LPSOCKADDR addr = NULL;

pCurrAddresses = pAddresses;
while (pCurrAddresses)
{
if(pCurrAddresses->OperStatus != IfOperStatusUp)
{
pCurrAddresses = pCurrAddresses->Next;
continue;
}

pUnicast = pCurrAddresses->FirstUnicastAddress;
while (pUnicast)
{
addr = pUnicast->Address.lpSockaddr;
ZeroMemory(buff, bufflen);
if (addr->sa_family == AF_INET6)
{
sockaddr_in6 *sa_in6 = (sockaddr_in6 *)addr;
inet_ntop(AF_INET6, &(sa_in6->sin6_addr), buff, bufflen);
}else
{
sockaddr_in *sa_in = (sockaddr_in *)addr;
inet_ntop(AF_INET, &(sa_in->sin_addr), buff, bufflen);
}
localIPs.push_back(buff);
pUnicast = pUnicast->Next;
}

pCurrAddresses = pCurrAddresses->Next;
}

free(pAddresses);
...

最後附上完整的範例：

// Test_LocalIPs.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include
#include
#include
#include
#include
#include

// Link with Iphlpapi.lib
#pragma comment(lib, "Ws2_32.lib")
#pragma comment(lib, "IPHLPAPI.lib")

using namespace std;

vector GetLocalIPs()
{
vector localIPs;
PIP_ADAPTER_ADDRESSES pAddresses = NULL;
ULONG outBufLen = 0;

GetAdaptersAddresses(AF_UNSPEC, 0, NULL, pAddresses, &outBufLen);

pAddresses = (IP_ADAPTER_ADDRESSES*) malloc(outBufLen);

if (GetAdaptersAddresses(AF_UNSPEC, GAA_FLAG_SKIP_ANYCAST, NULL, pAddresses, &outBufLen) != NO_ERROR)
{
free(pAddresses);
return localIPs;
}

char buff[100];
DWORD bufflen=100;
PIP_ADAPTER_ADDRESSES pCurrAddresses = NULL;
PIP_ADAPTER_UNICAST_ADDRESS pUnicast = NULL;
LPSOCKADDR addr = NULL;

pCurrAddresses = pAddresses;
while (pCurrAddresses)
{
if(pCurrAddresses->OperStatus != IfOperStatusUp)
{
pCurrAddresses = pCurrAddresses->Next;
continue;
}

pUnicast = pCurrAddresses->FirstUnicastAddress;
while (pUnicast)
{
addr = pUnicast->Address.lpSockaddr;
ZeroMemory(buff, bufflen);
if (addr->sa_family == AF_INET6)
{
sockaddr_in6 *sa_in6 = (sockaddr_in6 *)addr;
inet_ntop(AF_INET6, &(sa_in6->sin6_addr), buff, bufflen);
}else
{
sockaddr_in *sa_in = (sockaddr_in *)addr;
inet_ntop(AF_INET, &(sa_in->sin_addr), buff, bufflen);
}
localIPs.push_back(buff);
pUnicast = pUnicast->Next;
}

pCurrAddresses = pCurrAddresses->Next;
}

free(pAddresses);
return localIPs;
}

int _tmain(int argc, _TCHAR* argv[])
{
vector localIPs = GetLocalIPs();
for_each (localIPs.begin(), localIPs.end(), [&](string ip)
{
char szTmp[255];
sprintf(szTmp, "%s
", ip.c_str());
printf(szTmp);
});
return 0;
}

運行後可得到像下面這樣的結果：

## Link


GetAdaptersAddresses function

IP_ADAPTER_ADDRESSES structure

IP_ADAPTER_UNICAST_ADDRESS structure

SOCKET_ADDRESS structure