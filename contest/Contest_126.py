

# class Solution:
#     def commonChars(self, A):
#         def get_S_list(S):
#             A = [0 for i in range(26)]
#             for c in S:
#                 A[ord(c) - ord('a')] += 1
#             return A
#
#
#         ans = get_S_list(A[0])
#         for i in range(1, len(A)):
#             t = get_S_list(A[i])
#             for i in range(26):
#                 ans[i] = min(ans[i], t[i])
#
#
#         rnt = []
#         for i in range(26):
#             rnt += chr(ord('a') + i) * ans[i]
#         return rnt
#
#
#
# s = Solution()
# # A = ["bella","label","roller"]
# A = ["cool", "a"]
# print(s.commonChars(A))

# class Solution:
#     def isValid(self, S: str) -> bool:
#         N = len(S)
#         if N < 3 or N % 3 != 0:
#             return False
#
#         while len(S) > 0:
#             if S.find("abc") == -1:
#                 return False
#             S = S.replace("abc", "")
#
#         return True
#
# s = Solution()
# S = "cababc"
# print(s.isValid(S))

class Solution:
    def dfs(self, stones, K):
        if len(stones) == K:
            return sum(stones)

        # mins = 3005
        # for i in range(0, len(stones) - K + 1):
        #     cur = sum(stones[i:i + K])
        #     if cur < mins:
        #         mins = cur

        ans = -1
        for i in range(0, len(stones) - K + 1):
            cur = sum(stones[i:i + K])
            rnt = self.dfs(list(stones[:i] + [cur] + stones[i + K:]), K)
            if ans == -1:
                ans = rnt + cur
            else:
                ans = min(ans, rnt + cur)
        return ans


    def mergeStones(self, stones, K: int) -> int:
        N = len(stones)
        if N == 1:
            return 0

        if K >= 3 and N % (K - 1) != 1:
            return -1

        return self.dfs(stones, K)

s = Solution()
# stones = [3,2,4,1]
# K = 2
# stones = [3,2,4,1]
# K = 3
# stones = [3,5,1,2,6]
# K = 3
# stones = [4,6,4,7,5,7,9,8]
# K = 2
stones = [69,39,79,78,16,6,36,97,79,27,14,31,4]
K = 2
print(s.mergeStones(stones, K))

# class Solution:
#     def longestOnes(self, A, K: int) -> int:
#         before_zero = [0]
#         sum_to_n = [0]
#
#         cur_zero = 0
#         sum_n = 0
#
#         N = len(A)
#         flag = 0
#
#         if sum(A) + K >= N:
#             return N
#
#         for i in range(N):
#             if A[i] == 0:
#                 if flag == 0:
#                     cur_zero += 1
#                 else:
#                     sum_to_n.append(sum_n)
#                     flag = 0
#                     cur_zero += 1
#             else:
#                 if flag == 1:
#                     sum_n += 1
#                 else:
#                     before_zero.append(cur_zero)
#                     sum_n += 1
#                     flag = 1
#
#         before_zero.append(cur_zero)
#         sum_to_n.append(sum_n)
#         if flag == 1:
#             sum_to_n.append(sum_n)
#
#         # print(sum_to_n)
#         # print(before_zero)
#         N = len(before_zero)
#         p = 1
#         q = 2
#         ans = sum_to_n[1]
#         while q < N:
#             if p == q:
#                 ans = max(ans, sum_to_n[q] - sum_to_n[q - 1])
#                 q += 1
#
#             else:
#                 if before_zero[q] - before_zero[p] <= K:
#                     ans = max(ans, sum_to_n[q] - sum_to_n[p - 1] + K )
#                     q += 1
#                 else:
#                     p += 1
#             # print(p, q, ans)
#         return ans
#
#
# s = Solution()
# # A = [0,1,1,1,0,0,0,1,1,1,1,0]
# # K = 2
# A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
# K = 0
# print(s.longestOnes(A, K))












