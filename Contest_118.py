# class Solution:
#     def get_list(self, a, bound):
#         if a == 1:
#             return [1]
#
#         a_list = [1]
#         cnt = 1
#         while cnt < bound:
#             a_list.append(cnt)
#             cnt *= a
#         return a_list
#
#
#     def powerfulIntegers(self, x, y, bound):
#         """
#         :type x: int
#         :type y: int
#         :type bound: int
#         :rtype: List[int]
#         """
#         ans = set()
#
#         x_list = self.get_list(x, bound)
#         y_list = self.get_list(y, bound)
#
#         for a in x_list:
#             for b in y_list:
#                 if a + b <= bound:
#                     ans.add(a + b)
#
#         return list(ans)
#
# s = Solution()
# x = 1
# y = 1
# bound = 122
# print(s.powerfulIntegers(x,y, bound))

# class Solution:
#     def rev(self, A, N):
#         # print(A, N)
#         if N == 0:
#             return []
#
#         if A[N-1] == N:
#             return self.rev(A[:-1], N-1)
#
#         ans = []
#         if A[0] != N:
#             pos = A.index(N)
#             ans.append(pos + 1)
#             B = list(A[:pos + 1])
#             B.reverse()
#             C = list(A[pos+1:])
#             A = list(B + C)
#
#         ans.append(N)
#         A.reverse()
#         return ans + self.rev(A[:-1], N-1)
#
#     def pancakeSort(self, A):
#         """
#         :type A: List[int]
#         :rtype: List[int]
#         """
#         N = len(A)
#         return self.rev(A, N)
#
# s = Solution()
# # A = [3,2,4,1]
# A = [1,2,3]
# print(s.pancakeSort(A))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# class Solution:
#     def preorder(self, root):
#         if root == None:
#             return []
#
#         ans = []
#         if root.val != self.voyage[0]:
#             return [-1]
#
#         self.voyage = self.voyage[1:]
#
#
#
#         if root.left != None and root.right != None:
#             if root.right.val == self.voyage[0]:
#                 ans.append(root.val)
#                 root.left, root.right = root.right, root.left
#
#         left_ans = self.preorder(root.left)
#         if left_ans == [-1]:
#             return [-1]
#
#         right_ans = self.preorder(root.right)
#         if right_ans == [-1]:
#             return [-1]
#
#         return ans + left_ans + right_ans
#
#
#     def flipMatchVoyage(self, root, voyage):
#         """
#         :type root: TreeNode
#         :type voyage: List[int]
#         :rtype: List[int]
#         """
#         self.voyage = voyage
#         return self.preorder(root)

class Num:
    def __init__(self):
        self.IntPart = 0
        self.NonRep = ""
        self.Rep = ""

    def __str__(self):
        return str(self.IntPart) + "NonRep: " + self.NonRep + "Rep: " + self.Rep

class Solution:
    def safe(self, A):
        if A.NonRep == None:
            A.NonRep = ""

        if A.Rep == None:
            A.Rep = ""

        if A.Rep == "":
            A.Rep = "0"

        A.NonRep = A.NonRep + A.Rep * 16
        A.NonRep = A.NonRep[:16]

    def get_num(self, A):
        n = Num()

        if '.' in A:
            pos1 = A.index('.')
            n.IntPart = int(A[:pos1])
        else:
            n.IntPart = int(A)
            return n

        if '(' in A:
            pos2 = A.index('(')
            n.NonRep = A[pos1 + 1:pos2]
            n.Rep = A[pos2+1:-1]

            for i in range(len(n.Rep)-1):
                if n.Rep[i] != n.Rep[i+1]:
                    break
            else:
                n.Rep = n.Rep[:1]


            if len(n.Rep) == 4 and n.Rep[0] == n.Rep[2] and n.Rep[1] == n.Rep[3]:
                n.Rep = n.Rep[:2]

        else:
            if pos1 != len(A) - 1:
                n.NonRep = A[pos1+1:]
                # print(n.NonRep)
            return n


        if n.Rep == "9":
            n.Rep = ""
            if n.NonRep == None or n.NonRep == "":
                n.IntPart += 1

            else:
                l = len(n.NonRep)
                nonrep = str(int(n.NonRep) + 1)
                if len(nonrep) == l:
                    n.NonRep = nonrep
                elif len(nonrep) > l:
                    n.IntPart += 1
                    if int(nonrep[1:]) == 0:
                        n.NonRep = ""
                    else:
                        n.NonRep = nonrep[1:]
                elif len(nonrep) < l:
                    n.NonRep = '0' * (l - len(nonrep)) + nonrep

        return n

    def isRationalEqual(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        a = self.get_num(S)
        b = self.get_num(T)
        # print(a, b)

        self.safe(a)
        self.safe(b)
        # print(a, b)

        return a.IntPart == b.IntPart and a.NonRep == b.NonRep

s = Solution()
S = "0.(52)"
T = "0.5(25)"
# S = "0.08(9)"
# T = "0.09"
print(s.isRationalEqual(S, T))

