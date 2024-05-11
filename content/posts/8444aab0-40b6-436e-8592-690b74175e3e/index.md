---
title: "[C#]使用SHEmptyRecycleBin API清除資源回收桶"
slug: "[CSharp]使用SHEmptyRecycleBin API清除資源回收桶"
date: "2013-11-06 12:00:00"
description: "[C#]使用SHEmptyRecycleBin API清除資源回收桶"
tags: [CSharp]
---

<p>玩了一下怎樣刪除檔案並送到資源回收桶，就會想到送到資源回收桶後要怎樣刪除，這邊稍微研究並記錄一下。</p>  <p> </p>  <p>要清除資源回收桶，我們可以透過SHEmptyRecycleBin API，下面是它的函式原型。</p>  <div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:7b7424ee-5d5c-48df-9663-2a2a3b0c4ebb" class="wlWriterSmartContent"><pre name="code" class="c">HRESULT SHEmptyRecycleBin(
  _In_opt_  HWND hwnd,
  _In_opt_  LPCTSTR pszRootPath,
  DWORD dwFlags
);</pre></div>

<p> </p>

<p>裡面比較重要的是dwFlags這個參數，它可以有三個不同的值，用以設定是否要彈出系統對話框、是否顯示刪除進度的UI、以及是否要撥放刪除的聲音。</p>

<table border="0" cellspacing="0" cellpadding="2" width="400"><tbody>
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

<p> </p>

<p>如果都不指定就是預設的狀態，會彈出系統對話框詢問使用者，還會有刪除的進度與聲音。</p>

<p><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" src="\images\posts\8444aab0-40b6-436e-8592-690b74175e3e\image_thumb.png" width="490" height="111" /> </p>

<p> </p>

<p>這邊對應到的C# P/Invoke程式碼會像下面這樣：</p>

<p />

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:58849ada-77bf-4aab-97f6-be3f8cecbb68" class="wlWriterSmartContent"><pre name="code" class="c#">enum RecycleFlags : uint
{
	SHERB_NOCONFIRMATION = 0x00000001,
	SHERB_NOPROGRESSUI = 0x00000002,
	SHERB_NOSOUND = 0x00000004
}
...
[DllImport("Shell32.dll", CharSet = CharSet.Unicode)]
static extern uint SHEmptyRecycleBin(IntPtr hwnd, string pszRootPath, RecycleFlags dwFlags);</pre></div>

<p />

<p> </p>

<p>使用上就將需要的參數帶入就可以了。要特別注意到的是SHEmptyRecycleBin API的回傳值若是非S_OK (0)就是代表有發生錯誤，而回傳的值就是錯誤的代碼。</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:8e19476e-1bf6-4294-9ae1-68600442fb08" class="wlWriterSmartContent"><pre name="code" class="c#">private Boolean EmptyRecycleBin()
{
	return SHEmptyRecycleBin(IntPtr.Zero, null, RecycleFlags.SHERB_NOCONFIRMATION | RecycleFlags.SHERB_NOPROGRESSUI | RecycleFlags.SHERB_NOSOUND) == 0;
}</pre></div>

<p> </p>

<h2>Link</h2>

<ul>
  <li>Empty the Recycle Bin using C# </li>

  <li>Empty the Recycle Bin using C# </li>

  <li>Empty Windows Recycle Bin with C# </li>

  <li>SHEmptyRecycleBin function </li>

  <li>Emptying the Recycle Bin using C# </li>
</ul>
