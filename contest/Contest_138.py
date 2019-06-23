from contest.Tree import *

# class Solution:
#     def heightChecker(self, heights) -> int:
#         A = sorted(heights)
#         ans = 0
#         for i in range(len(A)):
#             if heights[i] != A[i]:
#                 ans += 1
#
#         return ans
#
#
#
#
# s = Solution()
# A = [1,1,4,2,1,3]
# print(s.heightChecker(A))

# class Solution:
#     def maxSatisfied(self, customers, grumpy, X: int) -> int:
#         N = len(customers)
#         sat = [0 for _ in range(N + 1)]
#         cnt = 0
#         for i in range(N):
#             if grumpy[i] == 1:
#                 cnt += customers[i]
#             sat[i + 1] = cnt
#         cnt = sum(customers) - cnt
#         # print(cnt, sat)
#         ans = cnt
#         for i in range(0, N-X+1):
#             ans = max(ans, cnt + (sat[i + X] - sat[i]))
#         return ans
#
# s = Solution()
# # C = [1,0,1,2,1,1,7,5]
# # G = [0,1,0,1,0,1,0,1]
# # X = 3
# C = [1,1,1]
# G = [0,0,0]
# X = 2
# print(s.maxSatisfied(C, G, X))

class Solution:
    def prevPermOpt1(self, A):
        # if A[-4:] == [3,1,1,3]:
        #     A[-4], A[-2] = A[-2], A[-4]
        #     return A
        N = len(A)
        if A == 1:
            return A

        for i in range(N - 2, -1, -1):
            curn = 0
            curp = 0
            for j in range(i + 1, N):
                if A[i] > A[j] and A[j] >= curn:
                    curn = A[j]
                    curp = j
            if curp:
                A[i], A[curp] = A[curp], A[i]
                return A
        return A

s = Solution()
# A = [3,2,1]
# A = [1,1,5]
# A = [1,9,4,6,7]
A = [3,1,1,3]
# A = [1]
print(s.prevPermOpt1(A))



# import collections
# class Solution:
#     def rearrangeBarcodes(self, barcodes):
#         N = len(barcodes)
#         col = collections.Counter(barcodes)
#         A = []
#         for k, v in col.items():
#             A.append((v, k))
#         A.sort()
#         ans = [0 for _ in range(N)]
#         i = 0
#         while len(A) > 0:
#             cur = A.pop()
#             for j in range(cur[0]):
#                 ans[i] = cur[1]
#                 i += 2
#                 if i >= N:
#                     i = 1
#         return ans
#
# s = Solution()
# # A = [1,1,1,1,2,2,3,3]
# A = [1,1,2]
# print(s.rearrangeBarcodes(A))










