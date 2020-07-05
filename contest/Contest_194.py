from typing import *
from Tree import *

# class Solution:
#     def xorOperation(self, n: int, start: int) -> int:
#         A = [start + 2 * i for i in range(n)]
#         ans = A[0]
#         for i in range(1, n):
#             ans ^= A[i]
#
#         return ans
#
#
# s = Solution()
# n = 5
# start = 0
# n = 4
# start = 3
# n = 1
# start = 7
#
# print(s.xorOperation(n, start))

# class Solution:
#     def getFolderNames(self, names: List[str]) -> List[str]:
#         used = {}
#         nset = set()
#         ans = []
#         for name in names:
#             if name not in nset:
#                 ans.append(name)
#                 used[name] = 0
#                 nset.add(name)
#             else:
#                 if name in used.keys():
#                     cur = used[name] + 1
#                 else:
#                     cur = 1
#                 while name + '(' + str(cur) + ')' in nset:
#                     cur += 1
#                 ans.append(name + '(' + str(cur) + ')')
#                 used[name] = cur
#                 nset.add(name + '(' + str(cur) + ')')
#         return ans
#
# s = Solution()
# names = ["pes", "fifa", "gta", "pes(2019)"]
# names = ["gta","gta(1)","gta","avalon"]
# names = ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"]
# names = ["wano","wano","wano","wano"]
# names = ["kaido","kaido(1)","kaido","kaido(1)"]
#
# names = ["kaido","kaido(1)","kaido","kaido(1)","kaido(2)"]
#
#
# print(s.getFolderNames(names))


import heapq
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        N = len(rains)
        next = [-1] * N
        days = set()
        pos = {}

        for i, rain in enumerate(rains):
            if rain == 0:
                continue
            else:
                if rain in days:
                    index = pos[rain]
                    next[index] = i
                    pos[rain] = i
                else:
                    pos[rain] = i
                    days.add(rain)

        days = set()
        ans = []
        h = []
        for i, rain in enumerate(rains):
            if rain == 0:
                if len(h) > 0:
                    index = heapq.heappop(h)
                    ans.append(rains[index])
                    days.remove(rains[index])
                else:
                    ans.append(1)
            else:
                ans.append(-1)

                if rain in days:
                    return []
                elif next[i] == -1:
                    continue
                else:
                    days.add(rain)
                    heapq.heappush(h, next[i])
        return ans

s = Solution()
rains = [1,2,3,4]
rains = [1,2,0,0,2,1]
rains = [1,2,0,1,2]
rains = [69,0,0,0,69]
rains = [10,20,20]

print(s.avoidFlood(rains))
























