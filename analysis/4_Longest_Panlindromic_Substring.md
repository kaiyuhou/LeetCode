Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

### 题意
给定一个字符串，求最长的回文字串

### 题解
使用Manacher's Algorithm可以在O(n)的时间内求解，相当精彩。
 > http://www.felix021.com/blog/read.php?2040
算法的基本思想是记录了包含当前结点的最长回文字串位子，由于对称性，当前结点的回文长度，至少等于和它对称的那个节点的回文长度。

通过将字符串 abc 变为 #a#b#c# 这样的形式，只用考虑奇数回文，而不用考虑偶数回文
 
后缀数组也可以做。