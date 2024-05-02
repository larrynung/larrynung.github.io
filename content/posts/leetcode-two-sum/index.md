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

<!-- More -->

<br/>


簡單說他要的是要一個功能，能輸入一個整數陣列與指定的目標數，會找出陣列中哪兩個索引指到的整數加起來會是指定的目標數。  

方法回傳的索引以 1 為基底，且第一個數值小於第二個數值。  

舉個例子來說...  

當我們輸入 numbers={2, 7, 11, 15}, target=9  

其輸出會是 index1=1, index2=2  

<br/>


這邊最直覺得解法，應該就是巢狀 for 迴圈下去處理，像是下面這樣：  

```c#
public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        for(var num1Idx = 0; num1Idx < nums.Length; ++num1Idx)
        {
            var num1 = nums[num1Idx];
            for(var num2Idx = num1Idx; num2Idx < nums.Length; ++num2Idx)
            {
                var num2 = nums[num2Idx];
                
                if(num1 + num2 == target)
                    return new int[] { num1, num2 };
            }
        }
        throw new ArgumentException("Invalid argument.");
    }
}
```

<br/>


但是這樣的寫法效能不彰，會超時時間限制...  

{% img /images/posts/TwoSum/1.png %}

<br/>


要改善的話我們可以用迴圈搭配 Dictionary，每跑一個數就去判斷 Dictionary 是否有資料，如果有則將資料取出與當前索引一併加一回傳，如果沒有則將 目標數 - 當前數 做 Key 值，把目前索引存放在 Dictionary 中。  

```c#
public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        var length = nums.Length;
        var dict = new Dictionary<int, int>();
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

<br/>


這樣跑出來的數值就會漂亮...

{% img /images/posts/TwoSum/2.png %}

<br/>

Link
----
* [Two Sum | LeetCode OJ](https://leetcode.com/problems/two-sum/)
