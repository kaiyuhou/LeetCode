# Problem: B. Odd Swap Sort
# Contest: Codeforces - Codeforces Round #771 (Div. 2)
# URL: https://codeforces.com/contest/1638/problem/B
# Memory Limit: 256 MB
# Time Limit: 1000 ms
# 
# Powered by CP Editor (https://cpeditor.org)

import collections
import math

from functools import lru_cache
from sys import stdin, stdout, setrecursionlimit

input = stdin.readline
print = lambda s: stdout.write(str(s) + '\n')
# setrecursionlimit(100000)


def main():
    n = int(input())
    A = list(map(int, input().split()))
    odd = []
    even = []
    for a in A:
        if a % 2 == 1:
            odd.append(a)
        else:
            even.append(a)
    if odd == sorted(odd) and even == sorted(even):
        print('Yes')
    else:
        print('No')
    


T = int(input())
for _ in range(T):
    main()