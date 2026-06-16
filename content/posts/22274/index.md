---
title: "[C#]Reading RSS Data"
slug: "csharp-reading-rss-data"
aliases: ["/posts/csharprss-資料讀取/"]
date: "2011-04-04 09:50:45"
description: "RSS訂閱資訊是透過XML技術實現的，其XML格式欄位對應可參閱RSS 2.0 at Harvard Law這網站。 這邊以點部落-最新文章 的資訊提供來做練習，檢視一下該RSS的XML，發現RSS XML的架構大概就是RSS Channel下面會含許多的RSS Channel Item，"
tags: [CSharp]
---

RSS訂閱資訊是透過XML技術實現的，其XML格式欄位對應可參閱RSS 2.0 at Harvard Law這網站。

這邊以點部落-最新文章 的資訊提供來做練習，檢視一下該RSS的XML，發現RSS XML的架構大概就是RSS Channel下面會含許多的RSS Channel Item，RSS Channel用來描述該RSS的識別資訊，RSS Channel Item用來描述RSS所要提供給訂閱者的資訊。

![image_thumb.png](/images/posts/22274/image_thumb.png)

有了以上的了解後，要讀取RSS資訊就很簡單了，簡單的說就是透過RSS訂閱位置取得RSS XML，接著進一步對其解析，從RSS XML中取得我們想要的資訊。像是若要取得RSS Channel Item就可以像下面這樣撰寫：

...

```
var xmlDom=new XmlDocument();
```

```
xmlDom.Load(tbxRSSURL.Text);
```

```
var rssItems = xmlDom.SelectNodes("/rss/channel/item");
```

...

這邊附上個完整的範例程式：

```
using System;
```

```
using System.Text;
```

```
using System.Windows.Forms;
```

```
using System.Xml;
```

```
using LevelUpLazy = LevelUp.Lazy;
```

```
using System.Diagnostics;
```

namespace WindowsFormsApplication2

{

    public partial class Form1 : Form

    {

```
        public Form1()
```

        {

```
            InitializeComponent();
```

        }

```
        private void btnSubmit_Click(object sender, EventArgs e)
```

        {

```
            Stopwatch sw=Stopwatch.StartNew ();
```

```
            var xmlDom=new XmlDocument();
```

```
            xmlDom.Load(tbxRSSURL.Text);
```

```
            var rssItems = xmlDom.SelectNodes("/rss/channel/item");
```

```
            trvRSSItem.Nodes.Clear();
```

```
            wbRSSContent.DocumentText = string.Empty;
```

```
            trvRSSItem.BeginUpdate();
```

            for (var idx = 0; idx < rssItems.Count; ++idx)

            {

```
                var xmlNode = rssItems[idx];
```

                trvRSSItem.Nodes.Add(xmlNode.ChildNodes[0].InnerText).Tag = new LevelUpLazy.Lazy<string>(() =>

                {

```
                    StringBuilder ret = new StringBuilder();
```

```
                    ret.AppendLine(xmlNode.SelectSingleNode("title").InnerText);
```

```
                    ret.AppendLine("<br/>");
```

```
                    ret.AppendLine(xmlNode.SelectSingleNode("description").InnerText);
```

```
                    return ret.ToString();
```

                });

            }

```
            trvRSSItem.EndUpdate();
```

```
            this.toolStripStatusLabel1.Text = string.Format("Elapsed: {0} ms", sw.ElapsedMilliseconds.ToString());
```

```
            LevelUpLazy.Lazy<string>.EnableBackgroundInit = true;
```

        }

```
        private void trvRSSItem_AfterSelect(object sender, TreeViewEventArgs e)
```

        {

            if (trvRSSItem.SelectedNode == null)

```
                return;
```

```
            var lazy=trvRSSItem.SelectedNode.Tag as LevelUpLazy .Lazy <string>;
```

```
            wbRSSContent.DocumentText = lazy.Value;
```

        }

    }

}

運行效果：

![image_thumb_2.png](/images/posts/22274/image_thumb_2.png)

![image_thumb_1.png](/images/posts/22274/image_thumb_1.png)

## Download

SimpleRSSReader.zip

## Link

* RSS 2.0 at Harvard Law
* 點部落-最新文章 的資訊提供
