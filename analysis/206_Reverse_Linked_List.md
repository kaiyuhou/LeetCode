Reverse a singly linked list.

### 题意
反转一个单链表

### 解法
r = q.next
q.next = p
p = q
q = r