# class Solution:
#     def checkStraightLine(self, C) -> bool:
#         N = len(C)
#         x1, y1 = C[0][0], C[0][1]
#         x2, y2 = C[1][0], C[1][1]
#         for i in range(2, N):
#             x, y = C[i][0], C[i][1]
#             if (x - x1) * (y2 - y1) != (x2 - x1) * (y - y1):
#                 return False
#         return True
#
#
# class Solution:
#     def removeSubfolders(self, folder):
#         folder.sort()
#         ans = [folder[0]]
#         for i, n in enumerate(folder):
#             if i == 0: continue
#             if len(n) > len(ans[-1]) and n[:len(ans[-1]) + 1] ==  ans[-1] + '/':
#                 continue
#             ans.append(n)
#         return ans
#
# s = Solution()
# folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
# folder = ["/a","/a/b/c","/a/b/d"]
# folder = ["/a/b/c","/a/b/ca","/a/b/d"]
# print(s.removeSubfolders(folder))

class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        key = ['Q', 'W', 'E', 'R']
        cnt = {'Q': 0, 'W': 0, 'E': 0, 'R': 0}
        for c in s:
            cnt[c] += 1

        target = {}
        target_key = []
        for k in key:
            if cnt[k] > n // 4:
                target[k] = cnt[k] - n // 4
                target_key.append(k)
            else:
                target[k] = 0

        if len(target_key) == 0:
            return 0

        ans = n
        cnt = {'Q': 0, 'W': 0, 'E': 0, 'R': 0}
        tail = 0

        # print(target)

        def ok(A, B):
            for k in target_key:
                if A[k] < B[k]:
                    return False
            return True

        for i, c in enumerate(s):
            cnt[c] += 1
            # print(i, cnt, tail)
            while tail <= i:
                if ok(cnt, target):
                    ans = min(ans, i - tail + 1)
                    cnt[s[tail]] -= 1
                    tail += 1
                else:
                    break
        return ans

ss = Solution()
s = "QWER"
s = "QQWE"
# s = "QQQW"
# s = "QQQQ"
# s = "WQWRQQQW"
print(ss.balancedString(s))







# class Solution:
#     def jobScheduling(self, startTime, endTime, profit) -> int:
#         n = len(startTime)
#         T = []
#         for i in range(n):
#             T.append((endTime[i], startTime[i], profit[i]))
#         T.sort()
#         dp = [0 for i in range(n)]
#         dp[0] = T[0][2]
#
#         # print(T)
#
#         import bisect
#         for i in range(1, n):
#             E, S, P = T[i][0], T[i][1], T[i][2]
#
#             dp[i] = max(dp[i - 1], P)
#             j = bisect.bisect_left(T, (S, S, 100000))
#             if j == 0:
#                 continue
#             dp[i] = max(dp[i], P + dp[j - 1])
#         return max(dp)
#
# s = Solution()
# startTime = [1,2,3,3]
# endTime = [3,4,5,6]
# profit = [50,10,40,70]
#
# # startTime = [1,2,3,4,6]
# # endTime = [3,5,10,6,9]
# # profit = [20,20,100,70,60]
#
# # startTime = [1,1,1]
# # endTime = [2,3,4]
# # profit = [5,6,4]
# print(s.jobScheduling(startTime, endTime, profit))




