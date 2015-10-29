You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

### 题意
给定两个链表，他们代表两个数，由低位到高位排列
输出他们求和的结果

### 题解
我的代码打败的99.55%的玩家。
使用的是在l1上做加法，而不去申请新的节点。
需要特判一下两个链表不一样长的情况。

因为要处理末尾的进位，所以保留了当前结点的上一个节点。
如果引入dumb节点，代码可以更优雅一点。