class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



# class Solution:
#     def canThreePartsEqualSum(self, A) -> bool:
#         S = sum(A)
#         d, m = divmod(S, 3)
#
#         if m != 0:
#             return False
#
#         ans = 0
#         cur = 0
#         for a in A:
#             ans += a
#             if ans == d:
#                 ans = 0
#                 cur += 1
#
#         if cur == 3 or (cur >= 3 and d == 0):
#             return True
#         else:
#             return False
#
# s = Solution()
# A = [0,0,0,0,0]
# print(s.canThreePartsEqualSum(A))


# class Solution:
#     def maxScoreSightseeingPair(self, A) -> int:
#         ans = 0
#         N  = len(A)
#         last_max = A[0] - 1
#
#         for i in range(1, N):
#             ans = max(last_max + A[i], ans)
#             last_max = max(last_max, A[i]) -1
#
#         return ans
#
# s = Solution()
# #A = [8,1,5,2,6]
# A = [1, 2]
# print(s.maxScoreSightseeingPair(A))

# class Solution:
#     def queryString(self, S: str, N: int) -> bool:
#         for i in range(1, N + 1):
#             b = bin(i)[2:]
#             if S.find(b) == -1:
#                 return False
#         return True
#
# s = Solution()
# S = "11111111111111111111111111111"
# N = 1000000000
# print(s.queryString(S, N))

class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 2 == 0 or K % 5 == 0:
            return -1

        ans = 1
        for i in range(100000):
            if ans % K == 0:
                return i + 1
            ans = ans * 10 + 1
        return -1


s = Solution()
# for i in range(1, 10000):
#     if i % 2 == 0 or i % 5 == 0:
#         continue
i = 3
print(s.smallestRepunitDivByK(i))
