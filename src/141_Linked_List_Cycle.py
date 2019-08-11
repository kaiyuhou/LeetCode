# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution(object):
#     def __init__(self):
#         self.nodes = set()
#
#     def hasCycle(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         if head == None:
#             return False
#         if head.next in self.nodes:
#             return True
#         self.nodes.add(head)
#         return self.hasCycle(head.next)

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        one_step = head
        two_step = head
        while two_step.next and two_step.next.next:
            one_step = one_step.next
            two_step = two_step.next.next
            if one_step == two_step:
                return True
        return False



