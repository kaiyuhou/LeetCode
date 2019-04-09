from Tree import *

class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        def dfs(nums, l, r):
            if r - l <= 0:
                return None
            if r - l == 1:
                return TreeNode(nums[l])

            mid = l + (r - l)//2
            root = TreeNode(nums[mid])
            root.left = dfs(nums, l, mid)
            root.right = dfs(nums, mid + 1, r)
            return root
        return dfs(nums, 0, len(nums))



