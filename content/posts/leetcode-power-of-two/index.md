---
title: "LeetCode - Power of Two"
date: "2015-08-23 23:01:00"
description: "LeetCode - Power of Two"
tags: [LeetCode]
---


LeetCode 的 Power of Two 題目如下：  

Given an integer, write a function to determine if it is a power of two.  

<!-- More -->

<br/>

簡單說他要的是要一個功能，給予一個整數，能判別他是否是 2 的冪次。  

<br/>


可以簡單的用迴圈反覆的除以 2，看是否可以整除。  

```c#
public class Solution {
    public bool IsPowerOfTwo(int n) {
        if (n == 0) 
            return false;
            
        if (n == 1) 
            return true;
            
        var mod = -1;
        do
        {
            mod = n % 2;
            n /= 2;
        }
        while(n != 1 && mod == 0);
        
        return n == 1 && mod == 0;
    }
}
```

<br/>


也可以用位元運算下去處理，寫起來會更為簡潔，像是這樣：  

```c#
public class Solution {
    public bool IsPowerOfTwo(int n) {
        while ((n & 1) == 0 && n > 0) {
            n >>= 1;
        }
        return n == 1;
    }
}
```

<br/>


{% img /images/posts/PowerOfTwo/1.png %}

<br/>


或者也可以判斷數值是否大於零，且是否可整除 1073741824 即可。1073741824 是來自 2^30，為最大的 2 冪次整數，如果某數值可以將之整除，即代表該數值為 2 的冪次。

```c#
public class Solution {
    public bool IsPowerOfTwo(int n) {
        return n > 0 && 1073741824 % n == 0;
    }
}
```

<br/>


{% img /images/posts/PowerOfTwo/2.png %}

<br/>

Link
----
* [Power of Two | LeetCode OJ](https://leetcode.com/problems/power-of-two/)
