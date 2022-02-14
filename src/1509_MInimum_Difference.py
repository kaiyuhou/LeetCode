from typing import  *
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        return min(nums[-2] - nums[2], nums[-3] - nums[1])

# 找最大的 k 个数
# 维护一个大小为 k 的堆
# 然后不断更新，那么时间复杂度就是 N log K

import heapq

a = [3, 1, 4, 6, 7, 8, 9]
h = a[:3]
heapq.heapify(h)
for i in range(3, len(a)):
    if h[0] < a[i]:
        heapq.heappop(h)
        heapq.heappush(h, a[i])
print(h)

