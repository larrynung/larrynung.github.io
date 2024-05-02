---
title: "[C#].NET 4.5 New Feature - Regex match with timeout"
date: "2011-10-25 01:20:13"
description: "[C#].NET 4.5 New Feature - Regex match with timeout"
tags: [CSharp]
---

<p>
	.Net 4.5中Regex多了一個內含Timespan的多載版本，該多載版本方法允許開發人員帶入一個TimeSpan指定Timeout的值，當正規表示式比對運行超過指定的時間即中止比對。</p>
<p>
	<img alt="image" border="0" height="98" src="\images\posts\46293\image_thumb_2.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="574" /></p>
<p>
	 </p>
<p>
	Timeout的時間除了可以透過上述的多載方法傳入外，也可以透過用AppDomain.SetData設定REGEX_DEFAULT_MATCH_TIMEOUT，可指定預設的Timeout值。當正規表示式在做比對時未帶入指定的Timeout值，系統都會使用設定到AppDomain的Timeout去處理。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:ddcbbef0-f166-450b-ac5c-8be2ee69f012" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c#" name="code">
AppDomain.CurrentDomain.SetData("REGEX_DEFAULT_MATCH_TIMEOUT", TimeSpan.FromSeconds(2));</pre>
</div>
<p>
	 </p>
<p>
	對於Timeout的設定值在設定時也有些限制，像是其值必須大於零，且必須要小於25天，不然在運行時會發出ArgumentOutOfRangeException的例外。</p>
<p>
	 </p>
<p>
	 </p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:2fae2e1f-1236-4bd9-9e17-59fd4fd4fc75" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c#" name="code">
isMatch = IsMatch(input, pattern, TimeSpan.FromMilliseconds(0));
isMatch = IsMatch(input, pattern, TimeSpan.FromMilliseconds(-2));
isMatch = IsMatch(input, pattern, TimeSpan.FromDays(25));</pre>
</div>
<p>
	 </p>
<p>
	 </p>
<p>
	若是想要不限制Timeout時間，可帶入-1或是Regex.InfiniteMatchTimeout來做為Timeout的設定值。</p>
<p>
	 </p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:c832cb47-6d1c-4fdc-99e8-a4f644f58e2a" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c#" name="code">
isMatch = IsMatch(input, pattern, Regex.InfiniteMatchTimeout);
isMatch = IsMatch(input, pattern, TimeSpan.FromMilliseconds(-1));</pre>
</div>
<p>
	 </p>
<p>
	設好Timeout後進行正規表示試的比對，當比對時間超過指定的Timeout時間時，系統會發出RegexMatchTimeoutException例外告知，可以從例外中取得比對的字串、比對的Pattern、Timeout值等資訊。(可參閱MSDN中的RegexMatchTimeoutException Class)</p>
<p>
	<img alt="image" border="0" height="209" src="\images\posts\46293\image_thumb.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="574" /></p>
<p>
	 </p>
<p>
	完整範例如下：</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:13a1fe07-c844-4ccd-bad7-e5ea9b3ab7e5" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c#" name="code">
    class Program
    {
        static void Main(string[] args)
        {
            string input = "The quick brown fox jumps over the lazy dog.";
            string pattern = @"([a-z ]+)*!";
            Boolean isMatch = false;

            AppDomain.CurrentDomain.SetData("REGEX_DEFAULT_MATCH_TIMEOUT", TimeSpan.FromSeconds(2));
            isMatch = IsMatch(input, pattern);

            Console.WriteLine();
            isMatch = IsMatch(input, pattern, TimeSpan.FromSeconds(4));
        }

        static Boolean IsMatch(string input, string pattern)
        {
            try
            {
                return Regex.IsMatch(input, pattern, RegexOptions.None);
            }
            catch (RegexMatchTimeoutException ex)
            {
                // handle exception
                Console.WriteLine("Match timed out!");
                Console.WriteLine("- Timeout interval specified: " + ex.MatchTimeout);
                Console.WriteLine("- Pattern: " + ex.Pattern);
                Console.WriteLine("- Input: " + ex.Input);
            }

            return false;
        }

        static Boolean IsMatch(string input, string pattern, TimeSpan timeout)
        {
            try
            {
                return Regex.IsMatch(input, pattern, RegexOptions.None, timeout);
            }
            catch(ArgumentOutOfRangeException ex)
            {
                Console.WriteLine(ex.Message);
            }
            catch (RegexMatchTimeoutException ex)
            {
                // handle exception
                Console.WriteLine("Match timed out!");
                Console.WriteLine("- Timeout interval specified: " + ex.MatchTimeout);
                Console.WriteLine("- Pattern: " + ex.Pattern);
                Console.WriteLine("- Input: " + ex.Input);
            }

            return false;
        }
    }</pre>
</div>
<p>
	 </p>
<p>
	運行結果如下：</p>
<p>
	<img alt="image" border="0" height="287" src="\images\posts\46293\image_thumb_3.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="537" /></p>
<p>
	 </p>
<h2>
	Link</h2>
<ul>
	<li>
		RegexMatchTimeoutException Class</li>
	<li>
		Regular Expressions with Timeout in .NET 4.5</li>
	<li>
		Regex engine updated to allow timeouts in .NET 4.5</li>
	<li>
		Regex.IsMatch Method (String, String, RegexOptions, TimeSpan)</li>
	<li>
		Regex.InfiniteMatchTimeout Field</li>
</ul>
