---
title: "[C#]How to Zip and Unzip Files Using the Windows Shell"
slug: "csharp-how-to-zip-and-unzip-files-using-the-windows-shell"
aliases: ["/posts/csharp如何使用windows-shell做zip檔的壓縮與解壓縮/"]
date: "2013-11-06 12:00:00"
description: "在.NET程式中開發人員要做壓縮與解壓縮有很多種方法，可以用BCL內建的壓縮類別，或是用 DotNetZip與SharpZipLib之類的第三方元件庫，抑或是使用Windows Shell來做。"
tags: [CSharp]
---

在.NET程式中開發人員要做壓縮與解壓縮有很多種方法，可以用BCL內建的壓縮類別，或是用 DotNetZip與SharpZipLib之類的第三方元件庫，抑或是使用Windows Shell來做。內建的壓縮方式與第三方元件很多人都做過了介紹，使用上也大概都不是問題，但對於Windows Shell的使用方式可能就比較沒有那麼熟悉，所以這邊筆者稍微簡介一下怎樣用Windows Shell來做Zip檔的壓縮與解壓縮。

要用Windows Shell來做Zip檔的壓縮與解壓縮，因為我們要使用Shell的功能，因此首先必須將Microsoft Shell Controls and Automation組件加入參考。

![image_thumb.png](/images/posts/2f48955e-1250-4dda-850c-d0318cbed27c/image_thumb.png)

組件參考加入後，還要記得引用Shell32命名空間，引用後我們可以開始進行Zip檔的壓縮與解壓縮。程式部份很簡單，Windows Shell將一般檔案系統的目錄與壓縮檔皆視為一個Folder物件。因此壓縮時是將檔案目錄裡面的FolderItems拷貝到壓縮檔的Folder物件，解壓縮就是將壓縮檔的FolderItems拷貝到目的目錄的Folder物件。這邊特別要注意的是要是壓縮時壓縮檔不存在的話，需要建立一個空的檔案，這樣程式才能正常的取得壓縮檔Folder物件。

```csharp
private static void ShellCopyTo(string from, string to)
{
	Shell sc = new Shell();
	Folder SrcFolder = sc.NameSpace(from);
	Folder DestFolder = sc.NameSpace(to);
	FolderItems items = SrcFolder.Items();
	DestFolder.CopyHere(items, 20);
}

public static void Compress(string sourceFolderPath, string zipFile)
{
	if (!Directory.Exists(sourceFolderPath))
		throw new DirectoryNotFoundException();

	if (!File.Exists(zipFile))
		File.Create(zipFile).Dispose();

	ShellCopyTo(sourceFolderPath, zipFile);
}

public static void DeCompress(string zipFile, string destinationFolderPath)
{
	if (!File.Exists(zipFile))
		throw new FileNotFoundException();

	if (!Directory.Exists(destinationFolderPath))
		Directory.CreateDirectory(destinationFolderPath);

	ShellCopyTo(zipFile, destinationFolderPath);
}
```

整個壓縮與解壓縮動作就是那麼簡單，若是不想要引用額外的參考，這邊也可以改成透過反射去做，替換下方的ShellCopyTo方法就可以了。

```csharp
private static void ShellCopyTo(string from, string to)
{
	Type shellType = Type.GetTypeFromProgID("Shell.Application");
	object shellObject = System.Activator.CreateInstance(shellType);
	object objSrcFile = shellType.InvokeMember("NameSpace", System.Reflection.BindingFlags.InvokeMethod, null, shellObject, new object[] { from });
	object objDestFolder = shellType.InvokeMember("NameSpace", System.Reflection.BindingFlags.InvokeMethod, null, shellObject, new object[] { to });
	Type FolderType = Type.GetTypeFromCLSID(new Guid("BBCBDE60-C3FF-11CE-8350-444553540000"));
	object items = FolderType.InvokeMember("Items", System.Reflection.BindingFlags.InvokeMethod, null, objSrcFile, null);
	FolderType.InvokeMember("CopyHere", System.Reflection.BindingFlags.InvokeMethod, null, objDestFolder, new object[] { items, 20 });
}
```

最後這邊筆者隨手試著整理了一個簡易的類別，可以做到基本的壓縮、解壓縮、以及查驗壓縮檔內含有什麼內容，有興趣的可以自行參閱使用。

```csharp
	public enum ZipEntryType
	{
		File,
 		Folder
	}

	public class ZipEntry
	{
		#region Private Property
		private FolderItem m_ShellItem { get; set; }
		private IEnumerable<ZipEntry> _entrys;
		#endregion

		#region Public Property
		/// <summary>
		/// Gets the name.
		/// </summary>
		/// <value>The name.</value>
		public string Name
		{
			get
			{
				return m_ShellItem.Name;
			}
		}

		/// <summary>
		/// Gets the type.
		/// </summary>
		/// <value>The type.</value>
		public ZipEntryType Type
		{
			get
			{
				return m_ShellItem.IsFolder ? ZipEntryType.Folder : ZipEntryType.File;
			}
		}

		/// <summary>
		/// Gets the modify date.
		/// </summary>
		/// <value>The modify date.</value>
		public DateTime ModifyDate
		{
			get
			{
				return m_ShellItem.ModifyDate;
			}
		}

		/// <summary>
		/// Gets the size.
		/// </summary>
		/// <value>The size.</value>
		public int Size
		{
			get
			{
				return m_ShellItem.Size;
			}
		}

		public IEnumerable<ZipEntry> Entrys
		{
			get
			{
				if (_entrys == null)
				{
					if (!m_ShellItem.IsFolder)
					{
						_entrys = new ZipEntry[0];
					}
					else
					{
						var folder = m_ShellItem.GetFolder as Folder;
						var items = new List<ZipEntry>();
						foreach (FolderItem shellItem in folder.Items())
						{
							items.Add(new ZipEntry(shellItem));
						}
						_entrys = items;
					}
				}
				return _entrys;
			}
		}
		#endregion

		#region Constructor
		/// <summary>
		/// Initializes a new instance of the <see cref="ZipEntry"/> struct.
		/// </summary>
		/// <param name="shellItem">The shell item.</param>
		public ZipEntry(FolderItem shellItem)
		{
			m_ShellItem = shellItem;
		}
		#endregion
	}

	public class ShellZip
	{
		#region Var
		private FolderItems _shellItems;
		private IEnumerable<ZipEntry> _items;
		#endregion

		#region Private Property
		/// <summary>
		/// Gets the m_ shell items.
		/// </summary>
		/// <value>The m_ shell items.</value>
		private FolderItems m_ShellItems
		{
			get
			{
				return _shellItems??(_shellItems = (new Shell()).NameSpace(FilePath).Items());
			}
		}
		#endregion

		#region Property
		/// <summary>
		/// Gets or sets the file.
		/// </summary>
		/// <value>The file.</value>
		public string FilePath { get; private set; }

		/// <summary>
		/// Gets the count.
		/// </summary>
		/// <value>The count.</value>
		public int Count
		{
			get
			{
				return m_ShellItems.Count;
			}
		}

		public IEnumerable<ZipEntry> Items
		{
			get
			{
				if (_items == null)
				{
					var items = new List<ZipEntry>();
					foreach (FolderItem shellItem in m_ShellItems)
					{
						items.Add(new ZipEntry(shellItem));
					}
					_items = items;
				}
				return _items;
			}
		}
		#endregion

		#region Constructor
		/// <summary>
		/// Initializes a new instance of the <see cref="ShellZip"/> class.
		/// </summary>
		/// <param name="zipFile">The zip file.</param>
		public ShellZip(string zipFile)
		{
			this.FilePath = zipFile;
		}
		#endregion

		#region Private Static Method
		/// <summary>
		/// Shells the copy to.
		/// </summary>
		/// <param name="from">From.</param>
		/// <param name="to">To.</param>
		private static void ShellCopyTo(string from, string to)
		{
			Shell sc = new Shell();
			Folder SrcFolder = sc.NameSpace(from);
			Folder DestFolder = sc.NameSpace(to);
			FolderItems items = SrcFolder.Items();
			DestFolder.CopyHere(items, 20);
		}
		#endregion

		#region Public Static Method
		/// <summary>
		/// Compresses the specified source folder path.
		/// </summary>
		/// <param name="sourceFolderPath">The source folder path.</param>
		/// <param name="zipFile">The zip file.</param>
		public static void Compress(string sourceFolderPath, string zipFile)
		{
			if (!Directory.Exists(sourceFolderPath))
				throw new DirectoryNotFoundException();

			if (!File.Exists(zipFile))
				File.Create(zipFile).Dispose();

			ShellCopyTo(sourceFolderPath, zipFile);
		}

		/// <summary>
		/// Des the compress.
		/// </summary>
		/// <param name="zipFile">The zip file.</param>
		/// <param name="destinationFolderPath">The destination folder path.</param>
		public static void DeCompress(string zipFile, string destinationFolderPath)
		{
			if (!File.Exists(zipFile))
				throw new FileNotFoundException();

			if (!Directory.Exists(destinationFolderPath))
				Directory.CreateDirectory(destinationFolderPath);

			ShellCopyTo(zipFile, destinationFolderPath);
		}
		#endregion

		#region Public Method
		/// <summary>
		/// Des the compress.
		/// </summary>
		/// <param name="destinationFolderPath">The destination folder path.</param>
		public void DeCompress(string destinationFolderPath)
		{
			DeCompress(this.FilePath, destinationFolderPath);
		}
		#endregion
	}
```

## Link

* System.Shell.Folder.copyHere method
* c#使用系統函數System.Shell.Folder.copyHere解壓.zip文件
* How to check when Shell32.Folder.CopyHere() is finished
* 如何利用shell對.zip文件進行解壓縮
* Easily zip / unzip files using Windows Shell32
* Zip and Unzip files using Shell 32 component
* Compress Zip files with Windows Shell API and C#
