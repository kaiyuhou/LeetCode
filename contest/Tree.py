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

    root = TreeNode(A[0])
    this_level = [root]
    next_level = []

    for i in range(1, len(A)):

        if i % 2 == 1:
            if this_level[0] == None:
                next_level.append(None)
                continue

            left = None if A[i] == None else TreeNode(A[i])
            this_level[0].left = left
            next_level.append(left)

        else:
            if this_level[0] == None:
                next_level.append(None)
                this_level = this_level[1:]
                continue

            right = None if A[i] == None else TreeNode(A[i])
            this_level[0].right = right
            next_level.append(right)
            this_level = this_level[1:]

        if len(this_level) == 0:
            this_level = next_level
            next_level = []

    return root


def tree_to_list(root):
    if root == None:
        return []
        # return [None]

    ans = [root.val]

    this_level = [root]
    next_level = []

    while this_level != []:
        node = this_level[0]
        this_level = this_level[1:]

        if node == None:
            ans.append(None)
            ans.append(None)

            next_level.append(None)
            next_level.append(None)

        else:
            if node.left == None:
                ans.append(None)
                next_level.append(None)
            else:
                ans.append(node.left.val)
                next_level.append(node.left)

            if node.right == None:
                ans.append(None)
                next_level.append(None)
            else:
                ans.append(node.right.val)
                next_level.append(node.right)


        if this_level == []:
            # print(next_level)
            for node in next_level:
                if node != None:
                    # print("break")
                    break
            else:
                # print("else")
                break

            this_level = next_level
            next_level = []

    while ans[-1] == None:
        ans.pop()

    return ans




if __name__ == "__main__":
    # root = list_to_tree([0,-3,9,-10,None,5])
    # print(tree_to_list(root))

    root = list_to_tree([])
    print(tree_to_list(root))






