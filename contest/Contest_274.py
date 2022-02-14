from typing import *
from Tree import *

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



# class Solution:
#     def checkString(self, s: str) -> bool:
#         is_b = False
#         for c in s:
#             if c == 'b':
#                 is_b = True
#             else:
#                 if is_b:
#                     return False
#         return True

# import collections
# class Solution:
#     def numberOfBeams(self, bank: List[str]) -> int:
#         ans = 0
#         last = 0
#         for b in bank:
#             C = collections.Counter(b)
#             cur = C['1']
#             if cur > 0:
#                 ans += cur * last
#                 last = cur
#         return ans

# class Solution:
#     def asteroidsDestroyed(self, mass: int, A: List[int]) -> bool:
#         A.sort()
#         for a in A:
#             if a <= mass:
#                 mass += a
#             else:
#                 return False
#         return True


class Solution:
    def maximumInvitations(self, fa: List[int]) -> int:
        n = len(fa)
        max_loop = 0
        pair = []
        good_guy = set()
        visited = [False] * n
        bros = [0] * n

        for start in range(n):
            if visited[start]:
                continue

            path = []
            cur = start
            bro = 0

            while not visited[fa[cur]]: # new item
                # print(cur)
                # print(visited)

                nxt = fa[cur]
                visited[cur] = True
                path.append(cur)

                if fa[nxt] == cur:
                    pair.append((cur, nxt))
                    bros[cur] = bro
                    bros[nxt] = bro

                    visited[nxt] = True
                    path.append(nxt)
                    good_guy |= set(path)
                    break
                else:
                    bro += 1
                    cur = nxt
            else:
                visited[cur] = True
                path.append(cur)
                nxt = fa[cur]
                if nxt in good_guy:
                    good_guy |= set(path)
                else:
                    if nxt in path:
                        nxt_index = path.index(nxt)
                        loop_len = len(path) - nxt_index
                        max_loop = max(loop_len, max_loop)

        follower = [[] for _ in range(n)]
        for i in range(n):
            follower[fa[i]].append(i)

        def longest_len(node):
            if len(follower[node]) == 0:
                return 1
            else:
                lpath = 0
                for f in follower[node]:
                    lpath = max(lpath, longest_len(f))
                return 1 + lpath

        ans = 0
        for a, b in pair:
            follower[a].remove(b)
            follower[b].remove(a)
            ans += longest_len(a) + longest_len(b)

        # print(pair, max_loop)

        return max(ans, max_loop)

s = Solution()
favorite = [2,2,1,2]
# favorite = [1,2,0]
favorite = [3,0,1,4,1]
print(s.maximumInvitations(favorite))































