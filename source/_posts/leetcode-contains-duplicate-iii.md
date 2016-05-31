---
layout: post
title: "LeetCode - Contains Duplicate III"
date: 2015-07-28 23:59:00
comments: true
tags: [LeetCode]
keywords: 
description: "LeetCode - Contains Duplicate III"
---

LeetCode 的 Contains Duplicate III 題目如下：  

Given an array of integers, find out whether there are two distinct indices i and j in the array such that the difference between nums[i] and nums[j] is at most t and the difference between i and j is at most k.  

<!-- More -->

<br/>


簡單說他要的是要一個功能，當給予一個整數陣列，能找出兩個不同的索引值，這兩個索引值的差距最多為 k，且這兩個索引值對應整數陣列所得到的整數值相差最多為 t。  

<br/>


這邊筆者是用迴圈搭配 Dictionary 來處理，Dictionary 內只存放 k 筆資料，每次處理一個數值時就去查看 Dictionary 內是否有相差 t 的數值。  如果有則去判斷索引值的差距是否在 k 內，是的話則回傳 true。  

{% codeblock lang:c# %}
public class Solution {
	    public bool ContainsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        var length = nums.Length;
        var dict = new Dictionary<int, long>(k);
        for(var idx = 0; idx < length; ++idx)
        {
            if(idx > k) dict.Remove(idx - k -1);
            var num = nums[idx];
            
            if(dict.Count > 0)
            {
                var greater = dict.Where(item => item.Value >= num).Take(1).ToArray();
                if(greater.Any()){
                    var diff = greater[0].Value - num;
                    if(diff <= t)
                        return true;
                }
                
                var smaller = dict.Where(item => num >= item.Value).Take(1).ToArray();
                if(smaller.Any()){
                    var diff = num - smaller[0].Value;
                    if(diff <= t)
                        return true;
                }
            }
            dict[idx] = num;
        }
        return false;
    }
}
{% endcodeblock %}

<br/>


{% img /images/posts/ContainsDuplicateIII/1.png %}

<br/>

Link
----
* [Contains Duplicate III | LeetCode OJ](https://leetcode.com/problems/contains-duplicate-iii/)
