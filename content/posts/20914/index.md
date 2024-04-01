---
title: ".NET 4.0 New Feature - 遍尋檔案系統項目與檔案內容的效能強化"
date: "2011-01-20 01:32:48"
description: ".NET 4.0 New Feature - 遍尋檔案系統項目與檔案內容的效能強化"
tags: [CSharp]
---

<p>.NET 4.0 BCL 在遍尋檔案系統項目與檔案內容方面新增了一些新的方法，可先回傳集合的迭代器物件，待開始遍尋迭代器時才逐步載入對應的資料，可延遲載入動作的執行，避免處理大量資料時的效能耗費，可改進效能並保有迭代器簡單好用的優點。</p>  <p> </p>  <p>在遍尋檔案系統項目方面，BCL在Directory類別新增了EnumerateFiles、EnumerateDirectories、與EnumerateFileSystemEntries三個方法，分別對應至原先的GetFiles、GetDirectories、與GetFileSystemEntries；在DirectoryInfo則新增了EnumerateFiles、EnumerateDirectories、與EnumerateFileSystemInfos三個方法，分別對應至原先的GetFiles、GetDirectories、與GetFileSystemInfos。這些新的方法可完全替代舊有的方法，跟以往舊有的不同的是，新的方法不會在一開始載入全部的資料，而會自己延遲載入處理，但對使用者來說程式碼跟使用舊有的方法幾乎是沒有任何的差異，程式的撰寫並不會因方法的替換而需採用不同架構的寫法，都是直接對集合下去處理。</p>  <p> </p>  <p>Directory</p>  <table cellspacing="0" cellpadding="2" width="507" border="1"><tbody>     <tr>       <td valign="top" width="194">Name</td>        <td valign="top" width="200">Description</td>        <td valign="top" width="107">Mapping</td>     </tr>      <tr>       <td valign="top" width="198">EnumerateFiles</td>        <td valign="top" width="200">傳回指定之路徑中檔案名稱的可列舉集合</td>        <td valign="top" width="107">GetFiles</td>     </tr>      <tr>       <td valign="top" width="200">EnumerateDirectories</td>        <td valign="top" width="200">傳回指定之路徑中目錄名稱的可列舉集合</td>        <td valign="top" width="107">GetDirectories</td>     </tr>      <tr>       <td valign="top" width="202">EnumerateFileSystemEntries</td>        <td valign="top" width="200">傳回指定之路徑中檔案系統項目的可列舉集合</td>        <td valign="top" width="107">GetFileSystemEntries</td>     </tr>   </tbody></table>  <p> </p>  <p>DirectoryInfo</p>  <table cellspacing="0" cellpadding="2" width="507" border="1"><tbody>     <tr>       <td valign="top" width="181">Name</td>        <td valign="top" width="177">Description</td>        <td valign="top" width="141">Mapping</td>     </tr>      <tr>       <td valign="top" width="185">EnumerateFiles</td>        <td valign="top" width="177">傳回目前目錄中檔案資訊的可列舉集合</td>        <td valign="top" width="141">GetFiles</td>     </tr>      <tr>       <td valign="top" width="187">EnumerateDirectories</td>        <td valign="top" width="177">傳回目前目錄中目錄資訊的可列舉集合</td>        <td valign="top" width="141">GetDirectories</td>     </tr>      <tr>       <td valign="top" width="189">EnumerateFileSystemInfos</td>        <td valign="top" width="177">傳回目前目錄中檔案系統資訊的可列舉集合</td>        <td valign="top" width="141">GetFileSystemInfos</td>     </tr>   </tbody></table>  <p> </p>  <p>在檔案內容的處理上，.NET 4.0 BCL一樣也做了相對應的強化，新增ReadLines方法取代舊有的ReadAllLines，並在WriteAllLines加入對迭代器處理的多載版本，對大型檔案做存取時可增進處理的效能。</p>  <p> </p>  <p>File</p>  <table cellspacing="0" cellpadding="2" width="501" border="1"><tbody>     <tr>       <td valign="top" width="136">Name</td>        <td valign="top" width="226">Description</td>        <td valign="top" width="134">Mapping</td>     </tr>      <tr>       <td valign="top" width="138">ReadLines</td>        <td valign="top" width="226">讀取檔案的所有行</td>        <td valign="top" width="134">ReadAllLines</td>     </tr>      <tr>       <td valign="top" width="139">WriteAllLines</td>        <td valign="top" width="226">建立新檔案，並於檔案中寫入一個或多個字串，然後關閉檔案</td>        <td valign="top" width="134">(None)</td>     </tr>   </tbody></table>  <p> </p>  <p>這邊以檔案內容的處理為例說明效能的強化與對程式撰寫的影響。以往在做檔案內容的處理時，我們使用ReadAllLines方法會一次將檔案的內容全部取回，因此在處理大型檔案時整個系統會被卡住，待全部檔案內容取回才會往下運行：</p>  <div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:6e285fa3-45a1-4f2c-949d-0e7bdb4db77e" style="padding-right: 0px; display: inline; padding-left: 0px; float: none; padding-bottom: 0px; margin: 0px; padding-top: 0px"><pre name="code" class="c#">        static string GetFileContent(string fileName, int lineIdx)
        {
            int idx = 0;
            var lines = File.ReadAllLines(fileName);
            foreach (string ling in lines)
            {
                if (++idx == lineIdx)
                    return ling;
            }
            return string.Empty;
        }</pre></div>

<p> </p>

<p>在.NET 4.0以前若要避免這樣的問題，我們得用StreamReader一行一行的讀取判斷，這樣是可以解決效能上的問題，但是撰寫時就無法直接以遍尋集合的方式下去處理，程式碼會變得較為複雜不好處理。</p>

<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:669c1f63-4225-41f5-a7b3-1da31ded7933" style="padding-right: 0px; display: inline; padding-left: 0px; float: none; padding-bottom: 0px; margin: 0px; padding-top: 0px"><pre name="code" class="c#">        static string GetFileContent(string fileName, int lineIdx)
        {
            using (TextReader reader = new StreamReader(fileName))
            {
                int idx = 0;
                string line;
                while ((line = reader.ReadLine()) != null)
                {
                    if (++idx == lineIdx)
                        return line;
                }
            }
            return string.Empty;
        }</pre></div>

<p> </p>

<p>在.NET 4.0後新增了ReadLines方法，我們能藉此方法避開效能上的問題，也能保有舊有遍尋集合的處理方式，而不會增加程式撰寫人員的負擔。</p>

<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:759bc07a-c169-461a-a966-ed1912091dff" style="padding-right: 0px; display: inline; padding-left: 0px; float: none; padding-bottom: 0px; margin: 0px; padding-top: 0px"><pre name="code" class="c#">        static string GetFileContent(string fileName, int lineIdx)
        {
            int idx = 0;
            var lines = File.ReadLines(fileName);
            foreach (string ling in lines)
            {
                if (++idx == lineIdx)
                    return ling;
            }
            return string.Empty;
        }</pre></div>
