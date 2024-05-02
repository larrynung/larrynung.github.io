---
title: "[VS 2010]Generate From Usage"
date: "2010-01-18 11:57:57"
description: "[VS 2010]Generate From Usage"
tags: [Visual Studio]
---

<h2>Introduction</h2><p>Generate From Usage是VS2010的新功能，其能讓使用者先使用類別與成員，事後再去定義它。這種特性對於TDD的開發方式特別有幫助、因為我們可以在撰寫單元測試的同時，利用Generate From Usage功能產生對應的程式框架。透過Generate From Usage產生程式的同時，焦點仍會保持在原本的程式編輯視窗，使用上十分方便。</p><p> </p><p>Generate From Usage在使用上我們可以透過把滑鼠移至小波浪下的小底線，或是把焦點設到波浪處後，按下熱鍵Ctrl+.。</p><p><img style="border-bottom: 0px; border-left: 0px; display: inline; border-top: 0px; border-right: 0px" title="image" border="0" alt="image" width="202" height="73" src="\images\posts\13098\image_thumb.png" /></a></p><p> </p><p>接著在彈出的圖示上按下滑鼠左鍵，並在快顯選單中選取所需使用的功能即可。</p><p><a rel="lightbox" href="http://files.dotblogs.com.tw/larrynung/1001/VS2010CodeGeneration_13F14/image_4.png"><img style="border-bottom: 0px; border-left: 0px; display: inline; border-top: 0px; border-right: 0px" title="image" border="0" alt="image" width="291" height="133" src="\images\posts\13098\image_thumb_1.png" /></a></p><p> </p><p>除此之外，也可以在小波浪處按下滑鼠右鍵，移至[Generate]，並選取所需使用的功能。</p><p><a rel="lightbox" href="http://files.dotblogs.com.tw/larrynung/1001/VS2010CodeGeneration_13F14/image_6.png"><img style="border-bottom: 0px; border-left: 0px; display: inline; border-top: 0px; border-right: 0px" title="image" border="0" alt="image" width="535" height="161" src="\images\posts\13098\image_thumb_2.png" /></a></p><p> </p><p>若選用New Type…，則會彈出Generate New Type視窗，提供進階的設定。</p><p><a rel="lightbox" href="http://files.dotblogs.com.tw/larrynung/1001/VS2010CodeGeneration_13F14/image_8.png"><img style="border-bottom: 0px; border-left: 0px; display: inline; border-top: 0px; border-right: 0px" title="image" border="0" alt="image" width="378" height="418" src="\images\posts\13098\image_thumb_3.png" /></a></p><p> </p><h2>Generate Class</h2><p>當宣告物件的類別在專案中找不到時，我們可透過Generate From Usage的Generate Class來替我們產生。</p><p><a rel="lightbox" href="http://files.dotblogs.com.tw/larrynung/1001/VS2010CodeGeneration_13F14/image_10.png"><img style="border-bottom: 0px; border-left: 0px; display: inline; border-top: 0px; border-right: 0px" title="image" border="0" alt="image" width="278" height="129" src="\images\posts\13098\image_thumb_4.png" /></p><p> </p><p>使用後，專案會自動幫我們產生類別檔 <br /> </p><div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:28413cae-5c47-463c-ad61-d43444e2f6d5" class="wlWriterEditableSmartContent"><pre class="c#:nocontrols" name="code">
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Generate_From_Usage
{
    class Person
    {
    }
}
</pre></div><p> </p><p> </p><h2>Generate Property</h2><p>當物件的屬性不存在時，我們可透過Generate From Usage的Generate Property來替我們產生。</p><p><img style="border-bottom: 0px; border-left: 0px; display: inline; border-top: 0px; border-right: 0px" title="image" border="0" alt="image" width="671" height="129" src="\images\posts\13098\image_thumb_6.png" /></p><p> </p><p>使用後，會幫我們產生對應的屬性</p><div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:8f4dd17d-f372-4c1f-95c2-3577df2fd915" class="wlWriterEditableSmartContent"><pre class="c#:nocontrols" name="code">
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Generate_From_Usage
{
    class Person
    {
        public string Name { get; set; }
    }
}
</pre></div><p> </p><p>若要產生靜態的屬性，我們可以透過"類別.屬性名稱"來作Generate Property</p><p><img style="border-bottom: 0px; border-left: 0px; display: inline; border-top: 0px; border-right: 0px" title="image" border="0" alt="image" width="601" height="145" src="\images\posts\13098\image_thumb_8.png" /></p><p> </p><p>使用後，靜態的屬性就產生了 <br /> </p><div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:01d1e0de-d298-4543-9eb8-0b88988f1ea6" class="wlWriterEditableSmartContent"><pre class="c#:nocontrols" name="code">
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Generate_From_Usage
{
    class Person
    {
        public string Name { get; set; }
        public static string StaticProperty { get; set; }
    }
}
</pre></div><p> </p><h2>Generate Field</h2><p>當物件的欄位不存在時，我們可透過Generate From Usage的Generate Field來替我們產生。</p><p><img style="border-bottom: 0px; border-left: 0px; display: inline; border-top: 0px; border-right: 0px" title="image" border="0" alt="image" width="709" height="131" src="\images\posts\13098\image_thumb_7.png" /></p><p> </p><p>使用後，會幫我們產生對應的欄位</p><div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:0d1fa504-27fd-4970-b779-4a81849cdb92" class="wlWriterEditableSmartContent"><pre class="c#:nocontrols" name="code">
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Generate_From_Usage
{
    class Person
    {
        private string _name;
        public string Name { get{return _name;} set; }
    }
}
</pre></div><p> </p><p>若要產生靜態的欄位，我們可以像下圖這般作Generate Field</p><p><img style="border-bottom: 0px; border-left: 0px; display: inline; border-top: 0px; border-right: 0px" title="image" border="0" alt="image" width="847" height="177" src="\images\posts\13098\image_thumb_9.png" /></p><p> </p><p>使用後，靜態的欄位就產生了 <br /> </p><div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:f62ec8c8-93a7-4339-8c00-b307d0276b9c" class="wlWriterEditableSmartContent"><pre class="c#:nocontrols" name="code">
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Generate_From_Usage
{
    class Person
    {
        private string _name;
        private static string _staticField;
        public string Name { get{return _name;} set; }

        public static string StaticProperty { get { return _staticField; } set; }
    }
}
</pre></div><p> </p><p>也可以透過"類別.欄位名稱"來作Generate Field</p><p><img style="border-bottom: 0px; border-left: 0px; display: inline; border-top: 0px; border-right: 0px" title="image" border="0" alt="image" width="580" height="161" src="\images\posts\13098\image_thumb_10.png" /></p><p> </p><p>同樣的，我們也可以產生靜態的欄位，只是存取範圍不同而已。</p><div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:10fb3388-9e07-4e2b-820b-86d7f81ba167" class="wlWriterEditableSmartContent"><pre class="c#:nocontrols" name="code">
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Generate_From_Usage
{
    class Person
    {
        private string _name;
        private static string _staticField;
        public static string StaticField;
        public string Name { get{return _name;} set; }

        public static string StaticProperty { get { return _staticField; } set; }
    }
}
</pre></div><p> </p><h2>Generate Constructer</h2><p>當物件的建構子不存在時，我們可透過Generate From Usage的Generate Constructer來替我們產生。</p><p><img style="border-bottom: 0px; border-left: 0px; display: inline; border-top: 0px; border-right: 0px" title="image" border="0" alt="image" width="556" height="105" src="\images\posts\13098\image_thumb_13.png" /></a></p><p><a rel="lightbox" href="http://files.dotblogs.com.tw/larrynung/1001/VS2010CodeGeneration_13F14/image_30.png"><img style="border-bottom: 0px; border-left: 0px; display: inline; border-top: 0px; border-right: 0px" title="image" border="0" alt="image" width="556" height="137" src="\images\posts\13098\image_thumb_14.png" /></p><p> </p><p>使用後，會幫我們產生對應的建構子 <br /> </p><div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:704243d8-9306-40f6-96a8-e42f6edfc4f7" class="wlWriterEditableSmartContent"><pre class="c#:nocontrols" name="code">
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Generate_From_Usage
{
    class Person
    {
        private string Name;
        private int Yesr;

        public Person(string Name, int Yesr)
        {
            // TODO: Complete member initialization
            this.Name = Name;
            this.Yesr = Yesr;
        }
    }
}
</pre></div><p> </p><h2>Generate Method</h2><p>當物件的方法不存在時，我們可透過Generate From Usage的Generate Method來替我們產生。</p><p><img style="border-bottom: 0px; border-left: 0px; display: inline; border-top: 0px; border-right: 0px" title="image" border="0" alt="image" width="538" height="126" src="\images\posts\13098\image_thumb_11.png" /></p><p> </p><p>使用後，會幫我們產生對應的方法 <br /> </p><div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:a6322d3f-e6a4-420e-819d-60c05e685183" class="wlWriterEditableSmartContent"><pre class="c#:nocontrols" name="code">
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Generate_From_Usage
{
    class Person
    {
        internal void SayHello()
        {
            throw new NotImplementedException();
        }
    }
}
</pre></div><p> </p><p>若要產生靜態的方法，我們可以像下圖這般作Generate Method</p><p><img style="border-bottom: 0px; border-left: 0px; display: inline; border-top: 0px; border-right: 0px" title="image" border="0" alt="image" width="599" height="137" src="\images\posts\13098\image_thumb_12.png" /></p><p> </p><p>使用後，靜態的方法就產生了 <br /> </p><div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:650a5634-2df9-4c9e-be66-0207af8c0d81" class="wlWriterEditableSmartContent"><pre class="c#:nocontrols" name="code">
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Generate_From_Usage
{
    class Person
    {
        internal void SayHello()
        {
            throw new NotImplementedException();
        }

        internal static void StaticSayHello()
        {
            throw new NotImplementedException();
        }
    }
}
</pre></div><p> </p><h2>Link</h2><ul><li>VS 2010 Generate From Usage</a></li><li><a target="_blank" href="http://msdn.microsoft.com/en-us/library/dd409796(VS.100).aspx">Generate From Usage</a></li><li><a target="_blank" href="http://msdn.microsoft.com/en-us/library/dd998313(VS.100).aspx">Walkthrough: TDD Support with the Generate From Usage Feature</a></li><li><a target="_blank" href="http://blog.noop.se/archive/2009/06/16/generate-from-usage-in-visual-studio-2010.aspx">Generate From Usage in Visual Studio 2010</a></li><li><a target="_blank" href="http://blogs.msdn.com/vbteam/archive/2008/12/13/walkthrough-tdd-support-with-the-generate-from-usage-feature-in-vs-2010-lisa-feigenbaum.aspx">Walkthrough: TDD Support with the Generate From Usage Feature in VS 2010 (Lisa Feigenbaum)</a></li><li><a target="_blank" href="http://blogs.msdn.com/charlie/archive/2009/11/07/hdi-video-generate-from-usage-with-karen-liu.aspx">HDI Video: Generate from Usage in Visual Studio 2010 with Karen Liu</a></li><li><a target="_blank" href="http://msdn.microsoft.com/en-us/vcsharp/ee633445.aspx">How Do I Use Generate from Usage in Visual Studio 2010?</li></ul>
