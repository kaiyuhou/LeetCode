from Tree import *

# import collections
# class Solution:
#     def maxNumberOfBalloons(self, text: str) -> int:
#         C = collections.Counter(text)
#         return min(C['b'], C['a'], C['l'] // 2, C['o'] // 2, C['n'])
#
# s = Solution()
# text = "nlaebolko"
# text = "loonbalxballpoon"
# text = "leetcode"
# print(s.maxNumberOfBalloons(text))


# class Solution:
#     def reverseParentheses(self, s: str) -> str:
#         ans = []
#         left_bracket = []
#         index = 0
#         for c in s:
#             if c == '(':
#                 left_bracket.append(index)
#                 continue
#             if c == ')':
#                 pos = left_bracket.pop()
#                 T = list(ans[pos:])
#                 T.reverse()
#                 ans = ans[:pos] + T
#                 continue
#             ans.append(c)
#             index += 1
#         return ''.join(ans)
#
# s = Solution()
# c = "(abcd)"
# c = "a(bcdefghijkl(mno)p)q"
# c = "()"
# print(s.reverseParentheses(c))

# class Solution:
#     def kConcatenationMaxSum(self, arr, k: int) -> int:
#         N = len(arr)
#
#         def dp_K(A):
#             ans = 0
#             cur = 0
#             for a in A:
#                 cur += a
#                 ans = max(ans, cur)
#                 if cur < 0:
#                     cur = 0
#             return ans
#
#         def max_large(A):
#             ans = 0
#             cur = 0
#             for a in A:
#                 cur += a
#                 ans = max(ans, cur)
#             return ans
#
#
#
#         if k == 1:
#             return dp_K(arr)
#
#         arr_r = list(arr)
#         arr_r.reverse()
#         return max( sum(arr) * (k - 2), sum(arr) * (k - 2) + max_large(arr) + max_large(arr_r), dp_K(arr), max_large(arr) + max_large(arr_r)) % 1000000007
#
# s = Solution()
# arr = [1,2]
# k = 3
# arr = [1,-2,1,5]
# k = 3
# # arr = [-1,-2]
# # k = 7
# print(s.kConcatenationMaxSum(arr, k))

class Solution:
    def criticalConnections(self, n: int, connections):
        G = [[] for _ in range(n)]
        for x, y in connections:
            G[x].append(y)
            G[y].append(x)
        ans = []
        V = [False] * n
        dfsn = [-1] * n
        dfs_low = [-1] * n
        parent = [-1] * n
        cnt = [0]

        def dfs(cur):
            V[cur] = True
            dfsn[cur] = [cnt[0]]
            dfs_low[cur] = [cnt[0]]
            cnt[0] += 1

            for v in G[cur]:
                if V[v] == False:
                    parent[v] = cur
                    dfs(v)
                    dfs_low[cur] = min(dfs_low[cur], dfs_low[v])

                    if dfs_low[v] > dfsn[cur]:
                        ans.append([cur, v])
                elif v != parent[cur]:
                    dfs_low[cur] = min(dfs_low[cur], dfsn[v])

        dfs(0)
        return list(ans)

s = Solution()
n = 4
connections = [[0,1],[1,2],[2,0],[1,3]]
connections = [[0,1],[1,2],[2,3],[0,3]]
print(s.criticalConnections(n, connections))




























