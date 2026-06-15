---
title: "Use ResourceDictionary to do multi-language in WPF"
date: "2013-11-06 12:00:00"
description: "Use ResourceDictionary to do multi-language in WPF"
tags: [CSharp]
---

這篇稍稍紀錄一下怎樣在WPF中使用ResourceDictionary去做多語系程式。

首先準備好要做多語系的程式，這邊筆者事先隨便開個WPF Window，在上面放個Label元件，裡面打入"Test"字樣。

```xml
<Window x:Class="WpfApplication5.MainWindow"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        Title="MainWindow"
        Width="525"
        Height="350">
    <Grid>
        <Label HorizontalAlignment="Center"
               VerticalAlignment="Center"
               Content="Test"
               FontSize="70" />
    </Grid>
</Window>
```

![image_thumb_1.png](/images/posts/4066d006-7d5c-4080-9dd8-fbe285bc438d/image_thumb_1.png)

要做多語系的程式準備好了後，我們要為專案加入ResourceDictionary去做多語，檔名這邊筆者是暫定為StringResources.xaml。裡面的XAML內容像下面這樣，加入System命名空間，然後在裡面設定String資源。

```xml
ResourceDictionary xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
                    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
                    xmlns:system="clr-namespace:System;assembly=mscorlib">
    <system:String x:Key="TestString">Test</system:String>
</ResourceDictionary>
```

英文版的設定好後，在檔案總管將StringResources.xaml檔複製並改名為StringResource.zh-tw.xaml檔，且將裡面的String資源訂定的值翻譯成中文。像是下面這樣：

```xml
<ResourceDictionary xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
                    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
                    xmlns:system="clr-namespace:System;assembly=mscorlib">
    <system:String x:Key="TestString">測試</system:String>
</ResourceDictionary>
```

接著開啟App.xaml檔，將String.Resources.xaml加到MergedDictionaries。

```xml
<Application x:Class="WpfApplication5.App"
             xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             Startup="Application_Startup"
             StartupUri="MainWindow.xaml">
    <Application.Resources>
        <ResourceDictionary>
            <ResourceDictionary.MergedDictionaries>
                <ResourceDictionary Source="StringResources.xaml" />
            </ResourceDictionary.MergedDictionaries>
        </ResourceDictionary>
    </Application.Resources>
</Application>
```

再回到我們的UI，把本來Hard Code寫死的字串改用Resource，像是"{DynamicResource TestString}"。這樣在UI的設計界面起碼就可以看到預設的語系畫面，也可以確定資源套用這部分是否是OK的。

```xml
<Window x:Class="WpfApplication5.MainWindow"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        Title="MainWindow"
        Width="525"
        Height="350">
    <Grid>
        <Label HorizontalAlignment="Center"
               VerticalAlignment="Center"
               Content="{DynamicResource TestString}"
               FontSize="70" />
    </Grid>
</Window>
```

資源套用都確定OK後，我們要開始依照語系去抽換使用到的資源檔，這部分要在App.xaml檔那邊去處理Application.Startup事件進行抽換(在建構子進行抽換的動作是無效的)。抽換資源檔時我們只要判斷是要切換到何語系(可能是讀登錄檔或是當前語系，這邊是看產品的需求)，由要切換的語系推斷出我們要抽換到哪個Resource檔，然後將該Resource檔載入到MergedDictionaries就可以了。詳細的實作可參閱下方的程式碼：

```xml
	private void Application_Startup(object sender, StartupEventArgs e)
	{
		ApplyMultiLanguageResource();
	}

	private void ApplyMultiLanguageResource()
	{
		ApplyMultiLanguageResource(CultureInfo.CurrentCulture);
	}

	private void ApplyMultiLanguageResource(CultureInfo cultureInfo)
	{
		var cultureName = cultureInfo.Name;
		var resourceFile = string.Empty;

		try
		{
			resourceFile = @"StringResources." + cultureName + ".xaml ";
		}
		catch (Exception)
		{
		}

		if (string.IsNullOrEmpty(resourceFile))
			resourceFile = @"StringResources.xaml";

		var rd = Application.LoadComponent(new Uri(resourceFile, UriKind.Relative)) as ResourceDictionary;

		var existsRD = this.Resources.MergedDictionaries.Where(item => item.Source.OriginalString.Equals(resourceFile, StringComparison.CurrentCultureIgnoreCase)).FirstOrDefault();

		if (existsRD != null)
			this.Resources.MergedDictionaries.Remove(existsRD);

		this.Resources.MergedDictionaries.Add(rd);
	}
}
```

實際運行後我們可以看到語系會正常的切換。

![image_thumb.png](/images/posts/4066d006-7d5c-4080-9dd8-fbe285bc438d/image_thumb.png)

若是程式中要使用，像是在做訊息的多語，可以像下面這樣：

```csharp
string text = (string)Application.Current.FindResource("TestString");
```
