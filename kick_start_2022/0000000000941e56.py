from functools import lru_cache
from sys import stdin, stdout, setrecursionlimit
import heapq

input = stdin.readline

def main(case):
    n = int(input())
    A = list(map(int, input().split()))
    
    q = []
    ans = [0] * n
    cur = 0
    for i, a in enumerate(A):
        if a <= cur:
            ans[i] = cur
        else:
            while q and q[0] <= cur:
                heapq.heappop(q)
            heapq.heappush(q, a)
            if len(q) > cur:
                cur += 1
            ans[i] = cur
    print(f'Case #{case + 1}: ', end='')
    print(*ans)
    


T = int(input())
for t in range(T):
    main(t)