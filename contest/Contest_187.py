from typing import *
from Tree import *

# class Solution:
#     def destCity(self, paths: List[List[str]]) -> str:
#         ans = []
#         for A, B in paths:
#             ans.append(B)
#         for A, B in paths:
#             if A in ans:
#                 ans.remove(A)
#         return ans[0]
#
#
# paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
# paths = [["B","C"],["D","B"],["C","A"]]
# paths = [["A","Z"]]
# s = Solution()
# print(s.destCity(paths))

# class Solution:
#     def kLengthApart(self, nums: List[int], k: int) -> bool:
#         cnt = -1
#         for a in nums:
#             if a == 1:
#                 if cnt == -1:
#                     cnt = 0
#                 elif cnt >= k:
#                     cnt = 0
#                 else:
#                     return False
#             else:
#                 if cnt != -1:
#                     cnt += 1
#         return True
#
# s = Solution()
# nums = [1,0,0,0,1,0,0,1]
# k = 2
# nums = [0,1,0,0,1,0,0,1]
# k = 2
# nums = [1,1,1,1,1]
# k = 0
# nums = [0,1,0,1]
# k = 1
# print(s.kLengthApart(nums, k))

class Solution:
    def longestSubarray(self, A: List[int], limit: int) -> int:
        smallest_index = 0
        largest_index = 0
        start_index = 0
        ans = 1
        n = len(A)

        for i in range(1, n):
            if A[i] < A[smallest_index]:
                smallest_index = i
                if A[largest_index] - A[i] <= limit:
                    pass
                else:
                    start_index = i - 1
                    largest_index = i
                    while A[start_index] - A[i] <= limit:
                        if A[start_index] > A[largest_index]:
                            largest_index = start_index
                        start_index -= 1
                    start_index += 1
            elif A[i] > A[largest_index]:
                largest_index = i
                if A[i] - A[smallest_index] <= limit:
                    pass
                else:
                    start_index = i - 1
                    smallest_index = i
                    while A[i] - A[start_index] <= limit:
                        if A[start_index] < A[smallest_index]:
                            smallest_index = start_index
                        start_index -= 1
                    start_index += 1
            ans = max(ans, i - start_index + 1)

        return ans

s = Solution()
nums = [8,2,4,7]
limit = 4
nums = [10,1,2,4,7,2]
limit = 5
nums = [4,2,2,2,4,4,2,2]
limit = 0

nums = [7,40,10,10,40,39,96,21,54,73,33,17,2,72,5,76,28,73,59,22,100,91,80,66,5,49,26,45,13,27,74,87,56,76,25,64,14,86,50,38,65,64,3,42,79,52,37,3,21,26,42,73,18,44,55,28,35,87]
limit = 63

print(s.longestSubarray(nums, limit))










# class Solution:
#     def kthSmallest(self, mat: List[List[int]], k: int) -> int:













