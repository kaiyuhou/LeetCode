Given two strings s and t, write a function to determine if t is an anagram of s.

### 题意
给定两个字符串，判断他们是否为anagram。

这里的anagram不要求字母出现的顺序一样，只要求字母出现的次数一样就可以了。

### 题解
return sorted(s) == sorted(t)