---
layout: post
title: "Microsoft Monitoring Agent"
date: 2013-11-20 23:48
comments: true
categories: 
---

Microsoft Monitoring Agent (MMA) 是可獨立運行的 IntelliTrace，不像以前的 IntelliTrace 需綁在Visual Studio 上。可用來收集診斷資料，例如效能標準、事件記錄檔和Trace。 

<!--More-->

透過 Microsoft Monitoring Agent ，我們可以Follow微軟建議的開發流程， 編寫程式=>建置=>發佈=>偵測=>診斷，不斷的進行迭代，讓程式更加的穩定。  

{% img /images/posts/MicrosoftMonitoringAgent/1.png %}


程式可至 [Microsoft Monitoring Agent 2013](http://www.microsoft.com/en-us/download/details.aspx?id=40316) 這邊下載安裝。  

Microsoft Monitoring Agent 建議環境為.NET Framework 3.5+、以及PowerShell 3.0+。

若是PowerShell 2.0可另行開啟PowerShell，並輸入下列命令去Import module，不然會無法使用後續的PowerShell Cmdlet。 

    PS C:>Import-Module "C:\Program Files\Microsoft Monitoring Agent\Agent\PowerShell\Microsoft.MonitoringAgent.PowerShell\Microsoft.MonitoringAgent.PowerShell.dll"

{% img /images/posts/MicrosoftMonitoringAgent/2.png %}


在使用上，我們只要開啟 PowerShell ，輸入下列命令將之啟動，讓 Microsoft Monitoring Agent 開始進行偵測。

    Start-WebApplicationMonitoring


命令叫用的同時，會詢問要監測的網站 (即IIS上網站的名稱)、偵測的類型 (Monitor、Trace、Custom)、以及 Intellitrace 檔輸出的位置。

{% img /images/posts/MicrosoftMonitoringAgent/3.png %}


若想在當下立即產生 IntelliTrace 檔案進行分析，可叫用命令:

    Checkpoint-WebApplicationMonitoring


{% img /images/posts/MicrosoftMonitoringAgent/4.png %}


若要終止偵測並將到目前為止的偵測儲存並產生 IntelliTrace 檔案，可叫用下列命令:

    Stop-WebApplicationMonitoring


{% img /images/posts/MicrosoftMonitoringAgent/5.png %}


產生的 IntelliTrace file 可以用 Visual Studio 2013 開啟。

若有需要 Microsoft Monitoring Agent 也可以與 System Center Operations Manager 做進ㄧ步的整合，提供更完善的Solution。

Link
----
* [Introducing Microsoft Monitoring Agent](http://blogs.msdn.com/b/visualstudioalm/archive/2013/09/20/introducing-microsoft-monitoring-agent.aspx)
* [Microsoft Monitoring Agent 2013](http://www.microsoft.com/en-us/download/details.aspx?id=40316)
* [Monitoring with Microsoft Monitoring Agent](http://technet.microsoft.com/en-us/library/dn465153.aspx)
* [Diagnose problems in deployment with Visual Studio and Microsoft Monitoring Agent](http://msdn.microsoft.com/library/dn449058\(v=vs.120\).aspx)
* [Monitor apps in deployment with Microsoft Monitoring Agent](http://msdn.microsoft.com/en-us/library/vstudio/hh398365.aspx)
