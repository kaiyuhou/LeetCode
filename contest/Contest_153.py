from Tree import *
#
# class Solution:
#     def distanceBetweenBusStops(self, distance, start: int, destination: int) -> int:
#         T = sum(distance)
#         A = min(start, destination)
#         B = max(start, destination)
#         return min(sum(distance[A:B]), T - sum(distance[A:B]))
#
# s = Solution()
#
# distance = [1,2,3,4]
# start = 0
# destination = 0
# print(s.distanceBetweenBusStops(distance, start, destination))


# import datetime
# class Solution:
#     def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
#         return datetime.date(year, month, day).strftime("%A")
#
# s = Solution()
# print(s.dayOfTheWeek(31, 8, 2019))

# class Solution:
#     def maximumSum(self, A) -> int:
#         N = len(A)
#         if N == 1:
#             return A[0]
#
#         dp = {}
#         dp[0, 0] = A[0]
#         dp[0, 1] = 0
#         ans = dp[0, 0]
#
#         for i in range(1, N):
#             dp[i, 0] = max(dp[i - 1, 0] + A[i], A[i])
#             dp[i, 1] = max(dp[i - 1, 1] + A[i], dp[i - 1, 0])
#             ans = max(ans, max(dp[i, 0], dp[i, 1]))
#
#         return ans
#
# s = Solution()
# A = [1,-2,0,3]
# A = [1,-2,-2,3]
# A = [-1,-1,-1,-1]
# A = [1, 2, -100, 3, 4]
# print(s.maximumSum(A))

import bisect
class Solution:
    def makeArrayIncreasing(self, A, B) -> int:
        B = list(set(B))
        B.sort()

        N = len(A)
        M = len(B)
        if N == 1:
            return 0

        MX = 1000000005
        dp = [MX for _ in range(N + 1)]
        dp[0] = A[0]
        if B[0] < A[0]:
            dp[1] = B[0]

        for i in range(1, N):
            T = [MX for _ in range(N + 1)]
            for t, last in enumerate(dp):
                if last == MX:
                    continue

                if last < A[i]:
                    T[t] = min(T[t], A[i])
                    pos = bisect.bisect_right(B, last)
                    if pos != M:
                        T[t + 1] = min(T[t + 1], B[pos])

                else:
                    pos = bisect.bisect_right(B, last)
                    if pos != M:
                        T[t + 1] = min(T[t + 1], B[pos])

            dp = T
        for i, last in enumerate(dp):
            if last != MX:
                return i
        return -1

s = Solution()
arr1 = [1,5,3,6,7]
arr2 = [1,3,2,4]
arr1 = [1,5,3,6,7]
arr2 = [4,3,1]
arr1 = [1,5,3,6,7]
arr2 = [1,6,3,3]
print(s.makeArrayIncreasing(arr1, arr2))














































