# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 17:25:45 2015

@author: Mike
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
    def disp(self):
        print self.val
        print '->'
        if self.next :
            self.next.disp()

class Solution(object):
    """
    Your runtime beast 99.61% of python submissions.
    """
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        #find the num n node
        dumb = ListNode(-1)
        dumb.next = head
        p = head
        for i in range(0,n):
            p = p.next
        
        q = dumb
        
        while p:
            q = q.next
            p = p.next
        
        q.next = q.next.next
        
        return dumb.next

testcase = ListNode(1)
p = testcase
i = 2
while i < 6 :   
    q = ListNode(i)
    p.next = q
    p = p.next
    i += 1
#testcase.disp()

sln = Solution()
ans = sln.removeNthFromEnd(testcase,5)
ans.disp()