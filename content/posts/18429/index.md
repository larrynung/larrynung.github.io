---
title: "[VB.NET]Attribute與反射的搭配使用"
date: "2010-10-18 08:59:31"
description: "[VB.NET]Attribute與反射的搭配使用"
tags: [VB.NET]
---

<p>有時在撰寫程式為了增加彈性或是便利性，我們可考慮使用Attribute來為類別、方法、欄位、與屬性附加一些資訊。這樣的設計方式在.NET中已經存在許久，這類應用也越來越普及，相信大家就算沒有用過也有看過，像是製作控制項時會用到的Browsable、Description、Category...，做序列化時會用到的XmlIgnore、XmlElement...，許多地方都會用到這樣的小技巧。 </p>  <p> </p>  <p>在Attribute的建立上，簡單的說只是一個繼承Attribute的類別，裡面存放著所要附加的資料，並透過AttributeUsage屬性設定該Attribute所能使用的範圍。像是：</p>  <div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:6fde8454-7de6-4d0b-b1c1-df1d9d4b13a1" class="wlWriterSmartContent"><pre name="code" class="vb">&lt;AttributeUsage(AttributeTargets.Property Or AttributeTargets.Field)&gt; 
Class NewPropertyOrFieldAttribute
    Inherits Attribute

    Property Data as Object

End Class</pre></div>

<p> </p>

<p>這邊以利用Attribute將資訊附加在列舉成員欄位為例，假設我們有要做類似於Office這樣的軟體需求，為求方便使用，可能會希望開出一個建構子或是成員方法，裡面可帶入列舉，依帶入的列舉值開啟對應的應用程式。這時就可以透過Attribute為列舉的成員欄位附加對應要開啟的類別資訊，像是下面這樣：</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:e78489f4-3df8-4a71-bbb3-52333a07d92e" class="wlWriterSmartContent"><pre name="code" class="vb">NotInheritable Class RelativedTypeAttribute
    Inherits Attribute

    Property RelativedType As Type

    Sub New(ByVal relativedType As Type)
        Me.RelativedType = relativedType
    End Sub

End Class

Enum ApplicationType
    &lt;RelativedType(GetType(LevelUp.Office.Word))&gt; _
    Word

    &lt;RelativedType(GetType(LevelUp.Office.Excel))&gt; _
    Excel

    &lt;RelativedType(GetType(LevelUp.Office.Access))&gt; _
    Access

    &lt;RelativedType(GetType(LevelUp.Office.PowerPoint))&gt; _
    PowerPoint

    &lt;RelativedType(GetType(LevelUp.Office.Visio))&gt; _
    Visio
End Enum</pre></div>

<p> </p>

<p>再透過反射取得列舉成員欄位對應的類別資訊，將其類別動態建立叫起使用就可以了。</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:2267baef-6da3-4664-a116-89423c36a760" class="wlWriterSmartContent"><pre name="code" class="vb">    Sub Main()
        StartApplication(ApplicationType.Word)
    End Sub

    Sub StartApplication(ByVal apType As ApplicationType)
        Dim type As Type = apType.GetType()
        Dim field = type.GetField(apType.ToString)
        Dim att = field.GetCustomAttributes(GetType(RelativedTypeAttribute), False).Cast(Of RelativedTypeAttribute)().FirstOrDefault()
        Activator.CreateInstance(att.RelativedType).Start()
    End Sub</pre></div>

<p> </p>

<p>又或是我們有需求透過列舉取得對應的描述字串，我們可以使用Attribute為列舉的成員欄位附加對應的資源編號，像是下面這樣：</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:71de81b2-1421-469d-8130-ece35426d696" class="wlWriterSmartContent"><pre name="code" class="vb">NotInheritable Class ResouceIDAttribute
    Inherits Attribute

    Property ResourceID As String

    Sub New(ByVal resourceID As String)
        Me.ResourceID = resourceID
    End Sub

End Class

Enum InterfaceType
    &lt;ResouceID("RS232_InterfaceName")&gt; _
    RS232

    &lt;ResouceID("RS485_InterfaceName")&gt; _
    RS485

    &lt;ResouceID("GPIB_InterfaceName")&gt; _
    GPIB

    &lt;ResouceID("I2C_InterfaceName")&gt; _
    I2C
End Enum</pre></div>

<p> </p>

<p>如此可透過反射去取得附加的資源ID，進一步取得資源檔所設定的字串。</p>

<p>
  </p><div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:b3ad328c-04cb-4e4b-9bf3-c0cecc619fd0" class="wlWriterSmartContent"><pre name="code" class="vb">    Sub Main()
        Dim instrumentInterface As InterfaceType
        Dim type As Type = instrumentInterface.GetType()
        Dim field = type.GetField(instrumentInterface.ToString)
        Dim resourceID = field.GetCustomAttributes(GetType(ResouceIDAttribute), False).Cast(Of ResouceIDAttribute)().FirstOrDefault.ResourceID
        Console.WriteLine(My.Resources.ResourceManager.GetString(resourceID))
    End Sub</pre></div>


<p> </p>

<p>當然還可以用在很多地方，這邊只是舉幾個例子稍作紀錄。</p>
