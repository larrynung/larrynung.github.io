---
title: "[C#]繪製DataGridView的垂直分隔線"
date: "2013-11-06 12:00:00"
description: "最近UX設計師給我了一個Design，裡面設計了一個用來管理帳號的Grid介面，這個Grid看起來非常的客製，但是用內建的設定都可以做到，比較麻煩的只有垂直分隔線的部份，內建的DataGridView可以設出垂直分隔線，但是在沒有資料列的部份垂直分隔線就會斷掉。"
tags: [CSharp]
---

最近UX設計師給我了一個Design，裡面設計了一個用來管理帳號的Grid介面，這個Grid看起來非常的客製，但是用內建的設定都可以做到，比較麻煩的只有垂直分隔線的部份，內建的DataGridView可以設出垂直分隔線，但是在沒有資料列的部份垂直分隔線就會斷掉。

![image_thumb_1.png](/images/posts/0e6c20a6-f9e8-4e50-b847-4e5454fd31c0/image_thumb_1.png)

所以這部份就改用繪製的方式來做，在繪製事件觸發時計算垂直分隔線的x偏移量，並用Graphics.DrawLine去繪製垂直分隔線。

```csharp
private void dataGridView1_Paint(object sender, PaintEventArgs e)
{
	var columnOffset = 0;
	foreach (DataGridViewColumn column in dataGridView1.Columns)
	{
		columnOffset += column.Width;
		e.Graphics.DrawLine(new Pen(Color.Black), columnOffset + 1, 0, columnOffset + 1, dataGridView1.Height);
	}
}
```

我們就可以讓DataGridView的垂直分隔線看起來比較正常一點。

![image_thumb_2.png](/images/posts/0e6c20a6-f9e8-4e50-b847-4e5454fd31c0/image_thumb_2.png)

## Link

* [RESOLVED] Datagridview vertical lines
