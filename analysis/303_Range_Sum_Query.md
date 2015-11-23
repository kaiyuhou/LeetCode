Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.

### 题意
求给定数组的子段和

### 题解
O(n)的时间计算出 sum[j],j form 1 to n 的结果.字段和i，j等于 sum[j] - sum[i]