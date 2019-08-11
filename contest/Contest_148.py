# class Solution:
# #     def movesToMakeZigzag(self, nums) -> int:
# #
# #         N = len(nums)
# #         if N == 1:
# #             return 0
# #
# #         cur = 0
# #         for i in range(1, N):
# #             if i % 2 == 0: continue
# #             if i == N - 1:
# #                 if nums[i] >= nums[i - 1]:
# #                     cur += nums[i] - nums[i - 1] + 1
# #             else:
# #                 if nums[i] >= min(nums[i - 1], nums[i + 1]):
# #                     cur += nums[i] - min(nums[i - 1], nums[i + 1]) + 1
# #
# #         ans = cur
# #
# #         cur = 0
# #         for i in range(N):
# #             if i % 2 == 1: continue
# #             if i == 0:
# #                 if nums[i] >= nums[i + 1]:
# #                     cur += nums[i] - nums[i + 1] + 1
# #             elif i == N - 1:
# #                 if nums[i] >= nums[i - 1]:
# #                     cur += nums[i] - nums[i - 1] + 1
# #             else:
# #                 if nums[i] >= min(nums[i - 1], nums[i + 1]):
# #                     cur += nums[i] - min(nums[i - 1], nums[i + 1]) + 1
# #
# #         return min(ans, cur)
# #
# # s = Solution()
# # # A = [1,2,3]
# # # A = [9,6,1,6,2]
# # # A = [2,7,10,9,8,9]
# # A = [10,4,4,10,10,6,2,3]
# # print(s.movesToMakeZigzag(A))

from contest.Tree import *

# class Solution:
#     def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
#         def num_node(root):
#             if root == None:
#                 return 0
#             return 1 + num_node(root.left) + num_node(root.right)
#
#         def get_node(root, x):
#             if root == None:
#                 return None
#             if root.val == x:
#                 return root
#             if get_node(root.left, x) != None:
#                 return get_node(root.left, x)
#             if get_node(root.right, x) != None:
#                 return get_node(root.right, x)
#
#         cur = get_node(root, x)
#         if n - num_node(cur) > num_node(cur):
#             return True
#         if n - num_node(cur.left) < num_node(cur.left):
#             return True
#         if n - num_node(cur.right) < num_node(cur.right):
#             return True
#         return False
# s = Solution()
# print(s.btreeGameWinningMove(list_to_tree([1]), 1, 1 ))

# class SnapshotArray:
#
#     def __init__(self, length: int):
#         self.N = length
#         self.A = [[(0, 0)] for i in range(self.N)]
#         self.snap_id = 0
#
#     def set(self, index: int, val: int) -> None:
#         if self.A[index][-1][0] == self.snap_id:
#             self.A[index][-1] = (self.snap_id, val)
#         else:
#             self.A[index].append((self.snap_id, val))
#
#     def snap(self) -> int:
#         self.snap_id += 1
#         return self.snap_id - 1
#
#     def get(self, index: int, snap_id: int) -> int:
#         B = self.A[index]
#         if snap_id >= B[-1][0]:
#             return B[-1][1]
#
#         M = len(B)
#         l = 0
#         r = M - 1
#         while l < r:
#             m = (l + r) // 2
#             if B[m][0] == snap_id:
#                 return B[m][1]
#             if B[m][0] < snap_id:
#                 l = m + 1
#             if B[m][0] > snap_id:
#                 r = m - 1
#             if B[l][0] > snap_id:
#                 return B[l - 1][1]
#         return B[l][1]
#
#
# obj = SnapshotArray(50000)
# obj.set(0, 5)
# param_2 = obj.snap()
# obj.snap()
# obj.set(0, 6)
#
# obj.snap()
# obj.snap()
# obj.snap()
# obj.set(0, 7)
# print(obj.get(0,0))
# print(obj.get(0,1))
# print(obj.get(1,1))
# print(obj.get(0,4))

class Solution:
    def longestDecomposition(self, text: str) -> int:
        N = len(text)
        if N == 0:
            return 0

        for i in range(N // 2):
            if text[:i + 1] == text[N - i - 1:]:
                return 2 + self.longestDecomposition(text[i + 1: N - i - 1])
        return 1

s = Solution()
# text = "ghiabcdefhelloadamhelloabcdefghi"
# text = "merchant"
text = "aaa"
print(s.longestDecomposition(text))










