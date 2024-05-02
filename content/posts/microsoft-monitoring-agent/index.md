---
title: "Microsoft Monitoring Agent"
date: "2013-11-20 23:48:00"
---


Microsoft Monitoring Agent (MMA) 是可獨立運行的 IntelliTrace，可用來收集診斷資料，例如效能標準、事件記錄檔和Trace。  

<!--More-->

不像以前的 IntelliTrace 主要是綁在 Visual Studio 上使用，它能獨立運行，且功能也做了些許的強化，能與 System Center Operations Manager 做進ㄧ步的整合，提供更完善的Solution。   

透過 Microsoft Monitoring Agent ，我們可以 Follow  編寫程式 => 建置 => 發佈 => 偵測 => 診斷 這樣的流程，不斷的進行迭代，讓產品更加的穩定。  

{% img /images/posts/MicrosoftMonitoringAgent/1.png %}

<br/>

Microsoft Monitoring Agent 主程式可至 [Microsoft Monitoring Agent 2013](http://www.microsoft.com/en-us/download/details.aspx?id=40316) 這邊下載安裝。  

{% img /images/posts/MicrosoftMonitoringAgent/2.png %}

<br/>

{% img /images/posts/MicrosoftMonitoringAgent/3.png %}

<br/>

{% img /images/posts/MicrosoftMonitoringAgent/4.png %}

<br/>

{% img /images/posts/MicrosoftMonitoringAgent/5.png %}

<br/>

{% img /images/posts/MicrosoftMonitoringAgent/6.png %}

<br/>

{% img /images/posts/MicrosoftMonitoringAgent/7.png %}

<br/>

{% img /images/posts/MicrosoftMonitoringAgent/8.png %}

<br/>

{% img /images/posts/MicrosoftMonitoringAgent/9.png %}

<br/>

建議環境為 .NET Framework 3.5+、以及 PowerShell 3.0+。


在使用上，我們只要開啟 PowerShell ，輸入對應的命令就可以了。  

若是使用的是 PowerShell 2.0，需先輸入下列命令去 Import module，不然會無法使用後續的 PowerShell Cmdlet。

    Import-Module "C:\Program Files\Microsoft Monitoring Agent\Agent\PowerShell\Microsoft.MonitoringAgent.PowerShell\Microsoft.MonitoringAgent.PowerShell.dll"

{% img /images/posts/MicrosoftMonitoringAgent/10.png %}

<br/>

要開始啟用 Microsoft Montoring Agent 進行偵測，只要輸入命令：

    Start-WebApplicationMonitoring


命令叫用的同時，會詢問要監測的網站 (即IIS上網站的名稱)、偵測的類型 (Monitor、Trace、Custom)、以及 Intellitrace 檔輸出的位置。

{% img /images/posts/MicrosoftMonitoringAgent/11.png %}

<br/>

若想在當下立即產生 IntelliTrace 檔案進行分析，可叫用命令:

    Checkpoint-WebApplicationMonitoring

{% img /images/posts/MicrosoftMonitoringAgent/12.png %}

<br/>

若要終止偵測並將到目前為止的偵測儲存並產生 IntelliTrace 檔案，可叫用下列命令:

    Stop-WebApplicationMonitoring [WebSite]

{% img /images/posts/MicrosoftMonitoringAgent/13.png %}

<br/>

產生的 IntelliTrace file 可用 Visual Studio 開啟。  

開啟後會看到像下面這樣的畫面，會顯示所偵測到的 Exception、 System Info 、以及 Module Info。

{% img /images/posts/MicrosoftMonitoringAgent/14.png %}

<br/>

這邊通常我們關注的會是 Exception 這塊，找看看有沒有不該丟出的例外，找到後選取，在下方可看到對應的呼叫堆疊。  

{% img /images/posts/MicrosoftMonitoringAgent/15.png %}

<br/>

進一步要查閱的話，可滑鼠左鍵連點，或是按下 `Start Debugging` 按鈕，會進入到偵錯模式，可以看到細部的區域變數或是呼叫堆疊，若有 PDB 檔的這邊也可以將之 Attach 上去，看更細部的資訊。

{% img /images/posts/MicrosoftMonitoringAgent/16.png %}

<br/>

Link
----
* [Introducing Microsoft Monitoring Agent](http://blogs.msdn.com/b/visualstudioalm/archive/2013/09/20/introducing-microsoft-monitoring-agent.aspx)
* [Microsoft Monitoring Agent 2013](http://www.microsoft.com/en-us/download/details.aspx?id=40316)
* [Monitoring with Microsoft Monitoring Agent](http://technet.microsoft.com/en-us/library/dn465153.aspx)
* [Diagnose problems in deployment with Visual Studio and Microsoft Monitoring Agent](http://msdn.microsoft.com/library/dn449058\(v=vs.120\).aspx)
* [Monitor apps in deployment with Microsoft Monitoring Agent](http://msdn.microsoft.com/en-us/library/vstudio/hh398365.aspx)
