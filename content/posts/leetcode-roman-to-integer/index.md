---
title: "LeetCode - Roman to Integer"
date: "2015-09-11 23:16:00"
description: "LeetCode - Roman to Integer"
tags: [LeetCode]
---


LeetCode 的 Roman to Integer 題目如下：  

Given a roman numeral, convert it to an integer.  

Input is guaranteed to be within the range from 1 to 3999.  

<!-- More -->

<br/>

簡單的說他是要一個功能，當給予一個羅馬數字，能將它轉換成對應的數值。  

這需要參考 [羅馬數字 - 維基百科，自由的百科全書](https://zh.wikipedia.org/wiki/%E7%BD%97%E9%A9%AC%E6%95%B0%E5%AD%97)，看羅馬數字背後的規則。  

<br/>


羅馬數字有七個字母組成，分別為 I（1）、V（5）、X（10）、L（50）、C（100）、D（500）和 M（1000）。當字母重複出現，則表示數值為重複倍。如果較大的字母右邊放上較小的字母，表示兩數要相加，反之表示大數要減小數。其它的規則跟這題無關，就不提了。  

<br/>


所以像是 4 對應到的就是 IV （5 - 1），XX 對應到 20 （10 + 10）， VIII 對應到 8 (5 + 1 + 1 + 1)，以此類推。   

<br/>


這邊筆者是用一個字典檔存放羅馬數字字元與其對應的數值，從輸入參數的後面往前處理，如果前一個字元對應到的數值大於現在這字元的數值，則將回傳值減去當前數值，反之則加上當前數值。  

```c#
public class Solution {
    public int RomanToInt(string s) {
        var dict = new Dictionary<char, int>()
		{
			{'I', 1},
			{'V', 5},
			{'X', 10},
			{'L', 50},
			{'C', 100},
			{'D', 500},
			{'M', 1000},
		};

		var ret = 0;
		var prev = -1;
		for(var idx = s.Length - 1; idx >= 0; --idx)
		{	
			var current = dict[s[idx]];
	
			if(prev > current)
				ret -= current;
			else
				ret += current;


			prev  = current;
		}
		return ret;
    }
}
```

{% img /images/posts/RomanToInt/1.png %}

<br/>	

Link
----
* [Roman to Integer | LeetCode OJ](https://leetcode.com/problems/roman-to-integer/)
