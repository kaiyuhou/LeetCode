# -*- coding: utf-8 -*-
"""
Created on Fri Oct 09 11:11:53 2015

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
    def addTwoNumbers(self, l1, l2):
        """
        Your runtime beats 99.55% of python submissions
        """
        p = l1
        q = l2
        bp = None
        m = 0
        while p and q:
            p.val = p.val + q.val + m
            m = p.val / 10
            p.val %= 10
            bp = p
            p = p.next
            q = q.next
        if q:
            bp.next = q
            p = q
        while p:
            p.val = p.val + m
            m = p.val / 10
            p.val %= 10
            bp =p
            p = p.next

        if m > 0:
            bp.next = ListNode(m)
        return l1

testcase = ListNode(1)
p = testcase
i = 2
while i < 6 :   
    q = ListNode(i)
    p.next = q
    p = p.next
    i += 1
testcase.disp()

testcase2 = ListNode(9)
p = testcase2
i = 2
while i < 3 :   
    q = ListNode(i)
    p.next = q
    p = p.next
    i += 1
testcase2.disp()

sln = Solution()
ans = sln.addTwoNumbers(testcase,testcase2)
ans.disp()
        