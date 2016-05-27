---
layout: post
title: "LeetCode - Plus One"
date: 2015-08-12 23:30:00
comments: true
categories: [LeetCode]
keywords: "LeetCode"
description: "LeetCode - Plus One"
---

LeetCode 的 Plus One 題目如下：  

Given a non-negative number represented as an array of digits, plus one to the number.  

The digits are stored such that the most significant digit is at the head of the list.  

<!-- More -->

<br/>


簡單說他要的是要一個類似加法器的功能。給予一個非負的數值陣列用以表示一個非負的數值，能回傳加一後的數值。  

<br/>


這邊筆者是用 for 迴圈從輸入的陣列尾端往前遍巡，第一個處理的陣列元素加一後如果有超過 10，則將當前數值改為除 10 後的餘數，且進位的值帶到下一個陣列數值去做相同的處理。最後跑完如果無進位值，則把當前處理完的陣列回傳。若有進位值，則將進位值與當前處理完的陣列合併回傳。  

{% codeblock lang:c# %}
public class Solution {
    public int[] PlusOne(int[] digits) {
        var carry = 1;
        var result = new int[digits.Length];
        for(var idx = digits.Length - 1; idx >= 0; --idx)
        {
            var digit = digits[idx];
            var newDigit = digit + carry;
            carry = newDigit / 10;
            result[idx] = newDigit % 10;
        }
        
        if(carry == 0)
            return result;
            
        return (new int[]{carry}).Concat(result).ToArray();
    }
}
{% endcodeblock %}

<br/>


{% img /images/posts/PlusOne/1.png %}

<br/>

Link
----
* [Plus One | LeetCode OJ](https://leetcode.com/problems/plus-one/)
