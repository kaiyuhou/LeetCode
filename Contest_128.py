
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution:
#     def bitwiseComplement(self, N: int) -> int:
#         s = bin(N)[2:]
#         s = s.replace('1','x').replace('0', '1').replace('x', '0')
#         return int(s, base=2)
#
# s = Solution()
# A = 0
# print(s.bitwiseComplement(A))

class Solution:
    def numPairsDivisibleBy60(self, time) -> int:
        reminder = [0 for i in range(60)]
        for t in time:
            reminder[t % 60] += 1

        ans = 0

        if reminder[0] > 1:
            ans += reminder[0] * (reminder[0] - 1) // 2

        if reminder[30] > 1:
            ans += reminder[30] * (reminder[30] - 1) // 2

        for i in range(1, 30):
            ans += reminder[i] * reminder[60 - i]

        return ans
s = Solution()
A = [40,40,60]
print(s.numPairsDivisibleBy60(A))


# import bisect
# 
# class Solution:
#     def is_OK(self, sumn, ans, D, N):
#         # sumn[first_index]
#         sum_now = 0
#         # print('round', ans)
#         for i in range(D):
#             index = bisect.bisect_left(sumn, sum_now + ans)
#             # print(index)
# 
#             if index == N:
#                 # print('out', index, sum_now, ans)
#                 return True
#             if index == N - 1 and sum_now + ans == sumn[-1]:
#                 # print('out', index, sum_now, ans)
#                 return True
# 
#             if sumn[index] == sum_now + ans:
#                 sum_now = sumn[index]
#             else:
#                 sum_now = sumn[index - 1]
# 
#             if sumn[-1] - sum_now > (D - i - 1) * ans:
#                 return False
#         return False
# 
#     def shipWithinDays(self, weights, D: int) -> int:
#         if D == 1:
# #             return sum(weights)
# #
#         s = 0
#         sumn = []
#         N = len(weights)
#         for w in weights:
#             s += w
#             sumn.append(s)
# 
#         ans = max(weights)
#         d, m = divmod(sumn[-1], D)
#         if m > 0:
#             d += 1
#         ans = max(d, ans)
# 
# 
#         left = ans
#         right = 50000 * 500
#         while left < right:
#             mid = (left + right) // 2
#             if self.is_OK(sumn, mid, D, N):
#                 right = mid
#             else:
#                 left = mid + 1
#         return left
# 
# s = Solution()
# # weights = [1,2,3,4,5,6,7,8,9,10]
# # D = 5
# 
# # weights = [3,2,2,4,1,4]
# # D = 3
# 
# # weights = [1,2,3,1,1]
# # D = 4
# 
# # weights = [147,73,265,305,191,152,192,293,309,292,182,157,381,287,73,162,313,366,346,47]
# # D = 10
#
# 
# print(s.shipWithinDays(weights, D))

# class Solution:
#     def numDupDigitsAtMostN(self, N: int) -> int:
#         for i in range(N):
#             a = str(N)
#
#         return a
#
# s = Solution()
# print(s.numDupDigitsAtMostN(100000000))


















