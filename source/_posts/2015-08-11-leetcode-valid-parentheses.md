---
layout: post
title: "LeetCode - Valid Parentheses"
date: 2015-08-11 23:21:00
comments: true
categories: [LeetCode]
keywords: "LeetCode"
description: "LeetCode - Valid Parentheses"
---

LeetCode 的 Valid Parentheses 題目如下：  

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.  

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.  

<!-- More -->

<br/>


簡單說他要的是要一個功能，帶入的字串只會由 '('、')'、'{', '}'、'[' 與 ']' 這幾個字元所組成，需判斷輸入是否正確。  

<br/>


輸入的字元需成對並符合一定的順序，成對的字元內不可夾雜不成對的字元，像是 "()" 與 "()[]{}" 就是正確的格式，而 "(]" 與 "([)]" 不是。  

<br/>


這邊筆者是用 Dictionary 去紀錄成對的字元。然後將帶入的字串字元依序處理。如果其字元跟堆疊最後的字元成對，則將堆疊最後的字元取出。若不成對則將當前字元放入堆疊內。  

<br/>


堆疊在使用前會先放一個空的字元，如果處理到最後堆疊內還剩一個字元，代表帶入的字串是正確的，反之則帶入的字串是錯誤的。  

{% codeblock lang:c# %}
public class Solution {
    public bool IsValid(string s) {
        var validChars = new Dictionary<char, char>()
		{
			{'(', ')'},
			{'{', '}'},
			{'[', ']'}
		};
		var length = s.Length;
		var st = new Stack<char>(length + 1);
		
		st.Push(' ');
		
		for (var idx = 0; idx < length; ++idx)
		{
			var current = s[idx];
			var top = st.Peek();
				
			if(validChars.ContainsKey(top))
			{
				var closeChar = validChars[top];
				
				if (current == closeChar)
				{
					 st.Pop();
					 continue;
				}
			}
			
			st.Push(current);
		}

		return st.Count == 1;
    }
}
{% endcodeblock %}

<br/>


{% img /images/posts/ValidParentheses/1.png %}

Link
----
* [Valid Parentheses | LeetCode OJ](https://leetcode.com/problems/valid-parentheses/)
