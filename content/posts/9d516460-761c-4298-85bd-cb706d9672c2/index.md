---
title: "[C#]使用Faker.Net輔助建立假的數據資料"
slug: "[CSharp]使用Faker.Net輔助建立假的數據資料"
date: "2013-11-06 12:00:00"
description: "[C#]使用Faker.Net輔助建立假的數據資料"
tags: [CSharp]
---

有時候在做些測試時，我們會期望有一定的資料量來做測試，這時我們可能會用程式來產生大量假的資料，而Faker.Net就是可以輔助我們完成這個需求的工具。

使用前需先加入組件參考，這部分可透過NuGet完成，帶入Faker.net關鍵字下去搜尋，並按下Faker.Net搜尋結果後方的Install按鈕就可以了。

![image_thumb.png](/images/posts/9d516460-761c-4298-85bd-cb706d9672c2/image_thumb.png)

加入完組件參考後，我們可以透過物件瀏覽器來看一下組件中含有哪些東西。可以看到的是裡面含有Address、Company、Internet、Name、Phone等物件，不難看出這個元件能為我們做些什麼，像是可以產生地址、公司名稱、電子郵件位置、使用者名字、與使用者電話等，Faker.Net都可以做到。

![image_thumb_1.png](/images/posts/9d516460-761c-4298-85bd-cb706d9672c2/image_thumb_1.png)

在實際使用上Faker.Net十分的簡單易用，透過類別的靜態方法就可以直接產生我們要的假資料，像是要取得一個假的使用者名稱，我們可以透過呼叫Faker.Name.FullName()，要取得假的電子郵件信箱，可以呼叫Faker.Internet.Email()，使用上就是那麼的簡單，沒有什麼難度，你需要的就是釐清各類別的用途，然後看看該類別具有哪些靜態方法，以及它能提供怎麼樣的資料。

這邊筆者來帶幾個簡單的使用範例，假設今天我們要產生的假資料是使用者的資訊，我們可以像下面這樣撰寫：

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ConsoleApplication11
{
	class Program
	{
		static void Main(string[] args)
		{
			for (int i = 0; i < 3; ++i)
			{
				ShowFakeUserInfo();
				Console.WriteLine(new String('=', 50));
			}
		}

		static void ShowFakeUserInfo()
		{
			Console.WriteLine(String.Format("User: {0}", Faker.Name.FullName()));
			Console.WriteLine(String.Format("Phone: {0}", Faker.Phone.Number()));
			Console.WriteLine(String.Format("Email1: {0}", Faker.Internet.Email()));
			Console.WriteLine(String.Format("Email2: {0}", Faker.Internet.FreeEmail()));
			Console.WriteLine(String.Format("Company: {0}", Faker.Company.Name()));
			Console.WriteLine(String.Format("Country: {0}", Faker.Address.Country()));
		}
	}
}
```

運行後可以得到像是下面這樣的結果，使用者的名字、電話、電子郵件、公司名稱、所屬城市這些資料是不是看起來都很真呢？

![image_thumb_2.png](/images/posts/9d516460-761c-4298-85bd-cb706d9672c2/image_thumb_2.png)

另外若是造假的資料是要一個句子或是一段話呢，我們可透過Faker.Lorem去做，像是：

```csharp
Console.WriteLine(Faker.Lorem.Sentence());
```

![image_thumb_5.png](/images/posts/9d516460-761c-4298-85bd-cb706d9672c2/image_thumb_5.png)

或是：

```csharp
onsole.WriteLine(Faker.Lorem.Paragraph());
```

![image_thumb_4.png](/images/posts/9d516460-761c-4298-85bd-cb706d9672c2/image_thumb_4.png)

## Link

* Use Faker.NET To Fake Your Data
