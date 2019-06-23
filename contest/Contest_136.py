from Tree import *

# class Solution:
#     def isRobotBounded(self, instructions: str) -> bool:
#         ans = set()
#         ans.add((0, 1))
#         next = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#         x, y, f = 0, 0, 0
#         inss = instructions * 100
#
#         for c in inss:
#             if c == 'G':
#                 x += next[f][0]
#                 y += next[f][1]
#                 ans.add((x, y))
#             elif c == 'L':
#                 f = (f - 1) % 4
#             else:
#                 f = (f + 1) % 4
#
#         for c in instructions:
#             if c == 'G':
#                 x += next[f][0]
#                 y += next[f][1]
#                 if (x, y) not in ans:
#                     return False
#             elif c == 'L':
#                 f = (f - 1) % 4
#             else:
#                 f = (f + 1) % 4
#
#         return True
#
# s = Solution()
# # ins = "GGLLGG"
# ins = "GL"
# print(s.isRobotBounded(ins))


# class Solution:
#     def gardenNoAdj(self, N: int, paths):
#         ans = [-1 for _ in range(N)]
#         nb = [[] for _ in range(N)]
#         possible = set()
#         possible.add(1)
#         possible.add(2)
#         possible.add(3)
#         possible.add(4)
#
#         for x, y in paths:
#             nb[x - 1].append(y - 1)
#             nb[y - 1].append(x - 1)
#
#         for i in range(N):
#             if ans[i] != -1:
#                 continue
#
#             if len(nb[i]) != 3:
#                 continue
#
#             used = set()
#             for j in nb[i]:
#                 used.add(ans[j])
#
#             a = possible - used
#             ans[i] = a.pop()
#
#             k = 0
#             while k < 3:
#                 if ans[nb[i][k]] != -1:
#                     k += 1
#                     continue
#
#                 ans[nb[i][k]] = a.pop()
#                 k += 1
#
#             # print(i, ans)
#
#         # print(ans)
#         for  i in range(N):
#             if ans[i] == -1 or len(nb[i]) != 2:
#                 continue
#
#             if ans[i] == ans[nb[i][0]] or ans[i] == ans[nb[i][1]]:
#                 used = set()
#                 used.add(ans[nb[i][0]])
#                 used.add(ans[nb[i][1]])
#                 a = possible - used
#                 ans[i] = a.pop()
#
#
#
#         for i, color in enumerate(ans):
#             if color != -1:
#                 continue
#
#             used = set()
#             for n in nb[i]:
#                 used.add(ans[n])
#             a = possible - used
#             ans[i] = a.pop()
#
#
#
#         return ans
#
#
#
# s = Solution()
# # N = 3
# # paths = [[1,2],[2,3],[3,1]]
# # N = 4
# # paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
# # N = 4
# # paths = [[1,2],[3,4]]
# N = 7
# paths = [[7,4],[4,2],[3,4],[5,1],[6,1],[2,6],[3,5],[1,3]]
# print(s.gardenNoAdj(N, paths))

import functools
class Solution:
    def maxSumAfterPartitioning(self, A, K: int) -> int:
        @functools.lru_cache(None)
        def dfs(A):
            n = len(A)
            if n <= K:
                return len(A) * max(A)

            ans = 0
            for i in range(n - 1, n - K - 1, -1):
                ans_cur = dfs(A[:i]) + dfs(A[i:])
                ans = max(ans, ans_cur)
            return ans

        return dfs(tuple(A))

s = Solution()
# A = [1,15,7,9,2,5,10]
# K = 3
# A = [987891,24022,127293,443921,201905,874309,829836,408396,500433,427773,629636,238769,584348,478161,773230,306581,540898,665495,971056,629207,77931,619588,655449,194336,497563,313629,922943,421165,160085,119677,870552,173493,664533,7626,922606,800318,461240,343155,880003,971474,855479,182549,449349,850466,884375,693559,914711,148472,424680,552914,253701,668874,963579,819525,709389,519033,352618,928423,116554,206548,817727,878399,851845,338365,318078,354919,872750,697127,204952,45554,408328,508941,292156,336407,841024,156523,649914,942053,791485,298447,869199,350997,41816,470130,172621,935903,18077,463195,254539,367201,225252,473046,764785,88727,293126,813292,860862,147721,171094,763304,224485,476494,886137,621957,599342,623266,165179,442399,284246,762913,439667,686578,20403,504730,998778,31916,654909,239492,120047,127128,600877,275927,711781,5253,912621,395524,445839,68920,354591,605073,763447,61628,402733,737575,698793,167812,677047,567019,752965,912146,897323,784801,161720,535888,833658,342947,227271,97869,407473,660080,964842,789796,11752,439783,2234,822060,561500,278069,585446,189192,319631,516917,127900,559661,477043,516550,504672,496732,298204,561021,313204,420717,724973,726497,911217,349328,559732,950263,225500,794178,327264,632657,229835,176193,615558,964834,940201,695202,417769,294514,127311,667749,983485,531843,138178,410083,541070,641800,910494,632547,738996,788159,161208,798711,845439,461196,780036,161288,261492,193428]
# K = 85
A = [1,15,7,9,2,5,10]
K = 3
# A = [10, 9 ,3, 2]
# K = 2
print(s.maxSumAfterPartitioning(A, K))