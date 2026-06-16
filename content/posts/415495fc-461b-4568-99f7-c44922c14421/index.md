---
title: "[C#]忽略在 HTTP 剖析期間發生的驗證錯誤"
slug: "[CSharp]忽略在 HTTP 剖析期間發生的驗證錯誤"
date: "2013-11-06 12:00:00"
description: "這次Sprint有解一個問題，就是我們的專案程式在抓取某些網站的縮圖(像是Yahoo...)時會抓取不到，但是Web版的程式看同一篇貼文卻是OK的，實際查驗了一下發現程式在抓取圖片時會丟出例外導致無法正確將圖片下載下來，"
tags: [CSharp]
---

這次Sprint有解一個問題，就是我們的專案程式在抓取某些網站的縮圖(像是Yahoo...)時會抓取不到，但是Web版的程式看同一篇貼文卻是OK的，實際查驗了一下發現程式在抓取圖片時會丟出例外導致無法正確將圖片下載下來，例外的訊息大概是這樣的"The server committed a protocol violation. Section=ResponseHeader Detail=CR must be followed by LF"，查驗了一下網路文章才知道這部份問題可能是違反了以下幾項：

* 在行結尾程式碼中使用 CRLF；不允許單獨使用 CR 或 LF。
* 標頭名稱中不應該有空格。
* 如果有多個狀態列，會將所有額外狀態列視為不正確的標頭名稱/值組。
* 除了狀態碼外，狀態列還必須有狀態描述。
* 標頭名稱中不能有非 ASCII 字元。無論這個屬性設定為 **true** 或 **false**，都會執行這個驗證。

必須將HttpWebRequestElement.UseUnsafeHeaderParsing 屬性設為true讓驗證動作睜一隻眼閉一隻眼。

在設定UseUnsafeHeaderParsing時我們可以將App.Config檔開啟，將下面這段插入在設定檔中。

```xml
<system.net>
  <settings>
   <httpWebRequest useUnsafeHeaderParsing="true" />
  </settings>
</system.net>
```

或是透過反射直接設定也可以。

```csharp
public static bool EnableUnsafeHeaderParsing()
{
	//Get the assembly that contains the internal class
	Assembly aNetAssembly = Assembly.GetAssembly(typeof(System.Net.Configuration.SettingsSection));
	if (aNetAssembly != null)
	{
		//Use the assembly in order to get the internal type for the internal class
		Type aSettingsType = aNetAssembly.GetType("System.Net.Configuration.SettingsSectionInternal");
		if (aSettingsType != null)
		{
			//Use the internal static property to get an instance of the internal settings class.
			//If the static instance isn't created allready the property will create it for us.
			object anInstance = aSettingsType.InvokeMember("Section",
			  BindingFlags.Static | BindingFlags.GetProperty | BindingFlags.NonPublic, null, null, new object[] { });

			if (anInstance != null)
			{
				//Locate the private bool field that tells the framework is unsafe header parsing should be allowed or not
				FieldInfo aUseUnsafeHeaderParsing = aSettingsType.GetField("useUnsafeHeaderParsing", BindingFlags.NonPublic | BindingFlags.Instance);
				if (aUseUnsafeHeaderParsing != null)
				{
					aUseUnsafeHeaderParsing.SetValue(anInstance, true);
					return true;
				}
			}
		}
	}
	return false;
}
```

## Link

* HttpWebRequest 錯誤訊息 “The server committed a protocol violation…" 的解法
* HttpWebRequestElement.UseUnsafeHeaderParsing 屬性
* how to set useUnsafeHeaderParsing in code
* How do I enable useUnsafeHeaderParsing from code? (.NET 2.0)
