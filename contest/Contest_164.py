from Tree import  *

# class Solution:
#     def minTimeToVisitAllPoints(self, ps) -> int:
#         cx, cy = ps[0][0], ps[0][1]
#         ans = 0
#         for i in range(1, len(ps)):
#             x, y = ps[i][0], ps[i][1]
#             dx = abs(x - cx)
#             dy = abs(y - cy)
#             ans += min(dx, dy) + abs(dx - dy)
#             cx, cy = x, y
#         return ans
#
# s = Solution()
# points = [[1,1],[3,4],[-1,0]]
# points = [[3,2]]
# print(s.minTimeToVisitAllPoints(points))

# class Solution:
#     def countServers(self, grid) -> int:
#         m = len(grid)
#         n = len(grid[0])
#         sx = [0] * m
#         sy = [0] * n
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == 1:
#                     sx[i] += 1
#                     sy[j] += 1
#         ans = 0
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == 1:
#                     if sx[i] > 1 or sy[j] > 1:
#                         ans += 1
#         return ans
#
# s = Solution()
# grid = [[1,0],[0,1]]
# grid = [[1,0],[1,1]]
# grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
# print(s.countServers(grid))

# class Solution:
#     def suggestedProducts(self, products, searchWord: str):
#         ans = []
#         class Node:
#             def __init__(self):
#                 self.word = None
#                 self.cnt = 0
#                 self.c = [None] * 26
#         root = Node()
#         for p in products:
#             curr = root
#             for letter in p:
#                 c = ord(letter) - 97
#                 if curr.c[c] is None:
#                     curr.c[c] = Node()
#                 curr = curr.c[c]
#             curr.word = p
#             curr.cnt += 1
#
#
#         count = []
#
#         def search(root):
#             if len(count) >= 3:
#                 return
#             if root.word is not None:
#                 for _ in range(min(3, root.cnt)):
#                     count.append(root.word)
#             for c in root.c:
#                 if c is not None:
#                     search(c)
#
#         curr = root
#         for letter in searchWord:
#             c = ord(letter) - 97
#             if curr.c[c] is None:
#                 ans.append([])
#                 curr = Node()
#             else:
#                 count = []
#                 search(curr.c[c])
#                 newl = list(count)
#                 if len(newl) > 3:
#                     newl = newl[:3]
#                 ans.append(newl)
#                 curr = curr.c[c]
#         return ans
#
# s = Solution()
# # products = ["mobile","mouse","moneypot","monitor","mousepad"]
# # searchWord = "mouse"
# products = ["havana", "havana"]
# searchWord = "havana"
# # products = ["bags","baggage","banner","box","cloths"]
# # searchWord = "bags"
# # products = ["havana"]
# # searchWord = "tatiana"
# print(s.suggestedProducts(products, searchWord))

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        arrLen = min(steps // 2 + 1,  arrLen)
        if arrLen == 1:
            return 1

        dp = [0] * arrLen
        dp[0] = 1
        for _ in range(steps):
            newdp = [0] * arrLen
            for i in range(arrLen):
                if i == 0:
                    newdp[i] = dp[i] + dp[i + 1]
                elif i == arrLen - 1:
                    newdp[i] = dp[i] + dp[i - 1]
                else:
                    newdp[i] = dp[i] + dp[i + 1] + dp[i - 1]
            dp = newdp
            # print(dp)
        return dp[0] % 1000000007
s= Solution()
steps = 3
arrLen = 2
steps = 2
arrLen = 4
steps = 1
arrLen = 1
print((s.numWays(steps, arrLen)))





















