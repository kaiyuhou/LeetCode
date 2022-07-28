# Problem: A. Min Or Sum
# Contest: Codeforces - Codeforces Round #772 (Div. 2)
# URL: https://codeforces.com/contest/1635/problem/0
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
    ans = set()
    for a in A:
        for i in range(31):
            if (1 << i) & a:
                ans.add(i)
    ret = 0
    for a in ans:
        ret += (1 << a)
    print(ret) 



T = int(input())
for _ in range(T):
    main()