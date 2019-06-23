from Tree import *

# class Solution:
#     def lastStoneWeight(self, stones) -> int:
#         if len(stones) == 0:
#             return 0
#
#         if len(stones) == 1:
#             return stones[0]
#         else:
#             stones.sort()
#             new_stone = stones[-1] - stones[-2]
#             stones = stones[:-2]
#             if new_stone > 0:
#                 stones.append(new_stone)
#             return self.lastStoneWeight(stones)
#
#
# s = Solution()
# stones = [2,2]
# print(s.lastStoneWeight(stones))

# class Solution:
#     def removeDuplicates(self, S: str) -> str:
#         ans = []
#         for c in S:
#             if not ans:
#                 ans.append(c)
#             elif c == ans[-1]:
#                 ans.pop()
#             else:
#                 ans.append(c)
#         return ''.join(ans)
#
# s = Solution()
# S = "abba"
# print(s.removeDuplicates(S))


# class Solution:
#     def longestStrChain(self, words) -> int:
#         W = [(len(w), w) for w in words]
#         W.sort()
#         # print(W)
#
#         def is_pre(A, B):
#             M = len(A)
#             if M != len(B) - 1:
#                 return False
#
#             j = 0
#             for i in range(M):
#                 if A[i] == B[j]:
#                     j += 1
#                 else:
#                     if i == j and A[i] == B[j + 1]:
#                         j += 2
#                     else:
#                         return False
#             return True
#
#         N = len(words)
#         pres = [[] for _ in range(N)]
#         for i in range(N - 1):
#             for j in range(i + 1, N):
#                 if is_pre(W[i][1], W[j][1]):
#                     pres[j].append(i)
#
#         # print(pres)
#         dp = [1 for _ in range(N)]
#         for i in range(N):
#             for j in pres[i]:
#                 dp[i] = max(dp[i], dp[j] + 1)
#
#         return max(dp)
#
# s = Solution()
# # W = ["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"]
# W = ["a","b","ba","bca","bda","bdca"]
# print((s.longestStrChain(W)))


class Solution:
    def lastStoneWeightII(self, stones) -> int:
        Best = sum(stones) // 2
        dp = [0 for _ in range(Best + 1)]
        dp[0] = 1
        for s in stones:
            for w in range(Best, s - 1, -1):
                if dp[w - s] == 1:
                    dp[w] = 1

        maxw = 0
        for i in range(Best, -1, -1):
            if dp[i] == 1:
                maxw = i
                break

        # print(dp)

        return sum(stones) - maxw - maxw

s = Solution()
S = [2, 6, 8]
print(s.lastStoneWeightII(S))







