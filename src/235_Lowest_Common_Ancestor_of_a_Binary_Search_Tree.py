# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 16:54:21 2015

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
    def lowestCommonAncestor(self, root, p, q):
        """
        Your runtime beats 94.55% of python submissions
        """
        current = root
        while (p.val < current.val and q.val < current.val) or (p.val > current.val and q.val > current.val):
            current = current.left if p.val < current.val else current.right
        return current

testcase = TreeNode(5)
a = [3,6,2,4,7,9]
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
print sln.lowestCommonAncestor(testcase,TreeNode(1),TreeNode(4))
        