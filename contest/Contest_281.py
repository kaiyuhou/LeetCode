from typing import *
from collections import *
from math import *

from Tree import *

def get_mask(word):
    return sum(1 << (ord(c) - ord("a")) for c in word)


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.weight = [1 for _ in range(n)]

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu != pv:
            if self.weight[pu] < self.weight[pv]:
                self.parent[pu] = pv
                self.weight[pv] = self.weight[pu] + self.weight[pv]
            else:
                self.parent[pv] = pu
                self.weight[pu] = self.weight[pu] + self.weight[pv]


# class Solution:
#     def countEven(self, num: int) -> int:
#         ans = 0
#         for i in range(1, num + 1):
#             cur = 0
#             for c in str(i):
#                 cur += int(c)
#             if cur % 2 == 0:
#                 ans += 1
#         return ans

# class Solution:
#     def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         ans = None
#         p = None
#         cur = 0
#         while head.next:
#             head = head.next
#             if head.val == 0:
#                 if not ans:
#                     ans = ListNode(cur)
#                     p = ans
#                 else:
#                     p.next = ListNode(cur)
#                     p = p.next
#                 cur = 0
#             else:
#                 cur += head.val
#         return ans



# class Solution:
#     def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
#         C = Counter(s)
#         A = list(C.keys())
#         A.sort(reverse=True)
#         ans = ''
#         last = ''
#         while len(A) > 1:
#             if last and last == A[0]:
#                 cur_rep = repeatLimit - 1
#             else:
#                 cur_rep = repeatLimit
#
#             ans += A[0] * min(cur_rep, C[A[0]])
#             ans += A[1]
#             last = A[1]
#
#             C[A[0]] -= min(cur_rep, C[A[0]])
#             C[A[1]] -= 1
#             if C[A[1]] == 0:
#                 A.pop(1)
#             if C[A[0]] == 0:
#                 A.pop(0)
#
#             # print(ans, A)
#
#         if len(A) == 1:
#             if last and last == A[0]:
#                 cur_rep = repeatLimit - 1
#             else:
#                 cur_rep = repeatLimit
#
#             ans += A[0] * min(cur_rep, C[A[0]])
#         return ans
#
# s = Solution()
# ss = "robnsdvpuxbapuqgopqvxdrchivlifeepy"
# re = 2
#
# print(s.repeatLimitedString(ss, re))


# ans = [0] * (10 ** 5 + 1)
# for i in range(2, 10 ** 5 + 1):
#     if ans[i] == 0:
#         nxt = i * 2
#         while nxt < 10 ** 5 + 1:
#             ans[nxt] = 1
#             nxt += i
#
# A = []
# for i in range(2, 10 ** 5 + 1):
#     if ans[i] == 0:
#         A.append(i)
#
# print(len(A))
# print(A)

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        Rs = []
        for i in range(1, k + 1):
            if k % i == 0:
                Rs.append(i)
    #
    #     ans = 0
    #     dp = defaultdict(int)
    #     for a in nums:
    #         G = gcd(a, k)
    #         r = k // G
    #         ans += dp[r]
    #         for r in Rs:
    #             if a % r == 0:
    #                 dp[r] += 1
    #     return ans

        # B = [[1] for _ in range(10 ** 5 + 1)]
        # for i in range(2, k + 1):

        B = [[] for _ in range(10 ** 5 + 1)]
        for i in Rs:
            cur = i
            while cur < 10 ** 5 + 1:
                B[cur].append(i)
                cur += i

        dp = defaultdict(int)
        ans = 0

        for a in nums:
            G = gcd(a, k)
            R = k // G
            ans += dp[R]
            # print(a, B[a])
            for part in B[a]:
                dp[part] += 1
            # print(dp)
        return ans



s = Solution()
nums = [1,2,3,4,5]
k = 2
nums = [3,2,6,1,8,4,1]
k = 3
# nums = [263,356,613,402,936,19,658,629,964,775,190,536,457,316,585,659,718,156,364,403,412,867,205,547,241,809,80,865,38,657,161,392,566,699,852,256,799,453,35,257,56,649,982,774,9,540,911,731,779,8,829,874,774,690,140,429,398,218,81,196,124,104,418,732,707,700,202,591,226,191,534,711,409,189,174,392,968,140,551,916,183,875,818,479,488,642,672,455,669,914,831,24,91,229,836,686,407,930,256,507,629,329,795,950,880,431,932,783,437,318,663,403,2,145,313,200,650,257,515,469,407,537,312,35,717,528,443,154,837,777,537,880,484,635,955,468,769,1000,325,194,973,19,581,873,364,570,547,648,290,286,251,256,783,330,151,582,960,853,965,130,132,256,201,379,147,187,414,172,5,880,303,344,741,1,260,975,406,245,737,323,272,88,893,138,904,210,152,363,177,228,134,456,760,602,80,764,382,918,305,5,684,845,462,215,406,773,595,719,589,990,694,39,986,512,264,413,51,902,582,15,266,421,358,90,735,201,998,100,32,833,709,337,647,739,579,216,382,901,792,857,793,549,375,280,788,26,697,683,6,281,147,34,214,661,334,882,535,920,164,761,728,950,456,369,270,748,142,140,215,36,850,451,980,275,971,467,49,775,888,77,26,659,410,521,362,350,250,991,104,80,75,766,228,458,857,229,243,866,427,930,780,592,269,859,896,415,858,562,803,629,306,193,643,859,684,222,468,809,236,437,353,907,376,265,721,987,265,528,446,848,560,747,421,499,1000,941,158,167,976,868,121,412,104,487,29,909,519,30,193,338,311,355,121,132,175,800,700,282,71,113,472,381,491,384,520,32,881,597,174,262,421,576,433,172,236,926,25,920,645,227,154,860,603,558,605,164,667,950,607,883,921,516,859,817,965,56,178,927,258,69,710,361,408,996,962,385,704,888,365,737,216,673,855,442,701,393,973,515,179,135,808,441,472,143,39,624,253,632,722,810,191,312,671,274,466,121,382,294,749,455,818,325,212,506,896,504,785,389,81,747,106,531,270,105,941,489,479,976,511,133,435,518,340,40,394,959,368,745,659,589,964,998,157,686,374,950,799,750,142,783,952,271,928,312,606,335,396,336,365,108,261,623,556,579,133,74,734,569,341,610,30,696,773,274,68,953,502,578,637,625,21,884,560,685,462,992,448,892,73,606,116,26,802,671,946,313,6,56,146,600,388,724,643,243,414,30,832,284,254,187,847,513,791,916,30,52,368,760,183,675,591,616,962,148,456,524,345,368,134,290,546,154,291,973,446,776,23,442,848,428,280,544,25,462,412,233,386,753,444,920,784,883,752,441,973,826,27,514,744,26,310,8,583,881,935,36,907,67,624,80,696,869,579,852,165,525,773,772,349,708,23,677,565,683,14,167,71,103,313,870,856,25,272,112,681,670,95,128,304,127,497,775,966,579,549,752,919,648,321,807,77,3,838,912,535,473,898,495,735,956,170,295,276,714,758,5,221,944,973,389,214,601,443,231,713,676,276,40,152,864,224,320,317,16,181,470,467,736,59,476,822,321,973,92,348,641,717,205,392,583,537,489,460,759]
# k = 729
# nums = [100000,100000]
# k = 100000
print(s.countPairs(nums, k))
































