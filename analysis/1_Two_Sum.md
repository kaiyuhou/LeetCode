Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. 

### 题意
给定一个无序数组，要求找出两个数的和等于目标，返回这两个数的下标

保证有一个解

### 题解
按照数组的顺序走一遍，将已经访问的数记录到dict里面。查找target - nums[i]在不在dict里面