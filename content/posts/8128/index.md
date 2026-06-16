---
title: "[C#][VB.NET]Isolated Storage 隔離儲存區"
slug: "[CSharp][VB.NET]Isolated Storage 隔離儲存區"
date: "2009-04-22 09:03:59"
description: "Abstract Namespace Assemble 功能 重要類別 隔離類型 儲存位置 使用時機 不該使用時機 取得隔離儲存區 刪除隔離儲存區 建立目錄 尋找目錄 尋找檔案 刪除目錄 刪除檔案 寫入檔案 讀取檔案 Namespace System.IO.IsolatedStorage…"
tags: [CSharp,VB.NET]
---

## Abstract

* Namespace
* Assemble
* 功能
* 重要類別
* 隔離類型
* 儲存位置
* 使用時機
* 不該使用時機
* 取得隔離儲存區
* 刪除隔離儲存區
* 建立目錄
* 尋找目錄
* 尋找檔案
* 刪除目錄
* 刪除檔案
* 寫入檔案
* 讀取檔案

## Namespace

System.IO.IsolatedStorage

## Assemble

mscorlib (在 mscorlib.dll)

## 功能

隔離儲存區 (Isolated Storage) 為資料儲存機制，藉著定義標準化方式，將程式碼與儲存的資料產生關聯，以提供隔離和安全。標準化也提供其他利益。

轉載自MSDN，詳細內容請參考『隔離儲存區』與『[隔離儲存區的簡介](http://msdn.microsoft.com/zh-tw/library/3ak841sy(VS.80).aspx)』。

## 重要類別

* **IsolatedStorageFile :** 提供隔體儲存區大部分的必要功能，可取得、刪除和管理隔離儲存區。
* **IsolatedStorageFileStream :** 處理存放區的檔案讀取和寫入。
* **IsolatedStorageScope :** 能夠建立和選取適當隔離類型的存放區。

## 隔離類型

* 依據使用者和組件的隔離
* 依據使用者、定義域和組件的隔離

  ![image_thumb.png](/images/posts/8128/image_thumb.png)

  轉載自MSDN，詳細內容請參考『[隔離的類型](http://msdn.microsoft.com/zh-tw/library/eh5d60e1(VS.80).aspx)』。

  ## 儲存位置

  <table border="0" cellpadding="2" cellspacing="0" width="614"><tbody><tr><td valign="top" width="202"><p>作業系統</p></td><td valign="top" width="409"><p>檔案系統中的位置</p></td></tr><tr><td valign="top" width="202"><p>Windows 98、Windows Me - 未啟用使用者設定檔</p></td><td valign="top" width="409"><p>啟用漫遊的存放區 =</p><p>&lt;SYSTEMROOT&gt;\Application Data</p><p>非漫遊存放區 = WINDOWS\Local Settings\Application Data</p></td></tr><tr><td valign="top" width="202"><p>Windows 98、Windows Me - 已啟用使用者設定檔</p></td><td valign="top" width="409"><p>啟用漫遊的存放區 =</p><p>&lt;SYSTEMROOT&gt;\Profiles\&lt;user&gt;\Application Data</p><p>非漫遊存放區 = Windows\Local Settings\Application Data</p></td></tr><tr><td valign="top" width="202"><p>Windows NT 4.0</p></td><td valign="top" width="409"><p>&lt;SYSTEMROOT&gt;\Profiles\&lt;user&gt;\Application Data</p></td></tr><tr><td valign="top" width="202"><p>Windows NT 4.0 - Service Pack 4</p></td><td valign="top" width="409"><p>啟用漫遊的存放區 =</p><p>&lt;SYSTEMROOT&gt;\Profiles\&lt;user&gt;\Application Data</p><p>非漫遊存放區 =</p><p>&lt;SYSTEMROOT&gt;\Profiles\&lt;user&gt;\Local Settings\Application Data</p></td></tr><tr><td valign="top" width="202"><p>Windows 2000、Windows XP、Windows Server 2003 - 從 NT 4.0 升級</p></td><td valign="top" width="409"><p>啟用漫遊的存放區 =</p><p>&lt;SYSTEMROOT&gt;\Profiles\&lt;user&gt;\Application Data</p><p>非漫遊存放區 =</p><p>&lt;SYSTEMROOT&gt;\Profiles\&lt;user&gt;\Local Settings\Application Data</p></td></tr><tr><td valign="top" width="202"><p>Windows 2000 - 全新安裝 (以及自 Windows 98 和 NT 3.51 升級)</p></td><td valign="top" width="409"><p>啟用漫遊的存放區 =</p><p>&lt;SYSTEMDRIVE&gt;\Documents and Settings\&lt;user&gt;\Application Data</p><p>非漫遊存放區 =</p><p>&lt;SYSTEMDRIVE&gt;\Documents and Settings\&lt;user&gt;\Local Settings\Application Data</p></td></tr><tr><td valign="top" width="202"><p>Windows XP、Windows Server 2003 - 全新安裝 (以及自 Windows 2000 和 Windows 98 升級)</p></td><td valign="top" width="409"><p>啟用漫遊的存放區 =</p><p>&lt;SYSTEMDRIVE&gt;\Documents and Settings\&lt;user&gt;\Application Data</p><p>非漫遊存放區 =</p><p>&lt;SYSTEMDRIVE&gt;\Documents and Settings\&lt;user&gt;\Local Settings\Application Data</p></td></tr></tbody></table>

  轉載自MSDN，詳細內容請參考『[隔離儲存區的簡介](http://msdn.microsoft.com/zh-tw/library/3ak841sy(VS.80).aspx)』。

  ## 使用時機

  1. 下載的控制項。從網際網路下載的 Managed 程式碼控制項不允許透過一般 I/O 類別寫入硬碟，但它們可以使用隔離儲存區保存 (Persist) 使用者的設定值和應用程式狀態。
  2. 永續性 Web 應用程式儲存區。Web 應用程式也會防止 I/O 類別的使用。這些程式可以使用隔離儲存區做為與下載元件相同的用途。
  3. 共用的元件儲存區。應用程式之間共用的元件可以使用隔離儲存區以提供對資料存放區的控制存取。
  4. 伺服器儲存區。伺服器應用程式可以使用隔離儲存區，提供個別存放區給向應用程式產生要求的大量使用者。因為隔離儲存區一直根據使用者來分離，伺服器必須模擬提出要求的使用者。在這個狀況中，資料是根據主體的識別 (應用程式用以區別其使用者的相同識別) 來隔離。
  5. 漫遊。應用程式也可以根據漫遊使用者設定檔來使用隔離儲存區。這允許使用者的隔離存放區隨著設定檔而漫遊。

  轉載自MSDN，詳細內容請參考『[隔離儲存區的案例](http://msdn.microsoft.com/zh-tw/library/kbcw921f(VS.80).aspx)』。

  ## 不該使用時機

  1. 因為隔離儲存區不能防範高度受信任程式碼、Unmanaged 程式碼或電腦的信任使用者，隔離儲存區不應該使用於存放具高度價值的秘密，例如未加密的金鑰 (Key) 或密碼。
  2. 隔離儲存區不應該被用來儲存程式碼。
  3. 隔離儲存區不應該被用來儲存系統管理員所控制的組態和部署設定值(使用者喜好不算是組態設定，因為系統管理員並不控制它們)。

  轉載自MSDN，詳細內容請參考『[隔離儲存區的案例』。](http://msdn.microsoft.com/zh-tw/library/kbcw921f(VS.80).aspx)

  ## 取得隔離儲存區

  取得隔離儲存區主要有四種方法：

  **1.透過GetUserStoreForAssembly**

  簡易範例如下：

  VB.NET

  ```
Dim isoFile As IsolatedStorageFile
isoFile = IsolatedStorageFile.GetUserStoreForAssembly()
```

  C#

```
IsolatedStorageFile isoFile;
isoFile = IsolatedStorageFile.GetUserStoreForAssembly();
```

**2.透過GetUserStoreForDomain**

簡易範例如下：

VB.NET

```
Dim isoFile As IsolatedStorageFile
isoFile = IsolatedStorageFile.GetUserStoreForDomain()
```

C#

```
IsolatedStorageFile isoFile;
isoFile = IsolatedStorageFile.GetUserStoreForDomain();
```

**3.透過GetMachineStoreForApplication**

簡易範例如下：

VB.NET

```
Dim isoFile As IsolatedStorageFile
isoFile = IsolatedStorageFile.GetMachineStoreForApplication ()
```

C#

```
IsolatedStorageFile isoFile;
isoFile = IsolatedStorageFile.GetMachineStoreForApplication ();
```

**4.透過GetStore**

簡易範例如下：

VB.NET

```
Dim isoStore As IsolatedStorageFile
isoStore = IsolatedStorageFile.GetStore(IsolatedStorageScope.User Or IsolatedStorageScope.Assembly, Nothing, Nothing)
```

C#

```
IsolatedStorageFile isoStore =  IsolatedStorageFile.GetStore(IsolatedStorageScope.User | IsolatedStorageScope.Assembly, null, null);
```

欲了解更多，可參考『HOW TO：取得離儲存區的存放區』。

## 刪除隔離儲存區

刪除隔離儲存區主要有二種方法：

**1.透過執行個體方法 Remove**

簡易範例如下：

VB.NET

```
Dim isoStore As IsolatedStorageFile
isoStore = IsolatedStorageFile.GetUserStoreForDomain()
isoStore.Remove()
isoStore.Dispose()
```

C#

```
IsolatedStorageFile isoStore;
isoStore = IsolatedStorageFile.GetUserStoreForDomain();
isoStore.Remove();
isoStore.Dispose();
```

**2.透過靜態方法 Remove**

簡易範例如下：

VB.NET

```
IsolatedStorageFile.Remove(IsolatedStorageScope.User)
```

C#

```
IsolatedStorageFile.Remove(IsolatedStorageScope.User);
```

欲了解更多，可參考『HOW TO：刪除隔離儲存區中的存放區』。

## 建立目錄

欲在Isolated Storage建立目錄，可分為幾個步驟：

1. 取得IsolatedStorageFile物件
2. 使用IsolatedStorageFile物件的CreateDirectory方法建立目錄
3. 關閉IsolatedStorageFile

簡易範例如下：

VB.NET

```
Dim isoStore As IsolatedStorageFile
isoStore = IsolatedStorageFile.GetUserStoreForDomain()
isoStore.CreateDirectory("Test")
isoStore.Dispose()
```

C#

```
IsolatedStorageFile isoStore;
isoStore = IsolatedStorageFile.GetUserStoreForDomain();
isoStore.CreateDirectory("Test");
isoStore.Dispose();
```

欲了解更多，可參考『HOW TO：讀取和寫入離儲存區中的檔案』。

## 尋找目錄

欲尋找Isolated Storage的目錄，可分為幾個步驟：

1. 取得IsolatedStorageFile物件
2. 使用IsolatedStorageFile物件的GetDirectoryNames方法尋找目錄
3. 關閉IsolatedStorageFile

簡易範例如下：

VB.NET

```
Dim isoStore As IsolatedStorageFile
isoStore = IsolatedStorageFile.GetUserStoreForDomain()
Dim dirNames As String() = isoStore.GetDirectoryNames("*")
isoStore.Dispose()
```

C#

```
IsolatedStorageFile isoStore;
isoStore = IsolatedStorageFile.GetUserStoreForDomain();
String dirNames() = isoStore.GetDirectoryNames("*");
isoStore.Dispose();
```

欲了解更多，可參考『HOW TO：尋找隔離儲存區中的現有檔案和目錄』。

## 尋找檔案

欲尋找Isolated Storage的檔案，可分為幾個步驟：

1. 取得IsolatedStorageFile物件
2. 使用IsolatedStorageFile物件的GetFileNames方法尋找檔案
3. 關閉IsolatedStorageFile

簡易範例如下：

VB.NET

```
Dim isoStore As IsolatedStorageFile
isoStore = IsolatedStorageFile.GetUserStoreForDomain
Dim fileNames As String() = isoStore.GetFileNames("*")
isoStore.Dispose()
```

C#

```
IsolatedStorageFile isoStore;
isoStore = IsolatedStorageFile.GetUserStoreForDomain();
Dim fileNames As String() = isoStore.GetFileNames("*");
isoStore.Dispose();
```

欲了解更多，可參考『HOW TO：尋找隔離儲存區中的現有檔案和目錄』。

## 刪除目錄

欲刪除目錄，可分為幾個步驟：

1. 取得IsolatedStorageFile物件
2. 使用IsolatedStorageFile物件的DeleteDirectory方法刪除目錄
3. 關閉IsolatedStorageFile

簡易範例如下：

VB.NET

```
Dim isoFile As IsolatedStorageFile = IsolatedStorageFile.GetUserStoreForDomain
isoFile.DeleteDirectory("Test")
isoFile.Dispose()
```

C#

```
IsolatedStorageFile isoFile = IsolatedStorageFile.GetUserStoreForDomain();
isoFile.DeleteDirectory("Test") ;
isoFile .Dispose();
```

欲了解更多，可參考『HOW TO：刪除隔離儲存區中的檔案和目錄』。

## 刪除檔案

欲刪除檔案，可分為幾個步驟：

1. 取得IsolatedStorageFile物件
2. 使用IsolatedStorageFile物件的DeleteFile方法刪除檔案
3. 關閉IsolatedStorageFile

簡易範例如下：

VB.NET

```
Dim isoStorage As IsolatedStorageFile
isoStorage = IsolatedStorageFile.GetUserStorageForDomain
isoStorage .DeleteFile("Test.xml")
isoStorage .Dispose()
```

C#

```
IsolatedStorageFile isoStorage;
isoStorage = IsolatedStorageFile.GetUserStorageForDomain;
isoStorage .DeleteFile("Test.xml");
isoStorage .Dispose();
```

欲了解更多，可參考『HOW TO：刪除隔離儲存區中的檔案和目錄』。

## 寫入檔案

欲寫入檔案，可分為幾個步驟：

1. 取得IsolatedStorageFile物件
2. 建立IsolatedStorageFileStream物件
3. 建立StreamWriter物件，並串連IsolatedStorageFileStream
4. 使用StreamWriter物件去寫入
5. 關閉StreamWriter
6. 關閉IsolatedStorageFileStream
7. 關閉IsolatedStorageFile

簡易範例如下：

```
Dim isoStorage As IsolatedStorage.IsolatedStorageFile
isoStorage = IsolatedStorage.IsolatedStorageFile.GetUserStoreForDomain
Dim stream As New IO.IsolatedStorage.IsolatedStorageFileStream("Test.Txt", FileMode.Create, isoStorage)
Dim sw As New StreamWriter(stream)
sw.WriteLine("Test")
sw.Dispose()
stream.Dispose()
isoStorage.Dispose()
```

欲了解更多，可參考『HOW TO：在隔離儲存區中建立檔案和目錄』。

## 讀取檔案

欲讀取檔案，可分為幾個步驟：

1. 取得IsolatedStorageFile物件
2. 建立IsolatedStorageFileStream物件
3. 建立StreamReader物件，並串連IsolatedStorageFileStream
4. 使用StreamReader物件去讀取
5. 關閉StreamReader
6. 關閉IsolatedStorageFileStream
7. 關閉IsolatedStorageFile

簡易範例如下：

```
Dim isoStorage As IsolatedStorage.IsolatedStorageFile
isoStorage = IsolatedStorage.IsolatedStorageFile.GetUserStoreForDomain
Dim stream As New IO.IsolatedStorage.IsolatedStorageFileStream("Test.Txt", FileMode.Open, isoStorage)
Dim sr As New StreamReader(stream)
Dim str As String = sr.ReadLine()
sr.Dispose()
stream.Dispose()
isoStorage.Dispose()
```

欲了解更多，可參考『HOW TO：讀取和寫入離儲存區中的檔案』。
