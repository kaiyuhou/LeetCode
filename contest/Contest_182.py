from typing import *
from Tree import *
#
# class Solution:
#     def findLucky(self, arr: List[int]) -> int:
#         import collections
#         C = collections.Counter(arr)
#         ans = [-1]
#         for k, v in C.items():
#             if k == v:
#                 ans.append(k)
#         return max(ans)
#
#
#
#
# s = Solution()
# arr = [2,2,3,4]
# arr = [1,2,2,3,3,3]
# arr = [2,2,2,3,3]
# arr = [5]
# arr = [7,7,7,7,7,7,7]
# print(s.findLucky(arr))

# class Solution:
#     def numTeams(self, rating: List[int]) -> int:
#         N = len(rating)
#         if N <= 2:
#             return 0
#         ans = 0
#
#         s_than_me = [0 for _ in range(N)]
#         for i in range(N):
#             for j in range(i):
#                 if rating[j] < rating[i]:
#                     s_than_me[i] += 1
#
#         for i in range(2, N):
#             for j in range(1, i):
#                 if rating[j] < rating[i]:
#                     ans += s_than_me[j]
#
#         rating.reverse()
#         s_than_me = [0 for _ in range(N)]
#         for i in range(N):
#             for j in range(i):
#                 if rating[j] < rating[i]:
#                     s_than_me[i] += 1
#
#         for i in range(2, N):
#             for j in range(1, i):
#                 if rating[j] < rating[i]:
#                     ans += s_than_me[j]
#
#         return ans
#
# s = Solution()
# rating = [2,5,3,4,1]
# rating = [2,1,3]
# rating = [1,2,3,4]
# print(s.numTeams(rating))

# class UndergroundSystem:
#
#     def __init__(self):
#         self.station_begin_end = {}
#         self.ids = {}
#
#     def checkIn(self, id: int, stationName: str, t: int) -> None:
#         self.ids[id] = (stationName, t)
#
#     def checkOut(self, id: int, stationName: str, t: int) -> None:
#         begin_station, begin_t = self.ids[id]
#         if (begin_station, stationName) not in self.station_begin_end.keys():
#             self.station_begin_end[(begin_station, stationName)] = (0, 0)
#         stime, cnt = self.station_begin_end[(begin_station, stationName)]
#         self.station_begin_end[(begin_station, stationName)] = (stime + (t - begin_t), cnt + 1)
#
#     def getAverageTime(self, startStation: str, endStation: str) -> float:
#         s, cnt = self.station_begin_end[(startStation, endStation)]
#         return s / cnt


def get_KMP_next(pattern):
    next_arr = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j and pattern[j] != pattern[i]:
            j = next_arr[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        next_arr[i] = j
    return next_arr

class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        M = len(evil)
        Mod = int(1E9 + 7)
        next_arr = get_KMP_next(evil)

        from functools import lru_cache
        @lru_cache(None)
        def dfs(idx: int, pre1: bool, pre2: bool, preE: int):
            if preE == M: return 0
            if idx == n: return 1

            total = 0
            first = ord(s1[idx]) if pre1 else ord('a')
            last = ord(s2[idx]) if pre2 else ord('z')

            for ci in range(first, last + 1):
                c = chr(ci)

                _pre1 = pre1 and ci == first
                _pre2 = pre2 and ci == last

                _preE = preE
                while _preE and c != evil[_preE]:
                    _preE = next_arr[_preE - 1]
                if c == evil[_preE]:
                    _preE += 1

                total += dfs(idx + 1, _pre1, _pre2, _preE)
                total %= Mod

            return total

        return dfs(0, True, True, 0)

































