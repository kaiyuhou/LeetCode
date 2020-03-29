from typing import *
from Tree import *


# from datetime import date
# class Solution:
#     def daysBetweenDates(self, date1: str, date2: str) -> int:
#         d1 = date.fromisoformat(date1)
#         d2 = date.fromisoformat(date2)
#         return abs(d1.toordinal() - d2.toordinal())
#
# date1 = "2019-06-29"
# date2 = "2019-06-30"
# date1 = "2020-01-15"
# date2 = "2019-12-31"
# s = Solution()
# print(s.daysBetweenDates(date1, date2))

# class TreeNode:
#     def __init__(self):
#         self.left = None
#         self.right = None
#         self.father = None
#
# class Solution:
#     def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
#         nodes = [TreeNode() for _ in range(n)]
#         for i, (l, r) in enumerate(zip(leftChild, rightChild)):
#             if l != -1:
#                 nodes[i].left = nodes[l]
#                 if nodes[l].father is not None:
#                     return False
#                 nodes[l].father = nodes[i]
#             if r != -1:
#                 nodes[i].right = nodes[r]
#                 if nodes[r].father is not None:
#                     return False
#                 nodes[r].father = nodes[i]
#         cnt = 0
#         for node in nodes:
#             if node.father == None:
#                 cnt += 1
#
#         return cnt == 1
#
# s = Solution()
# n = 4
# leftChild = [1,-1,3,-1]
# rightChild = [2,-1,-1,-1]
#
# n = 4
# leftChild = [1,-1,3,-1]
# rightChild = [2,3,-1,-1]
# n = 2
# leftChild = [1,0]
# rightChild = [-1,-1]
#
# n = 6
# leftChild = [1,-1,-1,4,-1,-1]
# rightChild = [2,-1,-1,5,-1,-1]
# print(s.validateBinaryTreeNodes(n, leftChild, rightChild))

# import math
# class Solution:
#     def closestDivisors(self, num: int) -> List[int]:
#         n1 = num + 1
#         n2 = num + 2
#         r = int(math.sqrt(n2))
#         for i in range(r, 0, -1):
#             if n1 % i == 0:
#                 return [i, n1 // i]
#             if n2 % i == 0:
#                 return [i, n2 // i]
#
# num = 8
# s = Solution()
# num = 123
# num = 999052154
# print(s.closestDivisors(num))

import collections
class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        C = collections.Counter(digits)
        ans = ''
        cnt2 = C[8] + C[5] + C[2]
        cnt2_rest = cnt2 % 3

        cnt1 = C[7] + C[4] + C[1]
        cnt1_rest = cnt1 % 3

        if cnt1 == 0:
            cnt2 -= cnt2_rest
        elif cnt2 == 0:
            cnt1 -= cnt1_rest
        elif cnt2_rest != cnt1_rest:
            diff = abs(cnt2_rest - cnt1_rest)
            if diff == 1:
                if cnt2_rest > cnt1_rest:
                    cnt2 -= 1
                else:
                    cnt1 -= 1
            else: # 2
                if cnt2_rest > cnt1_rest:
                    cnt1 -= 1
                else:
                    cnt2 -= 1

        for i in range(9, 0, -1):
            if i % 3 == 0:
                ans += str(i) * C[i]
            if i % 3 == 2:
                ans += str(i) * min(cnt2, C[i])
                cnt2 -= min(cnt2, C[i])
            if i % 3 == 1:
                ans += str(i) * min(cnt1, C[i])
                cnt1 -= min(cnt1, C[i])
        if ans == '' and C[0] > 0:
            return '0'
        ans += '0' * C[0]
        return ans


s = Solution()
digits = [8,1,9]
digits = [8,6,7,1,0]
digits = [1]
digits = [0,0,0,0,0,0]
digits = [9,9,0,0,0,0]
digits = [1,1,1,2,2,2,2]
digits = [5,8]
print(s.largestMultipleOfThree(digits))




















