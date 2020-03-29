from Tree import  *

# class Solution:
#     def numberOfSubarrays(self, nums, k: int) -> int:
#         dp = [0]
#         ans = 0
#         last = False
#         for a in nums:
#             if a % 2 == 0:
#                 if last: # odd
#                     if len(dp) == k:
#                         ans += dp[0]
#                     dp.append(1)
#                 else: # even
#                     if len(dp) == k + 1:
#                         ans += dp[0]
#                     dp[-1] += 1
#                 last = False
#             if a % 2 == 1:
#                 if last: # odd
#                     dp.append(1)
#                     if len(dp) == k:
#                         ans += dp[0]
#                     if len(dp) == k + 1:
#                         dp.pop(0)
#                         ans += dp[0]
#                 else: # even
#                     dp[-1] += 1
#                     if len(dp) == k:
#                         ans += dp[0]
#                     if len(dp) == k + 1:
#                         dp.pop(0)
#                         ans += dp[0]
#                 last = True
#             # print(dp)
#             # print(ans)
#         return ans
#
# nums = [1,1,2,1,1]
# k = 3
# nums = [2,4,6]
# k = 1
# nums = [2,2,2,2,2, 1 ,2,2,2]
# k = 1
# s = Solution()
# print(s.numberOfSubarrays(nums, k))

# class Solution:
#     def minRemoveToMakeValid(self, s: str) -> str:
#         left = []
#         right = []
#
#         for i, c in enumerate(s):
#             if c =='(':
#                 left.append(i)
#             if c == ')':
#                 if len(left) > 0:
#                     left.pop()
#                 else:
#                     right.append(i)
#         ans = []
#         for i, c in enumerate(s):
#             if i in left or i in right:
#                 continue
#             ans.append(c)
#         return ''.join(ans)
#
# ss = Solution()
# s = "lee(t(c)o)de)"
# s = "a)b(c)d"
# s = "))(("
# s = "(a(b(c)d)"
# print(ss.minRemoveToMakeValid(s))

# from math import *
# class Solution:
#     def isGoodArray(self, nums) -> bool:
#         N = len(nums)
#         if N == 1:
#             if nums[0] == 1:
#                 return True
#             return False
#
#         last = nums[0]
#
#         for i in range(1, N):
#             last = gcd(last, nums[i])
#             if last == 1:
#                 return True
#         if last == 1:
#             return True
#         return False
#
# s = Solution()
# nums = [12,5,7,23]
# nums = [29,6,10]
# nums = [3,6]
# print(s.isGoodArray(nums))

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        A = []
        B = []
        N = len(s1)
        for i in range(N):
            if s1[i] == s2[i]:
                continue
            A.append(s1[i])
            B.append(s2[i])
        # print(A, B)

        import collections
        C = collections.Counter(A + B)
        for k, v in C.items():
            if v % 2 == 1:
                return -1

        S = set()
        ans = 0
        for i in range(len(A)):
            cur = (A[i], B[i])
            if cur in S:
                ans += 1
                S.remove(cur)
            else:
                S.add(cur)
        ans += len(S)
        return ans

s = Solution()
s1 = "yx"
s2 = "yx"
# s1 = "xxyyxyxyxx"
# s2 = "xyyxyxxxyx"
s1 = "xy"
s2 = "yy"
print(s.minimumSwap(s1, s2))





