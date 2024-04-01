---
title: "[C#]從PE檔中讀取組件資訊"
date: "2013-11-06 12:00:00"
description: "[C#]從PE檔中讀取組件資訊"
tags: [CSharp]
---

<p>
	筆者在[C#]PE檔案格式簡易介紹與PE檔案的檢測這篇針對PE檔的格式已經做了初步的介紹，這邊接著這個議題下去探討，嘗試從PE檔中讀取一些進階的資訊，像是CPU的版本以及PE檔編譯時所設定的.NET Framework的版本。</p>
<p>
	 </p>
<p>
	延續[C#]PE檔案格式簡易介紹與PE檔案的檢測這篇，筆者已經帶到了PE Header，所以就不重複再帶這部分了，接著讓我們繼續往下看IMAGE_FILE_HEADER的部分。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:660da19f-0a6d-4816-8b46-f51eea3d5593" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c" name="code">
typedef struct _IMAGE_NT_HEADERS {
  DWORD                 Signature;
  IMAGE_FILE_HEADER     FileHeader;
  IMAGE_OPTIONAL_HEADER OptionalHeader;
} IMAGE_NT_HEADERS, *PIMAGE_NT_HEADERS;
</pre>
</div>
<p>
	 </p>
<p>
	IMAGE_FILE_HEADER的結構裡面比較重要的是Machine這個成員，它可以表示組件的目標平台。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:6dbf5ab9-1277-4475-bd97-c4de754be03d" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c" name="code">
typedef struct _IMAGE_FILE_HEADER {
  WORD  Machine;
  WORD  NumberOfSections;
  DWORD TimeDateStamp;
  DWORD PointerToSymbolTable;
  DWORD NumberOfSymbols;
  WORD  SizeOfOptionalHeader;
  WORD  Characteristics;
} IMAGE_FILE_HEADER, *PIMAGE_FILE_HEADER;</pre>
</div>
<p>
	<img alt="image" border="0" height="291" src="\images\posts�b420-305d-4175-a34c-64b3e9c4fab3\image_thumb.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="644" /></p>
<p>
	 </p>
<p>
	若不知道目標平台為何，可看一下Visual Studio的專案屬性設定那邊就知道在說什麼了。</p>
<p>
	<img alt="image" border="0" height="43" src="\images\posts�b420-305d-4175-a34c-64b3e9c4fab3\image_thumb_5.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="408" /></p>
<p>
	 </p>
<p>
	接著下來是IMAGE_OPTIONAL_HEADER...</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:af19de29-e546-4dc6-aee4-78c87cd842df" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c" name="code">
typedef struct _IMAGE_OPTIONAL_HEADER {
  WORD                 Magic;
  BYTE                 MajorLinkerVersion;
  BYTE                 MinorLinkerVersion;
  DWORD                SizeOfCode;
  DWORD                SizeOfInitializedData;
  DWORD                SizeOfUninitializedData;
  DWORD                AddressOfEntryPoint;
  DWORD                BaseOfCode;
  DWORD                BaseOfData;
  DWORD                ImageBase;
  DWORD                SectionAlignment;
  DWORD                FileAlignment;
  WORD                 MajorOperatingSystemVersion;
  WORD                 MinorOperatingSystemVersion;
  WORD                 MajorImageVersion;
  WORD                 MinorImageVersion;
  WORD                 MajorSubsystemVersion;
  WORD                 MinorSubsystemVersion;
  DWORD                Win32VersionValue;
  DWORD                SizeOfImage;
  DWORD                SizeOfHeaders;
  DWORD                CheckSum;
  WORD                 Subsystem;
  WORD                 DllCharacteristics;
  DWORD                SizeOfStackReserve;
  DWORD                SizeOfStackCommit;
  DWORD                SizeOfHeapReserve;
  DWORD                SizeOfHeapCommit;
  DWORD                LoaderFlags;
  DWORD                NumberOfRvaAndSizes;
  IMAGE_DATA_DIRECTORY DataDirectory[IMAGE_NUMBEROF_DIRECTORY_ENTRIES];
} IMAGE_OPTIONAL_HEADER, *PIMAGE_OPTIONAL_HEADER;</pre>
</div>
<p>
	 </p>
<p>
	這邊一樣也有很多資訊可以讀取，比較重要的是Magic與Subsystem這兩個成員，以Magic來說它可以讓你知道目標平台是否是設定為Any CPU。</p>
<p>
	<img alt="image" border="0" height="329" src="\images\posts�b420-305d-4175-a34c-64b3e9c4fab3\image_thumb_1.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="644" /></p>
<p>
	 </p>
<p>
	而SubSystem可以讓我們判斷該組件是有視窗的GUI程式還是Console程式，若值為2則是GUI程式，值為3則是Console程式。</p>
<p>
	<img alt="image" border="0" height="148" src="\images\posts�b420-305d-4175-a34c-64b3e9c4fab3\image23_thumb.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="644" /></p>
<p>
	 </p>
<p>
	最後比較重要的資訊就是CLR Header內的資訊，IMAGE_OPTIONAL_HEADER後有16個DataDirectory，CLR Header位於第15個DataDirectory，裡面可取得的資訊有組件所用的.Net Framework版本等。</p>
<p>
	<img alt="image" border="0" height="344" src="\images\posts�b420-305d-4175-a34c-64b3e9c4fab3\image_thumb_3.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="494" /></p>
<p>
	 </p>
<p>
	實際使用上程式碼該如何撰寫可參閱How to detect .NET 2.0 vs. .NET 4.0 assemblies, and x86 vs. x64 vs. AnyCPU</a>這篇所提供的<a href="http://wyupdate.googlecode.com/files/AssemblyParser-v2.zip">程式碼範例，這邊將主要的片段節錄如下，搭配上面的解說去看應該不會太難理解：</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:e0938709-3906-4e44-b9f5-a6107da88101" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c#" name="code">
using System.IO;

/// &lt;summary&gt;
/// AssemblyDetails is used in the update builder, wyBuild (http://wyday.com/wybuild/), 
/// to automagically detect .NET assemblies properties, namely:
///  - if they are compiled with a Strong Name,
///  - CPUVersion the assembly was compiled as,
///  - .NET Framework the assembly was compiled for (.NET 2.0 or 4.0)
/// &lt;/summary&gt;
public class AssemblyDetails
{
    /// &lt;summary&gt;
    /// The CPUVersion the assembly was compiled with.
    /// &lt;/summary&gt;
    public CPUVersion CPUVersion;

    /// &lt;summary&gt;
    /// The .NET Framework required for the assembly.
    /// &lt;/summary&gt;
    public FrameworkVersion FrameworkVersion;

    /// &lt;summary&gt;
    /// True if the assembly has a strong name. (Neccessary for GAC installations)
    /// &lt;/summary&gt;
    public bool StrongName;


    /// &lt;summary&gt;
    /// Get the AssemblyDetails of a .NET 2.0+ assembly.
    /// &lt;/summary&gt;
    /// &lt;param name="file"&gt;The file to get the AssemblyDetails of.&lt;/param&gt;
    /// &lt;returns&gt;An AssemblyDetails object for .NET 2.0+ assemblies. Null otherwise.&lt;/returns&gt;
    public static AssemblyDetails FromFile(string file)
    {
        AssemblyDetails assembInfo = new AssemblyDetails();

        using (FileStream s = new FileStream(file, FileMode.Open, FileAccess.Read))
        {
            using (BinaryReader r = new BinaryReader(s))
            {
                byte[] bytes = r.ReadBytes(2);

                // Verify file starts with "MZ" signature.
                if ((bytes[0] != 0x4d) || (bytes[1] != 0x5a))
                {
                    // Not a PE file.
                    return null;
                }

                // Partion II, 25.2.1

                // OFFSET_TO_PE_HEADER_OFFSET = 0x3c
                s.Seek(0x3c, SeekOrigin.Begin);

                // read the offset to the PE Header
                uint offset = r.ReadUInt32();

                // go to the beginning of the PE Header
                s.Seek(offset, SeekOrigin.Begin);

                bytes = r.ReadBytes(4);

                // Verify PE header starts with 'PE  '.
                if ((bytes[0] != 0x50) || (bytes[1] != 0x45) || (bytes[2] != 0) || (bytes[3] != 0))
                {
                    // Not a PE file.
                    return null;
                }


                // It's a PE file, verify that it has the right "machine" code.
                // Partion II, 25.2.2
                //
                ushort machineCode = r.ReadUInt16();

                // IMAGE_FILE_MACHINE_AMD64 (aka x64) = 0x8664
                // IMAGE_FILE_MACHINE_I386 (aka x86) = 0x14c
                if (!(machineCode == 0x014c || machineCode == 0x8664))
                {
                    // Invalid or unrecognized PE file of some kind.
                    return null;
                }


                // Locate the PE_OPTIONAL_HEADER


                // The PE_FILE_HEADER is 20bytes long we already
                // read the 2 byte machine code (hence 18byte seek)
                s.Seek(18, SeekOrigin.Current);

                ushort magic = r.ReadUInt16();

                switch (magic)
                {
                    case 0x10b: // PE32

                        // set to AnyCPU for now - we'll check later if image is x86 specific
                        assembInfo.CPUVersion = CPUVersion.AnyCPU;

                        break;

                    case 0x20b: // PE32+ (aka x64)
                        assembInfo.CPUVersion = CPUVersion.x64;
                        break;

                    default: // unknown assembly type
                        return null;
                }


                // Read the SectionAlignment &amp; FileAlignment for
                // conversion from RVA to file address
                s.Seek(30, SeekOrigin.Current);

                uint sectionAlignment = r.ReadUInt32();
                uint fileAlignment = r.ReadUInt32();


                // go to 'NumberOfRvaAndSizes' in the PE Header
                // at 92/108 from start of PE Header for PE32/PE32+
                s.Seek(magic == 0x10b ? 52 : 68, SeekOrigin.Current);

                // verify that the number of data directories is 0x10.

                uint numDataDirs = r.ReadUInt32();  // Partition II, 25.2.3.2

                if (numDataDirs != 0x10) // Partition II, 25.2.3.2
                {
                    // Invalid or unrecognized PE file of some kind.
                    return null;
                }


                // Go to the CLR Runtime Header
                // at 208/224 from start of PE Header for PE32/PE32+
                s.Seek(112, SeekOrigin.Current);


                // Check for the existence of a non-null CLI header.
                // If found, this is an assembly of some kind, otherwise
                // it's a native PE file of one kind or another.

                uint rvaCLIHeader = r.ReadUInt32();  // Partition II, 25.2.3.3, CLI Header (rva)
                // uint cliHeaderSize = UIntFromBytes(pPEOptionalHeader + 212); // Partition II, 25.2.3.3, CLI Header (size)

                if (rvaCLIHeader == 0)
                {
                    // Not an assembly.
                    return null;
                }


                // Partition II, 25.3.3 (CLI Header)


                // Go to the begginning of the CLI header (RVA -&gt; file address)

                /*
                -&gt; Converting from Relative Virtual Address to File Address:

                   FA = RVA - sectionAlignment + fileAlignment
                 
                       The section alignment in memory is sectionAlignment (usually 0x2000),
                   and since the RVA for the CLR header is 2008, on subtracting 2000 from
                   2008, the difference comes to 8. Thus, the CLR header is placed 8 bytes
                   away from the start of the section.
 
                       A file on disk has the alignment of fileAlignment (usually 512 bytes).
                   Therefore, the first section would start at position 512 from the start
                   of the file. As the CLR is 8 bytes away from the section start, 8 is added
                   to 512, (section start for a file on disk), thereby arriving at a value of 520.
                   The next 72 bytes (0x48) are picked up from this position, since they
                   constitute the CLR header, and they are loaded at location 0x4002008.

                */

                // Also, skip the CLI header size = 4 bytes
                s.Seek((rvaCLIHeader - sectionAlignment + fileAlignment) + 4, SeekOrigin.Begin);

                ushort majorVersion = r.ReadUInt16();
                ushort minorVersion = r.ReadUInt16();

                // 2.5 means the file is a .NET Framework 2.0+ assembly
                if (!(majorVersion == 2 &amp;&amp; minorVersion == 5))
                    return null;


                // RVA for the MetaData (we'll read the metadata later)
                uint rvaMetaData = r.ReadUInt32();
                s.Seek(4, SeekOrigin.Current); // skip the size

                // Partition II, 25.3.3.1

                // read the CLI flags
                uint cliFlags = r.ReadUInt32();

                // Detect if compiled with Platform Target of "x86"
                // COMIMAGE_FLAGS_32BITREQUIRED = 0x2;
                if (assembInfo.CPUVersion == CPUVersion.AnyCPU &amp;&amp; (cliFlags &amp; 0x2) == 0x2)
                {
                    assembInfo.CPUVersion = CPUVersion.x86;
                }

                // Detect if the assembly is built with a strong name
                // CLI_FLAG_STRONG_NAME_SIGNED = 0x8;
                assembInfo.StrongName = ((cliFlags &amp; 0x8) == 0x8);

                s.Seek((rvaMetaData - sectionAlignment + fileAlignment) + 12, SeekOrigin.Begin);

                
                // Read the framework version required (meta data - Partition II, 24.2.1 - pg 200)

                // read the version string length
                int versionLen = r.ReadInt32();

                char[] versionStr = r.ReadChars(versionLen);

                // read the .NET framework version required from the meta-data
                //Note: we only read the first 2 numbers of the version - if you want to
                //      detect beta vs. rc vs. rtm, then read the whole version.
                // We assume no one will be stupid enough to use beta created exes/dlls in the wild.
                if (versionStr[1] == '2' &amp;&amp; versionStr[3] == '0')
                    assembInfo.FrameworkVersion = FrameworkVersion.Net2_0;
                else if (versionStr[1] == '4' &amp;&amp; versionStr[3] == '0')
                    assembInfo.FrameworkVersion = FrameworkVersion.Net4_0;
                else
                    assembInfo.FrameworkVersion = FrameworkVersion.Unknown;
            }
        }

        return assembInfo;
    }
}</pre>
</div>
<p>
	 </p>
<h2>
	Link</h2>
<ul>
	<li>
		How to detect .NET 2.0 vs. .NET 4.0 assemblies, and x86 vs. x64 vs. AnyCPU</li>
	<li>
		[C#]PE檔案格式簡易介紹與PE檔案的檢測</li>
	<li>
		Peering Inside the PE: A Tour of the Win32 Portable Executable File Format</li>
	<li>
		IMAGE_FILE_HEADER structure</li>
	<li>
		IMAGE_OPTIONAL_HEADER structure</li>
	<li>
		IMAGE_DATA_DIRECTORY structure</li>
	<li>
		Windows PE Header</li>
	<li>
		Anatomy of a .NET Assembly - CLR metadata 1</li>
	<li>
		The PE File Format</li>
	<li>
		How to learn type of an executed file?</li>
	<li>
		How to determine whether a file is a .NET Assembly or not?</li>
</ul>
