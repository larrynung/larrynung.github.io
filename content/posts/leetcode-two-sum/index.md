---
title: "LeetCode - Two Sum"
date: "2015-07-05 21:56:00"
description: "LeetCode - Two Sum"
---

LeetCode 的 Two Sum 題目如下：

Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

簡單說他要的是要一個功能，能輸入一個整數陣列與指定的目標數，會找出陣列中哪兩個索引指到的整數加起來會是指定的目標數。

方法回傳的索引以 1 為基底，且第一個數值小於第二個數值。

舉個例子來說...

當我們輸入 numbers={2, 7, 11, 15}, target=9

其輸出會是 index1=1, index2=2

這邊最直覺得解法，應該就是巢狀 for 迴圈下去處理，像是下面這樣：

```c#
public class Solution {
public int[] TwoSum(int[] nums, int target) {
for(var num1Idx = 0; num1Idx ();
for(var idx = 0; idx < length; ++idx)
{
var num = nums[idx];
if(dict.ContainsKey(num))
return new int[] {dict[num] + 1, idx + 1};

dict[target - num] = idx;
}
throw new ArgumentException("Invalid argument.");
}
}
```

這樣跑出來的數值就會漂亮...

{% img /images/posts/TwoSum/2.png %}

Link
----
* [Two Sum | LeetCode OJ](https://leetcode.com/problems/two-sum/)