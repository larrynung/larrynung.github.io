---
title: "LeetCode - Power of Three"
date: "2016-02-18 23:44:00"
description: "LeetCode - Power of Three"
tags: [LeetCode]
---


LeetCode 的 Power of Three 題目如下：  

Given an integer, write a function to determine if it is a power of three.  

<!-- More -->

<br/>


簡單說他要的是要一個功能，給予一個整數，能判別是否為 3 的冪次。

<br/>


這邊我們只要判斷數值是否大於零，且是否可整除 1162261467 即可。1162261467 是來自 3^19，為最大的 3 冪次整數，如果某數值可以將之整除，即代表該數值為 3 的冪次。    

```c#
public class Solution {
    public bool IsPowerOfThree(int n) {
         return n > 0 && 1162261467 % n == 0;
    }
}
```

<br/>


{% img /images/posts/PowerOfThree/1.png %}

<br/>

Link
----
* [Power of Three | LeetCode OJ](https://leetcode.com/problems/power-of-three/)
