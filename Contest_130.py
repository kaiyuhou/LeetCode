from Tree import *

# class Solution:
#     def prefixesDivBy5(self, A):
#         b = ""
#         ans = []
#         for a in A:
#             b = b + str(a)
#             ans.append(int(b, 2) % 5 == 0)
#         return ans
#
# s = Solution()
# A = [1,1,1,0,1]
# print(s.prefixesDivBy5(A))

class Solution:
    def baseNeg2(self, N: int) -> str:
        # ans = ""
        # if N % 2 == 0:
        #     ans = "0"
        #     N //= 2
        # else:
        #     ans = "1"
        #     N += 1
        #     N //= 2
        #
        # while N != 0:
        #     if N % 4 == 0:
        #         ans = "10" + ans
        #     elif N % 4 == 2:
        #         ans = "11" + ans
        #     elif N % 4 == 3:
        #         ans = "01" + ans
        #         N += 1
        #     elif N % 4 == 1
        ans = 0
        def find_plus(N):
            ans = 0
            p = 0
            while ans < N:
                ans += 4 ** p

            return p

        while N != 0:
            find_plus(N)





























s = Solution()
N = 3
print(s.baseNeg2(N))

# class Solution:
#     def nextLargerNodes(self, head: ListNode):
#         if head == None:
#             return []
#
#         A = [head.val]
#         while head.next != None:
#             head = head.next
#             A.append(head.val)
#
#         N = len(A)
#         ans = [0 for i in range(N)]
#         next = [-1 for i in range(N)]
#         for i in range(N - 2, -1, -1):
#             next_i = i + 1
#             while next_i != -1 and A[next_i] <= A[i]:
#                 next_i = next[next_i]
#
#             if next_i != -1:
#                 ans[i] = A[next_i]
#                 next[i] = next_i
#         return ans
#
# s = Solution()

# class Solution:
#     def numEnclaves(self, A) -> int:
#         N = len(A)
#         M = len(A[0])
#
#         # 2 == ok
#         # 3 == not ok
#         # 4 == visited
#         next = [[0, 1], [0, -1], [1, 0], [-1, 0]]
#
#         def dfs(a, b):
#             if a == 0 or b == 0 or a == N - 1 or b == M - 1:
#                 A[a][b] = 2
#
#             if A[a][b] == 2:
#
#                 for step in next:
#                     x = a + step[0]
#                     y = b + step[1]
#
#                     if x < 0 or y < 0 or x == N or y == M:
#                         continue
#
#                     if A[x][y] == 1:
#                         A[x][y] = 2
#                         dfs(x, y)
#
#         for i in range(N):
#             for j in [0, M - 1]:
#                 if A[i][j] == 1:
#                     dfs(i, j)
#
#         for i in [0, N - 1]:
#             for j in range(M):
#                 if A[i][j] == 1:
#                     dfs(i, j)
#
#         rnt = 0
#         for i in range(N):
#             for j in range(M):
#                 if A[i][j] == 1:
#                     rnt += 1
#         return rnt
#
# s = Solution()
# # A = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# # A = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
# A = [[1]]
# print(s.numEnclaves(A))



