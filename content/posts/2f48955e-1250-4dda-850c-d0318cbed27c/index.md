---
title: "[C#]如何使用Windows Shell做Zip檔的壓縮與解壓縮"
slug: "[CSharp]如何使用Windows Shell做Zip檔的壓縮與解壓縮"
date: "2013-11-06 12:00:00"
description: "[C#]如何使用Windows Shell做Zip檔的壓縮與解壓縮"
tags: [CSharp]
---

<p>
	在.NET程式中開發人員要做壓縮與解壓縮有很多種方法，可以用BCL內建的壓縮類別，或是用 DotNetZip與SharpZipLib之類的第三方元件庫，抑或是使用Windows Shell來做。內建的壓縮方式與第三方元件很多人都做過了介紹，使用上也大概都不是問題，但對於Windows Shell的使用方式可能就比較沒有那麼熟悉，所以這邊筆者稍微簡介一下怎樣用Windows Shell來做Zip檔的壓縮與解壓縮。</p>
<p>
	 </p>
<p>
	要用Windows Shell來做Zip檔的壓縮與解壓縮，因為我們要使用Shell的功能，因此首先必須將Microsoft Shell Controls and Automation組件加入參考。</p>
<p>
	<img alt="image" border="0" height="450" src="\images\posts\2f48955e-1250-4dda-850c-d0318cbed27c\image_thumb.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="565" /></p>
<p>
	 </p>
<p>
	組件參考加入後，還要記得引用Shell32命名空間，引用後我們可以開始進行Zip檔的壓縮與解壓縮。程式部份很簡單，Windows Shell將一般檔案系統的目錄與壓縮檔皆視為一個Folder物件。因此壓縮時是將檔案目錄裡面的FolderItems拷貝到壓縮檔的Folder物件，解壓縮就是將壓縮檔的FolderItems拷貝到目的目錄的Folder物件。這邊特別要注意的是要是壓縮時壓縮檔不存在的話，需要建立一個空的檔案，這樣程式才能正常的取得壓縮檔Folder物件。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:c49ea984-af2a-49d3-96d8-9d2f202e1ed3" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c#" name="code">
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
		} </pre>
</div>
<p>
	 </p>
<p>
	整個壓縮與解壓縮動作就是那麼簡單，若是不想要引用額外的參考，這邊也可以改成透過反射去做，替換下方的ShellCopyTo方法就可以了。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:5dca3e09-cd71-42f9-aaf0-bb536ab11da7" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c#" name="code">
		private static void ShellCopyTo(string from, string to)
		{
			Type shellType = Type.GetTypeFromProgID("Shell.Application");
			object shellObject = System.Activator.CreateInstance(shellType);
			object objSrcFile = shellType.InvokeMember("NameSpace", System.Reflection.BindingFlags.InvokeMethod, null, shellObject, new object[] { from });
			object objDestFolder = shellType.InvokeMember("NameSpace", System.Reflection.BindingFlags.InvokeMethod, null, shellObject, new object[] { to });
			Type FolderType = Type.GetTypeFromCLSID(new Guid("BBCBDE60-C3FF-11CE-8350-444553540000"));
			object items = FolderType.InvokeMember("Items", System.Reflection.BindingFlags.InvokeMethod, null, objSrcFile, null);
			FolderType.InvokeMember("CopyHere", System.Reflection.BindingFlags.InvokeMethod, null, objDestFolder, new object[] { items, 20 });
		}</pre>
</div>
<p>
	 </p>
<p>
	最後這邊筆者隨手試著整理了一個簡易的類別，可以做到基本的壓縮、解壓縮、以及查驗壓縮檔內含有什麼內容，有興趣的可以自行參閱使用。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:9487ad36-c521-4090-908d-60245d4cd879" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c#" name="code">
	public enum ZipEntryType
	{
		File,
 		Folder
	}

	public class ZipEntry
	{
		#region Private Property
		private FolderItem m_ShellItem { get; set; }
		private IEnumerable&lt;ZipEntry&gt; _entrys; 
		#endregion

		#region Public Property
		/// &lt;summary&gt;
		/// Gets the name.
		/// &lt;/summary&gt;
		/// &lt;value&gt;The name.&lt;/value&gt;
		public string Name 
		{
			get
			{
				return m_ShellItem.Name;
			}
		}

		/// &lt;summary&gt;
		/// Gets the type.
		/// &lt;/summary&gt;
		/// &lt;value&gt;The type.&lt;/value&gt;
		public ZipEntryType Type 
		{
			get
			{
				return m_ShellItem.IsFolder ? ZipEntryType.Folder : ZipEntryType.File;
			}
		}

		/// &lt;summary&gt;
		/// Gets the modify date.
		/// &lt;/summary&gt;
		/// &lt;value&gt;The modify date.&lt;/value&gt;
		public DateTime ModifyDate
		{
			get
			{
				return m_ShellItem.ModifyDate;
			}
		}

		/// &lt;summary&gt;
		/// Gets the size.
		/// &lt;/summary&gt;
		/// &lt;value&gt;The size.&lt;/value&gt;
		public int Size 
		{
			get
			{
				return m_ShellItem.Size;
			}
		}

		public IEnumerable&lt;ZipEntry&gt; Entrys 
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
						var items = new List&lt;ZipEntry&gt;();
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
		/// &lt;summary&gt;
		/// Initializes a new instance of the &lt;see cref="ZipEntry"/&gt; struct.
		/// &lt;/summary&gt;
		/// &lt;param name="shellItem"&gt;The shell item.&lt;/param&gt;
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
		private IEnumerable&lt;ZipEntry&gt; _items; 
		#endregion


		#region Private Property
		/// &lt;summary&gt;
		/// Gets the m_ shell items.
		/// &lt;/summary&gt;
		/// &lt;value&gt;The m_ shell items.&lt;/value&gt;
		private FolderItems m_ShellItems
		{
			get
			{
				return _shellItems??(_shellItems = (new Shell()).NameSpace(FilePath).Items());
			}
		}
		#endregion


		#region Property
		/// &lt;summary&gt;
		/// Gets or sets the file.
		/// &lt;/summary&gt;
		/// &lt;value&gt;The file.&lt;/value&gt;
		public string FilePath { get; private set; }

		/// &lt;summary&gt;
		/// Gets the count.
		/// &lt;/summary&gt;
		/// &lt;value&gt;The count.&lt;/value&gt;
		public int Count
		{
			get
			{
				return m_ShellItems.Count;
			}
		}

		public IEnumerable&lt;ZipEntry&gt; Items 
		{
			get
			{
				if (_items == null)
				{
					var items = new List&lt;ZipEntry&gt;();
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
		/// &lt;summary&gt;
		/// Initializes a new instance of the &lt;see cref="ShellZip"/&gt; class.
		/// &lt;/summary&gt;
		/// &lt;param name="zipFile"&gt;The zip file.&lt;/param&gt;
		public ShellZip(string zipFile)
		{
			this.FilePath = zipFile;
		}
		#endregion


		#region Private Static Method
		/// &lt;summary&gt;
		/// Shells the copy to.
		/// &lt;/summary&gt;
		/// &lt;param name="from"&gt;From.&lt;/param&gt;
		/// &lt;param name="to"&gt;To.&lt;/param&gt;
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
		/// &lt;summary&gt;
		/// Compresses the specified source folder path.
		/// &lt;/summary&gt;
		/// &lt;param name="sourceFolderPath"&gt;The source folder path.&lt;/param&gt;
		/// &lt;param name="zipFile"&gt;The zip file.&lt;/param&gt;
		public static void Compress(string sourceFolderPath, string zipFile)
		{
			if (!Directory.Exists(sourceFolderPath))
				throw new DirectoryNotFoundException();

			if (!File.Exists(zipFile))
				File.Create(zipFile).Dispose();

			ShellCopyTo(sourceFolderPath, zipFile);
		}

		/// &lt;summary&gt;
		/// Des the compress.
		/// &lt;/summary&gt;
		/// &lt;param name="zipFile"&gt;The zip file.&lt;/param&gt;
		/// &lt;param name="destinationFolderPath"&gt;The destination folder path.&lt;/param&gt;
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
		/// &lt;summary&gt;
		/// Des the compress.
		/// &lt;/summary&gt;
		/// &lt;param name="destinationFolderPath"&gt;The destination folder path.&lt;/param&gt;
		public void DeCompress(string destinationFolderPath)
		{
			DeCompress(this.FilePath, destinationFolderPath);
		}
		#endregion
	}</pre>
</div>
<p>
	 </p>
<h2>
	Link</h2>
<ul>
	<li>
		System.Shell.Folder.copyHere method</li>
	<li>
		c#使用系統函數System.Shell.Folder.copyHere解壓.zip文件</li>
	<li>
		How to check when Shell32.Folder.CopyHere() is finished</li>
	<li>
		如何利用shell對.zip文件進行解壓縮</li>
	<li>
		Easily zip / unzip files using Windows Shell32</li>
	<li>
		Zip and Unzip files using Shell 32 component</li>
	<li>
		Compress Zip files with Windows Shell API and C#</li>
</ul>
