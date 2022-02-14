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


T = int(input())
for _ in range(T):
    main()