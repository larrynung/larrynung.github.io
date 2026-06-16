---
title: "[C#]使用SHEmptyRecycleBin API清除資源回收桶"
slug: "[CSharp]使用SHEmptyRecycleBin API清除資源回收桶"
date: "2013-11-06 12:00:00"
description: "玩了一下怎樣刪除檔案並送到資源回收桶，就會想到送到資源回收桶後要怎樣刪除，這邊稍微研究並記錄一下。 要清除資源回收桶，我們可以透過SHEmptyRecycleBin API，下面是它的函式原型。"
tags: [CSharp]
---

玩了一下怎樣刪除檔案並送到資源回收桶，就會想到送到資源回收桶後要怎樣刪除，這邊稍微研究並記錄一下。

要清除資源回收桶，我們可以透過SHEmptyRecycleBin API，下面是它的函式原型。

```c
HRESULT SHEmptyRecycleBin(
  _In_opt_  HWND hwnd,
  _In_opt_  LPCTSTR pszRootPath,
  DWORD dwFlags
);
```

裡面比較重要的是dwFlags這個參數，它可以有三個不同的值，用以設定是否要彈出系統對話框、是否顯示刪除進度的UI、以及是否要撥放刪除的聲音。

<table border="0" cellpadding="2" cellspacing="0" width="400"><tbody>
<tr>
<td valign="top" width="200"><strong>SHERB_NOCONFIRMATION</strong></td>
<td valign="top" width="200">No dialog box confirming the deletion of the objects will be displayed.</td>
</tr>
<tr>
<td valign="top" width="200"><strong>SHERB_NOPROGRESSUI</strong></td>
<td valign="top" width="200">No dialog box indicating the progress will be displayed.</td>
</tr>
<tr>
<td valign="top" width="200"><strong>SHERB_NOSOUND</strong></td>
<td valign="top" width="200">No sound will be played when the operation is complete.</td>
</tr>
</tbody></table>

如果都不指定就是預設的狀態，會彈出系統對話框詢問使用者，還會有刪除的進度與聲音。

![image_thumb.png](/images/posts/8444aab0-40b6-436e-8592-690b74175e3e/image_thumb.png)

這邊對應到的C# P/Invoke程式碼會像下面這樣：

```csharp
enum RecycleFlags : uint
{
	SHERB_NOCONFIRMATION = 0x00000001,
	SHERB_NOPROGRESSUI = 0x00000002,
	SHERB_NOSOUND = 0x00000004
}
...
[DllImport("Shell32.dll", CharSet = CharSet.Unicode)]
static extern uint SHEmptyRecycleBin(IntPtr hwnd, string pszRootPath, RecycleFlags dwFlags);
```

使用上就將需要的參數帶入就可以了。要特別注意到的是SHEmptyRecycleBin API的回傳值若是非S_OK (0)就是代表有發生錯誤，而回傳的值就是錯誤的代碼。

```csharp
private Boolean EmptyRecycleBin()
{
	return SHEmptyRecycleBin(IntPtr.Zero, null, RecycleFlags.SHERB_NOCONFIRMATION | RecycleFlags.SHERB_NOPROGRESSUI | RecycleFlags.SHERB_NOSOUND) == 0;
}
```

## Link

* Empty the Recycle Bin using C#
* Empty the Recycle Bin using C#
* Empty Windows Recycle Bin with C#
* SHEmptyRecycleBin function
* Emptying the Recycle Bin using C#
