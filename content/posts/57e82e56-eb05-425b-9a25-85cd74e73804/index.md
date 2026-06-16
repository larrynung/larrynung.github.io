---
title: "[C#]將指定的檔案刪除並送到資源回收桶"
date: "2013-11-06 12:00:00"
description: "最近在看網路文章發現這個議題，回想了一下以往在做刪除的動作都是直接刪掉，沒有注意到將刪除的檔案送到資源回收桶要怎樣處理，所以這邊花了點時間玩了一下，並隨手做個筆記。"
tags: [CSharp]
---

最近在看網路文章發現這個議題，回想了一下以往在做刪除的動作都是直接刪掉，沒有注意到將刪除的檔案送到資源回收桶要怎樣處理，所以這邊花了點時間玩了一下，並隨手做個筆記。

要將刪除的檔案送到資源回收桶在VB.NET中很容易處理，直接透過My.Computer.FileSystem.DeleteFile 方法就可以了，但在C#中我們在刪除檔案能用的只有[File.Delete 方法](http://msdn.microsoft.com/zh-tw/library/system.io.file.delete(v=vs.80).aspx)，從MSDN中很明顯的可以看出沒有相對的方法可以處理，所以我們必須借用VB.NET的方法來做。

先將Microsoft.VisualBasic.Dll加入參考。

![image_thumb_1.png](/images/posts/57e82e56-eb05-425b-9a25-85cd74e73804/image_thumb_1.png)

引用Microsoft.VisualBasic.FileIO命名空間。

```csharp
using Microsoft.VisualBasic.FileIO;
```

透過FileSystem.DeleteFile去刪除指定的檔案就可以了。

```csharp
...
if (openFileDialog1.ShowDialog() == System.Windows.Forms.DialogResult.OK)
{
	FileSystem.DeleteFile(openFileDialog1.FileName,
		UIOption.OnlyErrorDialogs,
		RecycleOption.SendToRecycleBin);
}
...
```

這邊可以帶入UIOption去指定刪除時是否要有系統對話框，也可以帶入RecycleOption指定是否要送到資源回收桶。

![image_thumb.png](/images/posts/57e82e56-eb05-425b-9a25-85cd74e73804/image_thumb.png)

除了可以使用VB.NET的方法外，我們也可以透過SHFileOperation這個Win32 API來實現，這邊筆者稍微整理了一個Helper類別。

```csharp
public class FileIOHelper
{
	[StructLayout(LayoutKind.Sequential, CharSet = CharSet.Auto, Pack = 1)]
	public struct SHFILEOPSTRUCT
	{
		public IntPtr hwnd;
		[MarshalAs(UnmanagedType.U4)]
		public int wFunc;
		public string pFrom;
		public string pTo;
		public short fFlags;
		[MarshalAs(UnmanagedType.Bool)]
		public bool fAnyOperationsAborted;
		public IntPtr hNameMappings;
		public string lpszProgressTitle;
	}

	#region Dllimport
	/// <summary>
	/// SHs the file operation.
	/// </summary>
	/// <param name="FileOp">The file op.</param>
	/// <returns></returns>
	[DllImport("shell32.dll", CharSet = CharSet.Auto)]
	public static extern int SHFileOperation(ref SHFILEOPSTRUCT FileOp);
	#endregion

	#region Const
	public const int FO_DELETE = 3;
	public const int FOF_ALLOWUNDO = 0x40;
	public const int FOF_NOCONFIRMATION = 0x10;
	#endregion

	#region Public Static Method
	public static void DeleteFileToRecyclebin(string file, Boolean showConfirmDialog = false)
	{
		var shf = new SHFILEOPSTRUCT();
		shf.wFunc = FO_DELETE;
		shf.fFlags = FOF_ALLOWUNDO;
		if (!showConfirmDialog)
		{
			shf.fFlags |= FOF_NOCONFIRMATION;
		}
		shf.pFrom = file + '\0' + '\0';
		SHFileOperation(ref shf);
	}
	#endregion
}
```

使用上時帶入要刪除的檔案位置就可以了。

```csharp
...
if (openFileDialog1.ShowDialog() == System.Windows.Forms.DialogResult.OK)
{
	FileIOHelper.DeleteFileToRecyclebin(openFileDialog1.FileName);
}
...
```

從輔助類別的實作我們不難看出整個的運作重點就是在於要塞SHFILEOPSTRUCT的資料，我們必須將wFunc設為FO_DELETE，指定是做刪除的動作。fFlags必須要設定FOF_ALLOWUNDO，代表刪除的資料是可以還原的，也就是要丟進資源回收桶。如果不希望彈出系統對話框，還需要將FOF_NOCONFIRMATION也設到fFlags。最後記得pForm這邊要設定要刪除的檔案位置。都設定完後將SHFILEOPSTRUCT帶給SHFileOperation運行就好了。

## Link

* SHFILEOPSTRUCT structure
* How to delete a file or folder to Recyclebin
* My.Computer.FileSystem.DeleteFile 方法
* File.Delete 方法
