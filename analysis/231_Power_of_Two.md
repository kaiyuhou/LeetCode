Given an integer, write a function to determine if it is a power of two.

### 题意
判断一个整数是否为2的次方

### 题解
隐含的条件是可能出现负数。

使用位运算，妙不可言
n>0 and (n&(n-1)) == 0