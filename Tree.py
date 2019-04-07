class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def list_to_tree(A):
    n = len(A)
    if n < 1:
        return None

    if A[0] == None:
        return None

    n_nodes_in_level = 0
    root = TreeNode(A[0])

    # for


