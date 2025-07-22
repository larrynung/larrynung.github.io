---
title: "DotNetZip"
date: "2011-01-03 01:48:28"
description: "DotNetZip"
tags: [.NET Resource, CSharp]
---

DotNetZip為一輕便又易於使用的開放源碼壓縮函式庫，開發人員可透過DotNetZip函式庫來做壓縮資料、讀取壓縮資料、更新壓縮資料、與列出壓縮檔資料內容等功能，能支援壓縮檔密碼保護、Zip64格式、產生自解壓縮檔、與Unicode編碼。
       
DotNetZip庫函式下載解壓後會看到主要有Ionic.Zip.dll、Ionic.Zip.CF.dll、與Ionic.Zip.Reduced.dll這三個Dll。Ionic.Zip.dll為PC程式所要使用的參考組件，Ionic.Zip.CF.dll為行動裝置所要使用的參考組件，Ionic.Zip.Reduced.dll則是精簡後的參考組件，少了產生自解壓縮檔的功能，檔案大小會比較小，這邊可依自己的需求將參考組件加入參考。       
在前置的準備上，除需將參考組件加入參考外，我們還需將Ionic.Zip命名空間加入。而在使用上，主要要使用的是ZipFile這個類別，這邊將其較重要的成員列表如下：  

Property
              Name        Description                  Password        設定壓縮檔密碼，若無密碼可不設定或設定null。                  Comment        取得或設定壓縮檔註解。                  CompressionLevel        取得或設定壓縮等級。                  Count        取得壓縮檔內被壓縮的檔案數量。                  MaxOutputSegmentSize        取得或設定最大輸出大小，設定完後壓縮時會依此設定值下去分割壓縮檔案。其可接受的輸入區間65536~2147483647。               
Method              Name        Description                  AddFile        加入指定檔案至壓縮檔。                  AddDirectory        加入指定目錄至壓縮檔。                  Save        儲存壓縮檔。                  UpdateFile        更新檔案。                  RemoveEntry        移除壓縮檔內指定的元素。                  ExtractAll        解壓縮所有檔案。                  SaveSelfExtractor        儲存自解壓縮檔。          

Event
              Name        Description                  SaveProgress        儲存進度。                  ExtractProgress        解壓縮進度。          

在壓縮時，主要是帶入指定壓縮檔的檔名到建構子中建立物件實體，透過屬性設定一些細部資訊，透過AddFile、AddDirectory、AddFileFromString...等方法的呼叫將要壓縮的檔案放入壓縮檔中,再透過Save方法產生對應的壓縮檔案。
          static void ZipToZipFile(string archiveFile, string archivePassword, string archiveCommon, string zipPath)
        {
            using (ZipFile zip = new ZipFile(archiveFile))
            {
                zip.Password = archivePassword;
                zip.Comment = archiveCommon;
                zip.CompressionLevel = Ionic.Zlib.CompressionLevel.BestCompression;
                //zip.MaxOutputSegmentSize = 65536;
                zip.AddFiles(System.IO.Directory.GetFiles(zipPath), string.Empty);
                zip.Save();
            }
        }

或是改呼叫SaveSelfExtractor方法產生自解壓縮檔案。

        static void ZipToSelfExtractor(string archiveFile, string archivePassword, string archiveCommon, string zipPath)
        {
            using (ZipFile zip = new ZipFile())
            {
                zip.Password = archivePassword;
                zip.Comment = archiveCommon;
                zip.CompressionLevel = Ionic.Zlib.CompressionLevel.BestCompression;
                //zip.MaxOutputSegmentSize = 65536;
                zip.AddFiles(System.IO.Directory.GetFiles(zipPath), string.Empty);
                zip.SaveSelfExtractor(archiveFile, SelfExtractorFlavor.WinFormsApplication);
            }
        }

要讀取壓縮檔資訊時，可帶入指定壓縮檔的檔名到建構子中建立物件實體，透過屬性取得壓縮檔的細部資訊，或透過ZipEntry取得被壓縮的檔案其細部資訊。

        static void ShowZipInfo(string archiveFile)
        {
            using (ZipFile zip = new ZipFile(archiveFile))
            {
                Console.WriteLine(zip.Comment);
                Console.WriteLine(zip.CompressionLevel);
                Console.WriteLine(zip.Count.ToString());
                foreach (ZipEntry item in zip)
                {
                    Console.WriteLine(item.FileName);
                }
            }
        }

解壓縮時，則是帶入指定壓縮檔的檔名到建構子中建立物件實體，透過ExtractAll解壓縮壓縮檔內全部的內容。

        static void ExtractAll(string archiveFile, string targetPath)
        {
            using (ZipFile zip = new ZipFile(archiveFile))
            {
                zip.ExtractAll(targetPath);
            }
        }

或是透過ZipFile.Entries找到指定的ZipEntry，並呼叫ZipEntry.Extract去做解壓縮的動作。

        static void Extract(string archiveFile,string fileInArchive, string targetPath)
        {
            using (ZipFile zip = new ZipFile(archiveFile))
            {
                var zipEntry = (from item in zip.Entries where item.FileName == fileInArchive select item).FirstOrDefault();
                if (zipEntry != null)
                    zipEntry.Extract(targetPath);
            }
        }

## Link

  介紹幾款好用的壓縮函示庫：SharpZipLib 與 DotNetZip 

  Manage ZIP files from within .NET applications 

  DotNetZip Library 

  DotNetZip v1.9 

  Getting Started with DotNetZip 

  DotNetZip 1.7 Release (2009/2/10)