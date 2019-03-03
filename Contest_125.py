# class Solution:
#     def findJudge(self, N: int, trust) -> int:
#         t = [0 for i in range(N)]
#         f = [0 for i in range(N)]
#
#         for a in trust:
#             # print(a)
#             t[a[1] - 1] += 1
#             f[a[0] - 1] += 1
#
#
#         for i, a in enumerate(t):
#             if a == N - 1:
#                 if f[i] == 0:
#                     return i + 1
#
#         return -1
#
# s = Solution()
# # N = 2
# # trust = [[1,2]]
# N = 4
# trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
# print(s.findJudge(N, trust))

# class Solution:
#     def numRookCaptures(self, board) -> int:
#         ans = 0
#         rx, ry = 0, 0
#         plist = []
#
#         for i in range(8):
#             for j in range(8):
#                 if board[i][j] == 'R':
#                     rx = i
#                     ry = j
#                 if board[i][j] == 'p':
#                     plist.append((i, j))
#
#
#         for p in plist:
#             if p[0] == rx:
#                 l = min(p[1], ry)
#                 r = max(p[1], ry)
#                 for i in range(l + 1, r):
#                     if board[rx][i] != '.':
#                         break
#                 else:
#                     ans += 1
#
#             if p[1] == ry:
#                 l = min(p[0], rx)
#                 r = max(p[0], rx)
#                 for i in range(l + 1, r):
#                     if board[i][ry] != '.':
#                         break
#                 else:
#                     ans += 1
#
#         return ans

# s = Solution()
# # board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
# # board =  [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
# board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
#
#
# print(s.numRookCaptures(board))

#
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# class Solution:
#     def get_tree(self, root):
#         if root == None:
#             return []
#
#         return self.get_tree(root.left) + [root.val] + self.get_tree(root.right)
#
#     def construct(self, B):
#         if B == [] or B == None:
#             return None
#
#         val = max(B)
#         index = B.index(val)
#
#         root = TreeNode(val)
#         root.left = self.construct(B[:index])
#         root.right = self.construct(B[index + 1:])
#         return root
#
#
#
#     def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
#         if root == None:
#             return TreeNode(val)
#
#         A = self.get_tree(root.left) + [root.val] + self.get_tree(root.right)
#         # print(A)
#
#         A.append(val)
#
#         return self.construct(A)
#
#
# s = Solution()
# root = TreeNode(4)
# root.left = TreeNode(1)
# root.right = TreeNode(3)
# root.right.left = TreeNode(2)
# val = 5
# s.insertIntoMaxTree(root, val)


class Solution:
    def gridIllumination(self, N: int, lamps, queries):
        x_dict = {}
        y_dict = {}
        x_diag = {}
        y_diag = {}
        pd = {}   # xy to index
        off = set() # index
        ans = []

        for i, p in enumerate(lamps):
            x, y = p[0], p[1]

            pd[(x, y)] = i

            xd = x - y
            yd = x + y

            if x not in x_dict.keys():
                x_dict[x] = []
            if y not in y_dict.keys():
                y_dict[y] = []
            if xd not in x_diag.keys():
                x_diag[xd] = []
            if yd not in y_diag.keys():
                y_diag[yd] = []

            x_dict[x].append(i)
            y_dict[y].append(i)
            x_diag[xd].append(i)
            y_diag[yd].append(i)


        for q in queries:
            x, y = q[0], q[1]
            xd = x - y
            yd = x + y

            cur = 0
            if cur == 0 and x in x_dict.keys():
                for p in x_dict[x]:
                    if p not in off:
                        cur = 1
                        break

            if cur == 0 and y in y_dict.keys():
                for p in y_dict[y]:
                    if p not in off:
                        cur = 1
                        break

            if cur == 0 and xd in x_diag.keys():
                for p in x_diag[xd]:
                    if p not in off:
                        cur = 1
                        break

            if cur == 0 and yd in y_diag.keys():
                for p in y_diag[yd]:
                    if p not in off:
                        cur = 1
                        break

            ans.append(cur)

            x_start = max(0, x - 1)
            x_end = min(N - 1, x + 1)
            y_start = max(0, y - 1)
            y_end = min(N - 1, y + 1)

            for i in range(x_start, x_end + 1):
                for j in range(y_start, y_end + 1):
                    if (i,j) in pd.keys():
                        off.add(pd[(i, j)])

        return ans

s = Solution()
N = 10
lamps = [[3,9],[3,6],[8,3],[5,3],[8,1],[1,3],[5,9],[4,2]]
queries = [[1,9],[4,9],[7,1],[6,9]]


# N = 100
# lamps = [[7,55],[53,61],[2,82],[67,85],[81,75],[38,91],[68,0],[60,43],[40,19],[12,75],[26,2],[24,89],[42,81],[60,58],[77,72],[33,24],[19,93],[7,16],[58,54],[78,57],[97,49],[65,16],[42,75],[90,50],[89,34],[76,97],[58,23],[62,47],[94,28],[88,65],[3,87],[81,10],[12,81],[44,81],[54,92],[90,54],[17,54],[27,82],[48,15],[8,46],[4,99],[15,13],[90,77],[2,87],[18,33],[52,90],[4,95],[57,61],[31,22],[32,8],[49,26],[24,65],[88,55],[88,38],[64,76],[94,76],[59,12],[41,46],[80,28],[38,36],[65,67],[75,37],[56,97],[83,57],[2,4],[44,43],[71,90],[62,40],[79,94],[81,11],[96,34],[38,11],[22,3],[54,96],[78,33],[54,54],[79,98],[1,28],[0,32],[37,11]]
# queries = [[24,84],[95,68],[80,35],[31,53],[69,45],[85,29],[87,25],[42,47],[7,59],[99,3],[31,70],[64,62],[44,91],[55,25],[15,52],[95,33],[21,29],[61,34],[93,34],[79,27],[30,86],[52,0],[18,10],[5,1],[40,21],[11,48],[55,94],[22,42],[81,0],[39,43],[5,25],[43,29],[45,47],[83,93],[77,70],[22,63],[30,73],[18,48],[39,88],[91,47]]


print(s.gridIllumination(N, lamps, queries))





















