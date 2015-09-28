# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 09:41:36 2015

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
    def binaryTreePaths(self, root):
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        ans = [str(root.val) + '->' + path for path in self.binaryTreePaths(root.left)]
        ans +=[str(root.val) + '->' + path for path in self.binaryTreePaths(root.right)]
        return ans            
        
testcase = TreeNode(4)
a = []#[2,7,1,3,6,9]
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
print sln.binaryTreePaths(testcase)
        