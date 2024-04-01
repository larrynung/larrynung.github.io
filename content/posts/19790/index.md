---
title: ".NET 4.0 New Feature - Environment.SpecialFolder"
date: "2010-11-29 09:58:32"
description: ".NET 4.0 New Feature - Environment.SpecialFolder"
tags: [CSharp]
---

<p>.NET 4.0對於Environment.SpecialFolder的成員也做了些擴充，這邊將其擴充的成員列表如下：</p>  <table border="1" cellspacing="0" cellpadding="2" width="535"><tbody>     <tr>       <td valign="top" width="104">成員名稱</td>        <td valign="top" width="429">說明</td>     </tr>      <tr>       <td valign="top" width="109">AdminTools</td>        <td valign="top" width="429">檔案系統目錄，用於儲存個別使用者的系統管理工具。 Microsoft Management Console (MMC) 會將自訂的主控台儲存至這個目錄，而這個目錄會隨著使用者一起漫遊。</td>     </tr>      <tr>       <td valign="top" width="113">CDBurning</td>        <td valign="top" width="429">等候寫入光碟之檔案儲存目錄</td>     </tr>      <tr>       <td valign="top" width="117">CommonAdminTools</td>        <td valign="top" width="429">電腦之所有使用者的系統管理工具目錄</td>     </tr>      <tr>       <td valign="top" width="120">CommonDocuments</td>        <td valign="top" width="429">檔案系統目錄，包含所有使用者共用的文件。          <br />適用於 Windows NT 系統、Windows 95 和已安裝 Shfolder.dll 的 Windows 98 系統</td>     </tr>      <tr>       <td valign="top" width="123">CommonMusic</td>        <td valign="top" width="429">所有使用者共用之音樂檔案儲存目錄</td>     </tr>      <tr>       <td valign="top" width="125">CommonOemLinks</td>        <td valign="top" width="429">基於回溯相容性，Windows Vista 中可以辨識這個值，但已不再使用特殊資料夾本身</td>     </tr>      <tr>       <td valign="top" width="127">CommonPictures</td>        <td valign="top" width="429">所有使用者共用之影像檔案儲存目錄</td>     </tr>      <tr>       <td valign="top" width="129">CommonStartMenu</td>        <td valign="top" width="429">檔案系統目錄，包含在所有使用者的 [開始] 功能表上出現的程式和資料夾。          <br />適用於 Windows NT 系統</td>     </tr>      <tr>       <td valign="top" width="130">CommonPrograms</td>        <td valign="top" width="429">這是存放多個應用程式共用元件的資料夾。         <br />適用 Windows NT 系統、Windows 2000 和 Windows XP 系統</td>     </tr>      <tr>       <td valign="top" width="131">CommonStartup</td>        <td valign="top" width="429">檔案系統目錄，包含在所有使用者的 [啟動] 資料夾中出現的程式。          <br />適用於 Windows NT 系統</td>     </tr>      <tr>       <td valign="top" width="132">CommonDesktopDirectory</td>        <td valign="top" width="429">檔案系統目錄，包含在所有使用者的桌面上出現的檔案和資料夾。          <br />適用於 Windows NT 系統</td>     </tr>      <tr>       <td valign="top" width="133">CommonTemplates</td>        <td valign="top" width="429">檔案系統目錄，包含所有使用者可用的範本。          <br />適用於 Windows NT 系統</td>     </tr>      <tr>       <td valign="top" width="134">CommonVideos</td>        <td valign="top" width="429">所有使用者共用之視訊檔案的儲存目錄</td>     </tr>      <tr>       <td valign="top" width="134">Fonts</td>        <td valign="top" width="429">字型目錄</td>     </tr>      <tr>       <td valign="top" width="134">MyVideos</td>        <td valign="top" width="429">使用者專屬視訊儲存目錄</td>     </tr>      <tr>       <td valign="top" width="134">NetworkShortcuts</td>        <td valign="top" width="429">檔案系統目錄，包含 [網路上的芳鄰] 虛擬資料夾中可能存在的連結物件</td>     </tr>      <tr>       <td valign="top" width="134">PrinterShortcuts</td>        <td valign="top" width="429">檔案系統目錄，包含 [印表機] 虛擬資料夾中可能存在的連結物件</td>     </tr>      <tr>       <td valign="top" width="134">UserProfile</td>        <td valign="top" width="429">使用者的設定檔資料夾。 應用程式不應該在這個層級建立檔案或資料夾，而應該將其資料放在 ApplicationData 所參考的位置下</td>     </tr>      <tr>       <td valign="top" width="134">CommonProgramFilesX86</td>        <td valign="top" width="429">[Program Files] 資料夾</td>     </tr>      <tr>       <td valign="top" width="134">ProgramFilesX86</td>        <td valign="top" width="429">[Program Files] 資料夾</td>     </tr>      <tr>       <td valign="top" width="134">Resources</td>        <td valign="top" width="429">資源目錄</td>     </tr>      <tr>       <td valign="top" width="134">LocalizedResources</td>        <td valign="top" width="429">當地語系化的資源目錄</td>     </tr>      <tr>       <td valign="top" width="134">SystemX86</td>        <td valign="top" width="429">Windows [System] 資料夾</td>     </tr>      <tr>       <td valign="top" width="134">Windows</td>        <td valign="top" width="429">Windows 目錄或 SYSROOT。 這個值對應至 %windir% 或 %SYSTEMROOT% 環境變數</td>     </tr>   </tbody></table>  <p> </p>  <p> </p>  <p>實際撰寫個範例來看其對應的位置：</p>  <div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:1c26c4b8-9961-48e6-8ef0-4484408e0ba3" class="wlWriterSmartContent"><pre name="code" class="c#">
using System;
namespace ConsoleApplication1
{
    class Program
    {
        static Environment.SpecialFolder[] folderNames = { Environment.SpecialFolder.AdminTools,
                                                           Environment.SpecialFolder.CDBurning,
                                                           Environment.SpecialFolder.CommonAdminTools,
                                                           Environment.SpecialFolder.CommonDocuments,
                                                           Environment.SpecialFolder.CommonMusic,
                                                           Environment.SpecialFolder.CommonOemLinks,
                                                           Environment.SpecialFolder.CommonPictures,
                                                           Environment.SpecialFolder.CommonStartMenu,
                                                           Environment.SpecialFolder.CommonPrograms,
                                                           Environment.SpecialFolder.CommonStartup,
                                                           Environment.SpecialFolder.CommonDesktopDirectory,
                                                           Environment.SpecialFolder.CommonTemplates,
                                                           Environment.SpecialFolder.CommonVideos,
                                                           Environment.SpecialFolder.Fonts,
                                                           Environment.SpecialFolder.MyVideos,
                                                           Environment.SpecialFolder.NetworkShortcuts,
                                                           Environment.SpecialFolder.PrinterShortcuts,
                                                           Environment.SpecialFolder.UserProfile,
                                                           Environment.SpecialFolder.CommonProgramFilesX86,
                                                           Environment.SpecialFolder.ProgramFilesX86,
                                                           Environment.SpecialFolder.Resources,
                                                           Environment.SpecialFolder.LocalizedResources,
                                                           Environment.SpecialFolder.SystemX86,
                                                           Environment.SpecialFolder.Windows };
        static void Main(string[] args)
        {
            foreach (Environment.SpecialFolder value in folderNames)
            {
                Console.WriteLine(value.ToString());
                Console.WriteLine(Environment.GetFolderPath(value));
                Console.WriteLine();
            }
        }
    }
}</pre></div>

<p> </p>

<p>運行後的結果如下：</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:38e2a697-70f2-4754-ad83-627d049a1bce" class="wlWriterSmartContent"><pre name="code" class="xml">AdminTools
C:\Documents and Settings\[User Account]\「開始」功能表\程式集\系統管理工具

CDBurning
C:\Documents and Settings\[User Account]\Local Settings\Application Data\Microsoft\C
D Burning

CommonAdminTools
C:\Documents and Settings\All Users\「開始」功能表\程式集\系統管理工具

CommonDocuments
C:\Documents and Settings\All Users\Documents

CommonMusic
C:\Documents and Settings\All Users\Documents\My Music

CommonOemLinks


CommonPictures
C:\Documents and Settings\All Users\Documents\My Pictures

CommonStartMenu
C:\Documents and Settings\All Users\「開始」功能表

CommonPrograms
C:\Documents and Settings\All Users\「開始」功能表\程式集

CommonStartup
C:\Documents and Settings\All Users\「開始」功能表\程式集\啟動

CommonDesktopDirectory
C:\Documents and Settings\All Users\桌面

CommonTemplates
C:\Documents and Settings\All Users\Templates

CommonVideos
C:\Documents and Settings\All Users\Documents\My Videos

Fonts
C:\WINDOWS\Fonts

MyVideos


NetworkShortcuts
C:\Documents and Settings\[User Account]\NetHood

PrinterShortcuts
C:\Documents and Settings\[User Account]\PrintHood

UserProfile
C:\Documents and Settings\[User Account]

CommonProgramFilesX86


ProgramFilesX86


Resources
C:\WINDOWSesources

LocalizedResources


SystemX86
C:\WINDOWS\system32

Windows
C:\WINDOWS</pre></div>

<p> </p>

<h2>Link</h2>

<ul>
  <li>Environment.SpecialFolder 列舉型別</li>
</ul>
