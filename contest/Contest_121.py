# class Solution:
#     def strWithout3a3b(self, A, B):
#         """
#         :type A: int
#         :type B: int
#         :rtype: str
#         """
#         ans = ""
#         chr1 = "a"
#         chr2 = "b"
#
#         if B > A:
#             A, B = B, A
#             chr1, chr2 = chr2, chr1
#
#         dif = A - B
#         dif2 = 0
#         if dif > B:
#             dif2 = dif - B
#             dif = B
#
#
#         ans = (chr1 + chr1 + chr2) * dif
#         ans += (chr1 + chr2) * (B - dif)
#         ans += chr1 * dif2
#
#         return ans
#
# s = Solution()
# A = 1
# B = 2
# print(s.strWithout3a3b(A,B))

# class TimeMap:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.mem = {}
#
#     def set(self, key: 'str', value: 'str', timestamp: 'int') -> 'None':
#         if key in self.mem.keys():
#             self.mem[key].append((timestamp, value))
#         else:
#             self.mem[key] = [(timestamp, value)]
#
#     def get(self, key: 'str', timestamp: 'int') -> 'str':
#         if timestamp < self.mem[key][0][0]:
#             return ""
#
#         N = len(self.mem[key])
#         if N == 1:
#             return self.mem[key][0][1]
#
#         left = 0
#         right = N - 1
#
#         while left <= right:
#            mid = (left + right)//2
#            if self.mem[key][mid][0] <= timestamp and ((mid + 1 == N) or (self.mem[key][mid + 1][0] > timestamp)):
#                return self.mem[key][mid][1]
#
#            if self.mem[key][mid][0] < timestamp:
#                left = mid + 1
#            else:
#                right = mid
#
# kv = TimeMap()
# # kv.set("foo", "bar", 1)
# kv.set("love","high",10)
# kv.set("love","low",20)
# print(kv.get("love",5))
# print(kv.get("love",10))
# print(kv.get("love",15))
# print(kv.get("love",20))
# print(kv.get("love",25))

# print(kv.get("foo", 1))
# print(kv.get("foo", 3))
# kv.set("foo", "bar2", 4)
# kv.set("foo", "bar3", 6)
# kv.set("foo", "bar4", 8)
# print(kv.get("foo", 4))
# print(kv.get("foo", 7))
#["get","get","get"], \
#[["love",15],["love",20],["love",25]]

# class Solution:
#     def mincostTickets(self, days: 'List[int]', costs: 'List[int]') -> 'int':
#         ans = [0] * 366
#         days.sort()
#
#         count = 0
#         i = 0
#         for day in days:
#             while i < day:
#                 ans[i] = count
#                 i += 1
#             count += 1
#         while i < 366:
#             ans[i] = count
#             i += 1
#
#         dp = [0] * 366
#         for i in range(1, 366):
#             cnt = dp[i-1]
#
#             if ans[i] - ans[i-1] > 0:
#                 cnt = cnt + costs[0]
#
#             if i >= 7:
#                 cnt = min(cnt, dp[i-7] + costs[1])
#             if i >= 30:
#                 cnt = min(cnt, dp[i-30] + costs[2])
#
#             dp[i] = cnt
#
#         return dp[365]
#
# s = Solution()
# days = [1,2,3,4,5,6,7,8,9,10,30,31]
# costs = [2,7,15]
# print(s.mincostTickets(days, costs))


class Solution:
    def countTriplets(self, A: 'List[int]') -> 'int':
        A.sort()
        cnt = 1
        dp = []

        for i in range(1, len(A)):
            if A[i-1] == A[i]:
                cnt +=1
            else:
                dp.append(cnt)
                cnt = 1

        dp.append(cnt)

        # print(dp)

        ans = 0
        N = len(dp)
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue

                ans += 2 * dp[j] * dp[i] * dp[i]
                # print("hit")


        for i in range(N - 2):
            for j in range(i + 1, N - 1):
                for k in range(j + 1, N):
                    ans += 6 * dp[i] * dp[j] * dp[k]
                    # print("hit3")

        if A[0] == 0:
            ans += dp[0] * dp[0] * dp[0]

        return ans

s = Solution()
A = [1, 2, 3]
print(s.countTriplets(A))











