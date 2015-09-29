# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 17:13:36 2015

@author: Mike
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
    def disp(self):
        print self.val,
        print '->',
        if self.next :
            self.next.disp()
        else:
            print 

class Solution(object):
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
        
        
testcase = ListNode(0)
p = testcase
l = [1]
for i in l :   
    q = ListNode(i)
    p.next = q
    p = p.next
testcase.disp()

sln = Solution()

sln.deleteNode(testcase.next)
testcase.disp()    