from typing import *
from Tree import *

class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, u):
        if u != self.parent.setdefault(u, u):
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu != pv:
            self.parent[pu] = pv



# class Solution:
#     def targetIndices(self, nums: List[int], target: int) -> List[int]:
#         ans = []
#         nums.sort()
#         for i, num in enumerate(nums):
#             if num == target:
#                 ans.append(i)
#         return ans
#
#
# class Solution:
#     def getAverages(self, nums: List[int], k: int) -> List[int]:
#         dp = [0]
#         for num in nums:
#             dp.append(dp[-1] + num)
#
#         ans = []
#         for i in range(len(nums)):
#             if i - k < 0 or i + k >= len(nums):
#                 ans.append(-1)
#                 continue
#             ans.append((dp[i + k + 1] - dp[i - k]) // (2 * k + 1))
#
#         return ans

# class Solution:
#     def minimumDeletions(self, nums: List[int]) -> int:
#         mi_index = nums.index(min(nums))
#         ma_index = nums.index(max(nums))
#         if mi_index > ma_index:
#             mi_index, ma_index = ma_index, mi_index
#         n = len(nums)
#
#         return min([mi_index + (ma_index - mi_index) + 1,  mi_index + 1 + (n-ma_index),  (n-mi_index)])
#


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        times = []
        time_persons = {}
        person_time = [{} for _ in range(n)]

        ms = []
        for a, b, t in meetings:
            ms.append((t, a, b))
        ms.sort()

        for t, a, b in ms:
            if not times or t != times[-1]:
                times.append(t)

            if t not in time_persons:
                time_persons[t] = set()
            time_persons[t].add(a)
            time_persons[t].add(b)

            if t not in person_time[a]:
                person_time[a][t] = set()
            if t not in person_time[b]:
                person_time[b][t] = set()

            person_time[a][t].add(b)
            person_time[b][t].add(a)

        ans = set()
        ans.add(0)
        ans.add(firstPerson)

        for t in times:
            cur_person = time_persons[t]
            know_person = cur_person & ans
            update_person = set()
            for p in know_person:
                for np in person_time[p][t]:
                    if np not in ans:
                        update_person.add(np)
                        ans.add(np)

            while update_person:
                next_update_person = set()
                for p in update_person:
                    for np in person_time[p][t]:
                        if np not in ans:
                            next_update_person.add(np)
                            ans.add(np)
                update_person = next_update_person

        return list(ans)


s = Solution()
n = 6
meetings = [[1,2,5],[2,3,8],[1,5,10]]
firstPerson = 1
print(s.findAllPeople(n, meetings, firstPerson))

































































