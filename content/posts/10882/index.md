---
title: "[C#]使用GetSystemPowerStatus API查看目前電源使用狀態"
date: "2009-10-02 09:01:15"
description: "[C#]使用GetSystemPowerStatus API查看目前電源使用狀態"
tags: [CSharp]
---

<h2>Introduction</h2>  <p>這篇簡單記錄一下，如何透過GetSystemPowerStatus API，來查看目前電源的使用狀態。</p>  <p> </p>  <h2>Library</h2>  <p>kernel32.dll</p>  <p> </p>  <h2>GetSystemPowerStatus API</h2>  <p>GetSystemPowerStatus API可取得系統電源狀態，包括使用交流電還是直流電、是否為充電狀態、剩餘可用時間等資訊。其函式原型如下：    <br />BOOL WINAPI GetSystemPowerStatus(__out LPSYSTEM_POWER_STATUS <i>lpSystemPowerStatus</i>);</p>  <p> </p>  <p>傳入的參數為LPSYSTEM_POWER_STATUS型態的結構    <br />typedef struct _SYSTEM_POWER_STATUS {     <br />BYTE ACLineStatus;     <br />BYTE BatteryFlag;     <br />BYTE BatteryLifePercent;     <br />BYTE Reserved1;     <br />DWORD BatteryLifeTime;     <br />DWORD BatteryFullLifeTime; } SYSTEM_POWER_STATUS,     <br />*LPSYSTEM_POWER_STATUS;</p>  <pre> </pre>

<pre>結構成員所代表的意義簡略如下：</pre>

<table border="1" cellspacing="0" cellpadding="2" width="701"><tbody>
    <tr>
      <td valign="top" width="200">BatteryFlag</td>

      <td valign="top" width="499">表示目前充電狀態。 
        <br />1為High(66%以上電力)、2為Low(33%以上電力)、4為Critical(5%以下電力)、8為Charging、128為NoBattery、255為UnKnow</td>
    </tr>

    <tr>
      <td valign="top" width="200">BatteryFullLifeTime</td>

      <td valign="top" width="499">表示充滿電力可使用多久時間(-1為不詳)。</td>
    </tr>

    <tr>
      <td valign="top" width="200">BatteryLifePercent</td>

      <td valign="top" width="499">表示電力剩餘多少百分比，其正常值為0~100，255為電力不詳。</td>
    </tr>

    <tr>
      <td valign="top" width="200">BatteryLifeTime</td>

      <td valign="top" width="499">表示剩餘電力可使用多久時間(-1為不詳)。</td>
    </tr>

    <tr>
      <td valign="top" width="200">ACLineStatus</td>

      <td valign="top" width="499">表示電源狀態。 
        <br />0為offline、1為online、255為unknow。</td>
    </tr>
  </tbody></table>

<pre> </pre>

<pre>使用時只要把LPSYSTEM_POWER_STATUS型態的結構傳入GetSystemPowerStatus，再從傳入的結構中取出感興趣的資料就可以了。</pre>

<pre> </pre>

<h2>Example</h2>

<p />

<p />

<p>為了使用方便，也便於對照比較。這邊我把GetSystemPowerStatus API包成了類似System.Windows.Form.PowerStatus的類別。 
  <br /></p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:2d1a6390-984e-4ddf-aa5e-fccbe38e6232" class="wlWriterEditableSmartContent"><pre name="code" class="c#:nocontrols">using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Runtime.InteropServices;

namespace Battery
{
    [Flags]
    public enum BatteryChargeStatus : byte
    {
        High = 1,
        Low = 2,
        Critical = 4,
        Charging = 8,
        NoSystemBattery = 128,
        Unknown = 255
    }

    public enum PowerLineStatus : byte
    {
        Offline = 0,
        Online = 1,
        Unknown = 255
    }

    class PowerStatus
    {
        [DllImport("kernel32", EntryPoint = "GetSystemPowerStatus")]
        private static extern void GetSystemPowerStatus(ref SystemPowerStatus powerStatus);
        
        private struct SystemPowerStatus
        {
            public PowerLineStatus PowerLineStatus;
            public BatteryChargeStatus BatteryChargeStatus;
            public Byte BatteryLifePercent;
            public Byte Reserved;
            public int BatteryLifeRemaining;
            public int BatteryFullLifeTime;
        }

        private SystemPowerStatus _powerStatus;

        public PowerLineStatus PowerLineStatus
        {
            get
            {
                return _powerStatus.PowerLineStatus;
            }
        }

        public BatteryChargeStatus BatteryChargeStatus
        {
            get
            {
                return _powerStatus.BatteryChargeStatus;
            }
        }

        public float BatteryLifePercent
        {
            get
            {
                return _powerStatus.BatteryLifePercent;
            }
        }

        public int BatteryLifeRemaining
        {
            get
            {
                return _powerStatus.BatteryLifeRemaining;
            }
        }

        public int BatteryFullLifeTime
        {
            get
            {
                return _powerStatus.BatteryFullLifeTime;
            }
        }

        public PowerStatus()
        {
            UpdatePowerInfo();
        }


        public void UpdatePowerInfo()
        {
            GetSystemPowerStatus(ref _powerStatus);
        }
    }
}
</pre></div>

<p />

<p> </p>

<p>使用上跟.NET內建的PowerStatus大同小異。只要取得對應的屬性值即可。 
  <br /></p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:f1bd1ae9-1cd8-4aa5-8f7f-4d8d79a532be" class="wlWriterEditableSmartContent"><pre name="code" class="c#:nocontrols">using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;


namespace BatteryPower
{
    public partial class Form1 : Form
    {


        public Form1()
        {
            InitializeComponent();
        }

        private void UpdateInfo()
        {
            Battery.PowerStatus power = new Battery.PowerStatus();
            this.tbxPowerStatus.Text = power.PowerLineStatus.ToString();
            this.tbxBatteryChargeStatus.Text = power.BatteryChargeStatus.ToString();
            this.tbxBatteryFullLifetime.Text = power.BatteryFullLifeTime.ToString();
            this.tbxBatteryLifePercent.Text = power.BatteryLifePercent.ToString();
            this.tbxBatteryLifeRemaining.Text = power.BatteryLifeRemaining.ToString();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            UpdateInfo();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            UpdateInfo();
        }
    }
}
</pre></div>

<p />

<p />

<p> </p>

<p>執行畫面</p>

<p />

<p />

<p><img style="border-right-width: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" title="image" border="0" alt="image" src="\images\posts\10882\image_thumb.png" width="304" height="179" /></p>

<p> </p>

<h2>Link</h2>

<ul>
  <li>GetSystemPowerStatus Function</li>

  <li>SYSTEM_POWER_STATUS Structure</li>

  <li>C#透過Windows API取得NoteBook電池使用狀況</li>

  <li>如何得知 Notebook中 電池 的使用狀況</li>
</ul>
