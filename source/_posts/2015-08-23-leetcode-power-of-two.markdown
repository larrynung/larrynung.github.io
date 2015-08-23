---
layout: post
title: "LeetCode - Power of Two"
date: 2015-08-23 23:01
comments: true
categories: [LeetCode]
keywords: "LeetCode"
description: "LeetCode - Power of Two"
---

LeetCode 的 Power of Two 題目如下：  

Given an integer, write a function to determine if it is a power of two.  

<!-- More -->

<br/>

簡單說他要的是要一個功能，給予一個整數，能判別他是否是 2 的冪次。  

<br/>

這邊筆者本來是反覆的用 2 去除，看是否可以整除。  

{% codeblock lang:c# %}
public class Solution {
    public bool IsPowerOfTwo(int n) {
        if (n == 0) 
            return false;
            
        if (n == 1) 
            return true;
            
        var mod = -1;
        do
        {
            mod = n % 2;
            n /= 2;
        }
        while(n != 1 && mod == 0);
        
        return n == 1 && mod == 0;
    }
}
{% endcodeblock %}

<br/>


後來參考網友的作法才想起來可以用位元運算下去處理，寫起來會更為簡潔，像是這樣：  

{% codeblock lang:c# %}
public class Solution {
    public bool IsPowerOfTwo(int n) {
        while ((n & 1) == 0 && n > 0) {
            n >>= 1;
        }
        return n == 1;
    }
}
{% endcodeblock %}

<br/>


{% img /images/posts/PowerOfTwo/1.png %}

<br/>

Link
----
* [Power of Two | LeetCode OJ](https://leetcode.com/problems/power-of-two/)
