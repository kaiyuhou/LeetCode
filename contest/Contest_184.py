from typing import *
from Tree import *

# class Solution:
# #     def stringMatching(self, words: List[str]) -> List[str]:
# #         ans = []
# #         N = len(words)
# #         for i in range(N):
# #             for j in range(N):
# #                 if i == j:
# #                     continue
# #                 if words[i] in words[j]:
# #                     ans.append(words[i])
# #                     break
# #             else:
# #                 continue
# #         return ans
# #
# # s = Solution()
# # words = ["mass","as","hero","superhero"]
# # words = ["leetcoder","leetcode","od","hamlet","am"]
# # # words = ["blue", "green", "bu"]
# # print(s.stringMatching(words))

# class Solution:
#     def processQueries(self, queries: List[int], m: int) -> List[int]:
#         ans = []
#         A = [m - i for i in range(m)]
#         # print(A)
#         for q in queries:
#             ans.append(m - A.index(q) - 1)
#             A.remove(q)
#             A.append(q)
#             # print(A)
#         return ans
#
# s = Solution()
# queries = [3,1,2,1]
# m = 5
# queries = [4,1,2,2]
# m = 4
# queries = [7,5,5,8,3]
# m = 8
# print((s.processQueries(queries, m)))


# import re
# class Solution:
#     def entityParser(self, S: str) -> str:
#         S = re.sub(r'&quot;', '"', S)
#         S = re.sub(r'&apos;', "'", S)
#         S = re.sub(r'&amp;', '&', S)
#         S = re.sub(r'&gt;', '>', S)
#         S = re.sub(r'&lt;', '<', S)
#         S = re.sub(r'&frasl;', '/', S)
#         return S
#
# s = Solution()
# text = "and I quote: &quot;...&quot;"
# text = "x &gt; y &amp;&amp; x &lt; y is always false"
# text = "leetcode.com&frasl;problemset&frasl;all"
# print(s.entityParser(text))

class Solution:
    def numOfWays(self, n: int) -> int:
        dp = {"ABC": 6, "ABA": 6}
        for i in range(2, n + 1):
            newdp = {}
            newdp["ABC"] = 2 * dp["ABC"] + dp["ABA"] * 2
            newdp["ABA"] = dp["ABC"] * 2 + dp["ABA"] * 3
            dp = newdp
        return (dp["ABC"] + dp["ABA"]) % 1000000007

s = Solution()
print(s.numOfWays(1))





