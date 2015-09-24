# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 09:16:05 2015

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
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        
        p = None
        q = head
        while q.next:
            r = q.next
            q.next = p
            p = q
            q = r
        q.next = p
        return q

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
ans = sln.reverseList(testcase)
ans.disp()