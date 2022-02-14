# Problem: A. Reverse
# Contest: Codeforces - Codeforces Round #771 (Div. 2)
# URL: https://codeforces.com/contest/1638/problem/0
# Memory Limit: 256 MB
# Time Limit: 1000 ms
# 
# Powered by CP Editor (https://cpeditor.org)

import collections
import math

from functools import lru_cache
from sys import stdin, stdout, setrecursionlimit

input = stdin.readline
# print = lambda s: stdout.write(str(s) + '\n')
# setrecursionlimit(100000)


def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = sorted(A)
    for i, b in enumerate(B):
        if b != A[i]:
            break
    C = A[i:]
    idx = C.index(min(C))
    D = A[:i] + C[:idx + 1][::-1] + C[idx + 1:]
    print(*D)


T = int(input())
for _ in range(T):
    main()