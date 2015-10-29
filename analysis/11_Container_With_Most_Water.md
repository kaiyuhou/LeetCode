Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

### 题意
这道题的题意有一点难理解
给定一组在x轴上排列的木棒的高度，任选取两个木棒，求他们能装下的水的体积

### 题解
左右两个指针，任意一个指针移动都会使得桶的长度变小，所以只能向高度变高的方向移动。
没有选择左右两个指针中短的那一个向中间移动，找到比当前高的木棒之后更新一下结果。