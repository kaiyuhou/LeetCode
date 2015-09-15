Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

### 题意
给定一个无序数组和数，移除数组中所有的这个数
可以改变数组顺序

### 题解
因为可以改变数组顺序，并且返回新的数组长度，而不用管老数组后面的空间使用
所以使用两个标记，从前向后和从后向前扫
如果后指针所指的数是给定数，那么直接向前走一步
如果前指针所指的数是给定数，将后指针指的数写入前指针的位置，两指针分别走一步
循环终止条件是相遇