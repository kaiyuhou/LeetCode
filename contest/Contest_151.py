from Tree import *

# class Solution:
#     def invalidTransactions(self, transactions):
#         T = {}
#         ans = set()
#         for t in transactions:
#             name, time, amount, city = t.split(',')
#             time = int(time)
#             if name not in T.keys():
#                 T[name] = [False for _ in range(1005)]
#             T[name][time] = city
#             if int(amount) > 1000:
#                 ans.add(t)
#
#         for t in transactions:
#             name, time, amount, city = t.split(',')
#             time = int(time)
#             for tt in range(max(0, time - 60), min(time + 61, 1001)):
#                 if T[name][tt] != False and T[name][tt] != city:
#                     ans.add(t)
#
#         return list(ans)
#
# s = Solution()
# # transactions = ["alice,111,800,mtv","alice,50,100,beijing"]
# transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
# transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
# print(s.invalidTransactions(transactions))

# class Solution:
#     def numSmallerByFrequency(self, queries, words):
#
#         def f(S: str):
#             c = min(S)
#             return S.count(c)
#
#         A = []
#         for w in words:
#             A.append((f(w)))
#         A.sort()
#
#         import bisect
#         ans = []
#         for q in queries:
#             num = f(q)
#             ans.append(len(A) - bisect.bisect_right(A, num))
#         return ans
#
# s = Solution()
# queries = ["cbd"]
# words = ["zaaaz"]
# # queries = ["bbb","cc", "a"]
# # words = ["a","aaa","aaaa"]
# print(s.numSmallerByFrequency(queries, words))


# class Solution:
#     def removeZeroSumSublists(self, head: ListNode) -> ListNode:
#         sum = 0
#         dp = {}
#         nav = ListNode(-1)
#         nav.next = head
#         dp[0] = nav
#
#         cur = head
#         while cur != None:
#             sum += cur.val
#             if sum in dp.keys():
#                 dp[sum].next = cur.next
#             else:
#                 dp[sum] = cur
#             cur = cur.next
#
#         return nav.next
#
# s = Solution()


from heapq import *
class DinnerPlates:

    def __init__(self, capacity: int):
        self.H = []
        self.C = capacity
        self.M = {}
        for i in range(100005):
            self.M[i] = []

        self.Right = -1
        heapify(self.H)

    def print(self):
        for i in range(5):
            print(self.M[i], end=',')
        print()

    def push(self, val: int) -> None:
        # self.print()

        if len(self.H) == 0:
            self.Right += 1
            heappush(self.H, (self.Right, self.C))
            self.M[self.Right] = []

        index, remain = heappop(self.H)
        if index > self.Right:
            self.H = []
            self.Right += 1
            index = self.Right
            remain = self.C

        self.M[index].append(val)
        if remain > 1:
            heappush(self.H, (index, remain - 1))

    def pop(self) -> int:
        # self.print()

        while self.Right != -1 and len(self.M[self.Right]) == 0:
            self.Right -= 1
        if self.Right == -1:
            return -1

        ans = self.M[self.Right].pop()
        while self.Right != -1 and len(self.M[self.Right]) == 0:
            self.Right -= 1
        return ans

    def popAtStack(self, index: int) -> int:
        # self.print()

        if len(self.M[index]) == 0:
            return -1

        ans = self.M[index].pop()
        while self.Right != -1 and len(self.M[self.Right]) == 0:
            self.Right -= 1
        if index <= self.Right:
            heappush(self.H, (index, 1))
        return ans


s = DinnerPlates(2)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
print(s.popAtStack(0))
s.push(20)
s.push(21)
print(s.popAtStack(1))
print(s.popAtStack(1))
print(s.pop())
print(s.pop())
# s.push(100)
print(s.pop())
print(s.pop())
print(s.pop())









