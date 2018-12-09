class Solution:
    def r(self, a, b, c, d):
        return str(a) + str(b) + ":" + str(c) + str(d)

    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        ans = ""

        A.sort()
        dp = [0 for i in range(10)]

        for a in range(23, -1, -1):
            for b in range(59, -1, -1):
                t = list(dp)
                a1 = a % 10












# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# class Solution:
#     def flipEquiv(self, root1, root2):
#         """
#         :type root1: TreeNode
#         :type root2: TreeNode
#         :rtype: bool
#         """
#         if root1 == None and root2 == None:
#             return True
#         elif root1 == None:
#             return False
#         elif root2 == None:
#             return False
#
#         if root1.val != root2.val:
#             return False
#
#
#         return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))
#

# class Solution:
#     def deckRevealedIncreasing(self, deck):
#         """
#         :type deck: List[int]
#         :rtype: List[int]
#         """
#
#         n = len(deck)
#         ans = [0 for i in range(n)]
#         deck.sort()
#
#         next_i = 0
#         while len(deck) > 1:
#             ans[next_i] = deck[0]
#             deck.pop(0)
#
#             count = 0
#             for i in range(n):
#                 next_i = (next_i + 1) % n
#                 if ans[next_i] == 0:
#                     if count == 0:
#                         count = 1
#                     else:
#                         break
#
#         for i in range(n):
#             if ans[i] == 0:
#                 ans[i] = deck[0]
#                 break
#
#         return ans
#
# s = Solution()
# # A = [17,13,11,2,3,5,7]
# A = [1]
# print(s.deckRevealedIncreasing(A))










