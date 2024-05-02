---
title: "DotNetZip"
date: "2011-01-03 01:48:28"
description: "DotNetZip"
tags: [.NET Resource, CSharp]
---

<p>DotNetZip為一輕便又易於使用的開放源碼壓縮函式庫，開發人員可透過DotNetZip函式庫來做壓縮資料、讀取壓縮資料、更新壓縮資料、與列出壓縮檔資料內容等功能，能支援壓縮檔密碼保護、Zip64格式、產生自解壓縮檔、與Unicode編碼。</p>  <p>   <br />DotNetZip庫函式下載解壓後會看到主要有Ionic.Zip.dll、Ionic.Zip.CF.dll、與Ionic.Zip.Reduced.dll這三個Dll。Ionic.Zip.dll為PC程式所要使用的參考組件，Ionic.Zip.CF.dll為行動裝置所要使用的參考組件，Ionic.Zip.Reduced.dll則是精簡後的參考組件，少了產生自解壓縮檔的功能，檔案大小會比較小，這邊可依自己的需求將參考組件加入參考。</p>  <p>   <br />在前置的準備上，除需將參考組件加入參考外，我們還需將Ionic.Zip命名空間加入。而在使用上，主要要使用的是ZipFile這個類別，這邊將其較重要的成員列表如下：</p>  <p> </p>  <p>Property</p>  <table border="1" cellspacing="0" cellpadding="2" width="474"><tbody>     <tr>       <td valign="top" width="177">Name</td>        <td valign="top" width="294">Description</td>     </tr>      <tr>       <td valign="top" width="177">Password</td>        <td valign="top" width="294">設定壓縮檔密碼，若無密碼可不設定或設定null。</td>     </tr>      <tr>       <td valign="top" width="177">Comment</td>        <td valign="top" width="294">取得或設定壓縮檔註解。</td>     </tr>      <tr>       <td valign="top" width="177">CompressionLevel</td>        <td valign="top" width="294">取得或設定壓縮等級。</td>     </tr>      <tr>       <td valign="top" width="177">Count</td>        <td valign="top" width="294">取得壓縮檔內被壓縮的檔案數量。</td>     </tr>      <tr>       <td valign="top" width="177">MaxOutputSegmentSize</td>        <td valign="top" width="294">取得或設定最大輸出大小，設定完後壓縮時會依此設定值下去分割壓縮檔案。其可接受的輸入區間65536~2147483647。</td>     </tr>   </tbody></table>  <p>   <br />Method</p>  <table border="1" cellspacing="0" cellpadding="2" width="473"><tbody>     <tr>       <td valign="top" width="181">Name</td>        <td valign="top" width="290">Description</td>     </tr>      <tr>       <td valign="top" width="181">AddFile</td>        <td valign="top" width="290">加入指定檔案至壓縮檔。</td>     </tr>      <tr>       <td valign="top" width="181">AddDirectory</td>        <td valign="top" width="290">加入指定目錄至壓縮檔。</td>     </tr>      <tr>       <td valign="top" width="181">Save</td>        <td valign="top" width="290">儲存壓縮檔。</td>     </tr>      <tr>       <td valign="top" width="181">UpdateFile</td>        <td valign="top" width="290">更新檔案。</td>     </tr>      <tr>       <td valign="top" width="181">RemoveEntry</td>        <td valign="top" width="290">移除壓縮檔內指定的元素。</td>     </tr>      <tr>       <td valign="top" width="181">ExtractAll</td>        <td valign="top" width="290">解壓縮所有檔案。</td>     </tr>      <tr>       <td valign="top" width="181">SaveSelfExtractor</td>        <td valign="top" width="290">儲存自解壓縮檔。</td>     </tr>   </tbody></table>  <p> </p>  <p>Event</p>  <table border="1" cellspacing="0" cellpadding="2" width="470"><tbody>     <tr>       <td valign="top" width="180">Name</td>        <td valign="top" width="288">Description</td>     </tr>      <tr>       <td valign="top" width="180">SaveProgress</td>        <td valign="top" width="288">儲存進度。</td>     </tr>      <tr>       <td valign="top" width="180">ExtractProgress</td>        <td valign="top" width="288">解壓縮進度。</td>     </tr>   </tbody></table>  <p> </p>  <p>在壓縮時，主要是帶入指定壓縮檔的檔名到建構子中建立物件實體，透過屬性設定一些細部資訊，透過AddFile、AddDirectory、AddFileFromString...等方法的呼叫將要壓縮的檔案放入壓縮檔中,再透過Save方法產生對應的壓縮檔案。</p>  <div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:6bcb5980-e143-4cfc-a44b-2f33338adc25" class="wlWriterSmartContent"><pre name="code" class="c#">        static void ZipToZipFile(string archiveFile, string archivePassword, string archiveCommon, string zipPath)
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
        }</pre></div>

<p> </p>

<p>或是改呼叫SaveSelfExtractor方法產生自解壓縮檔案。</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:de82fd37-d191-4bd6-b283-6076e3572719" class="wlWriterSmartContent"><pre name="code" class="c#">        static void ZipToSelfExtractor(string archiveFile, string archivePassword, string archiveCommon, string zipPath)
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
        }</pre></div>

<p> </p>

<p>要讀取壓縮檔資訊時，可帶入指定壓縮檔的檔名到建構子中建立物件實體，透過屬性取得壓縮檔的細部資訊，或透過ZipEntry取得被壓縮的檔案其細部資訊。</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:1998792e-6851-4fca-928a-ebd7eb8cc88b" class="wlWriterSmartContent"><pre name="code" class="c#">        static void ShowZipInfo(string archiveFile)
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
        }</pre></div>

<p> </p>

<p>解壓縮時，則是帶入指定壓縮檔的檔名到建構子中建立物件實體，透過ExtractAll解壓縮壓縮檔內全部的內容。</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:40d24615-d561-454e-9e48-0d004b19cac0" class="wlWriterSmartContent"><pre name="code" class="c#">        static void ExtractAll(string archiveFile, string targetPath)
        {
            using (ZipFile zip = new ZipFile(archiveFile))
            {
                zip.ExtractAll(targetPath);
            }
        }</pre></div>

<p> </p>

<p>或是透過ZipFile.Entries找到指定的ZipEntry，並呼叫ZipEntry.Extract去做解壓縮的動作。</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:ef3d9268-49f8-411d-bd67-fafbb462b4f4" class="wlWriterSmartContent"><pre name="code" class="c#">        static void Extract(string archiveFile,string fileInArchive, string targetPath)
        {
            using (ZipFile zip = new ZipFile(archiveFile))
            {
                var zipEntry = (from item in zip.Entries where item.FileName == fileInArchive select item).FirstOrDefault();
                if (zipEntry != null)
                    zipEntry.Extract(targetPath);
            }
        }</pre></div>

<p> </p>

<h2>Link</h2>

<ul>
  <li>介紹幾款好用的壓縮函示庫：SharpZipLib 與 DotNetZip </li>

  <li>Manage ZIP files from within .NET applications </li>

  <li>DotNetZip Library </li>

  <li>DotNetZip v1.9 </li>

  <li>Getting Started with DotNetZip </li>

  <li>DotNetZip 1.7 Release (2009/2/10) </li>
</ul>
