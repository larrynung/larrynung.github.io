---
title: "[Performance][C#]List V.S SortedList"
date: "2009-03-27 11:51:26"
description: "[Performance][C#]List V.S SortedList"
tags: [Performance,CSharp]
---

之前有看到網路文章介紹SortedList類別，該類別使用方式類似HashTable，也是由Key跟Value所組成的字典類別，而與其它字典類別最大的差異就在於SortedList類別會自動排序。

但我實在很難想到這種Key跟Value的組合有啥排序的必要性，因為通常這種字典類別都是直接把Key帶入用以取得Value。而這種用法實在沒排序之必要性，除非要列出所有的配對資料。

而我想應該也有滿多的人是直接把SortedList當作會自動排序的List用而已吧。這篇主要就是針對"把SortedList當作會自動排序的List用"的作法來做一些比較與探討。

廢話不多說，直接看例子：

```
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Collections;
using System.Diagnostics;

namespace HashTableVSSortedList
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            button1.Enabled = false;
            GoTest();
            button1.Enabled = true;
            MessageBox.Show("Ok");
        }

        private void GoTest()
        {
            this.textBox1.Clear();
            Test(1000);
            Test(10000);
            Test(100000);
        }

        private void Test(int testTimes)
        {
            this.textBox1.Text += string.Format("=================================\r\n測試 {0} 筆\r\n=================================\r\n", testTimes);
            ListTest(testTimes);
            SortedListTest(testTimes);
            Application.DoEvents();
        }

        private void ListTest(int testTimes)
        {
            Stopwatch sw = new Stopwatch();
            sw.Start();
            List<string> lt = new List<string>();
            for (int i = 0; i < testTimes; i++)
            {
                lt.Add(i.ToString());
                //lt.Sort();
            }
            lt.Sort();
            OutputResult("List", sw.ElapsedMilliseconds);
        }

        private void SortedListTest(int testTimes)
        {
            Stopwatch sw = new Stopwatch();
            sw.Start();
            SortedList<string, string> st = new SortedList<string, string>();
            for (int i = 0; i < testTimes; i++)
            {
                string tmp = i.ToString();
                st.Add(tmp, tmp);
            }
            OutputResult("SortedList", sw.ElapsedMilliseconds);
        }

        private void OutputResult(string title, long elapsedMilliseconds)
        {
            this.textBox1.Text += string.Format("{0}: {1} ms\r\n", title, elapsedMilliseconds);
            Application.DoEvents();
        }

    }
}
```

執行後的結果如下：

![image_thumb_1.png](/images/posts/7737/image_thumb_1.png)

統計一下測試資料

![image_thumb.png](/images/posts/7737/image_thumb.png)

由執行的結果我們可以看出，若程式的需求非每插入一筆就要排序好資料的話，在筆數少的情況下，用SortedList來作效率會較高，筆數高的話則把資料全部插入List後再用Sort排序反而有更好的效率。若程式的需是每插入一筆就要排序好資料的話(有興趣的可把上面範例的ListTest中Sort改為用迴圈內的)，不論筆數多寡都是用SortedList來作效率最好。

<table border="1" cellpadding="2" cellspacing="0" width="557"><tbody>
<tr>
<td valign="top" width="91"> </td>
<td valign="top" width="233">非每插入一筆就要排序好</td>
<td valign="top" width="229">每插入一筆就要排序好</td>
</tr>
<tr>
<td valign="top" width="93">筆數少</td>
<td valign="top" width="233">SortedList</td>
<td valign="top" width="229">SortedList</td>
</tr>
<tr>
<td valign="top" width="95">筆數多</td>
<td valign="top" width="233">List+Sort</td>
<td valign="top" width="229">SortedList</td>
</tr>
</tbody></table>
