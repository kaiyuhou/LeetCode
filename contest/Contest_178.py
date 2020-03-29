from typing import *
from Tree import *

# import bisect
# # # class Solution:
# # #     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
# # #         t = list(nums)
# # #         t.sort()
# # #         ans = []
# # #         for a in nums:
# # #             ans.append(bisect.bisect_right(t, a - 1))
# # #         return ans
# # #
# # # nums = [8,1,2,2,3]
# # # nums = [6,5,4,8]
# # # nums = [7,7,7,7]
# # # s = Solution()
# # # print(s.smallerNumbersThanCurrent(nums))

# class Solution:
#     def rankTeams(self, votes: List[str]) -> str:
#         N = len(votes[0])
#         dp = {}
#         for c in votes[0]:
#             dp[c] = [0] * N + [c]
#         for v in votes:
#             for i in range(N):
#                 dp[v[i]][i] -= 1
#         # print(dp)
#
#         A = []
#         for key, value in dp.items():
#             A.append(tuple(value))
#         A.sort()
#         # print(A)
#         ans = ""
#         for a in A:
#             ans += a[N]
#
#         return ans
#
# s = Solution()
# votes = ["ABC","ACB","ABC","ACB","ACB"]
# votes = ["WXYZ","XYZW"]
# votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
# votes = ["BCA","CAB","CBA","ABC","ACB","BAC"]
# votes = ["M","M","M","M"]
# print(s.rankTeams(votes))


# class Solution:
#     def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
#         ans = [False]
#
#         def dfs(head_cur, root):
#             if ans[0] == True:
#                 return
#             if head_cur is None:
#                 ans[0] = True
#                 return
#             if root is None:
#                 return
#
#             if head_cur.val == root.val:
#                 dfs(head_cur.next, root.left)
#                 dfs(head_cur.next, root.right)
#             else:
#                 dfs(head, root.left)
#                 dfs(head, root.right)
#
#         dfs(head, root)
#         return ans[0]

class Solution:
    def minCost(self, G: List[List[int]]) -> int:
        M = len(G)
        N = len(G[0])
        if M == 1 and N == 1:
            return 0
        Visited  = [[False for _ in range(N)] for _ in range(M)]
        next = ((0 ,1), (0, -1), (1, 0), (-1, 0))
        cost = 0
        unused = []

        def isOK(x, y):
            if x < 0 or y < 0 or x >= M or y >= N:
                return False
            return True

        def v(start_x, start_y):
            unused = []
            while Visited[start_x][start_y] == False:
                Visited[start_x][start_y] = True
                if start_x == M - 1 and start_y == N - 1:
                    return cost, None

                unused.append((start_x, start_y))
                nx, ny = next[G[start_x][start_y] - 1]
                start_x, start_y = start_x + nx, start_y + ny
                # print(start_x, start_y)
                if isOK(start_x, start_y) == False:
                    break
            return None, unused

        unused = [(0, 0)]
        for i in range(205):
            new_unused = []
            # print(unused)
            for x, y in unused:
                ans, cur_unused = v(x, y)
                if ans is not None:
                    return cost
                new_unused += list(cur_unused)
            # print(new_unused)

            unused = set()
            cost += 1
            for x, y in new_unused:
                for nx, ny in next:
                    xx, yy = x + nx, y + ny
                    if isOK(xx, yy) == False:
                        continue
                    if Visited[xx][yy]:
                        continue
                    if xx == M - 1 and yy == N - 1:
                        return cost
                    unused.add((xx, yy))
            unused = list(unused)

s = Solution()
grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
grid = [[1,1,3],[3,2,2],[1,1,4]]
grid = [[1,2],[4,3]]
grid = [[2,2,2],[2,2,2]]
grid = [[4]]
print(s.minCost(grid))


























