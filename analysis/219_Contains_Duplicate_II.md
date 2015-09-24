Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.

### 题意
给定数组a和整数k，判断是否存在a[i] = a[j]且|i-j|<=k

### 题解
用map记录最后一次出现某个字符的位子