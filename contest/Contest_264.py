from typing import *
from Tree import *


# class Solution:
#     def countValidWords(self, sentence: str) -> int:
#         words = sentence.strip().split(' ')
#         ans = 0
#         for w in words:
#             if w == ' ' or not w:
#                 continue
#             flag = False
#             for i, c in enumerate(w):
#                 if c.islower():
#                     continue
#                 if c.isdigit():
#                     break
#                 if c == '-':
#                     if flag:
#                         break
#                     if i == 0 or i == len(w) - 1:
#                         break
#                     if w[i-1].islower() and w[i+1].islower():
#                         flag = True
#                         continue
#                     break
#                 else:
#                     if i == len(w) - 1:
#                         continue
#                     break
#             else:
#                 # print(w)
#                 ans += 1
#         return ans
#
# s = Solution()
# sentence = "cat and  dog"
# sentence = "!this  1-s b8d!"
# sentence = "alice and  bob are playing stone-game10"
# sentence = "he bought 2 pencils, 3 erasers, and 1  pencil-sharpener."
# # sentence = 'a-b-c'
# print(s.countValidWords(sentence))

# from collections import Counter
# class Solution:
#     def nextBeautifulNumber(self, n: int) -> int:
#         def isgood(num):
#             c = Counter(str(num))
#             for k, v in c.items():
#                 if int(k) != v:
#                     return False
#             return True
#
#         for i in range(n + 1, 10**6):
#             if isgood(i):
#                 return i
#
#         return 1224444
#
# s = Solution()
# n = 1
# n = 1000
# n = 3000
# n = 10 ** 5
# n = 122333
# print(s.nextBeautifulNumber(n))

# class Solution:
#     def countHighestScoreNodes(self, parents: List[int]) -> int:
#         n = len(parents)
#
#         ch = {i: [] for i in range(n)}
#         for i, p in enumerate(parents):
#             if p == -1:
#                 continue
#             ch[p].append(i)
#
#         stack = []
#         for i in range(n):
#             if not ch[i]:
#                 stack.append(i)
#
#         cnt = [-1 for i in range(n)]
#
#         ans = [1, 0]
#
#         while stack:
#             cur = stack.pop(0)
#             cur_ans = 1
#             chs = 0
#
#             for lr in ch[cur]:
#                 cur_ch = cnt[lr]
#                 cur_ans *= cur_ch
#                 chs += cur_ch
#
#             rest = n - chs - 1
#             if rest != 0:
#                 cur_ans *= rest
#
#             if cur_ans == ans[0]:
#                 ans[1] += 1
#             elif cur_ans > ans[0]:
#                 ans = [cur_ans, 1]
#
#             cnt[cur] = chs + 1
#
#             if cur == 0:
#                 continue
#             else:
#                 for lr in ch[parents[cur]]:
#                     if cnt[lr] == -1:
#                         break
#                 else:
#                     stack.append(parents[cur])
#
#
#         # print(ch)
#
#         # def dfs(root):
#         #     nonlocal ans
#         #
#         #     cur_ans = 1
#         #     chs = 0
#         #
#         #     for lr in ch[root]:
#         #         cur_ch = dfs(lr)
#         #         if cur_ch != 0:
#         #             cur_ans *= cur_ch
#         #             chs += cur_ch
#         #
#         #     rest = n - chs - 1
#         #     if rest != 0:
#         #         cur_ans *= rest
#         #
#         #     if cur_ans == ans[0]:
#         #         ans[1] += 1
#         #     elif cur_ans > ans[0]:
#         #         ans = [cur_ans, 1]
#         #
#         #     # print(root, chs)
#         #
#         #     return chs + 1
#         #
#         # dfs(0)
#         return ans[1]
#
#
# s = Solution()
# # parents = [-1,2,0,2,0]
# parents = [-1,2,0]
# parents = [i - 1 for i in range(10 ** 5)]
# print(s.countHighestScoreNodes(parents))


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:

        pres = {i: [] for i in range(n)}
        nxts = {i: [] for i in range(n)}

        for pre, nxt in relations:
            pre -= 1
            nxt -= 1
            pres[nxt].append(pre)
            nxts[pre].append(nxt)

        needs = [len(pres[i]) for i in range(n)]

        ans = [-1 for _ in range(n)]
        stack = []

        for i in range(n):
            if needs[i] == 0:
                stack.append(i)

        while stack:
            cur = stack.pop(0)
            before = 0
            for pre in pres[cur]:
                before = max(before, ans[pre])
            ans[cur] = before + time[cur]
            for nxt in nxts[cur]:
                needs[nxt] -= 1
                if needs[nxt] == 0:
                    stack.append(nxt)
        return max(ans)

n = 3
relations = [[1,3],[2,3]]
time = [3,2,5]

n = 5
relations = [[1,5],[2,5],[3,5],[3,4],[4,5]]
time = [1,2,3,4,5]

n = 5 * (10 ** 4)
relations = [[i + 1, i + 2] for i in range(n - 1)]
time = [1 for i in range(n)]

s = Solution()
print(s.minimumTime(n, relations, time))

















































































