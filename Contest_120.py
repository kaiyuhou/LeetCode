# class Solution:
#     def sortedSquares(self, A):
#         """
#         :type A: List[int]
#         :rtype: List[int]
#         """
#         ans = []
#         for a in A:
#             ans.append(a * a)
#
#         ans.sort()
#         return  ans
#
# s = Solution()
# A = [-7,-3,2,3,11]
# print(s.sortedSquares(A))

# class Solution:
#     def maxTurbulenceSize(self, A):
#         """
#         :type A: List[int]
#         :rtype: int
#         """
#         N = len(A)
#         if N == 1:
#             return 1
#         elif N == 2:
#             if A[0] != A[1]:
#                 return 2
#             else:
#                 return 1
#
#         ans = 0
#         tmp = 1
#         for i in range(N-1):
#             if i % 2 == 1:
#                 if A[i] > A[i+1]:
#                     tmp += 1
#                 else:
#                     ans = max(ans, tmp)
#                     tmp = 1
#             else:
#                 if A[i] < A[i+1]:
#                     tmp += 1
#                 else:
#                     ans = max(ans, tmp)
#                     tmp = 1
#         ans = max(ans, tmp)
#
#         tmp = 1
#         for i in range(N - 1):
#             if i % 2 == 1:
#                 if A[i] < A[i + 1]:
#                     tmp += 1
#                 else:
#                     ans = max(ans, tmp)
#                     tmp = 1
#             else:
#                 if A[i] > A[i + 1]:
#                     tmp += 1
#                 else:
#                     ans = max(ans, tmp)
#                     tmp = 1
#
#         return ans
#
# s = Solution()
# # A = [9,4,2,10,7,8,8,1,9]
# # A = [4,8,12,16]
# A = [100]
# print(s.maxTurbulenceSize(A))


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# class Solution:
#     def get_total_coin(self, root):
#         if root == None:
#             return 0
#         else:
#             return root.val + self.get_total_coin(root.left) + self.get_total_coin(root.right)
#
#     def get_total_node(self, root):
#         if root == None:
#             return 0
#         else:
#             return 1 + self.get_total_node(root.left) + self.get_total_node(root.right)
#
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        ans = 0

        left_coins = self.get_total_coin(root.left)
        right_coins = self.get_total_coin(root.right)
        left_nodes = self.get_total_node(root.left)
        right_nodes = self.get_total_node(root.right)

        if left_coins - left_nodes > 0:
            ans += left_coins - left_nodes
            root.val += left_coins - left_nodes

        if right_coins - right_nodes > 0:
            ans += right_coins - right_nodes
            root.val += right_coins - right_nodes

        if left_coins - left_nodes < 0:
            ans += -(left_coins - left_nodes)
            root.val += left_coins - left_nodes

        if right_coins - right_nodes < 0:
            ans += -(right_coins - right_nodes)
            root.val += right_coins - right_nodes

        return ans + self.distributeCoins(root.left) + self.distributeCoins(root.right)
#
# s = Solution()

class Solution:
    def check(self, x, y):
        return x >= 0 and y >= 0 and x < self.N and y < self.M and self.visited[x][y] == False

    def dfs(self, x, y, step, grid):
        next_list = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for next in next_list:
            next_x = x + next[0]
            next_y = y + next[1]
            if self.check(next_x, next_y):
                if grid[next_x][next_y] == 2 and step == self.n_0:
                    self.ans += 1
                elif grid[next_x][next_y] == 0:
                    self.visited[next_x][next_y] = True
                    self.dfs(next_x, next_y, step + 1, grid)
                    self.visited[next_x][next_y] = False

    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.N = len(grid)
        self.M = len(grid[0])
        self.n_0 = 0
        for x in range(self.N):
            for y in range(self.M):
                if grid[x][y] == 0:
                    self.n_0 += 1
                elif grid[x][y] == 1:
                    start_x = x
                    start_y = y

        self.visited = [[False for j in range(self.M)] for i in range(self.N)]
        self.visited[start_x][start_y] = True
        self.ans = 0

        self.dfs(start_x, start_y, 0, grid)
        return self.ans

s = Solution()
# A = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
# A = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
# A = [[0,1],[2,0]]
A = [[1,2]]
print(s.uniquePathsIII(A))












