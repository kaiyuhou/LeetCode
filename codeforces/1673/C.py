# Problem: C. Palindrome Basis
# Contest: Codeforces - Codeforces Round #785 (Div. 2)
# URL: https://codeforces.com/contest/1673/problem/C
# Memory Limit: 256 MB
# Time Limit: 2000 ms
# 
# Powered by CP Editor (https://cpeditor.org)

#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
# sys.setrecursionlimit(100000)

import collections
import math

from functools import lru_cache


def main():
    T = int(input())
    a = 50000
    candi = [i for i in range(1, a + 1) if i == int(str(i)[::-1])]
    # candi = candi[::-1]
    n = len(candi)
    ans = 0
    MOD = 1000000007              

    # 133 ms
    # dp = [0] * ((a + 1) * (n + 1))

    # 256 ms
    dp = [[0] * (n + 1) for _ in range(a + 1)]

    # print(a, n, a * n)
    # 10000 198 1980000
    # 50000 598 29900000

    # 353 ms
    # for i in range(a + 1):
        # for j in range(n + 1):
            # dp[i][j] = 1

    # 160 ms
    # for i in range((a + 1) * (n + 1)):
        # dp[i] = 1

    for i in range(n):
        dp[0][i] = 1
              
    for rest in range(1, a + 1):
        for candi_idx in range(n -1, -1, -1):
            # 337 ms
            dp[rest][candi_idx] = dp[rest][candi_idx + 1]
            if rest - candi[candi_idx] < 0:
                continue
            dp[rest][candi_idx] += dp[rest - candi[candi_idx]][candi_idx]
            dp[rest][candi_idx] %= MOD
    for _ in range(T):
        a = int(input())
        print(dp[a][0])
        


##################################
# Region FastIO
# * code below is for accelerating IO in Python
# * not directly related to the solution
##################################


BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._file = file
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__ == "__main__":
    main()
