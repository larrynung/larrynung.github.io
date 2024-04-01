---
title: "LeetCode - Number of 1 Bits"
date: "2016-02-24 00:36:00"
description: "LeetCode - Number of 1 Bits"
tags: [LeetCode]
---


LeetCode 的 Number of 1 Bits 題目如下：  

Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).  

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.  


<!-- More -->

<br/>


簡單的說就是給予一個整數，回傳該數值用二進制表示時有多少個 1。  

<br/>


這邊我們可以用 while 迴圈持續的用 n-1 去做 and 運算，並計算運行次數，直至 n 變為 0。  

```c#
public class Solution {
    public int HammingWeight(uint n) {
         int count = 0;
         while(n > 0) {
             n &= (n-1);
             ++count;
         }
         return count;
    }
}
```

<br/>


{% img /images/posts/NumberOf1Bits/1.png %}

<br/>

Link
----
* [Number of 1 Bits | LeetCode OJ](https://leetcode.com/problems/number-of-1-bits/)
