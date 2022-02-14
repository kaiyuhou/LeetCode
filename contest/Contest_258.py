from typing import *
from Tree import *

# class Solution:
#     def reversePrefix(self, word: str, ch: str) -> str:
#         if ch not in word:
#             return  word
#         index = word.index(ch)
#         s = word[:index + 1]
#         p = word[index+1:]
#         return s[::-1] + p
#
#
#
#
# s = Solution()
# word = "abcdefd"
# ch = "d"
# word = "xyxzxe"
# ch = "z"
# word = "abcd"
# ch = "z"
# print(s.reversePrefix(word, ch))

# import math
# import collections
#
# class Solution:
#     def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
#         ratio = collections.Counter()
#         for w, h in rectangles:
#             cd = math.gcd(w, h)
#             ratio[(w // cd, h // cd)] += 1
#
#         ans = 0
#         for cnt in ratio.values():
#             ans += (cnt * (cnt - 1)) // 2
#
#         return ans
#
# s = Solution()
# rectangles = [[4,8],[3,6],[10,20],[15,30]]
# rectangles = [[4,5],[7,8]]
#
# print(s.interchangeableRectangles(rectangles))

# class Solution:
#     def maxProduct(self, s: str) -> int:
#         best = 0
#         n = len(s)
#         visited = set()
#
#         def dfs(i, a, b):
#             nonlocal best
#
#             if (i, a, b) in visited or (i, b, a) in visited:
#                 return
#             visited.add((i, a, b))
#
#             if a and b and a == a[::-1] and b == b[::-1]:
#                 best = max(best, len(a) * len(b))
#
#             if i >= n:
#                 return
#
#             # if (len(a) + (n + 1 - i) // 2) * (len(b) + (n + 1 - i) // 2) <= best:
#             #     return
#
#             dfs(i + 1, a + s[i], b)
#             dfs(i + 1, a, b + s[i])
#             dfs(i + 1, a, b)
#
#         dfs(0, '', '')
#         return best
#
#
# ss = Solution()
# s = "leetcodecom"
# s = "bb"
# s = "accbcaxxcxx"
# s = "xoriroix"
# print(ss.maxProduct(s))

import collections
import queue

class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        n = len(parents)
        ans = [0] * n
        ch = collections.defaultdict(list)
        for c, p in enumerate(parents):
            if c == 0:
                continue
            ch[p].append(c)

        sets = {}

        stack = []
        # leaf_stack = collections.deque()
        stack.append(0)

        visited = set()

        while stack:
            i = len(stack) - 1
            if stack[i] in visited:
                break
            while i >= 0 and stack[i] not in visited:
                cur = stack[i]
                visited.add(cur)
                for c in ch[cur]:
                    stack.append(c)
                i -= 1

        # print(stack)

        for i in range(n - 1, -1, -1):
            cur = stack[i]

            cur_ans = 1
            cur_set = {nums[cur]}
            for c in ch[cur]:
                cur_ans = max(ans[c], cur_ans)
                cur_set |= sets[c]
                sets[c] = None

            while cur_ans in cur_set:
                cur_ans += 1

            ans[cur] = cur_ans
            sets[cur] = cur_set

        return ans

        # def dfs(root):
        #     # print(root)
        #     if not ch[root]:
        #         ans[root] = 1 if nums[root] != 1 else 2
        #         return ans[root], {nums[root]}
        #
        #     cur_ans = 0
        #     cur_set = set()
        #     for c in ch[root]:
        #         c_ans, c_set = dfs(c)
        #         cur_ans = max(cur_ans, c_ans)
        #         cur_set |= c_set
        #
        #     cur_set.add(nums[root])
        #
        #     while cur_ans in cur_set:
        #         cur_ans += 1
        #     ans[root] = cur_ans
        #     return cur_ans, cur_set
        #
        # dfs(0)
        # return ans

s = Solution()
# parents = [-1,0,0,2]
# nums = [1,2,3,4]
# parents = [-1,0,1,0,3,3]
# nums = [5,4,6,2,1,3]
# parents = [-1,2,3,0,2,4,1]
# nums = [2,3,4,5,6,7,8]
parents = [-1,0,0,0,2]
nums = [6,4,3,2,1]
# parents = [-1,2,0,1,0]
# nums = [3,4,2,1,5]

print(len(parents))
print(s.smallestMissingValueSubtree(parents, nums))


































































