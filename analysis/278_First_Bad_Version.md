Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

### 题意
判断在一个数组用第一次出现BadVersion的位子

尽可能少的访问数组

### 题解
标准的二分查找，我第一次写的时候不出所料地写错了
l = 1
r = n
while r > l:
    m = (l + r) / 2
    if isBadVersion(m):
        r = m - 1
    else:
        l = m + 1       