from typing import  *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists is None or len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        elif len(lists) == 2:
            head = ListNode(-1)
            cur = head
            p = lists[0]
            q = lists[1]
            while p and q:
                if p.val < q.val:
                    cur.next = p
                    p = p.next
                else:
                    cur.next = q
                    q = q.next
                cur = cur.next
            if p:
                cur.next = p
            if q:
                cur.next = q
            return head.next
        else:
            return self.mergeKLists([self.mergeKLists(lists[:len(lists)//2]),
                                     self.mergeKLists(lists[len(lists)//2:])])
















