# class Solution:
#     def reorderLogFiles(self, logs):
#         """
#         :type logs: List[str]
#         :rtype: List[str]
#         """
#         letter = []
#         letter_no_id = []
#         letter_org = {}
#         digit = []
#
#         for i in logs:
#             if i.split(' ')[1][0].isnumeric():
#                 digit.append(i)
#             else:
#                 to_sort = i[i.find(' ') + 1:]
#                 letter_org[to_sort] = i
#                 letter.append(to_sort)
#
#         letter.sort()
#         ans = []
#         for i in letter:
#             ans.append(letter_org[i])
#         return ans + digit
#
# s = Solution()
# logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
# print(s.reorderLogFiles(logs))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# class Solution:
#     def rangeSumBST(self, root, L, R):
#         """
#         :type root: TreeNode
#         :type L: int
#         :type R: int
#         :rtype: int
#         """
#         if L > R:
#             return 0
#
#         ans = 0
#
#         if root.val > R and root.left != None:
#             ans += self.rangeSumBST(root.left, L, R)
#
#         elif root.val < L and root.right != None:
#             ans += self.rangeSumBST(root.right, L, R)
#
#         elif root.val <= R and root.val >= L:
#             ans += root.val
#
#             if root.left != None:
#                 ans += self.rangeSumBST(root.left, L, root.val - 1)
#             if root.right != None:
#                 ans += self.rangeSumBST(root.right, root.val + 1, R)
#
#         return ans

# class Solution:
#     def minAreaRect(self, points):
#         """
#         :type points: List[List[int]]
#         :rtype: int
#         """
#         x_list = {}
#         y_list = {}
#         x_set = set()
#         y_set = set()
#         for x, y in points:
#             if x not in x_set:
#                 x_list[x] = []
#             x_list[x].append(y)
#             x_set.add(x)
#
#             if y not in y_set:
#                 y_list[y] = []
#             y_list[y].append(x)
#             y_set.add(y)
#
#         x_num = list(x_set)
#         x_num.sort()
#
#         for x in x_num:
#             x_list[x].sort()
#
#
#         y_num = list(y_set)
#         y_num.sort()
#         for y in y_num:
#             y_list[y].sort()
#
#
#         INF = 40000 * 40000 * 2
#         ans = INF
#
#         for x in x_num:
#             size_x = len(x_list[x])
#
#             if size_x == 1:
#                 continue
#
#             for i in range(size_x - 1):
#                 y1 = x_list[x][i]
#
#                 for j in range(i + 1, size_x):
#                     y2 = x_list[x][j]
#
#                     len_y =  y2 - y1
#
#                     for next_x in y_list[y1]:
#                         if next_x > x and next_x in y_list[y2]:
#                             ans = min(ans, (next_x - x) * len_y)
#                             break
#
#         if ans == INF:
#             ans = 0
#
#         return ans
#
#
#
# s = Solution()
# ps = [[1,1]]
# print(s.minAreaRect(ps))

class Solution:
    def distinctSubseqII(self, S):
        """
        :type S: str
        :rtype: int
        """
        MOD = 1000000007

        n = len(S) + 1
        m = 129

        rank = [0]
        for c in S:
            rank.append(ord(c))

        rsort = [0 for i in range(m)]
        for i in range(1, n):
            rsort[rank[i]] += 1

        for i in range(1, m):
            rsort[i] += rsort[i - 1]

        sa = [0 for i in range(n)]
        for i in range(n, 0, -1):
            sa[rsort[rank[i]]] = i
            rsort[rank[i]] -= 1

        len = 1
        p = 0
        while(p < n - 1):





s = Solution()
S = 'afafa'
print(s.distinctSubseqII(S))











