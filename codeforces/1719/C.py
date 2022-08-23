# Problem: C. Fighting Tournament
# Contest: Codeforces - Codeforces Round #814 (Div. 2)
# URL: https://codeforces.com/contest/1719/problem/C
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
    MOD = 1000000007
    T = int(input())
    for _ in range(T):
        n, q = map(int, input().split())
        A = list(map(int, input().split()))
        nxt = [0] * n

        if A[0] > A[1]:
            cur_max = A[0]
            cur_idx = 0
        else:
            cur_max = A[1]
            cur_idx = 1
        
        cur_win = 1
        for i in range(2, n):
            if cur_max > A[i]:
                cur_win += 1
            else:
                nxt[cur_idx] = cur_win
                cur_win = 1
                cur_max = A[i]
                cur_idx = i
        
        nxt[cur_idx] = -1
        
        for _ in range(q):
            idx, k = map(int, input().split())
            idx -= 1
            if nxt[idx] == 0:
                print(0)
                continue
            if idx > 0:
                k -= idx - 1
            k = max(0, k)
            if nxt[idx] == -1:
                print(k)
                continue
            else:
                print(min(nxt[idx], k))


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
