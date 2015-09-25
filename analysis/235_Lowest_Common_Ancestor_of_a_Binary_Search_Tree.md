Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

### 题意
给一个二叉搜索树，和两个节点，求他们的最近公共父节点

### 解法
由于是二叉搜索树，所以两个节点分道扬镳的地方是第一次出现了两个节点一个比当前结点小，一个比当前结点大。