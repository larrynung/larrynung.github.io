---
layout: post
title: "LeetCode - Add Digits"
date: 2016-02-10 09:04:00
comments: true
tags: [LeetCode]
keywords: "LeetCode"
description: "LeetCode - Add Digits"
---

LeetCode 的 Add Digits 題目如下：  

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.  

For example:  

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.  

<!-- More -->

<br/>


簡單的說就是給予一個整數，反覆的將每個位數值加總，直至數值只有一個位數為止。  

<br/>


最直覺得解法就是用迴圈下去處理，判斷數值是否大於等於 10，如果大於等於 10，則將每個位數的數值加總取代本來的數值。如果數值小於 10，則直接將數值回傳。    

{% codeblock lang:c# %}
public class Solution {
    public int AddDigits(int num) {
        var value = num;
        while(value >= 10)
        {
            var originalValue = value;
            var newValue = 0;
            do
            {
                newValue += originalValue / 10;
                originalValue = originalValue % 10;
            }while(originalValue >= 10);
            
            newValue += originalValue;
            
            value = newValue;
        }
        return value;
    }
}
{% endcodeblock %}

<br/>

{% img /images/posts/AddDigits/1.png %}


<br/>


但比較漂亮的解法是像下面這樣：  

{% codeblock lang:c# %}
public class Solution {
    public int AddDigits(int num) {
        return (num - 1) % 9 + 1;
    }
}
{% endcodeblock %}

<br/>

{% img /images/posts/AddDigits/2.png %}


<br/>


Link
----
* [Add Digits | LeetCode OJ](https://leetcode.com/problems/add-digits/)
