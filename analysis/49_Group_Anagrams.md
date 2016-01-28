Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]

### 题意
给定一组字符串，把它们根据构成的字母分组

### 题解

1.排序后使用hash函数分组

2.使用高级的python特性