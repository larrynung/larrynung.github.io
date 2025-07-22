---
title: ".NET 4.0 New Feature - Environment.SpecialFolder"
date: "2010-11-29 09:58:32"
description: ".NET 4.0 New Feature - Environment.SpecialFolder"
tags: [CSharp]
---

.NET 4.0對於Environment.SpecialFolder的成員也做了些擴充，這邊將其擴充的成員列表如下：
              成員名稱        說明                  AdminTools        檔案系統目錄，用於儲存個別使用者的系統管理工具。 Microsoft Management Console (MMC) 會將自訂的主控台儲存至這個目錄，而這個目錄會隨著使用者一起漫遊。                  CDBurning        等候寫入光碟之檔案儲存目錄                  CommonAdminTools        電腦之所有使用者的系統管理工具目錄                  CommonDocuments        檔案系統目錄，包含所有使用者共用的文件。            
適用於 Windows NT 系統、Windows 95 和已安裝 Shfolder.dll 的 Windows 98 系統                  CommonMusic        所有使用者共用之音樂檔案儲存目錄                  CommonOemLinks        基於回溯相容性，Windows Vista 中可以辨識這個值，但已不再使用特殊資料夾本身                  CommonPictures        所有使用者共用之影像檔案儲存目錄                  CommonStartMenu        檔案系統目錄，包含在所有使用者的 [開始] 功能表上出現的程式和資料夾。            
適用於 Windows NT 系統                  CommonPrograms        這是存放多個應用程式共用元件的資料夾。           
適用 Windows NT 系統、Windows 2000 和 Windows XP 系統                  CommonStartup        檔案系統目錄，包含在所有使用者的 [啟動] 資料夾中出現的程式。            
適用於 Windows NT 系統                  CommonDesktopDirectory        檔案系統目錄，包含在所有使用者的桌面上出現的檔案和資料夾。            
適用於 Windows NT 系統                  CommonTemplates        檔案系統目錄，包含所有使用者可用的範本。            
適用於 Windows NT 系統                  CommonVideos        所有使用者共用之視訊檔案的儲存目錄                  Fonts        字型目錄                  MyVideos        使用者專屬視訊儲存目錄                  NetworkShortcuts        檔案系統目錄，包含 [網路上的芳鄰] 虛擬資料夾中可能存在的連結物件                  PrinterShortcuts        檔案系統目錄，包含 [印表機] 虛擬資料夾中可能存在的連結物件                  UserProfile        使用者的設定檔資料夾。 應用程式不應該在這個層級建立檔案或資料夾，而應該將其資料放在 ApplicationData 所參考的位置下                  CommonProgramFilesX86        [Program Files] 資料夾                  ProgramFilesX86        [Program Files] 資料夾                  Resources        資源目錄                  LocalizedResources        當地語系化的資源目錄                  SystemX86        Windows [System] 資料夾                  Windows        Windows 目錄或 SYSROOT。 這個值對應至 %windir% 或 %SYSTEMROOT% 環境變數          

實際撰寫個範例來看其對應的位置：
  
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
}

運行後的結果如下：

AdminTools
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
C:\WINDOWS
esources

LocalizedResources

SystemX86
C:\WINDOWS\system32

Windows
C:\WINDOWS

## Link

  Environment.SpecialFolder 列舉型別