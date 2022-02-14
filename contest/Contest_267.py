from typing import *
from Tree import *


# class Solution:
#     def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
#         ans = 0
#         cur = 0
#         while tickets[k] != 0:
#             if tickets[cur] != 0:
#                 tickets[cur] -= 1
#                 ans += 1
#             cur = (cur + 1) % len(tickets)
#         return ans
#
# s = Solution()
# tickets = [2,3,2]
# k = 2
# tickets = [5,1,1,1]
# k = 0
# tickets = [100] * 100
# k = 99
#
# print(s.timeRequiredToBuy(tickets,k))

# class Solution:
#     def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head:
#             return head
#
#         level = 1
#         last = ListNode(-1, head)
#
#         while last.next:
#             cur = last
#             seq = []
#             for _ in range(level):
#                 if cur.next:
#                     seq.append(cur.next.val)
#                     cur = cur.next
#
#             cur = last
#             # print(seq)
#             if len(seq) % 2 == 0:
#                 for _ in range(level):
#                     if cur.next:
#                         cur.next.val = seq.pop(-1)
#                         cur = cur.next
#             else:
#                 for _ in range(level):
#                     if cur.next:
#                         cur = cur.next
#             last = cur
#
#             level += 1
#         return head
#
#
# s = Solution()
# list = array_to_list([5,2,6,3,9,1,7,3,8,4])
# list = array_to_list([0,4,2,1,3])
# print(list_to_array(s.reverseEvenLengthGroups(list)))


# class Solution:
#     def decodeCiphertext(self, encodedText: str, rows: int) -> str:
#         if not encodedText:
#             return ''
#
#         NM = len(encodedText)
#         N = rows
#         M = NM // N
#         ans = []
#         for i in range(0, M):
#             for j in range(N):
#                 if j * M + i + j < NM:
#                     ans.append(encodedText[j * M + i + j])
#         while ans[-1] == ' ':
#             ans.pop(-1)
#         return ''.join(ans)
#
# s = Solution()
# encodedText = "ch   ie   pr"
# rows = 3
#
# # encodedText = "iveo    eed   l te   olc"
# # rows = 4
# encodedText = "coding"
# rows = 1
#
# encodedText = " b  ac"
# rows = 2
#
# print(s.decodeCiphertext(encodedText, rows))


class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, u):
        if u != self.parent.setdefault(u, u):
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu != pv:
            self.parent[pu] = pv

class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        uf = UnionFind()
        cur_res = set()
        for a, b in restrictions:
            cur_res.add((a, b))

        def update_res(new, old):
            nonlocal cur_res

            new_res = set()
            for a, b in cur_res:
                a = new if a == old else a
                b = new if b == old else b
                new_res.add((a, b))
            cur_res = new_res

        ans = []
        for a, b in requests:
            root_a = uf.find(a)
            root_b = uf.find(b)
            if root_a == root_b:
                ans.append(True)
                update_res(root_a, a)
                update_res(root_b, b)
            else:
                if (root_a, root_b) in cur_res or (root_b, root_a) in cur_res:
                    ans.append(False)
                else:
                    ans.append(True)
                    uf.union(root_a, root_b)
                    update_res(root_b, root_a)

        return ans



s = Solution()
n = 3
restrictions = [[0,1]]
requests = [[0,2],[2,1]]

n = 3
restrictions = [[0,1]]
requests = [[1,2],[0,2]]

n = 5
restrictions = [[0,1],[1,2],[2,3]]
requests = [[0,4],[1,2],[3,1],[3,4]]


print(s.friendRequests(n, restrictions, requests))


































































