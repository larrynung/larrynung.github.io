---
title: "[C#]原子能委員會輻射監控非官方API"
slug: "[CSharp]原子能委員會輻射監控非官方API"
date: "2011-03-17 07:25:18"
description: "[C#]原子能委員會輻射監控非官方API"
tags: [CSharp]
---

<p>
	最近日本的事件搞得大家人心惶惶，三不五時就要上一下原子能委員會的網站看一下輻射量是否超標，為了更有效的取得這樣的資訊，稍微花點時間去整理了一下API,有興趣的可直接取用，希望藉此拋磚引玉會有更多便民的工具被開發出來。</p>
<p>
	 </p>
<p>
	以下為API的使用範例:</p>
<pre>
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
 
namespace LevelUp.RadiationAPI.Demo
{
	public partial class Form1 : Form
	{
		private RadiationAgent _radiationAgent;
		private RadiationAgent m_RadiationAgent  {
			get
			{
				if (_radiationAgent == null)
				{
					_radiationAgent = new RadiationAgent();
					_radiationAgent.AutoUpdateInterval = 5000;
					_radiationAgent.EnableAutoUpdate = true;
				}
				return _radiationAgent;
			}
		}
 
		public Form1()
		{
			InitializeComponent();
		}
 
		private void UpdateRadiationValue()
		{
			listView1.Items.Clear();
			listView1.BeginUpdate();
			foreach (var data in m_RadiationAgent.RadiationDatas)
			{
				listView1.Items.Add(data.City).SubItems.AddRange(new string[] { data.RadiationValue.ToString(), data.State.ToString() });
			}
			listView1.EndUpdate();
		}
 
		private void timer1_Tick(object sender, EventArgs e)
		{
			UpdateRadiationValue();
		}
 
		private void Form1_Load(object sender, EventArgs e)
		{
			UpdateRadiationValue();
			m_RadiationAgent.RaditionDataUpdated += new EventHandler(m_RadiationAgent_RaditionDataUpdated);
		}
 
		void m_RadiationAgent_RaditionDataUpdated(object sender, EventArgs e)
		{
			UpdateRadiationValue();
		}
 
		private void button1_Click(object sender, EventArgs e)
		{
			m_RadiationAgent.Update();
			UpdateRadiationValue();
		}
	}
}</pre>
<p>
	 </p>
<p>
	運行結果如下:</p>
<p>
	<img alt="image" border="0" height="358" src="\images\posts\21890\image_thumb.png" width="378" /></p>
<p>
	 </p>
<h2>
	Download</h2>
<p>
	Radiation.rar</p>
