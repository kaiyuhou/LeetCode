iven a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

### 题意
给一个拨号序列，给出这个序列可能对应的字符串

### 题解
就是 3^len(list)种可能，标准的递归解全排列问题。
每次递归都是增加一重循环