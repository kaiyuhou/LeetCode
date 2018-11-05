# class Solution:
#     def get_e0(self, s):
#         ans = ""
#         for i in s:
#             if i == '.':
#                 continue
#             elif i == "+":
#                 return ans
#             else:
#                 ans += i
#         return ans
#
#     def numUniqueEmails(self, emails):
#         """
#         :type emails: List[str]
#         :rtype: int
#         """
#         ans = {}
#         for e in emails:
#             es = e.split('@')
#             e0 = self.get_e0(es[0])
#
#             if es[1] in ans.keys():
#                 ans[es[1]].add(e0)
#             else:
#                 ans[es[1]] = set()
#                 ans[es[1]].add(e0)
#
#         cnt = 0
#         for k in ans.keys():
#             # print(k)
#             # print(ans[k])
#             cnt += len(ans[k])
#
#         return cnt
#
# s = Solution()
# emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# print(s.numUniqueEmails(emails))


# class Solution:
#     def numSubarraysWithSum(self, A, S):
#         """
#         :type A: List[int]
#         :type S: int
#         :rtype: int
#         """
#         forward_0 = []
#         position_1 = []
#
#         cnt = 0
#         pos = 0
#         for i in A:
#             if i == 1:
#                 forward_0.append(cnt)
#                 cnt = 0
#                 position_1.append(pos)
#             else:
#                 cnt += 1
#             pos += 1
#
#         forward_0.append(cnt)
#
#         # print(forward_0)
#         # print(position_1)
#
#         count_1 = sum(A)
#         if count_1 < S:
#             return 0
#
#         ans = 0
#         if S == 0:
#             for i in forward_0:
#                 ans += (i + 1) * i // 2
#             return ans
#
#         ans = 0
#         for i in range(count_1 - S + 1):
#             left = i
#             right = i + S
#             ans += (forward_0[left] + 1) * (forward_0[right] + 1)
#
#         return ans
#
# s = Solution()
# # A = [1,0,1,0,1]
# # S = 2
# A = [1, 0, 0, 0, 1]
# S = 0
#
# print(s.numSubarraysWithSum(A, S))

# class Solution:
# #     def minFallingPathSum(self, A):
# #         """
# #         :type A: List[List[int]]
# #         :rtype: int
# #         """
# #         N = len(A)
# #         if N == 1:
# #             return A[0][0]
# #
# #
# #         for i in range(1, N):
# #             for j in range(N):
# #                 if j == 0:
# #                     A[i][j] += min(A[i-1][j], A[i-1][j+1])
# #                 elif j == N - 1:
# #                     A[i][j] += min(A[i-1][j-1], A[i-1][j])
# #                 else:
# #                     A[i][j] += min(A[i-1][j-1], A[i-1][j], A[i-1][j+1])
# #
# #         return min(A[N-1])
# #
# # s = Solution()
# # A = [[1,2,3],[4,5,6],[7,8,9]]
# # print(s.minFallingPathSum(A))

# class Solution:
#     def dfs(self, i, left, right, left_forbid, right_forbid):
#         l = left_forbid
#         r = right_forbid
#         back = True
#
#         if i not in left_forbid:
#             self.ans[left] = i
#             for j in range(left + 1, self.N * 2):
#                 if self.ans[j] == 0:
#                     break
#                 tmp = i * 2
#                 if tmp - self.ans[j] < i and tmp - self.ans[j] > 0:
#                     l.add(tmp - self.ans[j])
#             left -= 1
#             back = self.dfs(i - 1, left, right, l, r)
#             if back:
#                 return True
#
#         if i not in right_forbid:
#             self.ans[right] = i
#             for j in range(right - 1, 0, -1):
#                 if self.ans[j] == 0:
#                     break
#                 tmp = i * 2
#                 if tmp - self.ans[j] < i and tmp - self.ans[j] > 0:
#                     r.add(tmp - self.ans[j])
#             right += 1
#             back = self.dfs(i - 1, left, right, l, r)
#             if back:
#                 return True
#
#         return False
#
#
#     def beautifulArray(self, N):
#         """
#         :type N: int
#         :rtype: List[int]
#         """
#         pos = [0 for i in range(N)]
#         self.ans = [0 for i in range(N*2)]
#         self.N = N
#
#         left_forbid = set()
#         right_forbid = set()
#
#
#         left = N
#         right = N + 1
#
#         self.ans[left] = N
#         left -= 1
#         self.dfs(N - 1, left, right, left_forbid, right_forbid)
#
#
#
#         return self.ans[left + 1:right]

class Solution:
    def beautifulArray(self, N):
        """
        :type N: int
        :rtype: List[int]
        """
        if N==1:
            return [1]
        else:
            l=self.beautifulArray(N//2)
            r=self.beautifulArray(N-N//2)
            return [x*2 for x in l]+[x*2-1 for x in r]

s = Solution()
print(s.beautifulArray(8))


# def t(n)
#
#     for