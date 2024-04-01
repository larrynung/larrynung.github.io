---
title: "LeetCode - Contains Duplicate"
date: "2015-07-05 22:58:00"
description: "LeetCode - Contains Duplicate"
tags: [LeetCode]
---


LeetCode 的 Contains Duplicate 題目如下：  

Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.  

<!-- More -->

<br/>

簡單說他要的是要一個功能，當給予一個整數陣列，能找出陣列中是否有重複的數值。如果有重複則方法回傳 true，如果沒有重複則回傳 false。

<br/>

這邊筆者是用迴圈搭配 HashSet 來處理，每跑一個數就去判斷 HashSet 是否有重複的資料，有則回傳 true，沒有則加到 HashSet 中。  

```c#
public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        var length = nums.Length;
        var hs = new HashSet<int>();
        for(var idx = 0; idx < length; ++idx)
        {
            var num = nums[idx];
            if(hs.Contains(num))
                return true;
            hs.Add(num);
        }
        return false;
    }
}
```

<br/>

{% img /images/posts/ContainsDuplicate/1.png %}


<br/>

Link
----
* [Contains Duplicate | LeetCode OJ](https://leetcode.com/problems/contains-duplicate/)
