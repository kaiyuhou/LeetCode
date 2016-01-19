Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

For example, given candidate set 2,3,6,7 and target 7, 
A solution set is: 
[7] 
[2, 2, 3] 

The same repeated number may be chosen from C unlimited number of times.

### 题意
给定一个非重复数组，和一个数，求能够组成这个这个数的所以可能
可以重复使用数组中的数

### 题解
trick 1：给定的数组是无序的，需要排个序
trick 2: 要求给出的答案必须按照升序给出

直接搜索就好，搜索函数是def search(self, nums, sel, t, ans):
不停的减少搜索空间就好

tip: 不要再leetCode上使用全局变量，同样的算法，使用全局变量会超时，但是在本地编译器的时间是一致的。