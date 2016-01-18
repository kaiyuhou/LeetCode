Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"

### 题意
给定数字n，给出所有n个括号的合法组合

### 题解
考虑到第i个左括号（，它可以直接放在当前位置j
如果位置j可以放下m个合法的右括号），那么第i个左括号可以放在这m个右括号中的任意一个后面
所以第i个左括号（有 1 + m 个位置可以放

如果放在了第k个右括号的后面，那么下一个左括号只有 m - k + 1 个合法的放置位置

递归回溯求解 