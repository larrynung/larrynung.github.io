---
title: ".NET - Access Embeded Resource"
date: "2014-04-14 23:01:00"
description: ".NET - Access Embeded Resource"
tags: [CSharp]
---


Embeded Resource 可以將程式需要的檔案內嵌在程式組件內，會增加組件的大小，但是使用者看不到該檔案，也不會因為檔案位置錯誤造成程式出錯。當系統中存在有必要的檔案，且不希望讓使用者能夠輕易動到的話， 使用 Embeded Resource 是不錯的選擇。  

<!-- More -->

要設定 Embedded Resource ，只要將檔案加入專案，然後在屬性視窗中將 Build Action 設為 Embeded Resource。

要取用時透過 Assembly.GetExecutingAssembly() 取得當前組件，然後叫用 GetManifestResourceStream() 並帶入 Resource Name 取得指定 Embeded Resource 的 Stream，最後再從 Stream 讀出我們所要的資料就可以了。  

所以像是純文字檔，就可以像下面這樣處理：

```c#
private static string ReadAllTextFromEmbededResource(string resourceName)
{
    var assembly = Assembly.GetExecutingAssembly();
    using (var stream = assembly.GetManifestResourceStream(resourceName))
    using (var reader = new StreamReader(stream))
    {
        return reader.ReadToEnd();
    }
}
```

Link
----
* [c# - How to read embedded resource text file - Stack Overflow](http://stackoverflow.com/questions/3314140/how-to-read-embedded-resource-text-file)
* [How to read Embedded Resource in c# | Hadjloo's Daily Notes](http://hajloo.wordpress.com/2009/12/14/%E2%80%AAhow-to-read-embedded-resource-in-c/)
* [如何使用 Visual C# 內嵌和存取資源](http://support.microsoft.com/kb/319292/zh-tw)
