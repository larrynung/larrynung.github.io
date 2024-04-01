---
title: "[VB.NET]Detect Design-Time amp; Run-Time"
date: "2009-11-16 01:22:12"
description: "[VB.NET]Detect Design-Time &amp; Run-Time"
tags: [VB.NET]
---

<p />  <h2>Introduction</h2>  <p>在撰寫控制項時，我們常會需要依照不同的階段作不同的處理。像是在設計階段顯示與運行階段不同的畫面、關閉些在設計階段會造成錯誤的處理等等。這邊將對偵測目前所處階段的語法作些整理。</p>  <p> </p>  <h2>Detect Design-Time &amp; Run-Time</h2>  <p>若要在程式中分辨設計階段(Design-Time)與運行階段(Run-Time)，我們大致上有以下幾種方法。</p>  <p> </p>  <h3>WinForm </h3>  <p><strong>1.判斷Component.DesignMode</strong></p>  <p />  <div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:ff218bd6-25bb-47f2-8c68-c60eb05998b6" class="wlWriterEditableSmartContent"><pre name="code" class="vb:nocontrols">Dim isDesignTime As Boolean = Component.DesignMode</pre></div>

<p> </p>

<p><strong>2.判斷Site.DesignMode</strong></p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:67f16758-80f1-4244-9d03-37fcfaa70d07" class="wlWriterEditableSmartContent"><pre name="code" class="vb:nocontrols">Dim isDesignTime As Boolean = Me.Site IsNot Nothing AndAlso Me.Site.DesignMode</pre></div>

<p> </p>

<p><strong>3.判斷當前處理序是否為Visual Studio</strong></p>

<p />

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:3320e2d2-e447-4fdd-a578-118823eba722" class="wlWriterEditableSmartContent"><pre name="code" class="vb:nocontrols">Dim isDesignTime As Boolean = Process.GetCurrentProcess().ProcessName.Equals("devenv", StringComparison.OrdinalIgnoreCase)</pre></div>

<p />

<p> </p>

<p><strong>4.判斷LicenseUsageMode.UsageMode是否為LicenseUsageMode.Designtime</strong></p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:2ab7da6a-3db2-4c3b-a396-318fc7bf16ef" class="wlWriterEditableSmartContent"><pre name="code" class="vb:nocontrols">Dim isDesignTime As Boolean = System.ComponentModel.LicenseManager.UsageMode = System.ComponentModel.LicenseUsageMode.Designtime</pre></div>

<p> </p>

<p><strong>5.判斷GetService(GetType(System.ComponentModel.Design.IDesignerHost))不為空</strong></p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:de37d7dc-ea72-499d-ac2e-c4571165c371" class="wlWriterEditableSmartContent"><pre name="code" class="vb:nocontrols">Dim isDesignTime As Boolean = GetService(GetType(System.ComponentModel.Design.IDesignerHost)) IsNot Nothing</pre></div>

<p> </p>

<h3>ASP.NET</h3>

<p>請參閱Detecting Designmode in ASP.Net</p>

<p> </p>

<h3>WPF</h3>

<p>請參閱Detecting design time mode in WPF and Silverlight</p>

<p> </p>

<h2>Link</h2>

<ul>
  <li>
    <p>How Do I Detect Design-Time Vs Run-Time in a .NET Control?</p>
  </li>

  <li>
    <p>Identifying the Run-Time and the Design Mode</p>
  </li>

  <li>
    <p>Design Time Detection</p>
  </li>

  <li>
    <p>Detect if Code is Running from the IDE</p>
  </li>

  <li>
    <p>Detecting Design-time in C#</p>
  </li>

  <li>
    <h4>Windows Forms designer and DesignMode property issues</h4>
  </li>

  <li>
    <p>MSDN - Component.DesignMode Property</p>
  </li>

  <li>
    <p>MSDN - IDesignerHost 介面</p>
  </li>

  <li>
    <h4>Detecting Designmode in ASP.Net</h4>
  </li>

  <li>
    <h4>Detecting design time mode in WPF and Silverlight</h4>
  </li>
</ul>
