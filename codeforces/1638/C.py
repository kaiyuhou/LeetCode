# Problem: C. Inversion Graph
# Contest: Codeforces - Codeforces Round #771 (Div. 2)
# URL: https://codeforces.com/contest/1638/problem/C
# Memory Limit: 256 MB
# Time Limit: 1000 ms
# 
# Powered by CP Editor (https://cpeditor.org)

import collections
import math
import bisect

from functools import lru_cache
from sys import stdin, stdout, setrecursionlimit

input = stdin.readline
# print = lambda s: stdout.write(str(s) + '\n')
# setrecursionlimit(100000)


def main():
    n = int(input())
    A = list(map(int, input().split()))

    
    min_arr = [0] * n
    last = n + 1
    for i in range(n - 1, -1, -1):
        if A[i] < last:
            last = A[i]
        min_arr[i] = last 
    
    
    ans = 0
    for i, a in enumerate(A):
        if i == 0:
            ans += 1
            max_before = a
        if max_before < a and min_arr[i] > max_before:
            ans += 1
        max_before = max(max_before, a)
            
    print(ans)
        
    


T = int(input())
for _ in range(T):
    main()