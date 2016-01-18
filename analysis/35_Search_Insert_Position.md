Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

### 题意
给定一个升序无重复数组和一个数
求这个数应该插入的位子，如果存在，返回它的位子

### 题解
在有这个数的情况下就是二分搜索，
在没有的情况下，就是34这道题一个边界的请求。
需要特别考虑下插入到 n+1这个位子