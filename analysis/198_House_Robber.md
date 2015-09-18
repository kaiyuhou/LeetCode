You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

### 题意
一个小偷要偷钱，给一个数组，表示一排房子中拥有的钱的数量，不可以偷连续的两个房子。
问能够获得的钱的数量最大是多少。

### 题解
标准的动态规划问题。

考察到当前节点i，假设已知前i-1个节点的最优解。
那么节点i的最优解为  （节点i-2的最优解 和 节点i的钱） 与 （节点i-1的最优解） 的中的大者。

其中0节点的最优解为nums[0]

即 dp[i] = max(dp[i - 1],dp[i - 2] + nums[i])