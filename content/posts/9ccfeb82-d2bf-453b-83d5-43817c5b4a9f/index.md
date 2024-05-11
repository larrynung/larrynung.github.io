---
title: "[C#]DateTime 與 ISO8601 格式字串的相互轉換"
slug: "[CSharp]DateTime 與 ISO8601 格式字串的相互轉換"
date: "2013-11-06 12:00:00"
description: "[C#]DateTime 與 ISO8601 格式字串的相互轉換"
tags: [CSharp]
---

<p>要從DateTime轉換成ISO8601的格式，在.NET中我們有幾種方式，一種是直接帶入ISO8601的Format，像是：</p>  <div id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:730c0ece-bcdd-4a0f-96a0-8936a7482909" class="wlWriterSmartContent" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px"><pre name="code" class="c#">var ISO8601String = dt.ToString(@"yyyy-MM-dd\THH:mm:ss\Z");</pre></div>

<p> </p>

<p>一種是帶入s並在最後面加上"Z"：</p>

<div id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:5d81b4db-5690-4d5f-ab62-2bc8040bebd8" class="wlWriterSmartContent" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px"><pre name="code" class="c#">var ISO8601String = string.Format("{0}Z", dt.ToString("s"));</pre></div>

<p> </p>

<p>最後一種是帶入o：</p>

<div id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:0e2a21ff-973e-428f-870e-4429f788fbf2" class="wlWriterSmartContent" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px"><pre name="code" class="c#">var ISO8601String = dt.ToString("o");</pre></div>

<p> </p>

<p>實際程式撰寫會像下面這樣：</p>

<div id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:f5bf47b3-e999-42cc-8e8b-04b86a116875" class="wlWriterSmartContent" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px"><pre name="code" class="c#">            var dt = DateTime.UtcNow;
            Console.WriteLine(string.Format("{0}Z", dt.ToString("s")));
            Console.WriteLine(dt.ToString("o"));
            Console.WriteLine(dt.ToString(@"yyyy-MM-dd\THH:mm:ss\Z"));</pre></div>

<p> </p>

<p>運行後可以看到時間正確的轉換為ISO8601的格式：</p>

<p><img style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" border="0" alt="image" src="\images\posts\9ccfeb82-d2bf-453b-83d5-43817c5b4a9f\image_thumb_2.png" width="457" height="192" /> </p>

<p> </p>

<p>若要從ISO8601的字串格式轉換回DateTime，可以使用DateTime.TryParseExact，將ISO8601的格式帶入，像是下面筆者所整理的函式一樣：</p>

<p>
  </p><div id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:d886cc4b-db98-4cc4-93b5-7945faa84c6b" class="wlWriterSmartContent" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px"><pre name="code" class="c#">        static DateTime? ToDateTimeFromUTCISO8601(string dateTimeString)
        {
            DateTime dt;
            var sucessed = DateTime.TryParseExact(dateTimeString, new string[] { @"yyyy-MM-dd\THH:mm:ss\Z", "o" }, CultureInfo.InvariantCulture, DateTimeStyles.AssumeUniversal, out dt);

            return sucessed ? new DateTime?(dt) : null;
        }</pre></div>


<p> </p>

<p>使用起來會像下面這樣：</p>

<div id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:799da6f3-5373-48ea-8c4a-64ba568e9c58" class="wlWriterSmartContent" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px"><pre name="code" class="c#">            var dt = ToDateTimeFromUTCISO8601(@"2010-08-20T15:00:00Z");
            var utcDT = dt.Value.ToUniversalTime();</pre></div>

<p> </p>

<div id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:7cb7f632-8702-4a92-8990-1658d73f0783" class="wlWriterSmartContent" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px"><pre name="code" class="c#">            var dt = ToDateTimeFromUTCISO8601(@"2007-06-06T09:03:01.1234567+02:00");
            var utcDT = dt.Value.ToUniversalTime();</pre></div>
