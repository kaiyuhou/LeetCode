Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3

begin to intersect at node c1.

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.

### 题意
找到两个链表交汇的地方
在O(n)的时间和O(1)的空间，不能改变原来的两个链表结构

### 解法
找到两个链表的长度，从他们剩余长度相同的地方开始一一匹配