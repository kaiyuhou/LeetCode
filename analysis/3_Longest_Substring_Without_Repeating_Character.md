Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.

### 题意
给定一个字符串，求最长不重复字符的长度

### 题解
记录每一个字符上一次出现的位子，和上次出现重复字符的位子。
长度为 当前字符 - max（当前字符长次出现的位子，上次出现重复字符的位子）