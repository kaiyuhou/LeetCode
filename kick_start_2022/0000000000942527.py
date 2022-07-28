# Problem: Hex
# Contest: Google Coding Competitions - Coding Practice with Kick Start Session #1 - Kick Start 2022
# URL: https://codingcompetitions.withgoogle.com/kickstart/round/00000000008f4332/0000000000942527
# Memory Limit: 1024 MB
# Time Limit: 30000 ms
# 
# Powered by CP Editor (https://cpeditor.org)

import collections
import math

from functools import lru_cache
from sys import stdin, stdout, setrecursionlimit

input = stdin.readline

# print = lambda s: stdout.write(str(s) + '\n')
# setrecursionlimit(100000)



# impossible:
# A win and cnt B > A
# Nobody and max(A, B) - min(A, B) > 1
# # This cannot be the case: A win and B win
# A win and has two pathes with not shared node

def main():
    n = int(input())
    A = list(map(int, input().split()))





T = int(input())
for _ in range(T):
    main()