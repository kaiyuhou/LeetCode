# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 17:04:55 2015

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
        else :
            print
"""
Your runtime beats 93.72% of python submissions
"""
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        dumb = ListNode(-1)
        p = dumb
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        
        p.next = l1 if l1 else l2
        return dumb.next


#Test Case start here
testcase = ListNode(1)
p = testcase
i = 2
while i < 7 :   
    q = ListNode(i)
    p.next = q
    p = p.next
    i += 2
testcase.disp()

testcase2 = ListNode(3)
p = testcase2
i = 5
while i < 10 :   
    q = ListNode(i)
    p.next = q
    p = p.next
    i += 2
testcase2.disp()

sln = Solution()
ans = sln.mergeTwoLists(testcase,testcase2)
ans.disp()