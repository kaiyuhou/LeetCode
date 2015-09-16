# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 14:44:50 2015

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
    Your runtime beats 100.00% of python submissions
    """
    def getListLen(self,head):
        p = head
        l = 0
        while p:
            l += 1
            p = p.next
        return l
    
    def getIntersectionNode(self, headA, headB):
        lenA = self.getListLen(headA)
        lenB = self.getListLen(headB)
        
        for i in range(0,lenA-lenB):
            headA = headA.next
        for i in range(0,lenB-lenA):
            headB = headB.next
        while not (headA == headB):
            headA = headA.next
            headB = headB.next
        return headA
        
        
testcase = ListNode(1)
p = testcase
i = 2
while i < 6 :   
    q = ListNode(i)
    p.next = q
    p = p.next
    i += 1
    
testcase2 = ListNode(1)
p = testcase2
i = 2
while i < 6 :   
    q = ListNode(i)
    p.next = q
    p = p.next
    i += 1
    
sln = Solution()
print sln.getIntersectionNode(testcase,testcase)