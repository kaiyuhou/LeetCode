# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 15:01:30 2015

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
    def isPalindrome(self, head):
        if head == None or head.next == None:
            return True
        
        #get the middle pointer        
        first = head
        second = head
        while second.next and second.next.next:
            first = first.next
            second = second.next.next
        
        #reverse the second half
        second = first.next
        first.next = None
        p = None
        while second.next:
            r = second.next
            second.next = p
            p = second
            second = r
        second.next = p
        
        #compare
        first = head
        while second:
            if second.val != first.val:
                return False
            first = first.next
            second = second.next
        return True
        
testcase = ListNode(1)
p = testcase
l = [2,3,3,2,1]
for i in l :   
    q = ListNode(i)
    p.next = q
    p = p.next
testcase.disp()

sln = Solution()

print sln.isPalindrome(testcase)