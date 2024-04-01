---
title: "LeetCode - Missing Number"
date: "2016-02-29 22:32:00"
description: "LeetCode - Missing Number"
tags: [LeetCode]
---


LeetCode 的 Missing Number 題目如下：  

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.  

For example,  
Given nums = [0, 1, 3] return 2.  

Note:  
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?  

<!-- More -->

<br/>


簡單的說該方法會被帶入一個陣列，裡面的元素為 0 到 n 不重複的數值，需找到並回傳該陣列缺少的數值。像是如果帶入的陣列是 [0, 1, 3]，該陣列跳過了 2，所以回傳值會是 2。   

<br/>


因為長度為 n 的陣列如果沒有跳號，裡面的元素應該是 0, ..., n，且缺少的數值只有一個。所以我們可以把帶入的陣列跟本來預期的值相減後加總，然後用陣列的長度與之相減。  

```c#
public class Solution {
    public int MissingNumber(int[] nums) {
        var sum = 0;
        var length = nums.Length;
        for (var i = 0; i < length; i++)
            sum += nums[i] - i;
        return length - sum;
    }
}
```

<br/>


{% img /images/posts/MissingNumber/1.png %}

<br/>

Link
----
* [Missing Number | LeetCode OJ](https://leetcode.com/problems/missing-number/)
