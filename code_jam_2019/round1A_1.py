from math import *

class TreeNode:
    def __init__(self):
        self.val = set()
        self.child = [None for i in range(26)]


def dfs(root, ans):
    if len(root.val) <= 1:
        return

    for i in range(26):
        if root.child[i] != None:
            dfs(root.child[i], ans)

    diff = root.val - ans
    if len(diff) <= 1:
        return

    ans.add(diff.pop())
    ans.add(diff.pop())

t = int(input())
for T in range(1, t + 1):
    n = int(input())
    ans = set()
    root = TreeNode()

    for i in range(n):
        cur = root
        word = input()
        for j in range(len(word) - 1, -1, -1):
            index = ord(word[j]) - 65
            if cur.child[index] == None:

                cur.child[index] = TreeNode()

            cur.child[index].val.add(word)
            cur = cur.child[index]
    # print(root.child)

    for i in range(26):
        if root.child[i] != None:
            # print(i)
            dfs(root.child[i], ans)

    print("Case #{}: {}".format(T, len(ans)))
