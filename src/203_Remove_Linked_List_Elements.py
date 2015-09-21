# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 17:26:19 2015

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
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dumb = ListNode(-1)
        dumb.next = head
        p = dumb        
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return dumb.next
        
testcase = ListNode(1)
#p = testcase
#i = 1
#while i < 2 :   
#    q = ListNode(i)
#    p.next = q
#    p = p.next
#    i += 1
#testcase.disp()

sln = Solution()
ans = sln.removeElements(testcase, 1)
#ans.disp()