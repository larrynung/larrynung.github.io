---
title: "[C++]使用TinyXml讀寫Xml"
date: "2011-12-04 03:29:27"
description: "[C++]使用TinyXml讀寫Xml"
tags: [C++]
---

<p>
	在C++讀寫XML並不像在.NET一般容易，常看到的方法若不是自己解析，就是用MSXml或是TinyXml下去處理，這邊簡單的紀錄一下TinyXml的用法。</p>
<p>
	 </p>
<p>
	自網站下載完TinyXml後解壓縮後，我們可以看到裡面會有tinystr.cpp、tinystr.h、tinyxml.cpp、tinyxml.h、tinyxmlerror.cpp、與tinyxmlparser.cpp這六個檔案，TinyXml主要就是用這六個檔案。</p>
<p>
	<img alt="image" border="0" height="484" src="\images\posts\60602\image_thumb.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="486" /></p>
<p>
	 </p>
<p>
	將這六個檔案加入專案中，並在cpp檔前加入#include "stdafx"，將Precompile header加入 。</p>
<p>
	<img alt="image" border="0" height="132" src="\images\posts\60602\image3_thumb.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="420" /></p>
<p>
	 </p>
<p>
	在要使用到TinyXml的地方加入tinyxml.h與tinystr.h兩個必要的標頭檔，就可以開始使用了。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:a9d8d4e6-ac61-420c-aa42-0a2623cb1777" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c" name="code">
#include "tinyxml.h"   
#include "tinystr.h"</pre>
</div>
<p>
	 </p>
<p>
	TinyXml內含TiXmlBase、TiXmlNode、TiXmlDocument、TiXmlElement、TiXmlComment、TiXmlDeclaration、TiXmlText、TiXmlUnknown、TiXmlAttribute這幾個重要的類別，從命名就可以大致了解他們的用途，像是TiXmlDocument表示Xml文件、TiXmlElement是Xml元素節點、TiXmlComment是Xml中的註解、TiXmlAttribute是Xml節點的屬性。</p>
<p>
	 </p>
<p>
	在寫入Xml時，首先必須建立TiXmlDocument，為其加入TiXmlElement、TiXmlText與其它的Xml節點元素，再叫用SaveFile方法帶入Xml檔案位置就可以了。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:71620bc5-9678-4718-8b64-bd36e94c294f" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c" name="code">
void SaveXml(Person* person, string file)
{	
	TiXmlDocument xmlDoc;

	TiXmlNode* rootElement = xmlDoc.InsertEndChild(TiXmlElement("Person"));

	rootElement
		-&gt;InsertEndChild(TiXmlElement("Name"))
		-&gt;InsertEndChild(TiXmlText(person-&gt;m_sName.c_str()));

	rootElement
		-&gt;InsertEndChild(TiXmlElement("NickName"))
		-&gt;InsertEndChild(TiXmlText(person-&gt;m_sNickName.c_str()));

	char buffer[256];
	_itoa(person-&gt;m_nAge, buffer,10);
	rootElement
		-&gt;InsertEndChild(TiXmlElement("Age"))
		-&gt;InsertEndChild(TiXmlText(buffer));

	xmlDoc.SaveFile(file.c_str());
}</pre>
</div>
<p>
	 </p>
<p>
	讀取Xml時，一樣是要先建立TiXmlDocument物件，在建構時帶入Xml檔案位置，再叫用LoadFile將檔案讀入。讀入Xml後若讀取有問題，我們可叫用ErrorId判斷是否有錯誤發生，若取得的ErrorId大於0，可再叫用ErrorDesc去判斷發生的錯誤是甚麼。若Xml讀取沒問題的話可接著解析Xml的內容，透過RootElement可取得Xml的根節點，FirstChildElement可取得Xml子節點，NextSibling可用來取得Xml的兄弟節點，取得了Xml節點後透過GetText方法就可以得到Xml節點的內容。像是下面這樣：</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:a2bf1dfb-8e3b-415b-9a63-ac02dd65bf6d" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c" name="code">
void LoadXml(string file, Person* person)
{	
	TiXmlDocument xmlDoc(file.c_str());

	xmlDoc.LoadFile();

	if(xmlDoc.ErrorId() &gt; 0)
		return;

	TiXmlElement* pRootElement = xmlDoc.RootElement();

	if(!pRootElement)
		return;

	TiXmlElement* pNode = NULL;
	
	pNode = pRootElement-&gt;FirstChildElement("Name");
	if(pNode)
	{
		person-&gt;m_sName = pNode-&gt;GetText();		
	}

	pNode = pRootElement-&gt;FirstChildElement("NickName");
	if(pNode)
	{
		person-&gt;m_sNickName = pNode-&gt;GetText();		
	}

	pNode = pRootElement-&gt;FirstChildElement("Age");
	if(pNode)
	{
		person-&gt;m_nAge = atoi(pNode-&gt;GetText());		
	}
}</pre>
</div>
<p>
	 </p>
<p>
	完整的程式範例如下：</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:16772192-465f-451e-bdec-f2b1001bd16f" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c" name="code">
// ConsoleApplication11.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include &lt;string&gt;
#include "tinyxml.h"   
#include "tinystr.h"

using namespace std;

class Person
{
public:
	string	m_sName;
	string	m_sNickName;
	int		m_nAge;
};

void SaveXml(Person* person, string file)
{	
	TiXmlDocument xmlDoc;

	TiXmlNode* rootElement = xmlDoc.InsertEndChild(TiXmlElement("Person"));

	rootElement
		-&gt;InsertEndChild(TiXmlElement("Name"))
		-&gt;InsertEndChild(TiXmlText(person-&gt;m_sName.c_str()));

	rootElement
		-&gt;InsertEndChild(TiXmlElement("NickName"))
		-&gt;InsertEndChild(TiXmlText(person-&gt;m_sNickName.c_str()));

	char buffer[256];
	_itoa(person-&gt;m_nAge, buffer,10);
	rootElement
		-&gt;InsertEndChild(TiXmlElement("Age"))
		-&gt;InsertEndChild(TiXmlText(buffer));

	xmlDoc.SaveFile(file.c_str());
}

void LoadXml(string file, Person* person)
{	
	TiXmlDocument xmlDoc(file.c_str());

	xmlDoc.LoadFile();

	if(xmlDoc.ErrorId() &gt; 0)
		return;

	TiXmlElement* pRootElement = xmlDoc.RootElement();

	if(!pRootElement)
		return;

	TiXmlElement* pNode = NULL;
	
	pNode = pRootElement-&gt;FirstChildElement("Name");
	if(pNode)
	{
		person-&gt;m_sName = pNode-&gt;GetText();		
	}

	pNode = pRootElement-&gt;FirstChildElement("NickName");
	if(pNode)
	{
		person-&gt;m_sNickName = pNode-&gt;GetText();		
	}

	pNode = pRootElement-&gt;FirstChildElement("Age");
	if(pNode)
	{
		person-&gt;m_nAge = atoi(pNode-&gt;GetText());		
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	string file = "Person.xml";

	Person Larry;
	Larry.m_sName		= "Larry";
	Larry.m_sNickName	= "蹂躪";
	Larry.m_nAge		= 30;
	
	SaveXml(&amp;Larry, file);


	Person NewLarry;

	LoadXml(file, &amp;NewLarry);

	printf("Name: %s
", NewLarry.m_sName.c_str());
	printf("NickName: %s
", NewLarry.m_sNickName.c_str());
	printf("Age: %d
", NewLarry.m_nAge);

	return 0;
}</pre>
</div>
<p>
	 </p>
<p>
	範例運行後會產生個Xml，內容像下面這般：</p>
<p>
	<img alt="image" border="0" height="236" src="\images\posts\60602\image9_thumb.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="374" /></p>
<p>
	 </p>
<p>
	Xml的資料也能正常的解析。</p>
<p>
	<img alt="image" border="0" height="191" src="\images\posts\60602\image6_thumb.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="417" /></p>
<p>
	 </p>
<p>
	TinyXml使用上算是比較不複雜的，但是卻有個很麻煩的問題，就是轉碼的動作必須自己處理，若不經轉換可能會有亂碼的問題，網路上有些文章就是專門在討論這樣的問題。另外，它的Xml存檔格式是用ANSI的格是下去儲存，若是要以UTF-8去儲存，必須修改tinyxml的程式碼，直接搜尋程式找到useMicrosoftBOM，將這值設為true就可以了。</p>
<p>
	<img alt="image" border="0" height="597" src="\images\posts\60602\image_thumb_4.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="610" /></p>
<p>
	 </p>
<p>
	這邊筆者為了方便使用，有將TinyXml包成類似.NET的XmlWriter類別，存取Xml的部分就會變得像下面這樣：</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:0b41014e-ff73-4c37-97b8-d52c5e9e248b" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="brush:csharp;">
void SaveXml(Person* person, string file)
{
	XmlWriter xw(file);

	xw
		.WriteStartElement("Person")
		    .WriteElementValue("Name", person-&gt;m_sName)
		    .WriteElementValue("NickName", person-&gt;m_sNickName)
		    .WriteElementValue("Age", person-&gt;m_nAge)
		.WriteEndElement()
		.Close();
}</pre>
</div>
<p>
	 </p>
<p>
	程式碼分享於下方，有需要的自行取用。</p>
<p>
	XmlWriter.h</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:fdd0e569-acc7-4e5c-af72-24055f0de4ce" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c" name="code">
#pragma once
#include &lt;stack&gt;
#include &lt;string&gt;
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
	char				m_cBuffer[DEFAULT_BUFFER_SIZE];
	string				_sFile;
	TiXmlDocument		_XmlDoc;	
	stack&lt;TiXmlNode*&gt;	_StartNodes;
#pragma endregion


#pragma region Private Property
private:
	__declspec(property(get=Get_sFile,put=Set_sFile))
		string m_sFile;

	__declspec(property(get=Get_XmlDoc,put=Set_XmlDoc))
		TiXmlDocument&amp; m_XmlDoc;

	__declspec(property(get=Get_StartNodes))
		stack&lt;TiXmlNode*&gt;&amp; m_StartNodes;

	__declspec(property(get=Get_pCurrentNode,put=Set_pCurrentNode))
		TiXmlNode* m_pCurrentNode;
#pragma endregion


#pragma region Constructor &amp; DeConstructor
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

	inline TiXmlDocument&amp; Get_XmlDoc()
	{
		return _XmlDoc;
	}

	inline void Set_XmlDoc(TiXmlDocument&amp; value)
	{
		_XmlDoc = value;
	}

	inline TiXmlNode* Get_pCurrentNode()
	{		
		if(m_StartNodes.empty())
		{
			return &amp;m_XmlDoc;
		}
		return m_StartNodes.top();
	}

	inline stack&lt;TiXmlNode*&gt;&amp; Get_StartNodes()
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
	XmlWriter&amp; WriteStartElement(string localName);
	XmlWriter&amp; WriteEndElement();
	XmlWriter&amp; WriteElementValue(string localName, const char* value);
	XmlWriter&amp; WriteElementValue(string localName, string value);
	XmlWriter&amp; WriteElementValue(string localName, int value);
	void Close();
#pragma endregion
};</pre>
</div>
<p>
	 </p>
<p>
	XmlWriter.cpp</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:f9911ff1-b295-4972-88a2-3bf4a2a5f55d" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c" name="code">
#include "stdafx.h"
#include "XmlWriter.h"

#pragma region Constructor &amp; DeConstructor
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
	_sFile			= "";
	_XmlDoc.Clear();
}
#pragma endregion


#pragma region Public Method
XmlWriter&amp; XmlWriter::WriteStartElement(string localName)
{	
	m_StartNodes.push(m_pCurrentNode-&gt;InsertEndChild(TiXmlElement(localName.c_str())));

	return *this;
}

XmlWriter&amp; XmlWriter::WriteEndElement()
{
	if(!m_StartNodes.empty())
		m_StartNodes.pop();

	return *this;
}

XmlWriter&amp; XmlWriter::WriteElementValue(string localName, const char* value)
{
	m_pCurrentNode
		-&gt;InsertEndChild(TiXmlElement(localName.c_str()))
		-&gt;InsertEndChild(TiXmlText(value));

	return *this;
}

XmlWriter&amp; XmlWriter::WriteElementValue(string localName, string value)
{
	return WriteElementValue(localName, value.c_str());
}

XmlWriter&amp; XmlWriter::WriteElementValue(string localName, int value)
{
	_itoa(value, m_cBuffer,10);
	return WriteElementValue(localName, m_cBuffer);
}

void XmlWriter::Close()
{
	m_XmlDoc.SaveFile(m_sFile.c_str());
	Reset();
}
#pragma endregion</pre>
</div>
<p>
	 </p>
<h2>
	Link</h2>
<ul>
	<li>
		TinyXml Main Page</li>
	<li>
		TinyXml Documentation</li>
	<li>
		TinyXml Project Page</li>
	<li>
		TinyXML - 小巧好用的 XML parser</li>
	<li>
		TinyXML Tutorial 中文指南</li>
</ul>
