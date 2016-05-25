---
layout: post
title: "LeetCode - Move Zeroes"
date: 2016-02-28 21:01:00
comments: true
categories: [LeetCode]
keywords: "LeetCode"
description: "LeetCode - Move Zeroes"
---

LeetCode 的 Move Zeroes 題目如下：  

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.  

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].  

Note:  
You must do this in-place without making a copy of the array.  
Minimize the total number of operations.  

<!-- More -->

<br/>


簡單的說就是給予一串陣列，回傳的陣列會將所有的 0 往後移。  

<br/>


這邊我們可以用迴圈遍巡陣列中的每個元素，並用一個區域變數紀錄下一個非零值放置的索引。如果遍巡的元素值大於 0 則將該元素與下一個非零值索引位置的元素互換。  

{% codeblock lang:c# %}
public class Solution {
    public void MoveZeroes(int[] nums) {
        var temp = 0;
        var tempIdx = 0;
        var count = nums.Length;
        for(var idx = 0; idx < count; ++idx)
        {
            if (nums[idx] == 0)
                continue;
                
            temp = nums[idx];
            nums[idx] = nums[tempIdx];
            nums[tempIdx] = temp;
            
            ++tempIdx;
        }
    }
}
{% endcodeblock %}

<br/>


{% img /images/posts/MoveZeroes/1.png %}

<br/>

Link
----
* [Move Zeroes | LeetCode OJ](https://leetcode.com/problems/move-zeroes/)
