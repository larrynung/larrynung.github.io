---
layout: post
title: "LeetCode - Valid Anagram"
date: 2015-08-15 21:44
comments: true
categories: [LeetCode]
keywords: "LeetCode"
description: "LeetCode - Valid Anagram"
---

LeetCode 的 Valid Anagram 題目如下：   

Given two strings s and t, write a function to determine if t is an anagram of s.  

For example,  
s = "anagram", t = "nagaram", return true.  
s = "rat", t = "car", return false.  

Note:  
You may assume the string contains only lowercase alphabets.  

<!-- More -->

<br/>

簡單說他要的是要一個功能，當給予兩個字串，能判斷出這兩個字串是否只是不同的組合順序。  

舉個例子來說,
s = "anagram", t = "nagaram", 回傳 ture.  
s = "rat", t = "car", 回傳 false.  

<br/>


這邊我們可以統計兩個字串中的每個字元出現的個數是否一樣，也可以像筆者這樣簡單的將字串排序後直接比對。  

<br/>


{% codeblock lang:c# %}
public class Solution {
    public bool IsAnagram(string s, string t) {
        return SortString(s) == SortString(t);
    }
    private static string SortString(string str)
    {
		var ca = str.ToCharArray();
		Array.Sort(ca);
        return new String(ca);
    }
}
{% endcodeblock %}

<br/>


{% img /images/posts/ValidAnagram/1.png %}

<br/>

Link
----
* [Valid Anagram | LeetCode OJ](https://leetcode.com/problems/valid-anagram/)
