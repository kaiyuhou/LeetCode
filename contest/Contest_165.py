from Tree import *

# class Solution:
#     def subtractProductAndSum(self, n: int) -> int:
#         p = 1
#         s = 0
#         for c in str(n):
#             p *= int(c)
#             s += int(c)
#         return p - s
#
#
# s = Solution()
# print(s.subtractProductAndSum(234))

# class Solution:
#     def groupThePeople(self, groupSizes):
#         m = {}
#         for i, g in enumerate(groupSizes):
#             if g not in m.keys():
#                 m[g] = [i]
#             else:
#                 m[g].append(i)
#         ans = []
#         for k, v in m.items():
#             for i in range(len(v) // k):
#                 ans.append(list(v[i * k:i * k + k]))
#         return ans
#
# s = Solution()
# print(s.groupThePeople([1]))

# from math import *
# class Solution:
#     def smallestDivisor(self, nums, threshold: int) -> int:
#         left = 1
#         right = max(nums) + 1
#
#         def check(a):
#             ans = 0
#             for num in nums:
#                 ans += ceil(num / a)
#             return ans
#
#         while left < right:
#
#             mid = (left + right) // 2
#             # print(left, right, check(mid))
#             cur = check(mid)
#             if cur > threshold:
#                 left = mid + 1
#             else:
#                 right = mid
#
#         # print(left, right)
#         if check(left) <= threshold:
#             return left
#         return left + 1
#
# s = Solution()
# nums = [1,2,5,9]
# threshold = 6
# nums = [2,3,5,7,11]
# threshold = 11
# # nums = [19]
# # threshold = 5
# # nums = [962551,933661,905225,923035,990560]
# # threshold = 10
# print(s.smallestDivisor(nums, threshold))

import queue
class Solution:
    def minFlips(self, mat) -> int:
        M = len(mat)
        N = len(mat[0])
        K = M * N
        dst = tuple([mat[i][j] for i in range(M) for j in range(N)])
        src = tuple([0 for _ in range(M * N)])
        q = queue.Queue()
        q.put((src, 0))
        visited = set()

        nxt_step = [[-1, 0], [1, 0], [0, -1], [0, 1], [0, 0]]

        while not q.empty():
            cur, step = q.get()
            if cur in visited:
                continue
            visited.add(cur)

            if cur == dst:
                return step
            for k in range(K):
                i = k // N
                j = k % N
                net = list(cur)
                for x, y in nxt_step:
                    ni = i + x
                    nj = j + y
                    if ni >= 0 and ni < M and nj >= 0 and nj < N:
                        net[ni * N + nj] = 1 - net[ni * N + nj]
                if tuple(net) not in visited:
                    q.put((tuple(net), step + 1))
                # print(net)
            # print(cur)
        return -1
s = Solution()
mat = [[0,0],[0,1]]
mat = [[0]]
mat = [[1,0,0],[1,0,0]]
mat = [[1,0,0],[1,0,0], [0,0,1]]
print(s.minFlips(mat))





