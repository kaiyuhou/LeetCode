Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?

### 题意
给一个数，把每一位加起来，重复这个过程，直到变为一位数

### 题解
这是一个深刻的数学问题，叫做digital root

一个数如果被9整除，digital root就是9
否则就是模9的余数
