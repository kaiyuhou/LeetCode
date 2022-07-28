from typing import *
from collections import *
from math import *

from Tree import *

def get_mask(word):
    return sum(1 << (ord(c) - ord("a")) for c in word)


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.weight = [1 for _ in range(n)]

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu != pv:
            if self.weight[pu] < self.weight[pv]:
                self.parent[pu] = pv
                self.weight[pv] = self.weight[pu] + self.weight[pv]
            else:
                self.parent[pv] = pu
                self.weight[pu] = self.weight[pu] + self.weight[pv]



# class Solution:
#     def prefixCount(self, words: List[str], pref: str) -> int:
#         ans = 0
#         for w in words:
#             if w.startswith(pref):
#                 ans += 1
#         return ans


# class Solution:
#     def minSteps(self, s: str, t: str) -> int:
#         C1 = Counter(s)
#         C2 = Counter(t)
#         ans = 0
#         for i in range(26):
#             c = chr(ord('a') + i)
#             ans += abs(C1[c] - C2[c])
#         return ans


# class Solution:
#     def minimumTime(self, time: List[int], totalTrips: int) -> int:
#         left = min(time)
#         n = len(time)
#         right = min(left * totalTrips, (totalTrips // n + 1) * max(time))
#
#         def get_case(mid):
#             cnt = 0
#             for t in time:
#                 cnt += mid // t
#             return cnt
#
#         while left <= right:
#             if left == right:
#                 return left
#
#             mid = (left + right) // 2
#             case = get_case(mid)
#             if case < totalTrips:
#                 left = mid + 1
#             elif case >= totalTrips:
#                 right = mid
#
#         return min(left, right)


class Solution:
    def minimumFinishTime(self, T: List[List[int]], changeTime: int, numLaps: int) -> int:
        lap_time = defaultdict(int)

        TS = set()
        for f, r in T:
            TS.add((f, r))
        T = list(TS)
        n = len(TS)

        S = [0] * n
        C = [0] * n

        min_lap_time = 100005
        for i in range(n):
            min_lap_time = min(T[i][0], min_lap_time)
            C[i] = S[i] =T[i][0]
        lap_time[1] = min_lap_time

        cur_lap = 1
        while cur_lap <= numLaps:
            cur_lap += 1
            total_lap_time = S[0] + C[0] * T[0][1]

            for i in range(n):
                C[i] *= T[i][1]
                S[i] += C[i]
                total_lap_time = min(total_lap_time, S[i])

            cur_lap_time = total_lap_time - lap_time[cur_lap - 1]

            if cur_lap_time >= min_lap_time + changeTime:
                break

            lap_time[cur_lap] = total_lap_time

        for i in range(2, numLaps + 1):
            cur = lap_time[1] + lap_time[i - 1] + changeTime
            if i not in lap_time.keys():
                lap_time[i] = cur
            else:
                lap_time[i] = min(lap_time[i], cur)

            for j in range(2, i):
                lap_time[i] = min(lap_time[i], lap_time[j] + lap_time[i - j] + changeTime)

        return lap_time[numLaps]


s = Solution()
tires = [[2,3],[3,4]]
changeTime = 5
numLaps = 4

tires = [[1,10],[2,2],[3,4]]
changeTime = 6
numLaps = 5

tires = [[36,5],[32,5],[88,8],[11,4],[52,2],[2,2],[90,5],[49,6],[68,9],[77,3],[42,7],[17,3],[73,7],[89,2],[92,9],[40,7],[71,8],[79,3],[55,6],[77,9],[14,3],[87,10],[4,2],[63,7],[79,8],[3,9],[44,2],[49,9],[91,3],[58,6],[62,3],[72,7],[97,6],[29,5],[88,9],[40,8],[36,4],[82,8],[53,8],[26,2],[26,6],[92,2],[46,2],[75,6],[85,2],[6,10],[12,4],[15,4]]
changeTime = 24
numLaps = 27

# tires = [[1, i] for i in range(2, 8)]
# changeTime = 100000
# numLaps = 1000

print(s.minimumFinishTime(tires, changeTime, numLaps))






























