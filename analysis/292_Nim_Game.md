You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.

For example, if there are 4 stones in the heap, then you will never win the game: no matter 1, 2, or 3 stones you remove, the last stone will always be removed by your friend.

### 题意
这道题是标准Nim Game的简化版本
只有一堆石头，每次可以取1~3个，最后取得一个人获胜。
获胜测试是想办法在自己取之后将结果弄成4，那么下一手必胜。
如果在中间结果时，只要自己接手后能够将交给对手的是4的倍数，那么能在下一次接手是将结果继续修改为4的倍数。
所以，只要自己接手的时候不是4的倍数必胜。

Nim Game一般都是这样的思路。