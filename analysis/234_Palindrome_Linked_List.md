Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?

### 题意
判断一个链表是不是回文的
要求O(n)的时间和O(1)空间

### 题解
分三步
1.使用快慢指针找到链表的中点，即两个指针，一个走1步，一个走2步
2.反转后半段的链表，用LeetCode 206中的方法
3.判断