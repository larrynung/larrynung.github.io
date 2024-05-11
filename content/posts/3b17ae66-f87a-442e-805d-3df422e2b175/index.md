---
title: "[C#][VB.NET]使用MFT Scanner遍巡USN Journal，快速找出磁碟內的所有檔案"
slug: "[CSharp][VB.NET]使用MFT Scanner遍巡USN Journal，快速找出磁碟內的所有檔案"
date: "2013-11-06 12:00:00"
description: "[C#][VB.NET]使用MFT Scanner遍巡USN Journal，快速找出磁碟內的所有檔案"
tags: [CSharp]
---

<p>相信很多人都有玩過Everything這套搜尋軟體，也對他的快速搜尋印象深刻。其實它之所以快速是因為它很聰明的去掃了NTFS的USN Journal，它的資料量會比我們去遍巡檔案系統還要少的多，所以可以在很短的時間完成檔案的索引，自然運行起來就會很快速。</p>  <p> </p>  <p>那麼我們要怎樣在.NET程式中實現類似的效果呢？筆者暫時還不想長篇大論的跟大家解釋如何讀取USN Journal，所以這邊筆者是用MFT Scanner in VB.NET</a>來做到類似的效果。檔案下載下來後可以看到裡面只有ㄧ個專案，運行起來就是ㄧ個簡單的搜尋程式，上方的輸入框是輸入要找尋的檔案位置，而下方的輸入框是讓我們指定找到的檔案清單要寫到哪個目錄下，輸入完後按下Start Processing按鈕就會開始進行MFT的搜尋與ㄧ般遞迴的搜尋，搜尋結束下方會顯示出搜尋的結果。</p>  <p><a href="http://files.dotblogs.com.tw/larrynung/1210/CMFTScannerUSNJournal_13966/image_4.png"><img style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" border="0" alt="image" src="\images\posts\3b17ae66-f87a-442e-805d-3df422e2b175\image_thumb_1.png" width="553" height="598" /> </p>  <p> </p>  <p>若要將這功能套用到自己的專案中，我們可以將他專案中的cEnumMFT.vb檔加入到自己的專案，並建立出cEnumMFT的物件實體，最後再透過建立出來的物件實體去叫用FindAllFiles就可以了。叫用時必需要帶入要搜尋的磁碟槽以及ㄧ個委派去負責處裡找到的檔案，最後兩個參數個人覺得意義不大，所以直接傳入Nothing就可以了。像是下面這樣：</p>  <div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:e72a25b6-958d-4d74-b741-d2d2e48dda9c" class="wlWriterSmartContent"><pre name="code" class="vb">		Dim scanner = New cEnumMFT
		scanner.FindAllFiles("c:\", Sub(file, size)
									End Sub, Nothing, Nothing)</pre></div>

<p> </p>

<p>筆者也花了點時間將之轉成C#了，並做了些調整，有需要的可以直接取用。</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:f5b5743e-9d43-4275-b24a-14a3ca20c161" class="wlWriterSmartContent"><pre name="code" class="c#">using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Runtime.InteropServices;
using Microsoft.VisualBasic;

public class MFTScanner
{
	private static IntPtr INVALID_HANDLE_VALUE = new IntPtr(-1);
	private const uint GENERIC_READ = 0x80000000;
	private const int FILE_SHARE_READ = 0x1;
	private const int FILE_SHARE_WRITE = 0x2;
	private const int OPEN_EXISTING = 3;
	private const int FILE_READ_ATTRIBUTES = 0x80;
	private const int FILE_NAME_IINFORMATION = 9;
	private const int FILE_FLAG_BACKUP_SEMANTICS = 0x2000000;
	private const int FILE_OPEN_FOR_BACKUP_INTENT = 0x4000;
	private const int FILE_OPEN_BY_FILE_ID = 0x2000;
	private const int FILE_OPEN = 0x1;
	private const int OBJ_CASE_INSENSITIVE = 0x40;
	private const int FSCTL_ENUM_USN_DATA = 0x900b3;

	[StructLayout(LayoutKind.Sequential)]
	private struct MFT_ENUM_DATA
	{
		public long StartFileReferenceNumber;
		public long LowUsn;
		public long HighUsn;
	}

	[StructLayout(LayoutKind.Sequential)]
	private struct USN_RECORD
	{
		public int RecordLength;
		public short MajorVersion;
		public short MinorVersion;
		public long FileReferenceNumber;
		public long ParentFileReferenceNumber;
		public long Usn;
		public long TimeStamp;
		public int Reason;
		public int SourceInfo;
		public int SecurityId;
		public FileAttribute FileAttributes;
		public short FileNameLength;
		public short FileNameOffset;
	}

	[StructLayout(LayoutKind.Sequential)]
	private struct IO_STATUS_BLOCK
	{
		public int Status;
		public int Information;
	}

	[StructLayout(LayoutKind.Sequential)]
	private struct UNICODE_STRING
	{
		public short Length;
		public short MaximumLength;
		public IntPtr Buffer;
	}

	[StructLayout(LayoutKind.Sequential)]
	private struct OBJECT_ATTRIBUTES
	{
		public int Length;
		public IntPtr RootDirectory;
		public IntPtr ObjectName;
		public int Attributes;
		public int SecurityDescriptor;
		public int SecurityQualityOfService;
	}

	//// MFT_ENUM_DATA
	[DllImport("kernel32.dll", ExactSpelling = true, SetLastError = true, CharSet = CharSet.Auto)]
	private static extern bool DeviceIoControl(IntPtr hDevice, int dwIoControlCode, ref MFT_ENUM_DATA lpInBuffer, int nInBufferSize, IntPtr lpOutBuffer, int nOutBufferSize, ref int lpBytesReturned, IntPtr lpOverlapped);

	[DllImport("kernel32.dll", SetLastError = true, CharSet = CharSet.Auto)]
	private static extern IntPtr CreateFile(string lpFileName, uint dwDesiredAccess, int dwShareMode, IntPtr lpSecurityAttributes, int dwCreationDisposition, int dwFlagsAndAttributes, IntPtr hTemplateFile);

	[DllImport("kernel32.dll", ExactSpelling = true, SetLastError = true, CharSet = CharSet.Auto)]
	private static extern Int32 CloseHandle(IntPtr lpObject);

	[DllImport("ntdll.dll", ExactSpelling = true, SetLastError = true, CharSet = CharSet.Auto)]
	private static extern int NtCreateFile(ref IntPtr FileHandle, int DesiredAccess, ref OBJECT_ATTRIBUTES ObjectAttributes, ref IO_STATUS_BLOCK IoStatusBlock, int AllocationSize, int FileAttribs, int SharedAccess, int CreationDisposition, int CreateOptions, int EaBuffer,
	int EaLength);

	[DllImport("ntdll.dll", ExactSpelling = true, SetLastError = true, CharSet = CharSet.Auto)]
	private static extern int NtQueryInformationFile(IntPtr FileHandle, ref IO_STATUS_BLOCK IoStatusBlock, IntPtr FileInformation, int Length, int FileInformationClass);

	private IntPtr m_hCJ;
	private IntPtr m_Buffer;
	private int m_BufferSize;

	private string m_DriveLetter;

	private class FSNode
	{
		public long FRN;
		public long ParentFRN;
		public string FileName;

		public bool IsFile;
		public FSNode(long lFRN, long lParentFSN, string sFileName, bool bIsFile)
		{
			FRN = lFRN;
			ParentFRN = lParentFSN;
			FileName = sFileName;
			IsFile = bIsFile;
		}

	}


	private IntPtr OpenVolume(string szDriveLetter)
	{

		IntPtr hCJ = default(IntPtr);
		//// volume handle

		m_DriveLetter = szDriveLetter;

		hCJ = CreateFile("\\.\" + szDriveLetter, GENERIC_READ, FILE_SHARE_READ | FILE_SHARE_WRITE, IntPtr.Zero, OPEN_EXISTING, 0, IntPtr.Zero);

		return hCJ;

	}


	private void Cleanup()
	{
		if (m_hCJ != IntPtr.Zero)
		{
			// Close the volume handle.
			CloseHandle(m_hCJ);
			m_hCJ = INVALID_HANDLE_VALUE;
		}

		if (m_Buffer != IntPtr.Zero)
		{
			// Free the allocated memory
			Marshal.FreeHGlobal(m_Buffer);
			m_Buffer = IntPtr.Zero;
		}

	}


	public IEnumerable&lt;String&gt; EnumerateFiles(string szDriveLetter)
	{
		try
		{
			var usnRecord = default(USN_RECORD);
			var mft = default(MFT_ENUM_DATA);
			var dwRetBytes = 0;
			var cb = 0;
			var dicFRNLookup = new Dictionary&lt;long, FSNode&gt;();
			var bIsFile = false;

			// This shouldn't be called more than once.
			if (m_Buffer.ToInt32() != 0)
			{
				throw new Exception("invalid buffer");
			}

			// Assign buffer size
			m_BufferSize = 65536;
			//64KB

			// Allocate a buffer to use for reading records.
			m_Buffer = Marshal.AllocHGlobal(m_BufferSize);

			// correct path
			szDriveLetter = szDriveLetter.TrimEnd('\');

			// Open the volume handle 
			m_hCJ = OpenVolume(szDriveLetter);

			// Check if the volume handle is valid.
			if (m_hCJ == INVALID_HANDLE_VALUE)
			{
				throw new Exception("Couldn't open handle to the volume.");
			}

			mft.StartFileReferenceNumber = 0;
			mft.LowUsn = 0;
			mft.HighUsn = long.MaxValue;

			do
			{
				if (DeviceIoControl(m_hCJ, FSCTL_ENUM_USN_DATA, ref mft, Marshal.SizeOf(mft), m_Buffer, m_BufferSize, ref dwRetBytes, IntPtr.Zero))
				{
					cb = dwRetBytes;
					// Pointer to the first record
					IntPtr pUsnRecord = new IntPtr(m_Buffer.ToInt32() + 8);

					while ((dwRetBytes &gt; 8))
					{
						// Copy pointer to USN_RECORD structure.
						usnRecord = (USN_RECORD)Marshal.PtrToStructure(pUsnRecord, usnRecord.GetType());

						// The filename within the USN_RECORD.
						string FileName = Marshal.PtrToStringUni(new IntPtr(pUsnRecord.ToInt32() + usnRecord.FileNameOffset), usnRecord.FileNameLength / 2);

						bIsFile = !usnRecord.FileAttributes.HasFlag(FileAttribute.Directory);
						dicFRNLookup.Add(usnRecord.FileReferenceNumber, new FSNode(usnRecord.FileReferenceNumber, usnRecord.ParentFileReferenceNumber, FileName, bIsFile));

						// Pointer to the next record in the buffer.
						pUsnRecord = new IntPtr(pUsnRecord.ToInt32() + usnRecord.RecordLength);

						dwRetBytes -= usnRecord.RecordLength;
					}

					// The first 8 bytes is always the start of the next USN.
					mft.StartFileReferenceNumber = Marshal.ReadInt64(m_Buffer, 0);


				}
				else
				{
					break; // TODO: might not be correct. Was : Exit Do

				}

			} while (!(cb &lt;= 8));

			// Resolve all paths for Files
			foreach (FSNode oFSNode in dicFRNLookup.Values.Where(o =&gt; o.IsFile))
			{
				string sFullPath = oFSNode.FileName;
				FSNode oParentFSNode = oFSNode;

				while (dicFRNLookup.TryGetValue(oParentFSNode.ParentFRN, out oParentFSNode))
				{
					sFullPath = string.Concat(oParentFSNode.FileName, "\", sFullPath);
				}
				sFullPath = string.Concat(szDriveLetter, "\", sFullPath);

				yield return sFullPath;
			}
		}
		finally
		{
			//// cleanup
			Cleanup();
		}
	}
}
</pre></div>

<p> </p>

<p>因為USN Journal是綁磁碟的，所以筆者也將之整理成DriveInfo的擴充方法，使用上會比較方便些。</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:9fd5c367-96e0-458c-92b3-9d18b78f262b" class="wlWriterSmartContent"><pre name="code" class="c#">using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;

public static class DriveInfoExtension
{
	public static IEnumerable&lt;String&gt; EnumerateFiles(this DriveInfo drive)
	{
		return (new MFTScanner()).EnumerateFiles(drive.Name);
	}	
}

</pre></div>

<p> </p>

<p>使用起來會像下面這樣：</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:55c8f4d6-dc0f-401e-bbdb-c9ab816ebce2" class="wlWriterSmartContent"><pre name="code" class="c#">using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;
using System.Diagnostics;

namespace ConsoleApplication28
{
	class Program
	{
		static void Main(string[] args)
		{
			var sw = Stopwatch.StartNew();
			var files = (new DriveInfo(@"c:\")).EnumerateFiles().ToArray();
			var elapsed = sw.ElapsedMilliseconds.ToString();
			Console.WriteLine(string.Format("Found {0} files, elapsed {1} ms", files.Length, elapsed));
		}
	}
}
</pre></div>

<p> </p>

<p>運行後我們可以看到，程式找尋筆者的磁碟C，找到501230個檔案也才花了7344ms。</p>

<p><img style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" border="0" alt="image" src="\images\posts\3b17ae66-f87a-442e-805d-3df422e2b175\image_thumb.png" width="409" height="175" /> </p>

<p> </p>

<h2>Link</h2>

<ul>
  <li>MFT Scanner in VB.NET</li>
</ul>
