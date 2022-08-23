# Problem: C. Build Permutation
# Contest: Codeforces - Codeforces Round #812 (Div. 2)
# URL: https://codeforces.com/contest/1713/problem/C
# Memory Limit: 256 MB
# Time Limit: 1000 ms
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
    MOD = 1000000007
    T = int(input())
    nmax = 100000 * 2
    dp = []
    for i in range(500):
        # if i * i < nmax:
        dp.append(i * i) 
    
    for _ in range(T):
        # a, b = map(int, input().split())
        n = int(input())
        A = [-1] * n
        Can_in = [[] for _ in range(n)]
        Can_have = [[] for _ in range(n)]
        used = set()
        ans = True
        for i in range(n - 1, -1, -1):
            possible = - 1
            # print("i", i)
            for j, s in enumerate(dp):
                if s < i:
                    continue
                if s - i >= n:
                    if possible != -1:
                        A[i] = possible
                        used.add(possible)
                    else:
                        ans = False
                    break
                cur = s - i
                if cur not in used:
                    possible = cur
                    # print(possible) 
            if ans is False:
                break
        if ans:
            print(*A)
        else:
            print(-1)


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
