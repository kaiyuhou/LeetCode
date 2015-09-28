Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

### 题意
将数组中所有的0移到结尾，不改变其它元素的顺序。
要求不能使用新的数组

### 题解
是两个指针，一个指非0的元素，一个顺序前进，让后让非零的元素和0交换