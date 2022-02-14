class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_map = {}

        def dfs(root: TreeNode, parent):
            if root is None:
                return
            p_map[root] = parent
            dfs(root.left, root)
            dfs(root.right, root)

        dfs(root, None)

        def build_ancestor_array(node):
            ans = [node]
            while p_map[node] is not None:
                ans.append(p_map[node])
                node = p_map[node]
            return ans

        p_ancestor = build_ancestor_array(p)
        q_ancestor = build_ancestor_array(q)

        for i in range(min(len(p_ancestor), len(q_ancestor))):
            if p_ancestor[-(1 + i)].val != q_ancestor[-(1 + i)].val:
                return p_ancestor[-i]
        else:
            return p_ancestor[-(1 + i)]








