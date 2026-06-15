---
title: "[C++]使用TinyXml讀寫Xml"
date: "2011-12-04 03:29:27"
description: "[C++]使用TinyXml讀寫Xml"
tags: [C++]
---
在C++讀寫XML並不像在.NET一般容易，常看到的方法若不是自己解析，就是用MSXml或是TinyXml下去處理，這邊簡單的紀錄一下TinyXml的用法。

自網站下載完TinyXml後解壓縮後，我們可以看到裡面會有tinystr.cpp、tinystr.h、tinyxml.cpp、tinyxml.h、tinyxmlerror.cpp、與tinyxmlparser.cpp這六個檔案，TinyXml主要就是用這六個檔案。

將這六個檔案加入專案中，並在cpp檔前加入#include "stdafx"，將Precompile header加入 。

在要使用到TinyXml的地方加入tinyxml.h與tinystr.h兩個必要的標頭檔，就可以開始使用了。

#include "tinyxml.h"
#include "tinystr.h"

TinyXml內含TiXmlBase、TiXmlNode、TiXmlDocument、TiXmlElement、TiXmlComment、TiXmlDeclaration、TiXmlText、TiXmlUnknown、TiXmlAttribute這幾個重要的類別，從命名就可以大致了解他們的用途，像是TiXmlDocument表示Xml文件、TiXmlElement是Xml元素節點、TiXmlComment是Xml中的註解、TiXmlAttribute是Xml節點的屬性。

在寫入Xml時，首先必須建立TiXmlDocument，為其加入TiXmlElement、TiXmlText與其它的Xml節點元素，再叫用SaveFile方法帶入Xml檔案位置就可以了。

void SaveXml(Person* person, string file)
{
TiXmlDocument xmlDoc;

TiXmlNode* rootElement = xmlDoc.InsertEndChild(TiXmlElement("Person"));

rootElement
->InsertEndChild(TiXmlElement("Name"))
->InsertEndChild(TiXmlText(person->m_sName.c_str()));

rootElement
->InsertEndChild(TiXmlElement("NickName"))
->InsertEndChild(TiXmlText(person->m_sNickName.c_str()));

char buffer[256];
_itoa(person->m_nAge, buffer,10);
rootElement
->InsertEndChild(TiXmlElement("Age"))
->InsertEndChild(TiXmlText(buffer));

xmlDoc.SaveFile(file.c_str());
}

讀取Xml時，一樣是要先建立TiXmlDocument物件，在建構時帶入Xml檔案位置，再叫用LoadFile將檔案讀入。讀入Xml後若讀取有問題，我們可叫用ErrorId判斷是否有錯誤發生，若取得的ErrorId大於0，可再叫用ErrorDesc去判斷發生的錯誤是甚麼。若Xml讀取沒問題的話可接著解析Xml的內容，透過RootElement可取得Xml的根節點，FirstChildElement可取得Xml子節點，NextSibling可用來取得Xml的兄弟節點，取得了Xml節點後透過GetText方法就可以得到Xml節點的內容。像是下面這樣：

void LoadXml(string file, Person* person)
{
TiXmlDocument xmlDoc(file.c_str());

xmlDoc.LoadFile();

if(xmlDoc.ErrorId() > 0)
return;

TiXmlElement* pRootElement = xmlDoc.RootElement();

if(!pRootElement)
return;

TiXmlElement* pNode = NULL;

pNode = pRootElement->FirstChildElement("Name");
if(pNode)
{
person->m_s>GetText();
}

pNode = pRootElement->FirstChildElement("NickName");
if(pNode)
{
person->m_sNick>GetText();
}

pNode = pRootElement->FirstChildElement("Age");
if(pNode)
{
person->m_nAge = atoi(pNode->GetText());
}
}

完整的程式範例如下：

// ConsoleApplication11.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include
#include "tinyxml.h"
#include "tinystr.h"

using namespace std;

class Person
{
public:
string m_sName;
string m_sNickName;
int m_nAge;
};

void SaveXml(Person* person, string file)
{
TiXmlDocument xmlDoc;

TiXmlNode* rootElement = xmlDoc.InsertEndChild(TiXmlElement("Person"));

rootElement
->InsertEndChild(TiXmlElement("Name"))
->InsertEndChild(TiXmlText(person->m_sName.c_str()));

rootElement
->InsertEndChild(TiXmlElement("NickName"))
->InsertEndChild(TiXmlText(person->m_sNickName.c_str()));

char buffer[256];
_itoa(person->m_nAge, buffer,10);
rootElement
->InsertEndChild(TiXmlElement("Age"))
->InsertEndChild(TiXmlText(buffer));

xmlDoc.SaveFile(file.c_str());
}

void LoadXml(string file, Person* person)
{
TiXmlDocument xmlDoc(file.c_str());

xmlDoc.LoadFile();

if(xmlDoc.ErrorId() > 0)
return;

TiXmlElement* pRootElement = xmlDoc.RootElement();

if(!pRootElement)
return;

TiXmlElement* pNode = NULL;

pNode = pRootElement->FirstChildElement("Name");
if(pNode)
{
person->m_s>GetText();
}

pNode = pRootElement->FirstChildElement("NickName");
if(pNode)
{
person->m_sNick>GetText();
}

pNode = pRootElement->FirstChildElement("Age");
if(pNode)
{
person->m_nAge = atoi(pNode->GetText());
}
}

int _tmain(int argc, _TCHAR* argv[])
{
string file = "Person.xml";

Person Larry;
Larry.m_s;
Larry.m_sNick;
Larry.m_nAge = 30;

SaveXml(&Larry, file);

Person NewLarry;

LoadXml(file, &NewLarry);

printf("Name: %s
", NewLarry.m_sName.c_str());
printf("NickName: %s
", NewLarry.m_sNickName.c_str());
printf("Age: %d
", NewLarry.m_nAge);

return 0;
}

範例運行後會產生個Xml，內容像下面這般：

Xml的資料也能正常的解析。

TinyXml使用上算是比較不複雜的，但是卻有個很麻煩的問題，就是轉碼的動作必須自己處理，若不經轉換可能會有亂碼的問題，網路上有些文章就是專門在討論這樣的問題。另外，它的Xml存檔格式是用ANSI的格是下去儲存，若是要以UTF-8去儲存，必須修改tinyxml的程式碼，直接搜尋程式找到useMicrosoftBOM，將這值設為true就可以了。

這邊筆者為了方便使用，有將TinyXml包成類似.NET的XmlWriter類別，存取Xml的部分就會變得像下面這樣：

void SaveXml(Person* person, string file)
{
XmlWriter xw(file);

xw
.WriteStartElement("Person")
.WriteElementValue("Name", person->m_sName)
.WriteElementValue("NickName", person->m_sNickName)
.WriteElementValue("Age", person->m_nAge)
.WriteEndElement()
.Close();
}

程式碼分享於下方，有需要的自行取用。

XmlWriter.h

#pragma once
#include
#include
#include "tinyxml.h"
#include "tinystr.h"

using namespace std;
class XmlWriter
{
#pragma region Const
private:
#define DEFAULT_BUFFER_SIZE 512
#pragma endregion

#pragma region Var
private:
char m_cBuffer[DEFAULT_BUFFER_SIZE];
string _sFile;
TiXmlDocument _XmlDoc;
stack _StartNodes;
#pragma endregion

#pragma region Private Property
private:
__declspec(property(get=Get_sFile,put=Set_sFile))
string m_sFile;

__declspec(property(get=Get_XmlDoc,put=Set_XmlDoc))
TiXmlDocument& m_XmlDoc;

__declspec(property(get=Get_StartNodes))
stack& m_StartNodes;

__declspec(property(get=Get_pCurrentNode,put=Set_pCurrentNode))
TiXmlNode* m_pCurrentNode;
#pragma endregion

#pragma region Constructor & DeConstructor
public:
XmlWriter(string file);
~XmlWriter(void);
#pragma endregion

#pragma region Property Process Method
private:
inline string Get_sFile()
{
return _sFile;
}

inline void Set_sFile(string value)
{
if(_sFile == value)
return;

_sFile = value;
}

inline TiXmlDocument& Get_XmlDoc()
{
return _XmlDoc;
}

inline void Set_XmlDoc(TiXmlDocument& value)
{
_XmlDoc = value;
}

inline TiXmlNode* Get_pCurrentNode()
{
if(m_StartNodes.empty())
{
return &m_XmlDoc;
}
return m_StartNodes.top();
}

inline stack& Get_StartNodes()
{
return _StartNodes;
}
#pragma endregion

#pragma region Protected Method
protected:
void Reset();
#pragma endregion

#pragma region Public Method
public:
XmlWriter& WriteStartElement(string localName);
XmlWriter& WriteEndElement();
XmlWriter& WriteElementValue(string localName, const char* value);
XmlWriter& WriteElementValue(string localName, string value);
XmlWriter& WriteElementValue(string localName, int value);
void Close();
#pragma endregion
};

XmlWriter.cpp

#include "stdafx.h"
#include "XmlWriter.h"

#pragma region Constructor & DeConstructor
XmlWriter::XmlWriter(string file)
{
Reset();
m_sFile = file;
}

XmlWriter::~XmlWriter(void)
{
Reset();
}
#pragma endregion

#pragma region Protected Method
void XmlWriter::Reset()
{
_sFile = "";
_XmlDoc.Clear();
}
#pragma endregion

#pragma region Public Method
XmlWriter& XmlWriter::WriteStartElement(string localName)
{
m_StartNodes.push(m_pCurrentNode->InsertEndChild(TiXmlElement(localName.c_str())));

return *this;
}

XmlWriter& XmlWriter::WriteEndElement()
{
if(!m_StartNodes.empty())
m_StartNodes.pop();

return *this;
}

XmlWriter& XmlWriter::WriteElementValue(string localName, const char* value)
{
m_pCurrentNode
->InsertEndChild(TiXmlElement(localName.c_str()))
->InsertEndChild(TiXmlText(value));

return *this;
}

XmlWriter& XmlWriter::WriteElementValue(string localName, string value)
{
return WriteElementValue(localName, value.c_str());
}

XmlWriter& XmlWriter::WriteElementValue(string localName, int value)
{
_itoa(value, m_cBuffer,10);
return WriteElementValue(localName, m_cBuffer);
}

void XmlWriter::Close()
{
m_XmlDoc.SaveFile(m_sFile.c_str());
Reset();
}
#pragma endregion

##
Link

TinyXml Main Page

TinyXml Documentation

TinyXml Project Page

TinyXML - 小巧好用的 XML parser

TinyXML Tutorial 中文指南