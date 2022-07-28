import collections
import heapq
from functools import lru_cache
from sys import stdin, stdout
input = stdin.readline
print = lambda s: stdout.write(str(s) + '\n')


def main():
    n = int(input())
    H = list(map(int, input().split()))
    
    G = collections.defaultdict(list)
    for i in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        G[u].append(v)
        G[v].append(u)
    
    root = H.index(max(H))
    
    dp = [-1] * n
    ans = 0
    stack = []
    
    for v in G[root]:
        stack.append((v, root))

    while stack:
        cur, pre = stack.pop()
        
        nxts = []
        for v in G[cur]:
            if v == pre:
                continue
            if dp[v] == -1:
                nxts.append(v)
        if nxts:
            stack.append((cur, pre))
            for nxt in nxts:
                stack.append((nxt, cur))
        else:
            mx = 0
            for v in G[cur]:
                if v == pre:
                    continue
                mx = max(mx, dp[v])
            diff = max(0, H[cur] - mx)
            ans += diff
            dp[cur] = mx + diff
    
    mx1, mx2 = 0, 0
    for v in G[root]:
        if dp[v] > mx1:
            mx2 = mx1 
            mx1 = dp[v]
        elif dp[v] > mx2:
            mx2 = dp[v]
    ans += max(0, H[root] - mx1) + max(0, H[root] - mx2)
    print(ans)
        
    # def dfs(u, p):
        # nonlocal ans
#         
        # mx1 = 0
        # mx2 = 0
#         
        # for v in G[u]:
            # if v != p:
                # cur = dfs(v, u)
                # if cur > mx1:
                    # cur, mx1 = mx1, cur
                # if cur > mx2:
                    # cur, mx2 = mx2, cur
        # if p != -1:
            # diff = max(0, H[u] - mx1)
            # ans += diff
            # mx1 += diff
        # else:
            # ans += max(0, H[u] - mx1) + max(0, H[u] - mx2)
#         
        # return mx1
#     
    # dfs(root, -1)        
    # print(ans)
        
main()
    

        
    
     