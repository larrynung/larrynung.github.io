---
layout: post
title: "LeetCode - Contains Duplicate II"
date: 2015-07-11 15:26:00
comments: true
tags: [LeetCode]
keywords: "LeetCode, Contains Duplicate"
description: "LeetCode - Contains Duplicate II"
---

LeetCode 的 Contains Duplicate II 題目如下：  

<!-- More -->

Given an array of integers and an integer k, find out whether there there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.  

<br/>

簡單說他要的是要一個功能，當給予一個整數陣列與一個整數值 k，能找出兩個不同的索引值，這兩個索引值的差距最多為 k，且其對應到的整數陣列的值是相同的。  

<br/>


這邊筆者是用迴圈搭配 Dictionary 來處理，每跑一個數就去判斷 Dictionary 是否有含有一樣的數值，如果有則去判斷索引值的差距是否在 k 內，是的話則回傳 true。如果不是或是數值不存在在 Dictionary 內，則將其加入或是將 Dictionary 中的索引值更新，便於後續查找。如果整個陣列跑完都找不到結果，將 false 回傳。      

```c#
public class Solution {
    public bool ContainsNearbyDuplicate(int[] nums, int k) {
        var length = nums.Length;
        var dict = new Dictionary<int, int>();
        for(var idx = 0; idx < length; ++idx)
        {
            var num = nums[idx];
            var prevIdx = -1;
            if(dict.TryGetValue(num, out prevIdx))
            {
                if(idx - prevIdx <= k)
                    return true;
            }
            dict[num] = idx;
        }
        return false;
    }
}
```

<br/>

{% img /images/posts/ContainsDuplicateII/1.png %}

<br/>

Link
----
* [Contains Duplicate II | LeetCode OJ](https://leetcode.com/problems/contains-duplicate-ii/)
