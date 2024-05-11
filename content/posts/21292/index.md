---
title: "[C#]Effective C# 條款十五：利用using和try/finally語句來清理資源."
slug: "[CSharp]Effective C# 條款十五：利用using和try/finally語句來清理資源."
date: "2011-02-09 03:33:58"
description: "[C#]Effective C# 條款十五：利用using和try/finally語句來清理資源."
tags: [CSharp]
---

<p>
	非拖管資源故名思義該資源是非拖管的，跟一般的托管資源不同的是，這些非拖管資源在建立後必須自行去作釋放的動作，不然會產生資源洩漏。為解決這樣的問題，在.NET BCL提供IDisposable介面，提供.NET程式非拖管資源釋放的標準做法，藉由呼叫該介面的Dispose()方法，我們可以對非拖管的系統資源進行釋放的動作。在一般狀況下，這樣的釋放動作應由使用者自行叫用，也就是說當在程式中使用實作有IDisposable介面的類別時，需記得自行呼叫Dispose()方法去釋放資源。若忘了呼叫在釋放的動作，在標準的IDisposable介面實作上也提供了額外的保險措施，會在IDisposable介面實作時為解構子加入Dispose()方法的調用。因此若使用者忘了自行呼叫Dispose()方法釋放資源，在物件解構時仍會將資源給釋放掉。</p>
<p>
	 </p>
<p>
	雖然IDisposable介面標準的實作會加入保險措施，但是若使用的是第三方元件或是別的來源取得的程式，我們並不能保證撰寫的人會遵循應有的規則，因此我們使用到的是有可能沒有保險措施的類別。就算有加入保險措施，透過解構子去釋放物件存留在記憶體中的時間也會比較長，因此最好還是盡可能的自行手動釋放。</p>
<p>
	 </p>
<p>
	但若很單純的直接呼叫Dispose()方法釋放資源，其實也是有些問題存在，像是下面這個例子雖然在程式的後面有自行呼叫Dispose()方法釋放資源，但若運行到cmd.ExecuteNonQuery()這行，在執行SQL語法時發生了例外，則後面的Dispose()方法將永遠不會被調用到。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:f351b790-8fb5-482c-a8df-3da32a501192" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c#" name="code">
	public void ExecuteCommand(string connString, string CommandString)
        {
            SqlConnection conn = new SqlConnection(connString);
            SqlCommand cmd = new SqlCommand(CommandString, conn);

            conn.Open();
            cmd.ExecuteNonQuery();

            cmd.Dispose();
            conn.Dispose();
        }</pre>
</div>
<p>
	 </p>
<p>
	.NET語言的設計者為此提供了using與try/finally兩種語法，開發人員可藉由這兩種語法來避開這類問題。以上面的例子來看，用using語法可改寫為這樣：</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:32321914-6b10-4d6c-a349-4b650735c010" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c#" name="code">
	public void ExecuteCommand(string connString, string CommandString)
        {
            using (SqlConnection conn = new SqlConnection(connString))
            {
                using (SqlCommand cmd = new SqlCommand(CommandString, conn))
                {
                    conn.Open();
                    cmd.ExecuteNonQuery();
                }
            }
        }</pre>
</div>
<p>
	 </p>
<p>
	也可以用try/finally語法去改寫：</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:b7d36304-b0b9-4bbe-aa04-8142acb75fc1" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c#" name="code">
	public void ExecuteCommand(string connString, string CommandString)
        {
            SqlConnection conn = null;
            SqlCommand cmd = null;
            try
            {
                conn = new SqlConnection(connString);
                cmd = new SqlCommand(CommandString, conn);

                conn.Open();
                cmd.ExecuteNonQuery();
            }
            finally
            {
                if (cmd != null)
                    cmd.Dispose();

                if (conn != null)
                    conn.Dispose();
            }
        }</pre>
</div>
<p>
	 </p>
<p>
	using適用於只有少數物件需要釋放的情況，try/finally語法則適用於多個物件需要釋放的情況。這兩種語法是等價的，在編譯時編譯器會將using改為try/finally的寫法，故這兩種寫法皆可確保資源能有效的被釋放。</p>
<p>
	 </p>
<p>
	若遇有不確定是否實作有IDisposable介面的情形時，可用as輔助using語法來作釋放的動作。像是：</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:f61868f2-6ea9-45ea-b4a0-c68f11f47307" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c#" name="code">
	Object obj = GetObject();
            using (obj as IDisposable)
            {
                ...
            }</pre>
</div>
<p>
	 </p>
<p>
	利用as輔助當類別未實作IDisposable介面時，等同撰寫using (null)這樣的語句，只是不會作任何動作；若類別有時作IDisposable介面，則資源會被using語法給釋放。</p>
<p>
	 </p>
<p>
	若是類別含有Close()方法且實作有IDisposable介面，優先叫用Dispose()方法，因為叫用Close()方法物件仍會存留在終結佇列中，而若是呼叫Dispose()方法，除了會去作Close()方法的動作，也會在裡面叫用GC.SuppressFinalize()方法去停止終結操作。</p>
<p>
	 </p>
<p>
	另外ㄧ提，在呼叫Dispose()方法並不會將物件至記憶體中回收，只是會去釋放物件的非拖管資源，故當我們呼叫Dispose()方法釋放時，需確保物件不會再被使用，不然可能會出現難以偵測的問題。</p>
<p>
	 </p>
<h2>
	Link</h2>
<ul>
	<li>
		《Effective C#》Item 15：利用using和try-finally来释放资源</li>
	<li>
		IDisposable 介面</li>
</ul>
