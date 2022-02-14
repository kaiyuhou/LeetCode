class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        ans = 0

        def dfs(root):
            nonlocal ans

            if root is None:
                return 0
            dl = dfs(root.left)
            dr = dfs(root.right)
            ans = max(dl + dr, ans)
            return 1 + max(dl, dr)

        ans = max(dfs(root.left) + dfs(root.right), ans)
        return ans
