# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 15:46:14 2015

@author: Mike
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def disp(root):
    que = [root]
    while len(que) > 0:
        current = que[0]
        que.remove(current)
        print current.val,
        if current.left:
            que.append(current.left)
        if current.right:
            que.append(current.right)
    print

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            tmp = root.left
            root.left = root.right
            root.right = tmp
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root

testcase = TreeNode(4)
a = [2,7,1,3,6,9]
que = [testcase]
i = 0
while i < len(a):
    current = que[0]
    que.remove(current)
    current.left = TreeNode(a[i])
    current.right = TreeNode(a[i+1])
    que.append(current.left)
    que.append(current.right)
    i += 2   
    
disp(testcase)
sln = Solution()
ans = sln.invertTree(testcase)
disp(ans)
        