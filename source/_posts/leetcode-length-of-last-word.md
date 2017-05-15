---
layout: post
title: "LeetCode - Length of Last Word"
date: 2015-09-11 10:02:00
comments: true
tags: [LeetCode]
keywords: "LeetCode"
description: "LeetCode - Length of Last Word"
---

LeetCode 的 Length of Last Word 題目如下：  

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.  

If the last word does not exist, return 0.  

Note: A word is defined as a character sequence consists of non-space characters only.  

For example,   
Given s = "Hello World",  
return 5.  

<!-- MORE -->

<br/>

簡單說他要的是要一個功能，當給予一個由大小寫字元與空字元所組成的字串，會回傳最後一個 Word 的長度。  

如果最後一個 Word 不存在，則回傳0。  

舉個例子來說:  

給予 "Hello World", 會回傳 5.  

<br/>

這邊筆者的作法是先將字串尾端的空字元刪除，然後用字元的長度去減去最後空字元的索引。  
```c#
public class Solution {
    public int LengthOfLastWord(string s) {
        var input = s.TrimEnd();
        return (input.Length - 1) - input.LastIndexOf(' ');
    }
}
```

{% img /images/posts/LengthOfLastWord/1.png %}

<br/>

Link
----
* [Length of Last Word | LeetCode OJ](https://leetcode.com/problems/length-of-last-word/)
