# class Solution:
#     def sumEvenAfterQueries(self, A: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':
#         ans = 0
#         for a in A:
#             if a % 2 == 0:
#                 ans += a
#
#         output = []
#         for [val, index] in queries:
#             if A[index] % 2 == 0:
#                 ans -= A[index]
#
#             A[index] += val
#             if A[index] % 2 == 0:
#                 ans += A[index]
#
#             output.append(ans)
#
#         return output
#
# s = Solution()
# A = [1,2,3,4]
# queries = [[1,0],[-3,1],[-4,0],[2,3]]
# print(s.sumEvenAfterQueries(A,queries))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# class Solution:
#     def dfs(self, root, str):
#         ans = self.chs[root.val] + str
#         if root.left == None and root.right == None:
#             self.ans.append(ans)
#             return
#
#         if root.left != None:
#             self.dfs(root.left, ans)
#
#         if root.right != None:
#             self.dfs(root.right, ans)
#
#
#     def smallestFromLeaf(self, root: 'TreeNode') -> 'str':
#         if root == None:
#             return ''
#
#         self.chs = [chr(i + ord('a')) for i in range(26)]
#         self.ans = []
#         self.dfs(root, '')
#         self.ans.sort()
#         return self.ans[0]
#
#
# s = Solution()
# root = TreeNode(1)
# root.left = TreeNode(0)
# root.right = TreeNode(4)
#
# print(s.smallestFromLeaf(root))

# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
#
# class Solution:
#     def intervalIntersection(self, A: 'List[Interval]', B: 'List[Interval]') -> 'List[Interval]':
#         ans = []
#         N = len(A)
#         M = len(B)
#
#         if N == 0 or M == 0:
#             return []
#
#         i, j = 0 , 0
#
#         for b in B:
#             keep = True
#             if i >= N:
#                 break
#
#             while keep:
#                 keep = False
#                 while b.start > A[i].end:
#                     i += 1
#                     if i >= N:
#                         break
#
#                 if i >= N:
#                     break
#
#                 if b.end < A[i].start:
#                     break
#
#                 start = A[i].start
#                 if b.start > A[i].start:
#                     start = b.start
#                 end = b.end
#                 if b.end > A[i].end:
#                     end = A[i].end
#                     b.start = A[i].end + 1
#                     keep = True
#
#                 ans.append(Interval(start, end))
#         return ans
#
#
# s = Solution()
# A = [Interval(1,4),Interval(5,8)]
# B = [Interval(2,6), Interval(7,9)]
# ans = s.intervalIntersection(A, B)
# for i in ans:
#     print(i.start,i.end)


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self, root, x, y):
        self.mem.append((x, y, root.val))

        if root.left:
            self.dfs(root.left, x - 1, y + 1)
        if root.right:
            self.dfs(root.right, x + 1, y + 1)

    def verticalTraversal(self, root: 'TreeNode') -> 'List[List[int]]':
        if root == None:
            return []


        self.mem = []
        self.dfs(root, 0, 0)
        self.mem.sort()
        ans = []
        cur = [self.mem[0][2]]
        for i in range(1, len(self.mem)):
            if self.mem[i][0] == self.mem[i-1][0]:
                cur.append(self.mem[i][2])
            else:
                ans.append(cur)
                cur = [self.mem[i][2]]
        ans.append(cur)
        return ans

s = Solution()
root = TreeNode(3)
root.left = TreeNode(5)
root.left.right = TreeNode(1)
root.right = TreeNode(7)
root.right.left = TreeNode(3)
print(s.verticalTraversal(root))























