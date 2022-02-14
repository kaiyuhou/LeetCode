from typing import *
from Tree import *

# import functools
# @functools.lru_cache(None)

# class Solution:
#     def minimumDifference(self, nums: List[int], k: int) -> int:
#         nums.sort()
#         min_d = nums[k - 1] - nums[0]
#
#         for i in range(0, len(nums) - k + 1):
#             if nums[i + k - 1] - nums[i] < min_d:
#                 min_d = nums[i + k - 1] - nums[i]
#         return min_d
#
#
#
# s = Solution()
# nums = [90]
# k = 1
# nums = [9,4,1,7]
# k = 2
# print(s.minimumDifference(nums, k))

# class Solution:
#     def kthLargestNumber(self, nums: List[str], k: int) -> str:
#         A = [int(n) for n in nums]
#         A.sort()
#         return str(A[len(A) - k])
#
# s = Solution()
# nums = ["3","6","7","10"]
# k = 4
# nums = ["0","0"]
# k = 2
# nums = ["2","21","12","1"]
# k = 3
# print(s.kthLargestNumber(nums, k))

# class Solution:
#     def minSessions(self, tasks: List[int], sessionTime: int) -> int:
#         if len(tasks) == 0:
#             return 0
#
#         tasks.sort(reverse=True)
#         curTime = sessionTime - tasks[0]
#         # print(tasks[0])
#         tasks.remove(tasks[0])
#         best = [curTime, ()]
#         checked = set()
#
#         def best_remove(curTime, tasks, to_remove):
#             if (curTime, tuple(tasks), to_remove) in checked:
#                 return
#
#             checked.add((curTime, tuple(tasks), to_remove))
#
#             if len(tasks) == 0 or tasks[-1] > curTime:
#                 return
#             for i, t in enumerate(tasks):
#                 if t <= curTime:
#                     if (curTime - t) < best[0]:
#                         best[0] = curTime - t
#                         best[1] = to_remove + (t,)
#                     best_remove(curTime - t, tasks[:i] + tasks[i+1:], to_remove + (t,))
#
#         best_remove(curTime, tasks, ())
#         # print(best)
#         # print(tasks)
#         for t in best[1]:
#             tasks.remove(t)
#
#         return 1 + self.minSessions(tasks, sessionTime)
#
# s = Solution()
# tasks = [1,2,3]
# sessionTime = 3
# # tasks = [3,1,3,1,1]
# # sessionTime = 8
# # tasks = [1,2,3,4,5]
# # sessionTime = 15
# tasks = [2,3,3,4,4,4,5,6,7,10]
# sessionTime = 12
# # tasks = [10] * 14
# # sessionTime = 15
# print(s.minSessions(tasks, sessionTime))

class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        dp = [0, 0]
        for a in binary:
            if a == '0':
                dp = (sum(dp), dp[1])
            else:
                dp = (dp[0], sum(dp) + 1)
        return (sum(dp) + ('0' in binary)) % 100000007

s = Solution()
binary = "101"
print(s.numberOfUniqueGoodSubsequences(binary))





