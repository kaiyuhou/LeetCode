# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 10:06:39 2015

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
            print ''

class Solution(object):
    def swapPairs(self, head):
        dump = ListNode(-1)
        dump.next = head
        
        p = dump
        while (p.next and p.next.next):
            q = p.next
            p.next = p.next.next
            q.next = p.next.next
            p.next.next = q
            p = p.next.next                
            
        return dump.next
        
testcase = ListNode(1)
p = testcase
i = 2
while i < 6 :   
    q = ListNode(i)
    p.next = q
    p = p.next
    i += 1

testcase.disp()
sln = Solution()
ans = sln.swapPairs(testcase)
ans.disp()