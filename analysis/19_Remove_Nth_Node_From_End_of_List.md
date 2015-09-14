Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.

### 题意
移除链表中的第n个元素
希望能在一遍中完成

### 题解
使用前后节点，前节点快后节点n个节点，然后同时开始跑，前节点到结尾后删掉后节点
引入dumb节点来简化逻辑