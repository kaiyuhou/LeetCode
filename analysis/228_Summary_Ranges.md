Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

### 题意
输出一个数组中的ranges
range的概念是连续的数, 1 2 3 4 5的range是1->5

### 题解
就是顺序判断过去,判断a[i+1] - a[i]是否等于1
完全就是O(n)的操作
