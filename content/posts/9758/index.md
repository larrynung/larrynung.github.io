---
title: "[C#]利用FlowLayoutPanel控制項合併大量圖片"
slug: "[CSharp]利用FlowLayoutPanel控制項合併大量圖片"
date: "2009-07-31 09:00:04"
description: "[C#]利用FlowLayoutPanel控制項合併大量圖片"
tags: [CSharp]
---

## Introduction

這幾天看到論壇有人問到合併圖片的作法，直覺的想到了以前看過的歐大文章。人老了記憶不好就回去翻了一下順便復習。突然就蹦出了用FlowLayoutPanel控制項來實作的想法，順手做了個實驗並記錄一下。

使用FlowLayouyPanel控制項來合併大量圖片，純粹好玩、寫起來方便快速，可是可能會造成使用物件過多、記憶體用量過高等情況，效能方面也未做過比較，若要使用請自行評估仔細。

## 實作步驟

用FlowLayoutPanel控制項來合併大量圖片，基本上大概可分為下列幾步驟：
放入FlowLayoutPanel到表單，設定AutoSize屬性為True載入圖片時把圖片載入到PictureBox，設定Margin=new Padding(0)、SizeMode=AutoSize，並把PictureBox放入FlowLayoutPanel利用DrawToBitmap截取FlowLayoutPanel的畫面

## 完整程式範例 

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication5
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (openFileDialog1.ShowDialog() == DialogResult.OK )
            {
                listBox1.Items.Clear();
                listBox1.Items.AddRange(openFileDialog1.FileNames);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            flowLayoutPanel1.Controls.Clear();
            foreach(string file in listBox1.Items){
                flowLayoutPanel1.Controls.Add(new PictureBox() { Image = new Bitmap(file), SizeMode = PictureBoxSizeMode.AutoSize, Margin=new Padding(0)});
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (saveFileDialog1.ShowDialog() == DialogResult.OK)
            {
                Bitmap b = new Bitmap(flowLayoutPanel1.Width, flowLayoutPanel1.Height);
                flowLayoutPanel1.DrawToBitmap(b, flowLayoutPanel1.ClientRectangle);
                b.Save(saveFileDialog1.FileName );
            }
        }
    }
}

## 操作步驟與執行結果
Step1.開啟程式，並按下[Load Photo]按鈕
 
Step2.選取圖片後按下[開啟]

程式會顯示所選取的所有圖片路徑

Step3.按下[合併]按鈕 
合併完後會圖片會顯示在下方的FlowLayoutPanel區域

Step5.按下[Save]按鈕，在彈出的視窗選取存檔位置並按下儲存即可

儲存的檔案會像下面這樣合併完成

## Download
 MergePhoto.zip   
 
## Link
.NET菜鳥自救會-[C#]大量圖片合併程式